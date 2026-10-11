---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ROADMAP_EXECUCAO_E_VALIDACAO"
fase: "GOVERNANCA_E_INVENTARIO"
id_documento: "BM-ROADMAP-EXECUCAO-00-08-001"
titulo: "BRICKMASTER RAIZ — Roadmap de execução e validação (Fases 00–08)"
status: "EXPERIMENTAL"
versao: "1.0.7"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Decisões e instruções do projeto BRICKMASTER RAIZ; histórico Git preservado"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/roadmap-execucao-fases-00-08"
escopo: "Roadmap, critérios de passagem, governança de fases 00–08 e salvaguardas"
objetivo: "Ordenar a verificação, correção, execução e publicação com evidência verificável"
dependencias: "GOVERNANCA/NORMA-CABECALHO-PADRAO.md; Manual NTSL 4.4; FVG-ATLAS; BRICKMASTER_GERAL"
---

# BRICKMASTER RAIZ — Roadmap de execução e validação (Fases 00–08)

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Tipo:** ROADMAP DE EXECUÇÃO E VALIDAÇÃO  
> **Fase:** GOVERNANÇA E INVENTÁRIO  
> **ID:** BM-ROADMAP-EXECUCAO-00-08-001  
> **Estado:** EXPERIMENTAL — plano de execução, não certificação técnica  
> **Versão:** 1.0.1  
> **Criação:** 2026-10-11  
> **Atualização:** 2026-10-11  
> **Rastreabilidade:** feat/roadmap-execucao-fases-00-08

## Contexto Histórico

Este documento formaliza a sequência de trabalho do BRICKMASTER RAIZ sem substituir os artefactos técnicos nem apagar decisões históricas. A verificação do repositório confirmou uma norma documental e um workflow GitHub Actions que exige Front Matter YAML, campos obrigatórios e secções padronizadas. A versão 1.0.0 do roadmap usava um comentário HTML em vez desse formato; foi identificada uma incompatibilidade estática e esta versão corrige o cabeçalho antes de qualquer integração. A correção documental não constitui validação de trading.

## Estado

**Estado geral:** EM EXECUÇÃO. Nenhuma fase técnica é considerada concluída apenas por estar documentada.

**Regra de publicação:** feature → develop → validação baseada em evidências → principal. A existência da branch `develop` deve ser verificada antes de exigir esse percurso; não criar nem presumir uma branch sem decisão registada.

**Regra de segurança:** este roadmap não envia ordens. Execução financeira permanece desativada por padrão até aprovação explícita e validação independente.

### Correção de contagem

O plano possui nove etapas numeradas de 00 a 08: uma fase 00 de inventário/rastreabilidade, que funciona como portão de entrada, e oito fases de implementação (01–08). A fase 00 não será eliminada para forçar a contagem a oito.

### Quadro de execução

