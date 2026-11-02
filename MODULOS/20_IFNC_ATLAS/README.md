<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: IFNC ATLAS — Portal do Módulo
IDENTIFICADOR: BM-020
VERSÃO: 0.1.0
ESTADO: DOCUMENTADO — EXPERIMENTAL — NÃO VALIDADO
CRIADO EM: 2026-11-02
ÚLTIMA REVISÃO: 2026-11-02
SHA-256: ver CHECKSUMS.sha256 (SHA-256 do conteúdo integral)
COMMIT DE REFERÊNCIA: 4f5b5ad608fd045e6b5d48d8603239264843e719
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-11-02 | v0.1.0 | Especificação inicial do módulo IFNC ATLAS.
FONTE DA VERDADE: repositório oficial; metodologia e dados oficiais da B3.
-->

# BRICKMASTER IFNC ATLAS

## Missão
Medir o comportamento do setor financeiro brasileiro e avaliar se esse contexto acrescenta informação útil à leitura do IBOV e do WIN, sem produzir ordens ou substituir os módulos de fluxo, estrutura, risco e decisão.

## Escopo
- Ativo de contexto: IFNC (índice financeiro da B3).
- Alvos prioritários: IBOV e WIN.
- Horizonte de pesquisa: intradiário e diário; janelas intradiárias de 5 e 30 minutos e agregação diária.
- Gráficos operacionais do BRICKMASTER: ticks, incluindo 60K trades. A série IFNC/IBOV não deve ser artificialmente convertida em ticks se a fonte não fornecer eventos nesse grão.
- Saída: estado setorial, força relativa, amplitude, divergência, qualidade e confiança.

## Não objetivos
- Não enviar ordens.
- Não determinar compra/venda isoladamente.
- Não presumir que o IFNC antecipa o WIN.
- Não prometer a meta de 1% desde a abertura.
- Não substituir BM-011 Intermercado, BM-001 Giroscópio, BM-014 Risco ou BM-016 Replay.

## Integração
- BM-018 Dados e Qualidade: proveniência, timestamps, atraso e integridade.
- BM-011 IBOV / Intermercado: sincronização e contexto de índice.
- BM-020 IFNC ATLAS: inteligência setorial.
- BM-001 Giroscópio: consolidação sem apagar divergências.
- BM-014 Risco: bloqueios e elegibilidade soberana.
- BM-016 Replay e Backtest: validação temporal.
- BM-017 Watchdog: saúde e alertas.

## Maturidade
DOCUMENTADO / EXPERIMENTAL. Não há implementação, backtest ou vantagem operacional comprovada neste checkpoint.

## Documentos
- SPEC.md — arquitetura e definições matemáticas.
- CONTRACTS.md — contratos de dados e integração.
- TESTS.md — plano de testes e critérios de aceite.
- ROADMAP.md — fases e gates.

## Referências
- B3 — Índice Financeiro IFNC: https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/indice-financeiro-ifnc-b3.htm
- B3 — Metodologia dos índices: consultar metodologia oficial vigente antes de cada atualização de carteira.
- BRICKMASTER RAIZ — BRICKMASTER_ARQUITETURA/README.md e CONTRATO_MODULO.md.
