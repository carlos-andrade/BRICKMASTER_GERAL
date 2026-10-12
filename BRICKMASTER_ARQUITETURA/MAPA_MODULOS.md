<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Catálogo de Módulos
IDENTIFICADOR: BM-CAT-001
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

# Catálogo de módulos

| ID | Módulo | Pasta | Papel | Estado inicial |
|---|---|---|---|---|
| BM-001 | Giroscópio / Estado do Mercado | `MODULOS/01_GIROSCOPIO` | Síntese de regime, localização e confiança | DOCUMENTADO |
| BM-002 | Estado do Gráfico | `MODULOS/02_ESTADO_GRAFICO` | Responder onde o operador está no gráfico | DOCUMENTADO |
| BM-003 | Market DNA | `MODULOS/03_MARKET_DNA` | Classificar comportamento e regime | DOCUMENTADO |
| BM-004 | Estrutura de Mercado | `MODULOS/04_ESTRUTURA_MERCADO` | Swings, deslocamento e mudança estrutural | DOCUMENTADO |
| BM-005 | FVG Atlas | `MODULOS/05_FVG_ATLAS` | Detectar, medir e acompanhar FVGs | DOCUMENTADO |
| BM-006 | Liquidez | `MODULOS/06_LIQUIDEZ` | Varredura, captura e retorno a pools | DOCUMENTADO |
| BM-007 | Contador de Toques | `MODULOS/07_CONTADOR_TOQUES` | Contagem e qualidade de reações em zonas | DOCUMENTADO |
| BM-008 | VWAP/TWAP Gap | `MODULOS/08_VWAP_TWAP` | Distância, convergência e regime de preço | DOCUMENTADO |
| BM-009 | Fluxo e Volume | `MODULOS/09_FLUXO_VOLUME` | Volume financeiro, delta e absorção | DOCUMENTADO |
| BM-010 | Volatilidade / VIX | `MODULOS/10_VOLATILIDADE_VIX` | Contexto de risco e volatilidade | DOCUMENTADO |
| BM-011 | IBOV / Intermercado | `MODULOS/11_INTERMERCADO_IBOV` | Contexto do índice e relações externas | DOCUMENTADO |
| BM-012 | Calendário Econômico | `MODULOS/12_CALENDARIO` | Eventos, janelas e bloqueios | DOCUMENTADO |
| BM-013 | Alvo +1% da Abertura | `MODULOS/13_ALVO_ABERTURA_1PCT` | Referência de preço e acompanhamento | DOCUMENTADO |
| BM-014 | Risco e Elegibilidade | `MODULOS/14_RISCO` | Limites, bloqueios e sizing | DOCUMENTADO |
| BM-015 | Adaptador NTSL/Profit | `MODULOS/15_ADAPTADOR_NTSL` | Implementação compatível com plataforma | DOCUMENTADO |
| BM-016 | Replay e Backtest | `MODULOS/16_REPLAY_BACKTEST` | Reprodutibilidade e avaliação | DOCUMENTADO |
| BM-017 | Watchdog / Observabilidade | `MODULOS/17_WATCHDOG` | Saúde, logs, alertas e kill switch | DOCUMENTADO |
| BM-018 | Dados e Qualidade | `MODULOS/18_DADOS_QUALIDADE` | Integridade, sincronização e proveniência | DOCUMENTADO |
| BM-019 | Marcação a Mercado | `MODULOS/19_MARK_TO_MARKET` | P&L, exposição e reconciliação | DOCUMENTADO |

Todos são especificações iniciais; não implicam implementação existente.
