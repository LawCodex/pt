#!/usr/bin/env python3
"""Regenerate README.md from RAW/manifest.json (written by convert.py)."""
import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import DEFAULT_RAW  # noqa: E402

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

TEMPLATE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.template.md"), encoding="utf-8").read()


def fmt(n):
    return f"{n:,}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--retrieved", required=True)
    a = ap.parse_args()
    man = json.load(open(os.path.join(a.raw, "manifest.json")))
    by_dir = collections.OrderedDict()
    tipo_of = {}
    orig = collections.Counter()
    for m in sorted(man, key=lambda m: m["path"]):
        parts = m["path"].split("/")
        top = parts[0] if parts[0] != "outros" else "/".join(parts[:2])
        by_dir.setdefault(top, 0)
        by_dir[top] += 1
        tipo_of.setdefault(top, collections.Counter())[m["tipo"]] += 1
        if m.get("original"):
            orig[top] += 1
    order = ["constituicao", "codigos", "leis-constitucionais", "leis-organicas", "leis", "decretos-lei",
             "decretos-legislativos-regionais", "decretos-regulamentares", "decretos-regulamentares-regionais",
             "decretos", "decretos-presidente-republica", "resolucoes-assembleia-republica",
             "resolucoes-conselho-ministros", "portarias", "despachos-normativos", "despachos", "avisos",
             "declaracoes"]
    keys = [k for k in order if k in by_dir] + sorted(k for k in by_dir if k not in order)
    rows = []
    for k in keys:
        t = ", ".join(f"{n} ({c})" for n, c in tipo_of[k].most_common()) if k in ("codigos", "constituicao") or k.startswith("outros/") else tipo_of[k].most_common(1)[0][0]
        rows.append(f"| `{k}/` | {t} | {fmt(by_dir[k])} | {fmt(orig[k])} |")
    total = len(man)
    norig = sum(orig.values())
    codes = sorted((m for m in man if m["type"] == "code"), key=lambda m: m["title"])
    code_list = "\n".join(f"- [{m['title']}]({m['path']})" for m in codes)
    text = TEMPLATE.format(
        total=fmt(total), table="\n".join(rows), retrieved=a.retrieved,
        consolidated=fmt(total - norig), original=fmt(norig), ncodes=len(codes), code_list=code_list,
    )
    with open(os.path.join(REPO, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("README.md written", file=sys.stderr)


if __name__ == "__main__":
    main()
