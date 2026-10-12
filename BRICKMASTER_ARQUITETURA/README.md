<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Arquitetura Modular BRICKMASTER
IDENTIFICADOR: BM-ARC-001
VERSÃO: 1.0.0
ESTADO: PROPOSTA INICIAL — NÃO VALIDADA EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-11
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-10-11 | v1.0.0 | Estrutura inicial modular e regras de governança.
FONTE DA VERDADE: documentação e código versionados neste repositório.
-->

# BRICKMASTER RAIZ — Arquitetura Modular

## Objetivo
Evoluir o BRICKMASTER para um sistema operacional de leitura de contexto de mercado, com módulos independentes, contratos explícitos, observabilidade, validação e integração controlada com a NTSL/Profit.

## Princípio central
O operador não deve ficar sem saber **onde está no gráfico, em que regime está o mercado, quais evidências sustentam a leitura e o que invalida essa leitura**.

## Regras arquiteturais
1. **Modularidade real:** cada módulo tem pasta própria, documentação inicial, estado, entradas, saídas, dependências, testes e critérios de aceite.
2. **Não presumir capacidade NTSL:** toda função/sintaxe deve ser conferida prioritariamente no Manual NTSL 4.4 (03/08/2026), distinguindo fato documentado, hipótese e teste pendente.
3. **Sem indicador “burro” por padrão:** construir medidas próprias com definições matemáticas, contexto, proveniência e validação; não proibir indicadores clássicos quando servirem como referência comparativa.
4. **Sem promessa de lucro:** metas, incluindo referência de +1% desde a abertura, são hipóteses de pesquisa, nunca garantias.
5. **Sem execução real por padrão:** desenvolvimento começa em análise, replay/backtest e simulação; execução automatizada exige gate formal de risco.
6. **Sem look-ahead:** cada sinal usa somente dados disponíveis no instante de decisão.
7. **Auditabilidade:** toda leitura relevante deve poder ser reconstruída com dados, versão, timestamp, parâmetros e motivo.
8. **Falha segura:** dado ausente, stale, inconsistente ou módulo crítico indisponível reduz confiança e pode bloquear sinal.
9. **Separação de responsabilidades:** detecção, contexto, decisão, risco, execução e telemetria não devem ser fundidos num bloco monolítico.
10. **Preservar o histórico:** não sobrescrever decisões antigas sem trilha; correções geram nova versão e registro de mudança.

## Mapa de alto nível
- **Camada 0 — Dados:** feed, qualidade, sincronização, calendário e sessões.
- **Camada 1 — Estado do gráfico:** posição relativa, estrutura, regime, níveis e referência de 1% desde a abertura.
- **Camada 2 — Microestrutura e evidências:** FVG, liquidez, volume, delta, VWAP/TWAP, volatilidade e rejeição.
- **Camada 3 — Contexto intermercado:** IBOV, VIX e eventos macroeconômicos, com disponibilidade e defasagem documentadas.
- **Camada 4 — Giroscópio:** agrega sinais sem apagar divergências; estima estado, confiança e invalidação.
- **Camada 5 — Decisão e risco:** elegibilidade, exposição, limites, bloqueios e auditoria.
- **Camada 6 — Adaptadores:** NTSL/Profit e ferramentas externas, isolados do núcleo conceitual.
- **Camada 7 — Observabilidade:** logs, replay, métricas, watchdog e relatórios.

## Estado de maturidade
Esta estrutura é uma arquitetura inicial. Não significa que os módulos já estejam implementados, compilados ou lucrativos.
