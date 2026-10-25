# BRICKMASTER RAIZ — Regra Base de Coloração (Experimental)

> **ID:** BM-COL-RULE-001  
> **Estado:** EXPERIMENTAL — não validada no Profit  
> **Versão:** 1.0.1  
> **Data:** 2026-10-17  
> **Referência:** Manual NTSL 4.4 (03-08-2026), seção 5.1 para o padrão de `if/else` e `PaintBar`

## Objetivo

Definir um primeiro teste mínimo de coloração direcional usando somente a relação entre o fechamento da barra atual e o da barra anterior. É uma prova de integração visual, não a coloração definitiva do BRICKMASTER.

## Matriz de decisão

| Condição | Cor | Interpretação limitada |
|---|---|---|
| Close = Close[1] | Amarelo (`clYellow`) | Fechamento igual ao anterior |
| Close > Close[1] | Verde (`clGreen`) | Fechamento acima do anterior |
| Close < Close[1] | Vermelho (`clRed`) | Fechamento abaixo do anterior |
| Histórico insuficiente | Sem classificação garantida | Confirmar comportamento inicial no Profit |

## Base documental

O Manual NTSL 4.4 apresenta um exemplo de coloração com a mesma sequência de condições: igualdade, fechamento superior e, no caso restante, fechamento inferior, usando `PaintBar(clYellow)`, `PaintBar(clGreen)` e `PaintBar(clRed)`. O protótipo foi alinhado a esse exemplo. A referência documental não substitui a compilação e o teste no ambiente alvo.

## Restrições

- Não é sinal de compra ou venda.
- Não autoriza execução nem altera posições.
- Não interpretar sequência de cores como confirmação de tendência sem contexto adicional.
- Não declarar compatibilidade integral antes da compilação no Profit.
- A regra não valida fluxo, liquidez, volume financeiro, FVG, VWAP/TWAP ou contexto macroeconómico.

## Próxima evidência necessária

Guardar captura do editor/compilador, versão do Profit, ativo, tipo de gráfico e resultados dos casos de teste definidos em `04_PLANO_DE_TESTES_E_EVIDENCIAS.md`.
