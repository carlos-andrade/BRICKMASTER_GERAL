# BM_FORCE_BREAK — Regra de contabilização diária

| Campo | Valor |
|---|---|
| **ID** | BMFB-IMPL-001 |
| **Projeto** | BRICKMASTER RAIZ — BM_FORCE_BREAK |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | ESPECIFICACAO_TECNICA |
| **Fase** | FEATURE |
| **Estado** | EXPERIMENTAL |
| **Versão** | 0.4.0 |
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


## 10. Correção da saída gráfica — versão 0.4.0

Após relato do utilizador de compilação sem exibição, a versão 0.4.0 foi simplificada para utilizar as funções `Plot`, `Plot2`, `Plot3` e `Plot4`, documentadas na secção 19.19 do Manual NTSL 4.4. A implementação anterior com seis `PlotN` e configurações de histograma/cor foi retirada desta versão para reduzir variáveis na investigação.

**Limitação funcional temporária:** esta versão plota somente quatro das seis métricas (abaixo1, abaixo2, abaixo3 e acima1). Os contadores acima2 e acima3 continuam calculados, mas não são plotados nesta etapa. Não declarar como solução final até confirmar visualização no Profit. Após confirmação, criar uma abordagem final para disponibilizar todas as seis métricas sem depender de uma escala invisível ou de recursos de plot incompatíveis.

Commit do código v0.4.0: `c99c9e445ed9f68f85ad3eef895ecfbd6b16699c`. Estado: experimental, aguarda recompilação e evidência visual.


## 11. Alteração da visualização — versão 0.5.0

A pedido do utilizador, o `BMFB-002-CONTADORES.ntsl` deixou de desenhar linhas de contagem. Passa a desenhar as etiquetas `B1`, `B2`, `B3`, `A1`, `A2` e `A3` diretamente nos candles, com `PlotText`, seguindo a mesma forma visual do primeiro código `BMFB-001-INDICADOR-VISUAL.ntsl`. Os seis contadores cumulativos continuam calculados internamente e reiniciam na mudança de data.

Código v0.5.0 gravado na branch `feature/bm-force-break-001`, commit `27bf0fee7405f08a995eb048d93c8462a506ac7c`. A alteração requer nova compilação e confirmação visual no Profit; não declarar validada até receber essa evidência.


## 12. Correção semântica dos rompimentos — v0.3.0 / v0.6.0

A imagem reportada pelo utilizador demonstrou que a regra anterior para A3/B3 era insuficiente para a interpretação operacional pretendida: comparar somente com a máxima/mínima do candle exatamente N posições atrás. A regra foi clarificada para comparar o fechamento atual com **todos os N candles anteriores**:
- A1: Close > High[1]; B1: Close < Low[1].
- A2: Close > High[1] e High[2]; B2: Close < Low[1] e Low[2].
- A3: Close > High[1], High[2] e High[3]; B3: Close < Low[1], Low[2] e Low[3].
Todas as barras de referência também precisam pertencer à mesma data do candle atual. Assim, um candle que feche abaixo de qualquer uma das três mínimas anteriores não pode receber A3; A3 exige fechamento acima das três máximas anteriores.

Atualizados os dois códigos na branch `feature/bm-force-break-001`. Commits: indicador visual `b0d84a4c951cbc82c8f8da92e138edf83bfacba9`; contadores `5df2514293665f9ca36c9cc8b548a3424c05afc0`. Estado experimental; requer recompilação e validação no Profit.
