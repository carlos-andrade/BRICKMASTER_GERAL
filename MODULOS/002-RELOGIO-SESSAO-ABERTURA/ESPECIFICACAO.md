---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-ESPECIFICACAO"
titulo: "Contrato técnico — Relógio, sessão e abertura"
status: "ESPECIFICACAO_INICIAL; DECISOES_OPERACIONAIS_PENDENTES"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Roadmap BRICKMASTER RAIZ; Manual NTSL 4.4"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase02-03-contracts"
escopo: "Contrato de dados temporais e preço de referência da abertura"
objetivo: "Definir entradas, estados, saídas e bloqueios determinísticos da sessão"
dependencias: "Manual NTSL 4.4; calendário/sessão do instrumento; Módulo 001"
---

# Contrato técnico — Relógio, sessão e abertura

## Contexto Histórico

Contrato novo, sem substituir artefactos históricos. A definição operacional da abertura não será presumida.

## Estado

ESPECIFICAÇÃO INICIAL — NÃO IMPLEMENTADA. Fonte de abertura, horário oficial por instrumento e tolerância máxima de atraso ainda por confirmar.

## Contrato

### Entradas
- Instrumento e contrato/vencimento, quando aplicável.
- Tipo de gráfico e configuração, incluindo ticks/60K.
- Data/hora do candle, proveniência e modo de dados (histórico/replay/tempo real).
- Definição versionada da sessão: início, fim, fuso e exceções.
- Fonte e política do preço de abertura.
- Indicadores de qualidade/frescura.

### Decisão operacional em aberto
Antes da implementação, aprovar exatamente uma política:
1. primeiro negócio observado após início oficial da sessão;
2. preço oficial de abertura fornecido pela plataforma/fonte;
3. abertura do primeiro candle elegível, apenas se a aproximação for explicitamente aceite e testada.

As opções não são intercambiáveis. Sem decisão e evidência, a abertura fica `UNKNOWN` e o Módulo 001 não fixa níveis como se a referência estivesse confirmada.

### Máquina de estados
- `UNKNOWN`: instrumento, relógio ou configuração ausente/ambígua.
- `PREOPEN`: antes da janela válida.
- `OPENING_PENDING`: sessão iniciada, referência ainda não confirmada.
- `ACTIVE`: sessão e abertura confirmadas segundo política aprovada.
- `CLOSED`: sessão terminou segundo configuração versionada.
- `INVALID`: dados temporais impossíveis/contraditórios ou referência inválida.

A transição para `ACTIVE` ocorre uma vez por sessão. A referência não é recalculada a cada candle/tick. Sessão nova recebe `session_id` novo.

### Saídas
`session_id`; `session_state`; início/fim/fuso; `opening_price`; fonte e versão da política; estado da abertura (`CONFIRMED/PENDING/UNKNOWN/INVALID`); timestamp, modo e frescura dos dados; códigos de motivo/bloqueio.

### Regras de qualidade
- Nunca substituir abertura ausente por preço atual ou primeiro preço visível ao carregar o gráfico.
- Dados temporais ausentes/atrasados/contraditórios reduzem confiança; se afetarem instrumento, sessão ou abertura, bloquear consumidores.
- Não inventar limites de atraso: configurá-los após medir a fonte.
- `Time()` no Manual 4.4 representa a hora de abertura do candle. Em gráficos de ticks, um candle pode cruzar a transição; o comportamento deve ser testado.
- Sem sinais de compra/venda e sem envio de ordens.

### Dependências
Módulo 001; configuração de sessão/calendário do instrumento; fonte de abertura aprovada; Manual NTSL 4.4.

## Evidências

Manual NTSL 4.4, secção 16.15 (`Date()`) e 16.55 (`Time()`); especificação atual do Módulo 001 mantém a política de abertura pendente.

## Validação

Revisão estática do contrato. Não houve compilação nem execução. Critério de aceitação: mesmos dados/configuração geram mesmo `session_id`, estado e referência; ambiguidades bloqueiam.

## Resultado

Estados explícitos e bloqueios documentados. Módulo ainda não implementado nem validado.

## Próxima Ação

Aprovar a fonte de abertura e horários por instrumento; implementar em branch isolada e executar o plano de testes.

## Histórico de versões

- 0.1.0 — 2026-10-11 — primeiro contrato conceptual.
