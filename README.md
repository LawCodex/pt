# LawCodex — Portugal

Portuguese legislation as plain Markdown, one file per diploma, generated from the
consolidated texts (*Legislação Consolidada*) of the official **Diário da República
Eletrónico** (DRE), published by the Imprensa Nacional-Casa da Moeda (INCM).

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as Markdown in git.

- Jurisdiction: Portugal (`pt`), language: Portuguese
- Source: Diário da República Eletrónico — <https://diariodarepublica.pt/dr/home>
  (consolidated legislation: `https://diariodarepublica.pt/dr/legislacao-consolidada/...`)
- Retrieved: 2026-10-11
- Total: **4,840** diplomas — 4,503 consolidated texts + 337 unamended
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

**Unamended originals.** For some diplomas (337) the DRE marks the act as analysed for
consolidation but holds no article-level consolidated text (typically acts never amended since
publication: treaty notices, small resolutions, recent acts). For these the file contains the
original text as published, from the DRE detail page, and the front matter says
`text_version: "original (no amendments consolidated by DRE)"`.

| Directory | Type of act | Files | of which unamended originals |
|---|---|---:|---:|
| `constituicao/` | Decreto de Aprovação da Constituição (1) | 1 | 0 |
| `codigos/` | Decreto-Lei (23), Lei (15), Decreto Legislativo Regional (2) | 40 | 0 |
| `leis-organicas/` | Lei Orgânica | 13 | 0 |
| `leis/` | Lei | 517 | 3 |
| `decretos-lei/` | Decreto-Lei | 1,659 | 6 |
| `decretos-legislativos-regionais/` | Decreto Legislativo Regional | 259 | 3 |
| `decretos-regulamentares/` | Decreto Regulamentar | 71 | 2 |
| `decretos-regulamentares-regionais/` | Decreto Regulamentar Regional | 97 | 1 |
| `decretos/` | Decreto | 52 | 23 |
| `decretos-presidente-republica/` | Decreto do Presidente da República | 33 | 1 |
| `resolucoes-assembleia-republica/` | Resolução da Assembleia da República | 38 | 5 |
| `resolucoes-conselho-ministros/` | Resolução do Conselho de Ministros | 289 | 6 |
| `portarias/` | Portaria | 1,405 | 96 |
| `despachos-normativos/` | Despacho Normativo | 26 | 0 |
| `despachos/` | Despacho | 23 | 12 |
| `avisos/` | Aviso | 190 | 155 |
| `declaracoes/` | Declaração | 30 | 19 |
| `outros/acordo-colectivo-trabalho/` | Acordo Colectivo de Trabalho (1) | 1 | 0 |
| `outros/aviso-banco-portugal/` | Aviso do Banco de Portugal (2) | 2 | 0 |
| `outros/aviso-extrato/` | Aviso (extrato) (1) | 1 | 0 |
| `outros/decisao-conselho-ministros/` | Decisão do Conselho de Ministros (1) | 1 | 1 |
| `outros/declaracao-rectificacao/` | Declaração de Rectificação (5) | 5 | 0 |
| `outros/declaracao-retificacao/` | Declaração de Retificação (10) | 10 | 1 |
| `outros/decreto-governo/` | Decreto do Governo (3) | 3 | 0 |
| `outros/decreto-regional/` | Decreto Regional (2) | 2 | 0 |
| `outros/decreto-representante-republica-para-a-regiao-autonoma-madeira/` | Decreto do Representante da República para a Região Autónoma da Madeira (1) | 1 | 0 |
| `outros/deliberacao/` | Deliberação (2) | 2 | 0 |
| `outros/despacho-conselho-ministros/` | Despacho do Conselho de Ministros (1) | 1 | 1 |
| `outros/despacho-extrato/` | Despacho (extrato) (1) | 1 | 0 |
| `outros/diretiva/` | Diretiva (4) | 4 | 0 |
| `outros/edital/` | Edital (8) | 8 | 0 |
| `outros/mapa-oficial/` | Mapa Oficial (10) | 10 | 0 |
| `outros/regimento/` | Regimento (1) | 1 | 0 |
| `outros/regimento-assembleia-republica/` | Regimento da Assembleia da República (2) | 2 | 0 |
| `outros/regulamento/` | Regulamento (5) | 5 | 1 |
| `outros/regulamento-cmvm/` | Regulamento da CMVM (11) | 11 | 0 |
| `outros/resolucao/` | Resolução (3) | 3 | 1 |
| `outros/resolucao-assembleia-legislativa-regiao-autonoma-acores/` | Resolução da Assembleia Legislativa da Região Autónoma dos Açores (12) | 12 | 0 |
| `outros/resolucao-assembleia-legislativa-regiao-autonoma-madeira/` | Resolução da Assembleia Legislativa da Região Autónoma da Madeira (6) | 6 | 0 |
| `outros/resolucao-assembleia-legislativa-regional/` | Resolução da Assembleia Legislativa Regional (4) | 4 | 0 |
| `outros/resolucao-assembleia-regional/` | Resolução da Assembleia Regional (1) | 1 | 0 |

