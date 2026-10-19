---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-ESPECIFICACAO"
titulo: "Contrato técnico — Relógio, sessão e abertura"
status: "POLITICA_DE_ABERTURA_APROVADA; IMPLEMENTACAO_PENDENTE"
versao: "0.2.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-12"
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

Contrato novo, sem substituir artefactos históricos. Em 2026-10-12 foi aprovada a política B: usar o preço oficial de abertura fornecido pela plataforma ou por uma fonte oficial validada. A aprovação da política não valida ainda uma fonte concreta nem a implementação.

## Estado

POLÍTICA APROVADA; IMPLEMENTAÇÃO PENDENTE. A regra de referência está decidida, mas a fonte concreta por instrumento, o horário oficial, o comportamento de leilões e os limites de frescura ainda têm de ser validados.

## Contrato

### Entradas
- Instrumento e contrato/vencimento, quando aplicável.
- Tipo de gráfico e configuração, incluindo ticks/60K.
- Data/hora do candle, proveniência e modo de dados (histórico/replay/tempo real).
- Definição versionada da sessão: início, fim, fuso e exceções.
- Fonte e política do preço oficial de abertura; identificação do campo oficial e prova de validação por instrumento/contrato.
- Indicadores de qualidade/frescura.

### Política operacional aprovada — opção B
A referência da sessão é o **preço oficial de abertura fornecido pela plataforma ou por uma fonte oficial validada**. Não usar o primeiro negócio observado, o primeiro candle visível nem o preço atual como substitutos automáticos.

A política está aprovada; a fonte concreta ainda precisa de ser registada por instrumento/contrato, com nome do fornecedor/plataforma, campo utilizado, significado do campo, timestamp, fuso, calendário/sessão, método de acesso, versão e evidência de correspondência com a abertura oficial. Não declarar uma fonte validada sem evidência observável e reproduzível.

Regras:
1. A plataforma/fonte principal deve ser configurada explicitamente por instrumento/contrato; não escolher silenciosamente uma fonte alternativa.
2. Uma fonte secundária só pode ser usada se tiver sido validada e aprovada previamente para esse instrumento e sessão.
3. Se o valor estiver ausente, atrasado além do limite medido/aprovado, for inválido ou houver contradição não resolvida entre fontes oficiais, manter a abertura `UNKNOWN`/ `INVALID` e bloquear os consumidores dependentes.
4. Não inferir o preço oficial a partir de `Time()`, do primeiro candle do gráfico, do primeiro negócio visto após carregar o gráfico ou de uma fórmula de NTSL sem prova de que representa o campo oficial.
5. O preço confirmado é imutável durante a sessão. Uma correção oficial da fonte exige evento auditável, nova versão da referência e política explícita de reprocessamento; não alterar silenciosamente os níveis.
6. O Módulo 001 só calcula/expõe níveis quando recebe referência `CONFIRMED`, identificada por instrumento, sessão, fonte e timestamp.

A decisão de política não constitui evidência de que o Profit disponibiliza o campo necessário no contexto NTSL escolhido. Isso será verificado no Manual NTSL 4.4 e no Profit real.

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
Módulo 001; configuração de sessão/calendário do instrumento; adaptador da plataforma/fonte oficial validada; registo de fontes aprovadas; Manual NTSL 4.4.

## Evidências

Manual NTSL 4.4, secções 4.2, 4.4, 16.45, 16.55 e 20.90; análise em `GOVERNANCA/AUDITORIA_FONTE_ABERTURA_OFICIAL_NTSL44.md`. O manual fornece candidatos (`OpenD(0)`, `OpenDaily(0)`, séries diárias), mas não certifica universalmente qualquer um como preço oficial em todos os contextos.

## Validação

Revisão estática do contrato. Não houve compilação nem execução. Critério de aceitação: mesmos dados/configuração geram mesmo `session_id`, estado e referência; ambiguidades bloqueiam.

## Resultado

Estados explícitos e bloqueios documentados. Módulo ainda não implementado nem validado.

## Próxima Ação

Usar a auditoria documental `GOVERNANCA/AUDITORIA_FONTE_ABERTURA_OFICIAL_NTSL44.md`; comparar os candidatos com o campo oficial no Profit para um instrumento e sessão definidos, incluindo gráfico de ticks/60K; só depois selecionar a fonte e implementar.

## Histórico de versões

- 0.1.0 — 2026-10-11 — primeiro contrato conceptual.

- 0.2.0 — 2026-10-12 — aprovada a política B: preço oficial de abertura da plataforma ou fonte oficial validada; fonte concreta e validação técnica continuam pendentes.
