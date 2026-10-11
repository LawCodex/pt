#!/usr/bin/env python3
"""Convert the DRE consolidated-legislation JSON (from fetch.py) to Markdown.

Usage: python scripts/convert.py [--raw DIR] [--out DIR]

Writes one Markdown file per diploma into the repository:
  constituicao/                      Constituição da República Portuguesa
  codigos/<code>.md                  codes (diplomas whose consolidated designation is "Código ...")
  leis/<year>/, leis-organicas/<year>/, decretos-lei/<year>/, portarias/<year>/, ...
and RAW/manifest.json (path + metadata of every file written).
"""
import argparse
import glob
import gzip
import html
import json
import os
import re
import sys
import unicodedata
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import DEFAULT_RAW, tipo_slug  # noqa: E402

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITE = "https://diariodarepublica.pt"

TYPE_DIRS = {
    "Lei": "leis",
    "Lei Orgânica": "leis-organicas",
    "Lei Constitucional": "leis-constitucionais",
    "Decreto-Lei": "decretos-lei",
    "Decreto Legislativo Regional": "decretos-legislativos-regionais",
    "Decreto Regulamentar": "decretos-regulamentares",
    "Decreto Regulamentar Regional": "decretos-regulamentares-regionais",
    "Decreto": "decretos",
    "Decreto do Presidente da República": "decretos-presidente-republica",
    "Portaria": "portarias",
    "Resolução do Conselho de Ministros": "resolucoes-conselho-ministros",
    "Resolução da Assembleia da República": "resolucoes-assembleia-republica",
    "Despacho Normativo": "despachos-normativos",
    "Despacho": "despachos",
    "Aviso": "avisos",
    "Declaração": "declaracoes",
}
TYPE_KIND = {
    "Lei": "act", "Lei Orgânica": "organic_act", "Lei Constitucional": "constitutional_act",
    "Decreto-Lei": "decree_law", "Decreto Legislativo Regional": "regional_legislative_decree",
    "Decreto Regulamentar": "regulatory_decree", "Decreto Regulamentar Regional": "regulatory_decree",
    "Decreto": "decree", "Portaria": "ordinance", "Resolução do Conselho de Ministros": "resolution",
    "Resolução da Assembleia da República": "resolution",
}
CODE_TYPES = {"Lei", "Decreto-Lei", "Decreto Legislativo Regional", "Lei Orgânica"}
REVOKED = 4  # FragmentoVersao.VersaoEstadoId of a revoked fragment
ROOT_TYPES = {15}  # "Diploma" / "Ato": the act itself (preamble / heading text)
ARTICLE_TYPES = {11}


def slug(s, maxlen=90):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:maxlen].rstrip("-")


def yaml_str(s):
    return json.dumps(s if s is not None else "", ensure_ascii=False)


# ---------------------------------------------------------------- text cleanup

TAG_RE = re.compile(r"</?(?:br|a|u|span|div|p|b|i|strong|em|sup|sub|font|img|table|thead|tbody|tfoot|tr|td|th|col|colgroup|caption)\b[^>]*>", re.I)
TABLE_RE = re.compile(r"<table\b.*?</table>", re.I | re.S)


def table_to_md(t):
    """Simple HTML table -> Markdown table; complex ones (spans) are kept as HTML."""
    if re.search(r"(rowspan|colspan)\s*=\s*\"?\s*[2-9]", t, re.I) or re.search(r"<table\b[^>]*>.*<table", t[6:], re.I | re.S):
        return "\n\n" + re.sub(r"\s*\n\s*", " ", t) + "\n\n"
    rows = []
    for tr in re.findall(r"<tr\b.*?</tr>", t, re.I | re.S):
        cells = re.findall(r"<t[hd]\b[^>]*>(.*?)</t[hd]>", tr, re.I | re.S)
        cells = [inline(c).replace("\n", "<br>").replace("|", "\\|").strip() for c in cells]
        rows.append(cells)
    if not rows:
        return ""
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * n]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n\n" + "\n".join(out) + "\n\n"


def link(m):
    href = re.search(r'href\s*=\s*"([^"]*)"', m.group(1))
    text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
    if href and href.group(1).strip():
        h = href.group(1).strip()
        if h.startswith("/"):
            h = SITE + h
        if h.startswith("http"):
            return f"[{text}]({h.replace(' ', '%20').replace(')', '%29')})"
    return text


