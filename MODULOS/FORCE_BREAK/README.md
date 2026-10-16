# BRICKMASTER FORCE BREAK

**Identificador técnico:** `BM_FORCE_BREAK`

## Missão

Investigar e quantificar a força de rompimentos em que o fechamento de um candle ultrapassa a mínima ou a máxima de candles anteriores, começando pelas referências de 1, 2 e 3 candles.

## Princípios

- Preservar o histórico e a proveniência de cada estudo.
- Distinguir observação, hipótese, evidência e conclusão validada.
- Não declarar testes ou resultados sem evidências reproduzíveis.
- Manter estudos experimentais separados das regras validadas e de produção.
- Não emitir ordens nem alterar a lógica operacional do BRICKMASTER.
- Avaliar critérios, dependências, riscos e limitações antes de integrar descobertas.

## Estrutura de cada estudo

1. Identificador e pergunta investigada.
2. Fonte dos dados e contexto gráfico.
3. Definição matemática das condições.
4. Amostra e critérios de inclusão/exclusão.
5. Tabelas de resultados e verificações de consistência.
6. Limitações e evidências reproduzíveis.
7. Estado: `EXPERIMENTAL`, `EM_VALIDACAO`, `VALIDADA` ou `REJEITADA`.
8. Histórico de alterações e decisão de integração.

## Estudo inicial

O estudo `DESC-001` investiga fechamentos abaixo da mínima e acima da máxima de candles situados 1, 2 e 3 posições atrás. A regra está documentada, mas a contagem exata permanece pendente de dados OHLC correspondentes às imagens. Não considerar o estudo validado até essa reconciliação.