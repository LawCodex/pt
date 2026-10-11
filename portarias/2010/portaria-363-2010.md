---
title: "Portaria n.º 363/2010"
identifier: "Portaria n.º 363/2010"
type: ordinance
jurisdiction: pt
language: pt
date: 2010-06-23
last_amended: 2019-02-15
status: in_force
source: "https://diariodarepublica.pt/dr/legislacao-consolidada/portaria/2010-119668497"
retrieved: 2026-10-11
summary: "Regulamenta a certificação prévia dos programas informáticos de facturação do Código do Imposto sobre o Rendimento das Pessoas Colectivas"
issuer: "Ministério das Finanças e da Administração Pública"
series: "I"
eli: "https://data.dre.pt/eli/port/363/2010/p/cons/20190215/pt/html"
dre_id: 335230
dre_vigencia: "VIGENTE"
dre_consolidation_state: "CONCLUDED"
original_pdf: "https://files.diariodarepublica.pt/1s/2010/06/12000/0222102223.pdf"
text_version: "consolidated"
---

# Portaria n.º 363/2010

Portaria n.º 363/2010

de 23 de Junho

A utilização crescente de sistemas de processamento electrónico de dados, nomeadamente para facturação da transmissão de bens ou de prestações de serviços, acarreta inegáveis vantagens em termos de celeridade do tratamento da informação.

Todavia, introduz novos riscos em termos de controlo fiscal, pela possibilidade de subsequente adulteração dos dados registados, potenciando situações de evasão fiscal.

Nesta perspectiva, importa definir regras para que os programas de facturação observem requisitos que garantam a inviolabilidade da informação inicialmente registada, permitindo-se, consequentemente, que apenas os programas que respeitem tais requisitos possam ser utilizados, após certificação pela AT.

Foram observados os procedimentos de notificação à Comissão Europeia previstos no Decreto-Lei n.º 58/2000, de 18 de Abril.

Assim:

Manda o Governo, ao abrigo do disposto no n.º 8 do artigo 123.º do Código do Imposto sobre o Rendimento das Pessoas Colectivas, aprovado pelo Decreto-Lei n.º 442-B/88, de 30 de Novembro, pelo Ministro de Estado e das Finanças, o seguinte:

## Artigo 1.º — Objecto

*(Revogado)* — *Revogado pelo/a Artigo 44.º do/a Decreto-Lei n.º 28/2019 - Diário da República n.º 33/2019, Série I de 2019-02-15, em vigor a partir de 2019-02-16*

## Artigo 2.º — Utilização de programas de faturação

*(Revogado)* — *Revogado pelo/a Artigo 44.º do/a Decreto-Lei n.º 28/2019 - Diário da República n.º 33/2019, Série I de 2019-02-15, em vigor a partir de 2019-02-16*

## Artigo 3.º — Requisitos

A certificação dos programas de faturação depende da verificação cumulativa dos seguintes requisitos:

a) Ter a possibilidade de exportar o ficheiro a que se refere a Portaria n.º 321-A/2007, de 26 de Março;

b) Possuir um sistema que permita identificar a gravação do registo de faturas e documentos retificativos, através de um algoritmo de cifra assimétrica e de uma chave privada de conhecimento exclusivo do produtor do programa;

c) Possuir um controlo do acesso ao sistema informático, obrigando a uma autenticação de cada utilizador;

d) Não dispor de qualquer função que, no local ou remotamente, permita alterar, directa ou indirectamente, a informação de natureza fiscal, sem gerar evidência agregada à informação original.

e) Observar os demais requisitos técnicos aprovados por despacho do diretor-geral da AT.

- *Alterado pelo/a Artigo 3.º do/a [Portaria n.º 160/2013 - Diário da República n.º 79/2013, Série I de 2013-04-23](https://diariodarepublica.pt/dr/detalhe/portaria/160-2013-260384), em vigor a partir de 2013-04-28*
- *Alterado pelo/a Artigo 2.º do/a [Portaria n.º 22-A/2012 - Diário da República n.º 17/2012, 1º Suplemento, Série I de 2012-01-24](https://diariodarepublica.pt/dr/detalhe/portaria/22-a-2012-402697), produz efeitos a partir de 2012-04-01*

## Artigo 4.º — Obrigações

As empresas produtoras de software, antes da comercialização dos programas, para efeitos de certificação, devem enviar à AT:

a) Uma declaração de modelo oficial, aprovado por despacho do Ministro das Finanças;

b) A chave pública que permita validar a autenticidade e integridade do conjunto de dados a que se refere o artigo 6.º, assinados com a correspondente chave privada.

