<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Roadmap de Desenvolvimento
IDENTIFICADOR: BM-ROAD-001
VERSÃO: 1.0.0
ESTADO: PROPOSTA INICIAL — NÃO VALIDADA EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-19
SHA-256: 6cee6525bcef8f74cf0c81c39bcfa6ba3e55dc38387a8b26225f9d3907a43e11
COMMIT DE REFERÊNCIA: d1f91fdcae5d92ac56449b570022011ae7857e6b
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-10-11 | v1.0.0 | Estrutura inicial modular e regras de governança.
FONTE DA VERDADE: documentação e código versionados neste repositório.
-->

# Roadmap

## Fase 0 — Governança e inventário
- [ ] Inventariar código-fonte atual, módulos já existentes, dependências e duplicações.
- [ ] Mapear ideias existentes: FVG Atlas, contador de toques, Market DNA, liquidez e giroscópio.
- [ ] Definir contrato comum e cabeçalho oficial.
- [ ] Congelar baseline do código antes de refatorar.

## Fase 1 — Fundamentos verificáveis
- [ ] Modelo de dados e qualidade.
- [ ] Estado do gráfico e referência de +1% desde a abertura.
- [ ] Relógio/sessões e calendário econômico.
- [ ] Logs e replay determinístico.

## Fase 2 — Módulos de leitura
- [ ] Estrutura de mercado e Market DNA.
- [ ] FVG e mapa de zonas.
- [ ] Liquidez e varreduras.
- [ ] Contador de toques e reação.
- [ ] VWAP/TWAP e distância normalizada.
- [ ] Volume financeiro, delta e absorção — somente conforme disponibilidade real dos dados.
- [ ] Volatilidade realizada e contexto IBOV; VIX apenas como referência externa opcional, após validação de origem, atraso e relação estatística. A pasta autónoma `MODULOS/10_VOLATILIDADE_VIX` foi removida de `main` pelo PR #33.
- [ ] Giroscópio de estado.

## Fase 3 — Pesquisa e validação
- [ ] Definir rótulos de resultado e métricas antes de otimizar.
- [ ] Backtest sem look-ahead, com custos e slippage.
- [ ] Walk-forward e validação fora da amostra.
- [ ] Análise por horário, ativo, regime e eventos.
- [ ] Relatório de falsos positivos, drawdown e expectativa líquida.

## Fase 4 — Paper trading e operação
- [ ] Watchdog de dados, estratégia e execução.
- [ ] Kill switch e limites de perda.
- [ ] Reconciliação entre sinal, ordem, execução e posição.
- [ ] Aprovação formal antes de qualquer uso com capital real.

## Critério de avanço
Não avançar por entusiasmo ou por um backtest isolado. Cada fase exige evidência, critérios de aceite assinados e registro de limitações.
