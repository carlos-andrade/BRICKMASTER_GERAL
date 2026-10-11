<!--
Projeto: BRICKMASTER RAIZ
Documento: ROADMAP_EXECUCAO_FASES_00_08.md
Versao: 1.0.0
Estado: EXPERIMENTAL — plano de execução, não certificação técnica
Data: 2026-10-11
Responsável: Arquitetura BRICKMASTER RAIZ
Fonte principal: https://github.com/carlos-andrade/BRICKMASTER_GERAL
Referências: Manual NTSL 4.4 (03/08/2026); FVG-ATLAS; repositório BRICKMASTER_GERAL
--->

# BRICKMASTER RAIZ — Roadmap de execução e validação (Fases 00–08)

**Estado geral:** EM EXECUÇÃO — nenhuma fase é considerada concluída apenas por estar documentada.
**Regra de publicação:** feature → develop → validação baseada em evidências → principal.
**Regra de segurança:** nenhuma ordem real é enviada por este roadmap; execução financeira permanece desativada até aprovação explícita e validação independente.

## Correção de contagem

O plano registado possui **nove etapas numeradas de 00 a 08**: uma fase 00 de inventário/rastreabilidade, que funciona como portão de entrada, e oito fases de implementação (01–08). Não se deve apagar a fase 00 para forçar a contagem a oito; ela protege o histórico e evita construir sobre pressupostos não verificados.

## Critérios comuns de passagem

Cada fase só pode mudar para VALIDADA se houver: (1) contrato e critérios de aceitação; (2) alterações isoladas e rastreáveis; (3) testes reproduzíveis; (4) evidência anexada ou ligada ao checkpoint; (5) limitações e riscos registados; (6) revisão sem regressões conhecidas. DOCUMENTADA, IMPLEMENTADA, TESTADA e VALIDADA são estados distintos.

## Quadro de execução

| Etapa | Escopo | Entregável mínimo | Critério de aceitação | Estado inicial |
|---|---|---|---|---|
| 00 — Inventário e rastreabilidade | Fontes, versões, módulos, branches, workflows, testes e dívidas técnicas; preservar históricos | Inventário com refs, matriz de evidências e decisões | Nenhuma fonte crítica omitida; conflitos registados sem resolução inventada | PENDENTE |
| 01 — Arquitetura e governança | Contratos de módulos, dependências, versionamento, estados e fluxo de branches | Arquitetura de referência, ADRs, regras de integração e checkpoint mestre | PARCIAL — documentação existente; validar cobertura |
| 02 — Dados, sessão e abertura | Fontes, timestamps, sessão B3, abertura do dia, qualidade, atraso e reconciliação | Contrato de dados e estado de sessão; proveniência e freshness | Dados ausentes/atrasados/contraditórios reduzem confiança ou bloqueiam consumo; sessão e abertura reproduzíveis | PARCIAL — especificação incompleta |
| 03 — Estado do gráfico / Giroscópio | Contexto operacional: instrumento, tipo de gráfico, ticks (incluindo 60K), sessão, localização do preço e confiança | Máquina de estados e contrato de contexto | Estado explica onde o operador está no gráfico; transições determinísticas; contexto inválido bloqueia sinal | POR ESPECIFICAR/VALIDAR |
| 04 — Estrutura e módulos de mercado | Inventariar FVG-ATLAS, liquidez, VWAP/TWAP, delta cumulativo, volume financeiro, VIX, IBOV e Market DNA conforme fontes disponíveis | Catálogo de módulos com contrato, entradas, saídas, dependências e testes isolados | Cada módulo tem definição objetiva, limites e testes próprios; sem dados presumidos | PENDENTE DE INVENTÁRIO |
| 05 — Decisão e risco soberano | Separar inteligência, sinal, decisão, sizing, limites de perda, bloqueios e meta experimental de 1% | Contrato de decisão e camada soberana de risco | Risco pode vetar qualquer sinal; meta de 1% desde a abertura é hipótese, nunca garantia | PENDENTE |
| 06 — NTSL, Profit, execução conciliada e Watchdog | Validar compatibilidade NTSL 4.4, comportamento no Profit, ordens/posições, reconciliação e monitorização | Código isolado, matriz de compatibilidade, watchdog e eventos | Compilação e testes documentados; estado conciliado com plataforma; sem ordens reais por padrão | PENDENTE |
| 07 — Testes, replay e backtest | Testes unitários/contratuais, falhas, replay, backtest e gráficos atemporais/ticks | Plano de testes, datasets identificados, resultados e limitações | Resultados reproduzíveis, custos e limitações explícitos; sem alegar rentabilidade futura | PENDENTE |
| 08 — Integração e produção | Integrar módulos aprovados, observabilidade, rollback, configuração e lançamento | Release candidate, checklist de produção e plano de reversão | Portões anteriores aprovados; CI verde; aprovação explícita para execução | PENDENTE |

## Arquitetura obrigatória

1. **Dados:** ingestão, normalização, timestamp, proveniência, qualidade e freshness.
2. **Inteligência:** interpretação do contexto e hipóteses/sinais, sem executar ordens.
3. **Decisão:** regras explícitas e explicáveis; não substitui a camada de risco.
4. **Risco soberano:** pode bloquear sinais e execução; prevalece sobre metas e módulos.
5. **Execução conciliada:** estado de ordens e posições reconciliado com o Profit; desativado por padrão.
6. **Watchdog:** deteta dados obsoletos, perda de ligação, divergência de estado e falhas; em falha, reduz confiança ou bloqueia.

O **Giroscópio** consolida o contexto e informa ao operador a sua posição operacional no gráfico. Não é um sinal autónomo nem autorização para negociar.

## Plano de trabalho imediato

1. Fechar a Fase 00: inventariar o conteúdo real do repositório e artefactos ativos antes de alterar módulos.
2. Comparar documentos e branches existentes com este quadro; registar discrepâncias sem substituir históricos.
3. Auditar workflows de validação e o estado da regra de cabeçalho documental.
4. Completar a Fase 01 com contratos e critérios de passagem.
5. Avançar depois para dados/sessão (02) e Giroscópio (03), mantendo feature → develop → validação → principal.

## Checkpoint inicial — 2026-10-11

- Repositório oficial: https://github.com/carlos-andrade/BRICKMASTER_GERAL
- Branch de trabalho: feat/roadmap-execucao-fases-00-08
- Fonte NTSL prioritária: Manual NTSL 4.4, versão datada de 03/08/2026.
- Evidência recente observada no histórico GitHub: merge do PR #2 relativo à padronização dos cabeçalhos documentais (commit ac61750ca0e1413d127759b592a0bd296cf9f83e).
- Limitação: este checkpoint abre o plano; não comprova testes no Profit, validação de código NTSL, backtests ou prontidão de produção.
- Próximo checkpoint obrigatório: inventário de ficheiros e módulos com referências verificáveis, seguido da validação dos workflows e do estado real das branches.

## Histórico de versões

- 1.0.0 — 2026-10-11 — formalização do roadmap 00–08, critérios de passagem e salvaguardas de risco. Estado experimental até haver evidência técnica.