## Artigo 5.º — Emissão do certificado

1 - A AT emite, no prazo de 30 dias a contar da recepção da declaração referida no artigo anterior, o correspondente certificado do programa.

2 - A emissão do certificado pode ser precedida de testes de conformidade devendo, para o efeito, o produtor do programa ser notificado, ficando suspenso o prazo previsto no número anterior até à conclusão dos respectivos testes.

3 - Para verificação do cumprimento dos requisitos previstos no artigo 3.º, a AT pode, ainda, em qualquer momento, efectuar testes de conformidade, devendo o produtor do software disponibilizar um exemplar do programa e a documentação necessária, incluindo o dicionário de dados.

4 - A AT mantém no seu sítio, na Internet, uma lista actualizada dos programas e respectivas versões certificadas, bem como a identificação dos produtores.

5 - A versão certificada de um programa de faturação tem de observar os correspondentes requisitos, ainda que seja utilizada por sujeito passivo não obrigado a ter programa certificado.

- *Alterado pelo/a Artigo 2.º do/a [Portaria n.º 22-A/2012 - Diário da República n.º 17/2012, 1º Suplemento, Série I de 2012-01-24](https://diariodarepublica.pt/dr/detalhe/portaria/22-a-2012-402697), produz efeitos a partir de 2012-04-01*

## Artigo 6.º — Sistema de identificação

1 - O sistema de identificação a que se refere a alínea b) do artigo 3.º deve utilizar o algoritmo de cifra assimétrica RSA, recebendo como argumento os seguintes dados concatenados, pela ordem indicada, com o separador «;» (ponto e vírgula), que constituem a mensagem a assinar com a chave privada, constantes da tabela 4.1 - Documentos comerciais a clientes (SalesInvoices):

a) A data de criação do documento de venda [campo 4.1.4.6 - data do documento de venda (InvoiceDate) do SAF-T (PT)];

b) A data e hora da criação do documento de venda [campo 4.1.4.11 - data de gravação do documento (SystemEntryDate) do SAF-T (PT)];

c) O número do documento de venda [campo 4.1.4.1 - identificação única do documento de venda (InvoiceNo) do SAF-T (PT)];

d) O valor do documento de venda [campo 4.1.4.19.3 - total do documento com impostos (GrossTotal) do SAF-T (PT)];

e) A assinatura gerada no documento anterior, do mesmo tipo e série de documento [campo 4.1.4.3 - chave do documento (Hash) do SAF-T (PT)].

2 - A assinatura resultante do disposto no número anterior e a versão da chave privada de encriptação devem ficar guardadas na base de dados do programa de facturação.

3 - Os documentos assinados, nos termos do n.º 1, devem conter impresso:

a) Um conjunto de quatro caracteres da assinatura a que se refere o número anterior, correspondentes à 1.ª, 11.ª, 21.ª e 31.ª posições, e separado por hífen;

b) O número do certificado atribuído ao respetivo programa, utilizando para o efeito a expressão "Processado por programa certificado n.º...";

c) A identificação única dos documentos, conforme alínea c) do n.º 1 do presente artigo e pontos iii) das alíneas a) e b) do n.º 2 do artigo seguinte.

- *Alterado pelo/a Artigo 1.º do/a [Portaria n.º 340/2013 - Diário da República n.º 227/2013, Série I de 2013-11-22](https://diariodarepublica.pt/dr/detalhe/portaria/340-2013-503842), em vigor a partir de 2014-01-01*
- *Alterado pelo/a Artigo 3.º do/a [Portaria n.º 160/2013 - Diário da República n.º 79/2013, Série I de 2013-04-23](https://diariodarepublica.pt/dr/detalhe/portaria/160-2013-260384), em vigor a partir de 2013-04-28*

## Artigo 7.º — Documentos de transporte e outros

1 - São ainda assinados nos termos do artigo 6.º:

a) Os documentos, nomeadamente, guias de transporte ou de remessa, que sirvam de documento de transporte, de acordo com o disposto no regime de bens em circulação, aprovado pelo Decreto-Lei n.º 147/2003, de 11 de julho;

b) Quaisquer outros documentos, independentemente da sua designação, suscetíveis de apresentação ao cliente para conferência de entrega de mercadorias ou da prestação de serviços, nomeadamente as designadas consultas de mesa.

