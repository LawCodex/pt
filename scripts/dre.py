"""Minimal client for the Diário da República Eletrónico (https://diariodarepublica.pt).

The DRE site is an OutSystems "reactive" web app: pages are rendered client-side and
their data comes from JSON "screen service" endpoints
(POST /dr/screenservices/dr/<Module>/<Screen>/DataAction<Name>).
Each call must carry the current module version token (from /dr/moduleservices/moduleinfo)
and the action's API version (hard-coded in the screen's compiled JS, which we parse so
that this keeps working after DRE redeploys). Anonymous calls use OutSystems' public
anonymous CSRF token.
"""
import json
import re
import sys
import threading
import time

import requests

UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
BASE = "https://diariodarepublica.pt/dr/"
ANON_CSRF = "T6C+9iB49TLra4jEsMeSckDMNhQ="


class DRE:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA
        self._lock = threading.Lock()
        self._api = {}
        self.refresh()

    def _get(self, url, **kw):
        delay = 5
        for attempt in range(8):
            try:
                r = self.s.get(url, timeout=120, **kw)
                if r.status_code == 200:
                    return r
                print(f"HTTP {r.status_code} for {url}", file=sys.stderr)
            except requests.RequestException as e:
                print(f"error {e} for {url}", file=sys.stderr)
            time.sleep(delay)
            delay = min(delay * 2, 300)
        raise RuntimeError(f"giving up on {url}")

    def refresh(self):
        mi = self._get(BASE + "moduleservices/moduleinfo").json()["manifest"]
        self.version = mi["versionToken"]
        self.urls = mi["urlVersions"]
        self._api = {}

    def api_version(self, module, screen, action):
        """Find the apiVersion of `action` in /dr/scripts/dr.<module>.<screen>.mvc.js."""
        key = (module, screen, action)
        with self._lock:
            if key in self._api:
                return self._api[key]
            path = f"/dr/scripts/dr.{module}.{screen}.mvc.js"
            js = self._get("https://diariodarepublica.pt" + path + self.urls.get(path, "")).text
            m = re.search(r'callDataAction\("%s", "[^"]*", "[^"]*", "([^"]*)"' % re.escape(action), js)
            if not m:
                raise RuntimeError(f"apiVersion for {action} not found in {path}")
            self._api[key] = m.group(1)
            return m.group(1)

    def data_action(self, module, screen, action, variables, timeout=600):
        """Call a screen DataAction and return its `data` dict."""
        url = f"{BASE}screenservices/dr/{module}/{screen}/{action}"
        delay = 5
        for attempt in range(8):
            body = {
                "versionInfo": {"moduleVersion": self.version,
                                "apiVersion": self.api_version(module, screen, action)},
                "viewName": f"{module}.{screen}",
                "screenData": {"variables": variables},
                "clientVariables": {},
            }
            try:
                r = self.s.post(url, json=body, timeout=timeout,
                                headers={"X-CSRFToken": ANON_CSRF, "Accept": "application/json"})
                if r.status_code == 200:
                    j = r.json()
                    vi = j.get("versionInfo", {})
                    if vi.get("hasModuleVersionChanged") or vi.get("hasApiVersionChanged"):
                        print("DRE redeployed; refreshing version tokens", file=sys.stderr)
                        with self._lock:
                            self.refresh()
                        continue
                    if "exception" in j:
                        raise RuntimeError(f"{action}: {j['exception']}")
                    return j["data"]
                print(f"HTTP {r.status_code} for {action}", file=sys.stderr)
            except (requests.RequestException, ValueError) as e:
                print(f"error {e} for {action}", file=sys.stderr)
            time.sleep(delay)
            delay = min(delay * 2, 300)
        raise RuntimeError(f"giving up on {action}")

    # ---- high-level helpers -------------------------------------------------

    def search(self, filters, start=0, size=100, text="*", sort=None):
        """Elastic search over DRE content (as used by the site's search page)."""
        v = {
            "FiltrosDePesquisa": {"texto": text, "tipoConteudo": {"List": []}},
            "ListaFiltros": {"List": [{"Area": a, "Value": val} for a, val in filters]},
            "PesquisaSimplesFiltro": text,
            "Pesquisa": {"List": [text]},
            "IsPesquisaSimples": True,
            "StartIndex": start,
            "MaxRecordsPerPage": size,
            "TipoOrdenacaoId": 9,
            "Ordenacoes": {"List": [{"Field": f, "Order": o} for f, o in (sort or [("dbId", "asc")])]},
        }
        d = self.data_action("Pesquisas", "PesquisaResultado", "DataActionGetPesquisas", v)
        return json.loads(d["Resultado"])

    def codigos(self):
        d = self.data_action("MenusParaPesquisa", "LegislacaoPorCodigo", "DataActionGetCodigos", {})
        return [x["DiplomaFrag"] for x in d["CodigosList"]["List"]]

    def consolidated(self, diploma_legis_id):
        """Current consolidated version of a diploma: list of fragments + metadata."""
        v = {"DiplomaLegisId": str(diploma_legis_id), "DiplomaFragId": "0",
             "GetDiplomaFragByIdAndApplicationSetting": {}}
        return self.data_action("LegislacaoConsolidada", "LegCons_Detalhe", "DataActionGetData", v)

    def frag_info(self, diploma_frag_id):
        """Metadata of a consolidated diploma (designation, ELI, publication)."""
        v = {"DiplomaFragId": str(diploma_frag_id), "DiplomaLegisId": "0"}
        return self.data_action("LegislacaoConsolidada", "LegCons_Detalhe",
                                "DataActionGetDiplomaFragByIdAndApplicationSetting", v)
