<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: IFNC ATLAS — Roadmap
IDENTIFICADOR: BM-020-ROADMAP
VERSÃO: 0.1.0
ESTADO: PLANEADO — EXPERIMENTAL
CRIADO EM: 2026-11-02
ÚLTIMA REVISÃO: 2026-11-02
SHA-256: consultar CHECKSUMS.sha256 após checkpoint
COMMIT DE REFERÊNCIA: checkpoint inicial da branch feature/ifnc-atlas
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-11-02 | v0.1.0 | Roadmap inicial.
FONTE DA VERDADE: repositório oficial.
-->

# ROADMAP — IFNC ATLAS

## Fluxo de branches
feature/ifnc-atlas -> develop -> validação formal -> principal.
Não fazer merge em principal antes dos gates. Não reescrever histórico; correções incrementais e commits rastreáveis.

## Fase 0 — Baseline e inventário
- [x] Consultar README, arquitetura, governança, mapa, contrato e roadmap do BRICKMASTER_GERAL.
- [x] Criar branch feature/ifnc-atlas a partir de develop.
- [ ] Inventariar BM-011, BM-018, BM-001, BM-016 e dados históricos disponíveis.
- [ ] Congelar baseline e registar commit/hash.
Gate: dependências e fontes confirmadas.

## Fase 1 — Dados e histórico
- [ ] Definir fornecedor e granularidade real do IFNC.
- [ ] Capturar IFNC, IBOV e séries de WIN por contrato.
- [ ] Obter carteiras históricas oficiais, pesos, vigências e revisões.
- [ ] Implementar armazenamento bruto append-only e normalização.
- [ ] Construir quality gate, relógio e calendário.
Gate: cobertura, atraso e proveniência medidos; snapshots históricos auditáveis.

## Fase 2 — Feature Engine
- [ ] Implementar força relativa, divergência, breadth, participação ponderada e dispersão.
- [ ] Implementar volatilidade relativa.
- [ ] VWAP alignment somente se granularidade e dados forem adequados.
- [ ] Testes unitários e casos-limite.
Gate: fórmulas reproduzíveis e cobertura mínima aprovada.

## Fase 3 — Atlas State e integração
- [ ] Implementar estados descritivos e confidence de qualidade.
- [ ] Implementar adaptador BM-020 -> BM-001.
- [ ] Preservar contradições e invalidações.
- [ ] Integrar watchdog e logs.
Gate: testes de integração e falha segura aprovados.

## Fase 4 — Replay e pesquisa
- [ ] Implementar replay temporal sem look-ahead.
- [ ] Medir relação com IBOV e WIN em 5m, 30m e diário.
- [ ] Comparar com benchmarks sem IFNC.
- [ ] Walk-forward, fora da amostra, regimes e custos.
- [ ] Publicar relatório de resultados negativos e positivos.
Gate: evidência de incrementalidade ou decisão documentada de não prosseguir.

## Fase 5 — Paper / observação
- [ ] Monitorização em tempo real sem ordens.
- [ ] Aferir latência, estabilidade e divergências.
- [ ] Rever thresholds e alertas sem otimização sobre teste final.
Gate: aprovação formal para paper; nenhum uso de capital real por omissão.

## Fase 6 — Produção controlada
- [ ] Revisão independente de risco e segurança.
- [ ] Revisão de operação, watchdog e rollback.
- [ ] Aprovação explícita do proprietário.
Gate: autorização específica; IFNC ATLAS continua sem poder de execução.

## Checkpoint atual
2026-11-02: arquitetura e contratos documentados em branch de trabalho. Implementação e testes ainda pendentes.
