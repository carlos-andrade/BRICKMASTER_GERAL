# BRICKMASTER V12_versao7 ULTRA — Análise Técnica

**Base analisada:** `BRICKMASTER_V12_versao7_EXEC_COMPLETO2.src` (2595 linhas, NTSL) + `Manual Operacional Completo` (HTML)
**Plataforma:** Profit One / Nelogica — carregado como Estratégia
**Autor:** Carlos Andrade

---

## 1. Visão geral da arquitetura

O arquivo é um sistema único de operação real, dividido em 5 partes que rodam em sequência a cada candle:

| Parte | Função |
|---|---|
| **1** | Indicador de bandas percentuais (±0,5/±1/±2/±3%) sobre a abertura do dia, médias curta/longa (M9/M25), proxy de fluxo via VWAP + posição no range, e Score direcional (Comprador × Vendedor) |
| **1.5** | Cumulative Volume Anômalo — 8 janelas horárias, com média histórica incremental (Welford-like) construída dia a dia |
| **1.6** | Força do Volume (0–100), combinando força do candle e força do dia |
| **2** | Módulo de execução: Sinal → Permissão → Execução (`BuyStop`/`SellShortStop`) |
| **2.5** | Saída em duas fases: stop fixo + alvo fixo (Fase 1) até lucro mínimo, depois trailing pela M9 com trava de não-regressão (Fase 2) |
| **3–4** | Plotagem completa e sistema de alertas em 4 níveis (N1 toque → N4 execução/gestão de risco) |

A cadeia de sinal segue: **Toque → Rejeição/Aceitação → Armadilha → Confirmação** (com filtro de VWAP, pressão compradora/vendedora e, opcionalmente, CVD e divergência VWAP-abertura×fechamento). Só a **Confirmação** alimenta o módulo de execução.

---

## 2. Pontos fortes identificados

- **Controle de reprocessamento de candle** via `CurrentBar()` — evita múltiplos disparos dentro do mesmo candle.
- **Trava de não-regressão no trailing**: o stop, uma vez movido a favor da posição, nunca pode voltar atrás (`if StopTrailingCompra < StopTrailingAnteriorC then StopTrailingCompra := StopTrailingAnteriorC`), inclusive espelhado corretamente para vendas.
- **Preço de execução real**: usa `BuyPrice()`/`SellPrice()` para registrar a entrada, em vez do preço de disparo do stop — importante para gestão de risco correta em caso de slippage.
- **Trava financeira em R$ real** via `DailyResult(true)`, que já inclui o resultado da posição em aberto — mais realista que travar só por pontos acumulados.
- **`CancelPendingOrders`** antes de qualquer novo envio, e zeragem forçada no fim do pregão (`ClosePosition` após `HorarioZeragem`).
- **Duas janelas de horário operacional** (M1 e M2), separando manhã e tarde — evita operar no período de almoço, historicamente mais errático.
- Rastreamento de performance embutido (`UsarRastreamento23`) que registra ACERTO/ERRO no próprio candle de origem, útil para auditoria visual sem depender de relatório externo.

---

## 3. Achado principal: o filtro de Score/Volume Anômalo não afeta a execução real

Este é o ponto mais importante da análise porque contradiz a leitura mais natural do manual e dos comentários de cabeçalho do código.

**O que o cabeçalho do `.src` e o manual dizem:**
> "Quando `AlertaVolumeAnomalo` ativo: exige `DiferencaMinimaScore` + 2 pontos antes de liberar `ContextoComprador`/`ContextoVendedor` (filtro B+D)"

**O que o código efetivamente faz:**
- `ContextoComprador`/`ContextoVendedor` são calculados a partir do `Score` e usados em exatamente três lugares: o painel visual (`PainelCompraForte`/`PainelVendaForte`), os alertas de contexto (N-informativo) e o sinal `DiaDirecionalCompra`/`DiaDirecionalVenda`.
- O único sinal de entrada que consome `ContextoComprador`/`ContextoVendedor` é `DiaDirecionalCompra`/`Venda`.
- Esse sinal só entra na cadeia de execução se `UsarSinalDiaDirecional(true)` — **e no arquivo atual esse parâmetro está `false`** (linha 117).
- Os sinais que estão de fato ativos por padrão (`UsarSinalRejeicaoConfirmada`, `UsarSinalArmadilhaConfirmada`, `UsarSinalArmadilhaMeio`) vêm todos das variáveis `Confirmou*`, cujas condições (linhas ~965–1112) checam **VWAP, pressão compradora/vendedora, CVD e divergência VWAP** — nunca `Score`, `ContextoComprador`, `ContextoVendedor` ou `AlertaVolumeAnomalo`.

