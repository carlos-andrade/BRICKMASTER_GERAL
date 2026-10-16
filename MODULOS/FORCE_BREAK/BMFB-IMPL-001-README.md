# BM_FORCE_BREAK — Regra de contabilização diária

| Campo | Valor |
|---|---|
| **ID** | BMFB-IMPL-001 |
| **Projeto** | BRICKMASTER RAIZ — BM_FORCE_BREAK |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | ESPECIFICACAO_TECNICA |
| **Fase** | FEATURE |
| **Estado** | EXPERIMENTAL |
| **Versão** | 0.3.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular conforme GOV-CAB-NORMA-001 v1.0.3 |
| **Commit de referência (versão anterior)** | [876f2017ae8ae5fe83d77605ea80dbf737d5a6f9](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/876f2017ae8ae5fe83d77605ea80dbf737d5a6f9) |
| **Data de criação** | 2026-10-17 |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente |
| **Origem** | Requisito do utilizador após observar contagens a incluir candles do dia anterior |
| **Autoridade superior** | [GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Dependências** | Profit/NTSL; séries Date, Close, Low, High; especificação BMFB-001 |
| **Rastreabilidade** | [Estudo BMFB-001](BMFB-001-FECHAMENTOS-MINIMAS-MAXIMAS.md); branch `feature/bm-force-break-001` |

## 1. Objetivo

Impedir que a visualização e os contadores do BM_FORCE_BREAK utilizem candles de uma data anterior à do candle avaliado.

## 2. Regra oficial de sessão diária

Para a barra atual, uma condição com distância N só pode ser avaliada se `Date = Date[N]`. Assim, o fechamento atual é comparado à máxima/mínima do candle N posições atrás somente quando ambos pertencem à mesma data de negociação apresentada pela série `Date` do Profit.

- N=1: exigir `Date = Date[1]`.
- N=2: exigir `Date = Date[2]`.
- N=3: exigir `Date = Date[3]`.

Na primeira barra em que `Date <> Date[1]`, todos os seis contadores são inicializados a zero. As condições N=1, 2 e 3 ficam bloqueadas quando a barra de referência pertence a outra data. A regra não pressupõe que exista uma barra exatamente na abertura; usa a data fornecida pelo Profit.

## 3. Artefactos

- `BMFB-001-INDICADOR-VISUAL.ntsl`: marcações B1–B3/A1–A3 apenas quando a barra de referência tem a mesma data.
- `BMFB-002-CONTADORES.ntsl`: seis contadores cumulativos reiniciados quando muda `Date`.

## 4. Isolamento e segurança

- Sem chamadas de compra, venda, cancelamento ou alteração de ordens.
- Sem integração automática com a estratégia operacional BRICKMASTER.
- Indicadores experimentais independentes.
- Os contadores representam somente as ocorrências do dia da barra, dentro do histórico que o Profit calcula.

## 5. Evidência e validação

O utilizador informou que a versão anterior compilou no Profit e forneceu uma captura de gráfico onde aparecem etiquetas em sequência. A captura motiva a correção, mas não demonstra por si só os valores OHLC nem valida a nova regra diária.

A versão 0.2.0 foi gravada na branch de feature. **A alteração da regra diária ainda precisa de ser compilada e conferida no Profit.** Não declarar esta versão compilada ou validada antes dessa verificação.

## 6. Testes de aceitação

1. No primeiro candle de uma nova data, todos os contadores devem ficar em zero antes de contar ocorrências válidas desse candle.
2. Nenhum B1/A1 deve surgir se `Date <> Date[1]`.
3. Nenhum B2/A2 deve surgir se `Date <> Date[2]`.
4. Nenhum B3/A3 deve surgir se `Date <> Date[3]`.
5. Na mesma data, as seis desigualdades originais permanecem inalteradas.
6. Confirmar contagens após recarregar o gráfico e em gráficos de ticks, incluindo 60K.
7. Guardar evidência de compilação e comparação manual com OHLC.

## 7. Limitações

- A semântica depende da série `Date` disponibilizada pelo Profit para o gráfico utilizado.
- Ainda não foi verificado se a configuração de sessão do ativo define a data de negociação esperada para o utilizador.
- SHA-256 canónico pendente de cálculo determinístico.
- Nenhuma ordem é emitida e nenhuma integração em produção foi autorizada.

## 8. Histórico de alterações

- **0.1.0 — 2026-10-17:** primeira versão experimental, sem filtro diário.
- **0.2.0 — 2026-10-17:** filtro `Date = Date[N]` para cada distância e reinício dos seis contadores quando muda a data; aguarda recompilação no Profit.


## 9. Correção de visualização — versão 0.3.0

Após relato de compilação sem plot visível, os seis plots foram configurados explicitamente como histogramas por `SetPlotType` e receberam cores distintas por `SetPlotColor`. Como os valores dos contadores são pequenos em comparação com os preços do ativo, o indicador deve ser adicionado num painel separado para usar uma escala própria, não sobre a escala de preços principal.

Esta alteração foi gravada na branch `feature/bm-force-break-001`, commit `835817c6addbc606e574a28afc063f869ac270b3`. A compilação anterior relatada pelo utilizador não valida esta alteração de visualização. Aguardar nova compilação e confirmar que os histogramas aparecem e incrementam quando as condições B1–B3/A1–A3 ocorrem.
