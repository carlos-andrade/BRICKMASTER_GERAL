# Checkpoints e Evidências

Estado: PROPOSTA PARA REVISÃO. Data: 2026-10-11.

Um checkpoint deve permitir retomar o trabalho sem adivinhar. Relatos como “continuar” ou “funcionou” não são evidência suficiente.

## Campos obrigatórios
- ID e data/hora com fuso.
- Repositório, branch e commit-base.
- Objetivo, escopo e estado inicial.
- Arquivos criados, alterados ou movidos.
- Ambiente, comandos e configuração.
- Testes planejados e executados.
- Resultado esperado e observado.
- Links para logs, artefatos e commits.
- Limitações, riscos e bloqueios.
- Decisão e próximo passo com critério objetivo.

## Níveis de evidência
- E0: declaração sem artefato; não comprova validação.
- E1: artefato identificável, como log, saída, arquivo ou commit.
- E2: procedimento e ambiente reproduzíveis.
- E3: revisão ou reprodução independente.
- E4: histórico operacional monitorado.

## Resultados
PASS significa que todos os critérios foram cumpridos e as evidências estão referenciadas. FAIL indica critério violado. BLOCKED indica dependência ou risco que impediu execução. PENDING significa não executado ou sem evidência. NOT_APPLICABLE exige justificativa. Nunca converter PENDING em PASS por ausência aparente de erro.

## Evidências de mercado
Registrar dados/fixture, fonte, timestamp, instrumento, sessão, configuração, parâmetros, commit, resultado, custos e limitações. Distinguir backtest OHLC de tick a tick; incluir gráficos de ticks, incluindo 60K, quando fizer parte do cenário alegado.

## Encerramento de etapa
Salvar evidências, atualizar checkpoint, registrar decisão e risco residual, e indicar exatamente o próximo passo. Nunca incluir segredos em logs.