Directories are sharded by year of publication (`leis/2009/lei-7-2009.md`), except
`constituicao/` and `codigos/`. Minor act types are under `outros/<type>/<year>/`.

### Codes (40)

Codes are stored under `codigos/` under the code's name (instead of under the approving
diploma). A diploma is treated as a code when it is listed on DRE's *Legislação por código*
page or when its consolidated designation starts with "Código". The file contains the whole
approving diploma (preamble and articles) followed by the code itself (usually its *Anexo*).

- [Código Administrativo](codigos/codigo-administrativo.md)
- [Código Civil](codigos/codigo-civil.md)
- [Código Cooperativo](codigos/codigo-cooperativo.md)
- [Código Fiscal do Investimento](codigos/codigo-fiscal-do-investimento.md)
- [Código Fiscal do Investimento na Região Autónoma da Madeira](codigos/codigo-fiscal-do-investimento-na-regiao-autonoma-da-madeira.md)
- [Código Penal](codigos/codigo-penal.md)
- [Código da Ação Social dos Açores](codigos/codigo-da-acao-social-dos-acores.md)
- [Código da Contribuição Industrial](codigos/codigo-da-contribuicao-industrial.md)
- [Código da Estrada](codigos/codigo-da-estrada.md)
- [Código da Execução das Penas e Medidas Privativas da Liberdade](codigos/codigo-da-execucao-das-penas-e-medidas-privativas-da-liberdade.md)
- [Código da Insolvência e da Recuperação de Empresas](codigos/codigo-da-insolvencia-e-da-recuperacao-de-empresas.md)
- [Código da Propriedade Industrial](codigos/codigo-da-propriedade-industrial.md)
- [Código da Publicidade](codigos/codigo-da-publicidade.md)
- [Código das Expropriações](codigos/codigo-das-expropriacoes.md)
- [Código das Sociedades Comerciais](codigos/codigo-das-sociedades-comerciais.md)
- [Código de Justiça Militar](codigos/codigo-de-justica-militar.md)
- [Código de Procedimento e Processo Tributário](codigos/codigo-de-procedimento-e-processo-tributario.md)
- [Código de Processo Civil](codigos/codigo-de-processo-civil.md)
- [Código de Processo Penal](codigos/codigo-de-processo-penal.md)
- [Código de Processo do Trabalho](codigos/codigo-de-processo-do-trabalho.md)
- [Código de Processo nos Tribunais Administrativos](codigos/codigo-de-processo-nos-tribunais-administrativos.md)
- [Código do Direito de Autor e dos Direitos Conexos](codigos/codigo-do-direito-de-autor-e-dos-direitos-conexos.md)
- [Código do IRS - Imposto sobre o Rendimento das Pessoas Singulares](codigos/codigo-do-irs-imposto-sobre-o-rendimento-das-pessoas-singulares.md)
- [Código do IVA - Código do Imposto sobre o Valor Acrescentado](codigos/codigo-do-iva-codigo-do-imposto-sobre-o-valor-acrescentado.md)
- [Código do Imposto do Selo](codigos/codigo-do-imposto-do-selo.md)
- [Código do Imposto sobre Veículos e Código do Imposto Único de Circulação](codigos/codigo-do-imposto-sobre-veiculos-e-codigo-do-imposto-unico-de-circulacao.md)
- [Código do Imposto sobre o Rendimento das Pessoas Coletivas](codigos/codigo-do-imposto-sobre-o-rendimento-das-pessoas-coletivas.md)
- [Código do Notariado](codigos/codigo-do-notariado.md)
- [Código do Procedimento Administrativo](codigos/codigo-do-procedimento-administrativo.md)
- [Código do Registo Civil](codigos/codigo-do-registo-civil.md)
- [Código do Registo Comercial](codigos/codigo-do-registo-comercial.md)
- [Código do Registo Predial](codigos/codigo-do-registo-predial.md)
- [Código do Trabalho](codigos/codigo-do-trabalho.md)
- [Código do Trabalho - CT antigo](codigos/codigo-do-trabalho-ct-antigo.md)
- [Código dos Contratos Públicos](codigos/codigo-dos-contratos-publicos.md)
- [Código dos Impostos Especiais de Consumo](codigos/codigo-dos-impostos-especiais-de-consumo.md)
- [Código dos Regimes Contributivos do Sistema Previdencial de Segurança Social](codigos/codigo-dos-regimes-contributivos-do-sistema-previdencial-de-seguranca-social.md)
- [Código dos Valores Mobiliários](codigos/codigo-dos-valores-mobiliarios.md)
- [Códigos do Imposto Municipal sobre Imóveis - CIMI - e do Imposto Municipal sobre as Transmissões Onerosas de Imóveis](codigos/codigos-do-imposto-municipal-sobre-imoveis-cimi-e-do-imposto-municipal-sobre-as-transmisso.md)
- [Novo Regime do Arrendamento Urbano](codigos/novo-regime-do-arrendamento-urbano.md)

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
retrieved: 2026-10-11
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