def inline(s):
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"<a\b([^>]*)>(.*?)</a>", link, s, flags=re.I | re.S)
    s = re.sub(r"<img\b[^>]*src\s*=\s*\"([^\"]+)\"[^>]*>",
               lambda m: f"![]({SITE + m.group(1) if m.group(1).startswith('/') else m.group(1)})", s, flags=re.I)
    s = TAG_RE.sub("", s)
    if re.search(r"&(?:[a-z]+|#\d+|#x[0-9a-f]+);", s, re.I):
        s = html.unescape(s)
    return s


def escape_line(line):
    if re.match(r"^\s*(#|>|\+\s|\*|=+\s*$|-{3,}\s*$|_{3,}\s*$)", line):
        return "\\" + line.lstrip()
    return line


def body_text(t):
    if not t:
        return ""
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    parts = []
    pos = 0
    for m in TABLE_RE.finditer(t):
        parts.append(("t", t[pos:m.start()]))
        parts.append(("table", m.group(0)))
        pos = m.end()
    parts.append(("t", t[pos:]))
    out = []
    for kind, chunk in parts:
        if kind == "table":
            out.append(table_to_md(chunk).strip("\n"))
            continue
        chunk = inline(chunk)
        lines = [escape_line(re.sub(r"[ \t ]+", " ", ln).strip()) for ln in chunk.split("\n")]
        lines = [ln for ln in lines if ln]
        if lines:
            out.append("\n\n".join(lines))
    return "\n\n".join(o for o in out if o)


def note_text(s):
    """DRE amendment note: '... [L]<a ...>Lei n.º X ...</a>[/L], em vigor ...'."""
    s = s.replace("[L]", "").replace("[/L]", "")
    s = inline(s)
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- document

def heading_label(f):
    t = (f.get("Tituo") or "").strip()
    e = (f.get("Epigrafe") or "").strip()
    if not t:
        t = (f.get("Identificacao") or "").strip()
    if t and e:
        return f"{t} {e}" if e.startswith("(") else f"{t} — {e}"
    return t or e


def render(rec):
    src = rec["search"]
    data = rec["data"]
    frags = data["LegConsBase"]["List"]
    out = []
    for x in frags:
        f = x["FragmentoVersao"]
        c = x["ConsolidacaoFragmento"]
        if x.get("IsHidden"):
            continue
        level = int(x.get("Nivel") or 0)
        revoked = f.get("VersaoEstadoId") == REVOKED
        if f.get("TipoFragmentoId") in ROOT_TYPES and level == 0:
            txt = body_text(f.get("Texto"))
            if txt:
                out.append(txt)
            continue
        label = heading_label(f).replace("\n", " ")
        label = re.sub(r"\s+", " ", label).strip()
        h = level + 1
        if label:
            if h <= 6:
                out.append("#" * h + " " + label)
            elif f.get("TipoFragmentoId") in ARTICLE_TYPES:
                out.append("###### " + label)
            else:
                out.append(f"**{label}**")
        if revoked:
            desc = note_text(c.get("AssociacaoDescription") or "")
            out.append(f"*(Revogado)*" + (f" — *{desc}*" if desc else ""))
            continue
        txt = body_text(f.get("Texto"))
        if txt:
            out.append(txt)
        alts = [note_text(a) for a in (x.get("AlteracoesList") or {}).get("List", []) if a]
        if alts:
            out.append("\n".join(f"- *{a}*" for a in alts))
    return "\n\n".join(out)


def short_title(src):
    t = src.get("title") or ""
    t = re.split(r"\s+-\s+Di[áa]rio d", t)[0]
    return re.sub(r"\s+", " ", t).strip()


