# LawCodex — Portugal

Portuguese legislation as plain Markdown, one file per diploma, generated from the
consolidated texts (*Legislação Consolidada*) of the official **Diário da República
Eletrónico** (DRE), published by the Imprensa Nacional-Casa da Moeda (INCM).

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as Markdown in git.

- Jurisdiction: Portugal (`pt`), language: Portuguese
- Source: Diário da República Eletrónico — <https://diariodarepublica.pt/dr/home>
  (consolidated legislation: `https://diariodarepublica.pt/dr/legislacao-consolidada/...`)
- Retrieved: {retrieved}
- Total: **{total}** diplomas — {consolidated} consolidated texts + {original} unamended
  originals (see below)

## Coverage

Everything that the DRE exposes as *legislação consolidada* (public consolidation) and that
is **in force**: the Constitution, the codes and all consolidated *leis*, *leis orgânicas*,
*decretos-lei*, regional legislative decrees, regulatory decrees, *portarias*, resolutions, etc.

Selection: every diploma in the DRE search index with a public consolidation
(`consolidacaoVisibility = PUBLIC`, 5,778 diplomas at retrieval time), **minus** those DRE
marks as revoked or lapsed (`consolidacaoEstado` REVOKED / EXPIRED, or `vigencia`
NAO_VIGENTE / CADUCADO — 938 diplomas). Diplomas whose consolidation is still in progress
(`IN_PROGRESS`) or whose force is conditional (`VIGENCIA_CONDICIONADA`) are included; their
state is recorded in the front matter (`dre_consolidation_state`, `dre_vigencia`).

Each consolidated file contains the current version as published by the DRE (all amendments
applied). Revoked articles are kept as headings marked *(Revogado)* with DRE's revocation note,
and each article is followed by DRE's list of the amendments that produced its current wording
(*Alterado pelo/a …*, with links to the amending acts).

**Unamended originals.** For some diplomas ({original}) the DRE marks the act as analysed for
consolidation but holds no article-level consolidated text (typically acts never amended since
publication: treaty notices, small resolutions, recent acts). For these the file contains the
original text as published, from the DRE detail page, and the front matter says
`text_version: "original (no amendments consolidated by DRE)"`.

| Directory | Type of act | Files | of which unamended originals |
|---|---|---:|---:|
{table}

Directories are sharded by year of publication (`leis/2009/lei-7-2009.md`), except
`constituicao/` and `codigos/`. Minor act types are under `outros/<type>/<year>/`.

### Codes ({ncodes})

Codes are stored under `codigos/` under the code's name (instead of under the approving
diploma). A diploma is treated as a code when it is listed on DRE's *Legislação por código*
page or when its consolidated designation starts with "Código". The file contains the whole
approving diploma (preamble and articles) followed by the code itself (usually its *Anexo*).

{code_list}

Notes: the *Novo Regime do Arrendamento Urbano* is not formally a code but is listed by the DRE
among its codes; "Código do Trabalho - CT antigo" is the 2003 Labour Code (Lei n.º 99/2003),
largely revoked by the 2009 Code but still flagged in force by the DRE for its surviving provisions.

## Not covered

- **Non-consolidated legislation.** The DRE consolidates only a subset of the legislation in
  force (about 4,800 diplomas). The many thousands of other acts in force that were never
  consolidated (most *decretos-lei*, *portarias*, *despachos*… published in Série I/II) are
  not included: the DRE only offers them as originally published, without amendments applied.
- **Código Comercial (Carta de Lei de 28 de junho de 1888).** Not consolidated by the DRE (only
  the 1888 original is available, at
  <https://diariodarepublica.pt/dr/detalhe/carta-lei/1888-321492>), and not available as a
  consolidated text from the secondary source checked (PGDL, <https://www.pgdlisboa.pt/leis/>).
  Omitted rather than publishing a heavily outdated original. No PGDL texts are used in this
  repository: every file comes from the official DRE.
- Revoked / lapsed consolidated diplomas (938, see above). `scripts/fetch.py --all` fetches them too.
- Regional legislation of the Azores and Madeira is included only where consolidated by the DRE
  (regional legislative/regulatory decrees published in the Diário da República).
- Case law, Série II acts not consolidated, *Jornal Oficial* of the autonomous regions.
- Embedded (base64) images inside a few texts are replaced by a placeholder; images hosted
  by the DRE are linked. Each file's `original_pdf` points to the official PDF of the original
  publication.

## File format

```markdown
---
title: "Código Civil"
identifier: "Decreto-Lei n.º 47344"
type: code
jurisdiction: pt
language: pt
date: 1966-11-25                 # publication date in the Diário
last_amended: 2026-06-23         # date of DRE's latest consolidated version
status: in_force                 # in_force (DRE vigência VIGENTE) | unknown
source: "https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/1966-34509075"
retrieved: {retrieved}
act: "Decreto-Lei n.º 47344"
summary: "Aprova o Código Civil e regula a sua aplicação - …"   # official sumário
issuer: "Ministério da Justiça - Gabinete do Ministro"
series: "I"
eli: "https://data.dre.pt/eli/dec-lei/47344/1966/p/cons/20260623/pt/html"
dre_id: 477358                   # DRE DiplomaLegis id
dre_vigencia: "VIGENTE"
dre_consolidation_state: "CONCLUDED"
original_pdf: "https://files.diariodarepublica.pt/1s/1966/11/27400/18832086.pdf"
text_version: "consolidated"
---

# Código Civil
```

The DRE fragment hierarchy (Parte / Livro / Título / Capítulo / Secção / Subsecção / Divisão /
Artigo / Anexo) is mapped to Markdown headings by depth (`##` … `######`); structural
levels deeper than `######` become bold lines, articles stay `######`. Simple tables are
converted to Markdown tables, tables with merged cells are kept as HTML.

## Licence

Official texts published in the Diário da República are not protected by copyright
(Código do Direito de Autor e dos Direitos Conexos, art. 7.º, n.º 1, al. c): texts of laws, regulations and official decisions are excluded from protection).
The DRE content is made available for reuse by INCM under the terms of Decreto-Lei n.º 83/2016
(free, universal access to the Diário da República). This repository's conversion scripts are
offered under CC0.

The texts reproduced here have no official value; only the Diário da República as published
is authentic.

## How it was made / regenerate

The DRE is an OutSystems single-page app with no bulk download or documented API (no dataset
on dados.gov.pt). `scripts/dre.py` calls the JSON "screen services" that the site itself uses
(search index, consolidated-diploma fragments, detail pages), discovering API versions from
the site's JavaScript so that it survives redeployments.

```sh
pip install -r scripts/requirements.txt
python scripts/fetch.py            # list + download into ../_raw/pt/json (cached, ~2 h, 3 workers)
python scripts/convert.py          # write Markdown into this repo + ../_raw/pt/manifest.json
python scripts/readme.py --retrieved YYYY-MM-DD
```
