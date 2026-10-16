# BMFB-001 — Fechamentos além da mínima/máxima de candles anteriores

- **Módulo:** BRICKMASTER FORCE BREAK (`BM_FORCE_BREAK`)
- **Estado:** EXPERIMENTAL — regra de contagem definida; apuração numérica pendente
- **Documento migrado de:** `MODULOS/DESCOBERTA/DESC-001-FECHAMENTOS-RELATIVOS-CANDLES.md`
- **Fontes:** duas imagens de gráfico fornecidas na conversa
- **Amostra A:** candles numerados de 1 a 96
- **Amostra B:** candles numerados de 1 a 72
- **Validação OHLC:** pendente; os dados numéricos exportados não foram fornecidos

## 1. Objetivo

Contar quantas vezes o fechamento do candle atual ultrapassa a mínima ou a máxima de um candle anterior, considerando distâncias de 1, 2 e 3 candles.

## 2. Regra oficial definida pelo utilizador

Para um candle atual de índice i e distância N:

- **Abaixo de 1 candle:** `Close[i] < Low[i-1]`
- **Abaixo de 2 candles:** `Close[i] < Low[i-2]`
- **Abaixo de 3 candles:** `Close[i] < Low[i-3]`
- **Acima de 1 candle:** `Close[i] > High[i-1]`
- **Acima de 2 candles:** `Close[i] > High[i-2]`
- **Acima de 3 candles:** `Close[i] > High[i-3]`

Onde:
- `Close[i]` = preço de fechamento do candle atual.
- `Low[i-N]` = mínima do candle N posições atrás.
- `High[i-N]` = máxima do candle N posições atrás.

A comparação é feita com a mínima ou máxima do candle específico situado N posições atrás — não com o fechamento anterior e não com a mínima/máxima combinada de vários candles.

Igualdade não conta como abaixo nem acima: as condições são estritas (`<` e `>`).

## 3. Convenção visual das cores

Nas imagens fornecidas, verde indica candle que fechou acima da própria abertura e vermelho indica candle que fechou abaixo da própria abertura. A cor, isoladamente, não determina se o fechamento atual ficou abaixo da mínima ou acima da máxima de um candle anterior; para isso, é necessário comparar os níveis de preço definidos na seção 2.

## 4. Estado da apuração

As imagens mostram a sequência numerada, mas não fornecem uma tabela OHLC exportável. Uma leitura aproximada de pixels pode produzir erros nos níveis de máxima, mínima e fechamento, sobretudo em candles pequenos, sobrepostos ou com escala comprimida. Portanto, não declarar contagens exatas com base apenas nas cores.

| Métrica | Amostra A (96 candles) | Amostra B (72 candles) | Total |
|---|---:|---:|---:|
| Fechamento atual abaixo da mínima de 1 candle atrás | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento atual abaixo da mínima de 2 candles atrás | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento atual abaixo da mínima de 3 candles atrás | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento atual acima da máxima de 1 candle atrás | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento atual acima da máxima de 2 candles atrás | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |
| Fechamento atual acima da máxima de 3 candles atrás | PENDENTE OHLC | PENDENTE OHLC | PENDENTE OHLC |

## 5. Tabelas individuais de apuração

### Abaixo da mínima de 1 candle atrás

| Amostra | Candles elegíveis | Fechamentos abaixo | Não abaixo |
|---|---:|---:|---:|
| A | 95 | PENDENTE | PENDENTE |
| B | 71 | PENDENTE | PENDENTE |

### Abaixo da mínima de 2 candles atrás

| Amostra | Candles elegíveis | Fechamentos abaixo | Não abaixo |
|---|---:|---:|---:|
| A | 94 | PENDENTE | PENDENTE |
| B | 70 | PENDENTE | PENDENTE |

### Abaixo da mínima de 3 candles atrás

| Amostra | Candles elegíveis | Fechamentos abaixo | Não abaixo |
|---|---:|---:|---:|
| A | 93 | PENDENTE | PENDENTE |
| B | 69 | PENDENTE | PENDENTE |

### Acima da máxima de 1 candle atrás

| Amostra | Candles elegíveis | Fechamentos acima | Não acima |
|---|---:|---:|---:|
| A | 95 | PENDENTE | PENDENTE |
| B | 71 | PENDENTE | PENDENTE |

### Acima da máxima de 2 candles atrás

| Amostra | Candles elegíveis | Fechamentos acima | Não acima |
|---|---:|---:|---:|
| A | 94 | PENDENTE | PENDENTE |
| B | 70 | PENDENTE | PENDENTE |

### Acima da máxima de 3 candles atrás

| Amostra | Candles elegíveis | Fechamentos acima | Não acima |
|---|---:|---:|---:|
| A | 93 | PENDENTE | PENDENTE |
| B | 69 | PENDENTE | PENDENTE |

## 6. Procedimento de validação

Obter exportação OHLC dos candles correspondentes a cada imagem. Manter as amostras separadas, preservar a ordem e usar o mesmo conjunto de candles que aparece em cada imagem. Para cada distância N em {1, 2, 3}, testar as seis condições da seção 2.

Pseudológica:

- Para N em {1, 2, 3}, contar os casos em que `Close[i] < Low[i-N]`.
- Para N em {1, 2, 3}, contar os casos em que `Close[i] > High[i-N]`.

Critérios de controle:
- A amostra A e a amostra B são apuradas separadamente.
- Para cada N, existem n-N observações elegíveis, se os candles forem consecutivos e completos.
- Abaixo e acima são contagens independentes; não se deve assumir que sejam complementares.
- Validar o resultado por revisão dos casos sinalizados e guardar a origem dos dados.

## 7. Limitações e conclusão

- Os números de candles visíveis nas imagens não provam que as séries sejam contínuas ou que não haja candles ocultos.
- A contagem numérica continua pendente até obter os preços OHLC correspondentes.
- O critério foi definido conforme a instrução explícita do utilizador.
- Estado atual: **EXPERIMENTAL — definição confirmada, contagem pendente de dados OHLC**.
- Não utilizar como estatística validada, backtest ou regra de produção antes da validação.