def plain(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def classify(rec, code_frag_ids):
    src = rec["search"]
    tipo = src.get("tipo") or ""
    frag = rec.get("frag") or {}
    desig = ((frag.get("DiplomaFrag") or {}).get("Designacao") or src.get("designacao") or "").strip()
    year = (src.get("ano") or (src.get("dataPublicacao") or "0000")[:4])
    if tipo == "Decreto de Aprovação da Constituição":
        return "constitution", "constituicao", "constituicao-da-republica-portuguesa", desig
    is_code = str(src.get("DiplomaFragmentadoId") or "") in code_frag_ids or (
        tipo in CODE_TYPES and re.match(r"^C[óo]digos? ", desig))
    if is_code:
        name = re.sub(r"\s+-\s+[A-Z]{2,6}$", "", desig)  # drop trailing acronym
        return "code", "codigos", slug(name), desig
    d = TYPE_DIRS.get(tipo) or f"outros/{tipo_slug(tipo) or 'sem-tipo'}"
    num = (src.get("numero") or "").strip()
    base = tipo_slug(tipo)
    name = f"{base}-{slug(num)}" if num else f"{base}-{src.get('dataPublicacao', '')}-{src['dbId']}"
    return TYPE_KIND.get(tipo, "regulation"), f"{d}/{year}", name, desig


def frontmatter(meta):
    lines = ["---"]
    for k, v in meta.items():
        if v is None or v == "":
            continue
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            lines.append(f"{k}: {v}")
        elif k in ("date", "last_amended", "retrieved") and re.match(r"^\d{4}-\d{2}-\d{2}$", str(v)):
            lines.append(f"{k}: {v}")
        elif k in ("type", "jurisdiction", "language", "status"):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {yaml_str(v)}")
    lines.append("---")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--out", default=REPO)
    a = ap.parse_args()
    raw = os.path.abspath(a.raw)
    out = os.path.abspath(a.out)
    retrieved = date.fromtimestamp(os.path.getmtime(os.path.join(raw, "list.json"))).isoformat()
    codes = json.load(open(os.path.join(raw, "codigos.json")))
    code_frag_ids = set()
    for c in codes:
        m = re.search(r"-(\d+)$", c.get("LinkSiteMap") or "")
        if m:
            code_frag_ids.add(m.group(1))
    files = sorted(glob.glob(os.path.join(raw, "json", "*.json.gz")), key=lambda p: int(os.path.basename(p).split(".")[0]))
    used = {}
    manifest = []
    for p in files:
        rec = json.load(gzip.open(p, "rt", encoding="utf-8"))
        src = rec["search"]
        data = rec["data"]
        if not data["LegConsBase"]["List"]:
            print(f"empty: {src['dbId']} {src.get('title')}", file=sys.stderr)
            continue
        kind, d, name, desig = classify(rec, code_frag_ids)
        rel = f"{d}/{name}.md"
        if rel in used:
            rel = f"{d}/{name}-{src['dbId']}.md"
        used[rel] = src["dbId"]
        frag = (rec.get("frag") or {}).get("DiplomaFrag") or {}
        eli = frag.get("ELI") or ""
        if not re.search(r"/eli/.+", eli):
            eli = ""
        act = short_title(src)
        if kind == "constitution":
            title = "Constituição da República Portuguesa"
        elif kind == "code":
            title = re.sub(r"\s+-\s+[A-Z]{2,6}$", "", desig)
        else:
            title = act
        vig = src.get("vigencia") or ""
        status = "in_force" if vig == "VIGENTE" else "unknown"
        source = rec.get("url") or f"{SITE}/dr/detalhe/{tipo_slug(src.get('tipo') or '')}/{src.get('ano')}-{src['dbId']}"
        last = (data.get("DataUltimaConsolidada") or "")[:10]
        if last.startswith("1900"):
            last = ""
        meta = {
            "title": title,
            "identifier": act,
            "type": kind,
            "jurisdiction": "pt",
            "language": "pt",
            "date": (src.get("dataPublicacao") or "")[:10],
            "last_amended": last,
            "status": status,
            "source": source,
            "retrieved": retrieved,
            "act": act if kind in ("code", "constitution") else "",
            "designation": desig if desig and desig != act and kind not in ("code",) and not desig.startswith(plain(src.get("sumario"))[:40] or "\0") else "",
            "summary": plain(src.get("sumario")),
            "issuer": src.get("emissor") or "",
            "series": src.get("serie") or "",
            "eli": eli,
            "dre_id": int(src["dbId"]),
            "dre_vigencia": vig,
            "dre_consolidation_state": src.get("consolidacaoEstado") or "",
            "original_pdf": data.get("URLPDF") or "",
        }
        body = render(rec)
        h1 = title if kind != "code" else f"{title}"
        md = frontmatter(meta) + f"\n\n# {h1}\n\n"
        if kind in ("code", "constitution"):
            md += f"*{act}*\n\n"
        md += body.rstrip() + "\n"
        path = os.path.join(out, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(md)
        manifest.append({"path": rel, "dre_id": src["dbId"], "type": kind, "tipo": src.get("tipo"),
                         "title": title, "status": status, "bytes": len(md.encode())})
    with open(os.path.join(raw, "manifest.json"), "w") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=0)
    print(f"wrote {len(manifest)} files", file=sys.stderr)


if __name__ == "__main__":
    main()
