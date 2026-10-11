# Plano de testes — Módulo 001

**Estado:** PLANEADO — AINDA NÃO EXECUTADO

| ID | Teste | Resultado esperado | Evidência |
|---|---|---|---|
| T001 | Cálculo com preço de abertura conhecido | Oito níveis coincidem com a fórmula | Tabela de cálculo |
| T002 | Simetria percentual | Cada nível respeita a percentagem indicada em relação a P₀ | Cálculo independente |
| T003 | Congelamento da referência | P₀ não muda com a oscilação intrassessão | Registo de sessão |
| T004 | Nova sessão | A referência muda apenas para a nova sessão válida | Captura antes/depois |
| T005 | Carregamento a meio do pregão | Recupera a abertura real, não o primeiro preço visível | Captura e log |
| T006 | Gráfico de ticks | Deteção de sessão funciona sem barras temporais fixas | Captura e log |
| T007 | Tick size | Níveis plotados respeitam a regra aprovada | Tabela pré/pós-arredondamento |
| T008 | Plotagem | Linha-base e oito níveis são visíveis e corretos | Captura do Profit |
| T009 | Reprocessamento histórico | Referências diárias permanecem corretas | Capturas de dias diferentes |
| T010 | Efeitos colaterais | Nenhuma ordem é enviada e nenhuma posição é alterada | Verificação da estratégia |

## Registo por execução

Para cada teste, registar data/hora, instrumento, tipo de gráfico, configuração, resultado esperado, resultado observado, estado (PASS/FAIL/BLOCKED), evidência e defeito associado.

Não marcar PASS sem evidência observável. Testes não executados devem permanecer PLANEADO; bloqueios devem identificar a dependência em falta.