| Etapa | Escopo | Entregável mínimo | Critério de aceitação | Estado |
|---|---|---|---|---|
| 00 — Inventário e rastreabilidade | Fontes, versões, módulos, branches, workflows, testes e dívidas técnicas; preservar históricos | Inventário com referências, matriz de evidências e decisões | Fontes críticas identificadas; conflitos registados sem invenção | PARCIAL — snapshot de 212 artefactos; auditoria semântica pendente |
| 01 — Arquitetura e governança | Contratos de módulos, dependências, versionamento, estados e fluxo de branches | Arquitetura de referência, ADRs, regras de integração e checkpoint mestre | Cobertura documental comparada com a estrutura real e CI | PARCIAL |
| 02 — Dados, sessão e abertura | Fontes, timestamps, sessão B3, abertura do dia, qualidade, atraso e reconciliação | Contrato de dados/sessão com proveniência e freshness | Dados ausentes, atrasados ou contraditórios reduzem confiança ou bloqueiam consumo; abertura reproduzível | CONTRATO INICIAL DOCUMENTADO; IMPLEMENTAÇÃO PENDENTE |
| 03 — Estado do gráfico / Giroscópio | Instrumento, tipo de gráfico, ticks incluindo 60K, sessão, localização do preço e confiança | Máquina de estados e contrato de contexto | Estado explica a posição operacional; transições determinísticas; contexto inválido bloqueia sinal | CONTRATO INICIAL DOCUMENTADO; IMPLEMENTAÇÃO/TESTES PENDENTES |
| 04 — Estrutura e módulos de mercado | Inventariar FVG-ATLAS, liquidez, VWAP/TWAP, delta cumulativo, volume financeiro, VIX, IBOV e Market DNA conforme fontes disponíveis | Catálogo de módulos com contratos, dependências e testes isolados | Definições objetivas, limites e testes próprios; sem dados presumidos | PARCIAL — FVG-ATLAS inventariado; restantes módulos por auditar |
| 05 — Decisão e risco soberano | Separar inteligência, sinal, decisão, dimensionamento, limites de perda, bloqueios e meta experimental de 1% | Contrato de decisão e camada soberana de risco | Risco pode vetar qualquer sinal; meta de 1% desde a abertura é hipótese, nunca garantia | PENDENTE |
| 06 — NTSL, Profit, execução conciliada e Watchdog | Compatibilidade NTSL 4.4, comportamento no Profit, ordens/posições, reconciliação e monitorização | Código isolado, matriz de compatibilidade, watchdog e eventos | Compilação e testes documentados; estado conciliado com plataforma; sem ordens reais por padrão | PARCIAL — revisão estática de candidato de volume; compilação/Profit pendentes |
| 07 — Testes, replay e backtest | Testes unitários/contratuais, falhas, replay, backtest e gráficos atemporais/ticks | Plano de testes, datasets identificados, resultados e limitações | Resultados reproduzíveis, custos e limitações explícitos; sem alegar rentabilidade futura | PENDENTE |
| 08 — Integração e produção | Integrar módulos aprovados, observabilidade, rollback, configuração e lançamento | Release candidate, checklist de produção e plano de reversão | Portões anteriores aprovados, CI verde e aprovação explícita para execução | PENDENTE |

### Arquitetura obrigatória

1. **Dados:** ingestão, normalização, timestamp, proveniência, qualidade e frescura.
2. **Inteligência:** interpretação do contexto e hipóteses/sinais, sem executar ordens.
3. **Decisão:** regras explícitas e explicáveis; não substitui a camada de risco.
4. **Risco soberano:** pode bloquear sinais e execução; prevalece sobre metas e módulos.
5. **Execução conciliada:** estado de ordens e posições reconciliado com o Profit; desativado por padrão.
6. **Watchdog:** deteta dados obsoletos, perda de ligação, divergência de estado e falhas; em falha, reduz confiança ou bloqueia.

O **Giroscópio** consolida o contexto e informa ao operador a sua posição operacional no gráfico. Não é sinal autónomo nem autorização para negociar.

### Correspondência com as camadas detalhadas da baseline arquitetural

A lista de seis domínios acima é uma vista lógica resumida; não substitui nem renumera as camadas L0–L9 definidas em `ARQUITETURA/BRICKMASTER_RAIZ/ARQUITETURA_MODULAR_BASELINE_2026-10-11.md`.

| Domínio lógico do roadmap | Camadas detalhadas | Regra de fronteira |
|---|---|---|
| Dados | L0 — Dados e integridade; L1 — Relógio e estado da sessão | Entrega dados com proveniência, qualidade e estado de sessão; não produz decisão de trading |
| Inteligência | L2 — Giroscópio; L3 — Estrutura de preço; L4 — Fluxo; L5 — Calendário macroeconómico | Produz contexto e eventos observáveis, não ordens |
| Decisão | L6 — Motor de hipóteses e confluência | Produz hipótese/sinal explicável, sujeito ao veto do risco |
| Risco soberano | L7 — Risco e objetivo diário | Pode bloquear decisão e execução, independentemente do sinal |
| Execução conciliada | L8 — Execução NTSL | Recebe apenas decisões autorizadas; permanece desativada por padrão |
| Watchdog | L9 — Observabilidade e auditoria | Monitora freshness, sessão, falhas e divergências; não autoriza operação |

Esta correspondência evita que a vista resumida de seis domínios seja interpretada como substituição da arquitetura detalhada existente.

### Critérios comuns de passagem

Uma fase só pode mudar para **VALIDADA** se houver: (1) contrato e critérios de aceitação; (2) alterações isoladas e rastreáveis; (3) testes reproduzíveis; (4) evidência anexada ou ligada ao checkpoint; (5) limitações e riscos registados; (6) revisão sem regressões conhecidas. DOCUMENTADA, IMPLEMENTADA, TESTADA e VALIDADA são estados distintos.

## Evidências