2 - Para efeitos do disposto no número anterior, devem ser utilizados os seguintes dados:

a) No caso da tabela 4.2 - Documentos de movimentação de mercadorias (MovementOfGoods):

i) A data de criação do documento de movimentação de mercadorias [campo 4.2.3.6 - data do documento de movimentação de mercadorias (MovementDate) do SAF-T (PT)];

ii) A data e hora da criação do documento de movimentação de mercadorias [campo 4.2.3.8 - data de gravação do documento (SystemEntryDate) do SAF-T (PT)];

iii) O número do documento de movimentação de mercadorias [campo 4.2.3.1 - identificação única do documento de movimentação de mercadorias (DocumentNumber) do SAF-T (PT)];

iv) O valor do documento de movimentação de mercadorias [campo 4.2.3.21.3 - total do documento com impostos (GrossTotal) do SAF-T (PT)];

v) A assinatura gerada no documento anterior, do mesmo tipo e série do documento [campo 4.2.3.3 - chave do documento (Hash) do SAF-T (PT)].

b) No caso da tabela 4.3 - Documentos de conferência de entrega de mercadorias ou da prestação de serviços (WorkingDocuments):

i) A data de criação do documento de conferência [campo 4.3.4.6 - data do documento (WorkDate) do SAF-T (PT)];

ii) A data e hora da criação do documento de conferência [campo 4.3.4.10 - data de gravação do documento (SystemEntryDate) do SAF-T (PT)];

iii) O número do documento de conferência [campo 4.3.4.1 - identificação única do documento (DocumentNumber) do SAF-T (PT)];

iv) O valor do documento de conferência [campo 4.3.4.13.3 - total do documento com impostos (GrossTotal) do SAF-T (PT)];

v) A assinatura gerada no documento anterior, do mesmo tipo e série do documento [campo 4.3.4.3 - chave do documento (Hash) do SAF-T (PT)].

- *Alterado pelo/a Artigo 3.º do/a [Portaria n.º 160/2013 - Diário da República n.º 79/2013, Série I de 2013-04-23](https://diariodarepublica.pt/dr/detalhe/portaria/160-2013-260384), em vigor a partir de 2013-04-28*
- *Aditado pelo/a Artigo 3.º do/a [Portaria n.º 22-A/2012 - Diário da República n.º 17/2012, 1º Suplemento, Série I de 2012-01-24](https://diariodarepublica.pt/dr/detalhe/portaria/22-a-2012-402697), produz efeitos a partir de 2012-04-01*

## Artigo 8.º — Utilização de faturas impressas em tipografias

*(Revogado)* — *Revogado pelo/a Artigo 44.º do/a Decreto-Lei n.º 28/2019 - Diário da República n.º 33/2019, Série I de 2019-02-15, em vigor a partir de 2019-02-16*

## Artigo 9.º — Documentos emitidos por máquinas registadoras

*(Revogado)* — *Revogado pelo/a Artigo 44.º do/a Decreto-Lei n.º 28/2019 - Diário da República n.º 33/2019, Série I de 2019-02-15, em vigor a partir de 2019-02-16*

## Artigo 10.º — Revogação do certificado

O membro do Governo responsável pela área das finanças, por proposta do director-geral dos Impostos, pode determinar a revogação do certificado emitido nos termos do artigo 5.º, quando deixarem de ser observados os requisitos previstos no artigo 3.º

- *Alterado pelo/a [Portaria n.º 22-A/2012 - Diário da República n.º 17/2012, 1º Suplemento, Série I de 2012-01-24](https://diariodarepublica.pt/dr/detalhe/portaria/22-a-2012-402697), produz efeitos a partir de 2012-04-01*

## Artigo 11.º — Alteração à Portaria n.º 1192/2009

*(Revogado)* — *Revogado pelo/a Artigo 4.º do/a Portaria n.º 160/2013 - Diário da República n.º 79/2013, Série I de 2013-04-23, em vigor a partir de 2013-04-28*

## Assinatura

O Ministro de Estado e das Finanças, Fernando Teixeira dos Santos, em 7 de Maio de 2010.
