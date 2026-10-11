#!/usr/bin/env python3
"""Download the consolidated legislation ("Legislação Consolidada") of the
Diário da República Eletrónico (DRE).

Usage: python scripts/fetch.py [--raw DIR] [--workers N] [--all] [--refresh]

1. Lists every diploma that has a public consolidated version
   (Elastic search filter consolidacaoVisibility = PUBLIC), saved to RAW/list.json.
2. For each selected diploma downloads
   - the consolidated-diploma metadata (designation, e.g. "Código Civil - CC"), and
   - the current consolidated text (all fragments: parts/titles/chapters/articles)
   into RAW/json/<dbId>.json.gz (skipped if cached, unless --refresh).

By default only diplomas in force are fetched (see `selected()`); --all fetches every
consolidated diploma, including revoked/expired ones.
"""
import argparse
import concurrent.futures as cf
import gzip
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dre import DRE  # noqa: E402

DEFAULT_RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_raw", "pt")
FILTERS = [("docType_facet.keyword", "LEGISLACAO"), ("consolidacaoVisibility", "PUBLIC")]

STOP = {"de", "do", "da", "dos", "das"}


def tipo_slug(tipo):
    """DRE URL slug of an act type: 'Decreto do Presidente da República' -> 'decreto-presidente-republica'."""
    s = unicodedata.normalize("NFKD", tipo).encode("ascii", "ignore").decode().lower()
    words = [w for w in re.split(r"[^a-z0-9]+", s) if w and w not in STOP]
    return "-".join(words)


def selected(src):
    """In-force consolidated diplomas."""
    if src.get("consolidacaoEstado") in ("REVOKED", "EXPIRED"):
        return False
    if src.get("vigencia") in ("NAO_VIGENTE", "CADUCADO"):
        return False
    return True


def fetch_list(dre, raw):
    out, start, size = [], 0, 100
    while True:
        r = dre.search(FILTERS, start, size)
        hits = r["hits"]["hits"]
        total = r["hits"]["total"]["value"]
        out += [h["_source"] for h in hits]
        print(f"list: {len(out)}/{total}", file=sys.stderr)
        if not hits or len(out) >= total:
            break
        start += size
    ids = {x["dbId"] for x in out}
    if len(ids) != total:
        print(f"WARNING: got {len(ids)} unique of {total}", file=sys.stderr)
    with open(os.path.join(raw, "list.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=0)
    return out


def fetch_one(dre, raw, src, refresh):
    path = os.path.join(raw, "json", f"{src['dbId']}.json.gz")
    if os.path.exists(path) and not refresh:
        return "cached"
    rec = {"search": src, "frag": None}
    frag = src.get("DiplomaFragmentadoId")
    if frag:
        key = f"{src['ano']}-{frag}"
        fi = dre.data_action("LegislacaoConsolidada", "LegCons_Detalhe",
                             "DataActionGetDiplomaFragByIdAndApplicationSetting",
                             {"Tipo": tipo_slug(src["tipo"]), "Key": key, "DiplomaFragId": str(frag)})
        if not fi.get("IsSitemapErro"):
            rec["frag"] = fi["ConsolidadaConteudoDetalhe"]
            rec["url"] = f"https://diariodarepublica.pt/dr/legislacao-consolidada/{tipo_slug(src['tipo'])}/{key}"
    rec["data"] = dre.consolidated(src["dbId"])
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False)
    os.replace(tmp, path)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--skip-list", action="store_true", help="reuse RAW/list.json")
    a = ap.parse_args()
    raw = os.path.abspath(a.raw)
    os.makedirs(os.path.join(raw, "json"), exist_ok=True)
    dre = DRE()
    lp = os.path.join(raw, "list.json")
    lst = json.load(open(lp)) if a.skip_list and os.path.exists(lp) else fetch_list(dre, raw)
    todo = [s for s in lst if a.all or selected(s)]
    # codes listed on the DRE "Legislação por código" page
    with open(os.path.join(raw, "codigos.json"), "w") as f:
        json.dump(dre.codigos(), f, ensure_ascii=False, indent=0)
    print(f"{len(todo)} diplomas to fetch", file=sys.stderr)
    done = 0
    errors = []
    with cf.ThreadPoolExecutor(a.workers) as ex:
        futs = {ex.submit(fetch_one, dre, raw, s, a.refresh): s for s in todo}
        for fu in cf.as_completed(futs):
            s = futs[fu]
            try:
                fu.result()
            except Exception as e:  # noqa: BLE001
                errors.append((s["dbId"], str(e)))
                print(f"FAILED {s['dbId']} {s.get('title')}: {e}", file=sys.stderr)
            done += 1
            if done % 100 == 0:
                print(f"{done}/{len(todo)}", file=sys.stderr)
    with open(os.path.join(raw, "errors.json"), "w") as f:
        json.dump(errors, f, indent=1)
    print(f"done, {len(errors)} errors", file=sys.stderr)


if __name__ == "__main__":
    main()