- Repositório oficial consultado: https://github.com/carlos-andrade/BRICKMASTER_GERAL
- Norma documental consultada: `GOVERNANCA/NORMA-CABECALHO-PADRAO.md`.
- Validador consultado: `scripts/validar_cabecalhos_markdown.sh`; exige Front Matter YAML, 17 campos e seis secções.
- Workflow consultado: `.github/workflows/validar-cabecalhos-documentais.yml`; executa o validador em pull requests e em pushes nas branches configuradas.
- Branch de trabalho: `feat/roadmap-execucao-fases-00-08`.
- PR de documentação: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/4
- Commit inicial do roadmap: `af6fc5287f39d6751ae79a39fd1186f184d1f3fe`.
- Manual NTSL prioritário indicado pelo projeto: versão 4.4, datada de 03/08/2026.
- Não há, neste documento, evidência de compilação NTSL, teste no Profit, backtest, replay ou execução de ordens.

## Validação

**Validação estática do conteúdo:** o cabeçalho e as secções foram ajustados para corresponder ao contrato do validador observado no repositório. A execução efetiva do workflow no GitHub Actions ainda deve ser consultada após o commit; não se declara CI verde nesta versão.

**Validação técnica de trading:** PENDENTE. A correção deste documento não comprova comportamento do código, compatibilidade com NTSL 4.4, desempenho nem prontidão de produção.

**Limitação de branches:** a consulta inicial não encontrou branch `develop`; a política deve ser decidida e documentada antes de integração em principal.

## Resultado

Roadmap versionado com nove etapas explícitas (00–08), oito fases de implementação (01–08), arquitetura em camadas, critérios de passagem e salvaguardas de risco. Estado EXPERIMENTAL até validação por evidência.

## Próxima Ação

1. Executar/observar o workflow de cabeçalhos no PR #4 e corrigir qualquer falha real reportada.
2. Completar o inventário recursivo da Fase 00 com caminhos, refs, hashes/versões e estado dos artefactos, preservando o histórico.
3. Comparar os documentos de arquitetura e o Módulo 001 com os contratos do roadmap.
4. Registar a decisão sobre a branch `develop` e o fluxo de promoção.
5. Só depois iniciar alterações funcionais às fases 02 e 03.

## Checkpoint de continuidade — 2026-10-11

### Inventário FVG-ATLAS — fase 04 iniciada

- Repositório externo consultado: `carlos-andrade/FVG-ATLAS`, branch `main`.
- Snapshot: 249 blobs, árvore recursiva não truncada, SHA `379115a60f70d8835f1fa71278dd344e6a253bd0`.
- Código de referência identificado pelo roadmap externo: `FVG_ATLAS_V2.1.33_REGRESSAO_INTEGRADA_LATCH_HISTORICO.src`, blob SHA `1294ff5054754060ac52dd87b368c6e474e6179d`.
- O roadmap externo declara V2.1.33 aprovada para regressão integrada do ciclo de vida e ainda lista pendências para congelamento formal, FVG Engine científico, MFE/MAE/FILL, base de dados, observabilidade, testes de stress e validação estatística.
- Relatório BRICKMASTER: `GOVERNANCA/INVENTARIO_FVG_ATLAS_FASE04_2026-10-11.md`.
- O registo mestre foi atualizado para marcar o inventário FVG como inicial/concluído e para registar Market DNA como lacuna de inventário: não foi identificado como módulo na árvore `BRICKMASTER_GERAL/main` consultada. Isso não prova que não exista noutro histórico/conversa.
- A evidência de regressão é proveniente da documentação FVG-ATLAS; não é teste executado nesta sessão, nem prova de integração ou compatibilidade Profit/NTSL no BRICKMASTER.

### Inventário de candidatos de fluxo — fase 04 em curso

- Foram identificados candidatos existentes para VWAP, TWAP, delta e volume financeiro em `ROBÔ_TRADE/` e `BRICKMASTER_CLAUDE/CÓDIGO NTSL/`; os caminhos e hashes constam em `GOVERNANCA/INVENTARIO_CANDIDATOS_FLUXO_FASE04_2026-10-11.md`.
- O código `BRICKMASTER_CumulativeVolume_Standalone.src` declara no comentário inicial Manual NTSL v4.2; compatibilidade com Manual 4.4 ainda não foi verificada.
- Os códigos de delta encontrados têm nomes/limitações associados a Renko; não devem ser presumidos compatíveis com gráficos de ticks/60K.
- Giroscópio, Liquidez, Contador de Toques e Watchdog não foram encontrados por nome de ficheiro na árvore atual; a auditoria semântica continua parcial e a ausência por nome não prova inexistência em históricos ou outros repositórios.
- Market DNA foi acrescentado ao registo como lacuna de inventário; nenhuma implementação foi presumida.

