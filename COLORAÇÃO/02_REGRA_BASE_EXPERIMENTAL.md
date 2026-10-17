# BRICKMASTER RAIZ — Regra Base de Coloração (Experimental)

> **ID:** BM-COL-RULE-001  
> **Estado:** EXPERIMENTAL — não validada no Profit  
> **Versão:** 1.0.0  
> **Data:** 2026-10-17  
> **Referência:** Manual NTSL 4.4 (03-08-2026), a confirmar em compilação local

## Objetivo

Definir um primeiro teste mínimo de coloração direcional usando somente a relação entre o preço de fechamento da barra atual e o da barra anterior. Esta regra é uma prova de integração visual, não é a coloração definitiva do BRICKMASTER.

## Matriz de decisão

| Condição | Estado visual | Interpretação limitada |
|---|---|---|
| Close > Close[1] | Alta local | Fechamento acima do anterior |
| Close < Close[1] | Baixa local | Fechamento abaixo do anterior |
| Close = Close[1] | Neutro | Sem alteração entre os dois fechamentos |
| Histórico insuficiente | Neutro/indeterminado | Não classificar até haver dados suficientes |

## Pseudocódigo independente de plataforma

```text
se não houver histórico suficiente:
    estado = NEUTRO
senão se Close > Close[1]:
    estado = ALTA_LOCAL
senão se Close < Close[1]:
    estado = BAIXA_LOCAL
senão:
    estado = NEUTRO
```

## Restrições

- Não é sinal de compra ou venda.
- Não usar para autorizar execução.
- Não interpretar sequência de cores como confirmação de tendência sem contexto adicional.
- Não declarar compatibilidade NTSL apenas com base no pseudocódigo.
- A implementação NTSL deve ser verificada contra a sintaxe e os exemplos do Manual 4.4 e compilada no Profit antes de mudar de estado.

## Próxima evidência necessária

Guardar captura do editor/compilador, versão do Profit, tipo de gráfico, ativo e resultados dos casos de teste definidos em `04_PLANO_DE_TESTES_E_EVIDENCIAS.md`.