**Consequência prática:** com a configuração de parâmetros atual, o módulo de Volume Anômalo (Parte 1.5) e o Score direcional funcionam como **camada informativa/visual**, não como filtro de risco real — apesar do texto do manual (seção "Filtro B+D") descrever o comportamento como se ele bloqueasse sinais de fato. Se a intenção é que o alerta de volume anômalo realmente exija mais confirmação antes de operar, é preciso ou:
1. Ativar `UsarSinalDiaDirecional(true)`, ou
2. Adicionar explicitamente `ContextoComprador`/`ContextoVendedor` (ou uma checagem de `Score`) como condição dentro dos blocos `Confirmou*` ou na seção **E2 — Permissão**.

Vale confirmar com você se esse comportamento é intencional (Score só para leitura visual do operador) ou se é uma lacuna a corrigir.

---

## 4. Outros riscos e pontos de atenção no código

### 4.1 Conflito entre `SinalCompra` e `SinalVenda` no mesmo candle
Na seção **E3 — Execução** (linhas ~1651–1665), os dois blocos `if PermissaoCompra` e `if PermissaoVenda` são avaliados em sequência. Se, por qualquer combinação rara de bandas (ex.: `ArmadilhaMeio` de compra e `ArmadilhaConfirmada` de venda no mesmo candle), ambos os sinais vierem `true`, cada bloco chama `CancelPendingOrders` antes de enviar sua própria ordem — o que faz o segundo bloco cancelar a ordem stop do primeiro. Resultado: só a ordem de venda sobrevive, sem nenhuma lógica explícita de prioridade ou desempate. Não há como saber, sem testar, se esse é o comportamento desejado.

### 4.2 Ausência de dimensionamento de posição
Todo o sistema opera implicitamente com contratação fixa (1 contrato, dado que `PerdaMaximaDiariaRS(300.0)` é calibrado como "padrão: 1 contrato WIN", conforme o próprio comentário). Não há nenhuma variável de quantidade (`Quantity`) nem lógica de scaling. Se em algum momento a estratégia for usada com outro ativo (WDO, por exemplo) ou volume de contratos maior, os R$ das travas (`PerdaMaximaDiariaRS`, `GanhoMaximoDiarioRS`) e os pontos de stop/alvo (`StopPontos`, `AlvoPontos`) precisam ser recalibrados manualmente — não há proteção automática contra isso.

### 4.3 Offset duplicado na ordem stop de entrada
```
BuyStop(Close + (OffsetExecucao * MinPriceIncrement),
        Close + (OffsetExecucao * MinPriceIncrement) + (OffsetExecucao * MinPriceIncrement));
```
O preço de disparo (trigger) usa `OffsetExecucao` (5 ticks) acima do fechamento, e o preço-limite da ordem stop-limit usa mais `OffsetExecucao` acima do trigger — ou seja, 10 ticks de folga entre fechamento e o limite máximo de preenchimento. Em mercado rápido isso pode ser insuficiente (ordem não preenchida) ou, se `MinPriceIncrement` for maior do que o esperado no ativo carregado, gerar slippage maior que o presumido pelo `StopPontos`/`AlvoPontos`. Vale documentar explicitamente essa escolha de 2×`OffsetExecucao` no manual, já que hoje só aparece implícita no código.

### 4.4 Dependência de histórico contínuo para o volume anômalo
Já documentado no próprio manual, mas reforço aqui como risco operacional: a média histórica das 8 janelas não persiste entre reinícios do Profit (NTSL não guarda arrays entre sessões). Nos primeiros `MinimoDiasParaComparar` (5) pregões após qualquer reinício/recarregamento do indicador, o alerta fica estruturalmente desativado — e, pelo achado da seção 3, isso hoje não teria efeito sobre a execução mesmo depois de "aquecido", a menos que o item 3 seja corrigido.

