---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "README_MODULO"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-README"
titulo: "Módulo 002 — Relógio, sessão e abertura"
status: "ESPECIFICACAO_INICIAL; IMPLEMENTACAO_PENDENTE"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Roadmap BRICKMASTER RAIZ e Manual NTSL 4.4"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase02-03-contracts"
escopo: "Instrumento, relógio, sessão e referência de abertura"
objetivo: "Fornecer estado temporal reproduzível e bloquear quando sessão/abertura não são fiáveis"
dependencias: "Manual NTSL 4.4; configuração oficial de sessão; Módulo 001"
---

# Módulo 002 — Relógio, sessão e abertura

## Contexto Histórico

O registo mestre identificava relógio/sessão/abertura como módulo fundador ainda por inventariar. O Manual NTSL 4.4 define `Date()` como data do candle e `Time()` como hora de abertura do candle, mas isso não determina por si só o preço oficial de abertura do pregão.

## Estado

ESPECIFICAÇÃO INICIAL. Sem implementação aprovada nesta pasta. A política de abertura e a sessão por instrumento permanecem por confirmar.

## Evidências

Roadmap BRICKMASTER, Manual NTSL 4.4 secções 16.15 e 16.55, e os documentos desta pasta.

## Validação

Contrato documentado; código, compilação, replay, teste Profit e gráfico de 60K ticks ainda não validados.

## Resultado

Módulo delimitado como fornecedor de estado temporal e referência de abertura; não produz sinais nem envia ordens.

## Próxima Ação

Confirmar a fonte da abertura, horários e política para candles que cruzam a transição da sessão; implementar e testar isoladamente.