### Revisão estática NTSL 4.4 — candidato Cumulative Volume

- Documento: `GOVERNANCA/REVISAO_ESTATICA_CUMULATIVE_VOLUME_NTSL44.md`.
- Manual 4.4 consultado: confirma `Volume` como volume financeiro por candle (secção 4.2), `Date()` como data do candle (16.15), `Time()` como hora de abertura do candle (16.55) e arrays estáticos (4.3).
- Achados registados: limites de sessão sem bloqueio explícito antes da hora inicial/depois da hora final; atribuição por hora de abertura pode deslocar volume de candles que cruzam fronteiras em gráficos de ticks; “Welford” é descrição imprecisa para o cálculo de média implementado.
- Nenhum teste Profit/replay/backtest foi executado. O código legado permanece sem alteração e não está aprovado para integração.

### Contratos iniciais das fases 02 e 03

- Módulo 002: `MODULOS/002-RELOGIO-SESSAO-ABERTURA/ESPECIFICACAO.md` e `tests/PLANO-DE-TESTES.md`.
- Módulo 003: `MODULOS/003-GIROSCOPIO/ESPECIFICACAO.md` e `tests/PLANO-DE-TESTES.md`.
- O contrato do Módulo 002 mantém a definição da abertura como decisão em aberto e bloqueia referência se a política não estiver confirmada.
- O contrato do Giroscópio separa localização/contexto de sinal, decisão, risco e execução; não usa score numérico arbitrário nem considera módulos não validados como entradas essenciais.
- Os planos têm casos de teste identificados, todos NOT_RUN. Nenhum código foi implementado nesta etapa.


- O PR #4 foi integrado em `develop` após sucesso do workflow documental; `main` não foi alterada.
- A branch `develop` foi criada a partir de `main` para cumprir o fluxo feature → develop → validação → main.
- O snapshot recursivo em `GOVERNANCA/INVENTARIO_FASE_00_SNAPSHOT_2026-10-11.md` regista 212 blobs na árvore de `main`, com `truncated=false`; a diferença para os 209 ficheiros do inventário anterior foi reconciliada com os três novos artefactos do PR #2.
- O workflow de cabeçalhos documentais passou no head do PR: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/38181403462
- A revisão focalizada do Módulo 001 encontrou notação matemática ambígua na lista de percentagens; a especificação foi clarificada por tabela e o changelog atualizado. Nenhum código NTSL foi alterado.
- O Módulo 001 continua sem implementação NTSL na sua pasta e o plano de testes continua marcado como não executado; logo, não está aprovado para integração.
- A diferença entre 209 e 212 ficheiros foi reconciliada com os três artefactos adicionados no PR #2 (norma documental, workflow e script de validação). A Fase 00 continua PARCIAL porque a auditoria semântica de todos os artefactos ainda não foi concluída.

## Histórico de versões

- 1.0.0 — 2026-10-11 — formalização inicial do roadmap 00–08.
- 1.0.1 — 2026-10-11 — correção do cabeçalho para Front Matter YAML e inclusão das secções obrigatórias após auditoria do validador documental.
- 1.0.2 — 2026-10-11 — inventário estrutural registado, correspondência entre domínios lógicos e camadas L0–L9 clarificada e checkpoint de continuidade acrescentado.
- 1.0.3 — 2026-10-11 — reconciliação da contagem histórica de ficheiros e correção do estado do inventário.
- 1.0.4 — 2026-10-11 — inventário inicial FVG-ATLAS registado, fase 04 marcada parcial e lacuna Market DNA identificada.
- 1.0.5 — 2026-10-11 — candidatos legados de fluxo/VWAP/TWAP/volume inventariados e limites de compatibilidade registados.
- 1.0.6 — 2026-10-11 — revisão estática de candidato Cumulative Volume confrontada com Manual NTSL 4.4; testes de plataforma continuam pendentes.
- 1.0.7 — 2026-10-11 — contratos iniciais e planos de teste para as fases 02/03 registados; implementação e testes permanecem pendentes.