### 4.5 `ReversaoExecutada` e reversão automática
A trava `ReversaoExecutada` impede múltiplas reversões no mesmo candle, e é resetada corretamente quando `not HasPosition`. Ponto de atenção: `UsarReversaoAutomatica(true)` está ativo por padrão, o que significa que uma armadilha confirmada contra a posição aberta inverte a posição imediatamente via `ReversePosition()`, **sem passar pelo stop fixo da Fase 1**. Isso é coerente com a filosofia do sistema, mas dobra a exposição instantaneamente (fecha + abre no lado oposto) — vale ter certeza de que o dimensionamento de risco diário (`PerdaMaximaDiariaRS`) contempla esse cenário de reversão, que gasta 2 operações de `MaxOperacoesPorDia` de uma vez.

---

## 5. Checklist de validação antes de operar com dinheiro real

Formalizando o que já está no manual/comentários do código, mais alguns itens desta análise:

- [ ] Rodar em **simulador por no mínimo 20 pregões consecutivos e sem interrupção** (necessário também para o histórico de volume anômalo amadurecer, ainda que hoje sem efeito prático — ver item 3)
- [ ] Decidir e testar a correção do item 3 (Score/Volume Anômalo como filtro real de execução) antes de considerar o "Filtro B+D" como proteção ativa
- [ ] Verificar em backtest se `SinalCompra` e `SinalVenda` já ocorreram simultaneamente no mesmo candle e qual ordem prevaleceu (item 4.1)
- [ ] Confirmar `MinPriceIncrement` do contrato carregado e se 10 ticks de folga (item 4.3) é adequado para o ativo/horário operado
- [ ] Confirmar se `PerdaMaximaDiariaRS`/`GanhoMaximoDiarioRS` continuam válidos para o número real de contratos operados (item 4.2)
- [ ] Validar cenário de reversão automática (item 4.5) isoladamente, com foco no impacto de duas operações consumidas de `MaxOperacoesPorDia`
- [ ] Conferir que `ZerarNoFimDoPregao` e `HorarioZeragem(1745)` cobrem folga suficiente antes do fechamento do book para o ativo operado

---

## 6. Parâmetros críticos — quando revisar

| Parâmetro | Valor atual | Revisar quando... |
|---|---|---|
| `StopPontos` / `AlvoPontos` | 50 / 80 pts | Mudar de ativo (WIN→WDO) ou regime de volatilidade muda a amplitude média do candle |
| `LucroMinimoParaTrailing` | 40 pts | Muitas operações saindo no stop fixo antes de ativar o trailing (Fase 2 raramente ativa) |
| `DistanciaMinimaTrailing` | 15 pts | Trailing "grudando" demais no preço e sendo estopado por ruído normal da M9 |
| `PerdaMaximaDiariaRS` / `GanhoMaximoDiarioRS` | 300 / 600 | Mudar quantidade de contratos operados |
| `MaxOperacoesPorDia` | 4 | Reversão automática consumindo 2 por evento (item 4.5) — pode esgotar o limite mais rápido que o esperado |
| `DiferencaMinimaScore` / `ReforcoScoreEmAlerta` | 3.0 / 2.0 | Só relevantes na prática se `UsarSinalDiaDirecional` for ativado ou se o item 3 for corrigido |
| `FatorAlertaAnomalia` / `MinimoDiasParaComparar` | 2.0 / 5 | Ativo com pouca liquididade/histórico curto pode exigir `MinimoDiasParaComparar` maior |
| `HorarioInicioM1/FimM1`, `M2` | 905–1200, 1430–1730 | Mudança de horário de pregão da B3 ou se o "gap de almoço" deixar de ser um período ruim para operar |

---

*Relatório gerado a partir da leitura completa do `.src` e do índice/seções do manual HTML fornecidos. Não substitui backtest/forward test — os pontos das seções 3 e 4 são leituras de código, não resultados de simulação.*
