---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "README_MODULO"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-README"
titulo: "Módulo 002 — Relógio, sessão e abertura"
status: "POLITICA_B_APROVADA; IMPLEMENTACAO_PENDENTE"
versao: "0.2.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-12"
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

POLÍTICA B APROVADA em 2026-10-12: utilizar o preço oficial de abertura da plataforma ou de fonte oficial validada. A fonte/campo concreto por instrumento, a sessão oficial e a validação no Profit continuam pendentes; o módulo não está implementado.

## Evidências

Roadmap BRICKMASTER, Manual NTSL 4.4 secções 16.15 e 16.55, e os documentos desta pasta.

## Validação

Contrato documentado; código, compilação, replay, teste Profit e gráfico de 60K ticks ainda não validados.

## Resultado

Módulo delimitado como fornecedor de estado temporal e referência de abertura; não produz sinais nem envia ordens.

## Próxima Ação

Registar a fonte/campo oficial para o instrumento prioritário, confirmar sessão/horário e evidência de correspondência; implementar e testar isoladamente, incluindo gráficos de ticks/60K.

## Decisão registada — 2026-10-12

A opção B foi aprovada: preço oficial de abertura fornecido pela plataforma ou por fonte oficial validada. A aprovação define a política, não certifica uma fonte específica. Na ausência de referência fiável ou perante contradições, o estado permanece `UNKNOWN/INVALID` e os consumidores dependentes ficam bloqueados.

- 0.2.0 — 2026-10-12 — política B registada; implementação e fonte concreta pendentes.
