# DESC-001 — Fechamentos relativos a candles anteriores

- **Módulo:** DESCOBERTA
- **Estado:** EXPERIMENTAL — contagem visual preliminar
- **Fontes:** duas imagens de gráfico fornecidas na conversa
- **Amostra A:** gráfico com candles numerados de 1 a 96
- **Amostra B:** gráfico com candles numerados de 1 a 72
- **Validação OHLC:** não realizada; os dados numéricos de abertura, máxima, mínima e fechamento não foram fornecidos

## 1. Objetivo

Investigar quantas vezes o fechamento de um candle ficou abaixo ou acima do fechamento de 1, 2 e 3 candles anteriores.

## 2. Regra operacional provisória

Para este registro, “abaixo de N candles” significa:

\`Close[i] < Close[i-N]\`

e “acima de N candles” significa:

\`Close[i] > Close[i-N]\`

A comparação é com o **preço de fechamento** do candle de N posições atrás, não com a mínima/máxima dos candles intermediários. Igualdade é neutra e não conta em nenhum lado. Os primeiros N candles de cada gráfico não têm referência suficiente e ficam fora da contagem dessa distância.

**Importante:** esta definição é uma hipótese metodológica adotada para tornar a pergunta mensurável. Se a intenção era fechar abaixo da mínima ou acima da máxima de um conjunto de 1, 2 ou 3 candles, trata-se de um estudo diferente.

## 3. Resultado

As imagens permitem identificar a sequência visual e os números dos candles, mas não fornecem os valores OHLC exportáveis. Por isso, uma contagem exata de comparações entre preços de fechamento **não pode ser validamente derivada apenas da imagem** sem risco de erro de leitura de pixels, escala, sombras, compressão ou arredondamento.

| Métrica solicitada | Amostra A — 96 candles | Amostra B — 72 candles | Total |
|---|---:|---:|---:|
| Fechamento abaixo do fechamento de 1 candle anterior | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento abaixo do fechamento de 2 candles anteriores | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento abaixo do fechamento de 3 candles anteriores | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento acima do fechamento de 1 candle anterior | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento acima do fechamento de 2 candles anteriores | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento acima do fechamento de 3 candles anteriores | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |

## 4. Tabelas de apuração a preencher após obtenção do OHLC

### Abaixo do fechamento de 1 candle anterior

| Amostra | Candles elegíveis | Contagem abaixo | Contagem igual | Contagem acima |
|---|---:|---:|---:|---:|
| A | 95 | PENDENTE | PENDENTE | PENDENTE |
| B | 71 | PENDENTE | PENDENTE | PENDENTE |

### Abaixo do fechamento de 2 candles anteriores

| Amostra | Candles elegíveis | Contagem abaixo | Contagem igual | Contagem acima |
|---|---:|---:|---:|---:|
| A | 94 | PENDENTE | PENDENTE | PENDENTE |
| B | 70 | PENDENTE | PENDENTE | PENDENTE |

### Abaixo do fechamento de 3 candles anteriores

| Amostra | Candles elegíveis | Contagem abaixo | Contagem igual | Contagem acima |
|---|---:|---:|---:|---:|
| A | 93 | PENDENTE | PENDENTE | PENDENTE |
| B | 69 | PENDENTE | PENDENTE | PENDENTE |

### Acima do fechamento de 1 candle anterior

| Amostra | Candles elegíveis | Contagem acima | Contagem igual | Contagem abaixo |
|---|---:|---:|---:|---:|
| A | 95 | PENDENTE | PENDENTE | PENDENTE |
| B | 71 | PENDENTE | PENDENTE | PENDENTE |

### Acima do fechamento de 2 candles anteriores

| Amostra | Candles elegíveis | Contagem acima | Contagem igual | Contagem abaixo |
|---|---:|---:|---:|---:|
| A | 94 | PENDENTE | PENDENTE | PENDENTE |
| B | 70 | PENDENTE | PENDENTE | PENDENTE |

### Acima do fechamento de 3 candles anteriores

| Amostra | Candles elegíveis | Contagem acima | Contagem igual | Contagem abaixo |
|---|---:|---:|---:|---:|
| A | 93 | PENDENTE | PENDENTE | PENDENTE |
| B | 69 | PENDENTE | PENDENTE | PENDENTE |

## 5. Como concluir a contagem exata

Exportar os candles das duas amostras com índice sequencial e preço de fechamento (OHLC completo é preferível). Para cada distância N em {1, 2, 3}, comparar cada fechamento elegível com o fechamento N posições antes, contando separadamente abaixo, igual e acima. Deve-se preservar o identificador da amostra para não concatenar sequências não contíguas.

Pseudológica:

\`for N in [1, 2, 3]:\`
\`  for i from N to number_of_candles - 1:\`
\`    compare Close[i] with Close[i-N]\`

Critério de controle: para cada N e amostra, \`abaixo + igual + acima = candles elegíveis\`.

## 6. Limitações e conclusão

- As 96 e 72 observações são contagens dos candles numerados visíveis nas imagens; não comprovam que as sequências sejam séries históricas contínuas.
- Não há confirmação dos preços de fechamento por exportação de dados.
- Nenhum total numérico de fechamentos acima/abaixo foi estimado ou inventado.
- O estudo permanece **EXPERIMENTAL / PENDENTE DE DADOS OHLC**.
- Não usar este registo como evidência estatística, backtest ou regra operacional do BRICKMASTER até a reconciliação com dados brutos.
