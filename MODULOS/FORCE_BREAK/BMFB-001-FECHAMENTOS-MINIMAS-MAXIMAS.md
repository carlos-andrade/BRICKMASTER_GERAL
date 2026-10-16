# BMFB-001 — Fechamentos além da mínima/máxima de candles anteriores

| Campo | Valor |
|---|---|
| **ID** | BMFB-001 |
| **Projeto** | BRICKMASTER RAIZ — módulo FORCE BREAK |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | RELATORIO |
| **Fase** | DESCOBERTA_E_ESPECIFICACAO |
| **Estado** | EXPERIMENTAL |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — cálculo determinístico ainda não executado nesta sessão |
| **Commit de referência (versão anterior)** | [83090e784663cdc1ff2313e628c986e83c066493](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/83090e784663cdc1ff2313e628c986e83c066493) |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente — aprovação do estudo não registada |
| **Origem** | Instruções do utilizador e duas imagens de gráfico fornecidas nesta conversa; documento migrado de `MODULOS/DESCOBERTA/DESC-001-FECHAMENTOS-RELATIVOS-CANDLES.md` |
| **Autoridade superior** | [Norma de cabeçalho documental GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); [Governança técnica BRICKMASTER](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/main/BRICKMASTER_ARQUITETURA/GOVERNANCA.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | [Commit de correção da regra original](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/aeee3925a4cae60ca1823ead5ccc536cf1398bbf); [commit de migração](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/a76a7d453ccddbbdf5126160ee46d1b2658fe279) |
| **Escopo** | Contagem experimental das seis condições matemáticas sobre duas amostras visuais; não inclui execução operacional |
| **Objetivo** | Definir e apurar quantas vezes o fechamento do candle atual ultrapassa mínima ou máxima do candle exatamente N posições atrás |
| **Dependências** | Exportações OHLC correspondentes às imagens; preservação da ordem das observações; revisão reproduzível das ocorrências |

## Contexto Histórico

O estudo foi iniciado a partir de duas imagens com candles numerados de 1 a 96 e de 1 a 72. A regra foi esclarecida pelo utilizador e corrigida em commit anterior à migração. Em 2026-10-16, o estudo foi movido de `MODULOS/DESCOBERTA/` para `MODULOS/FORCE_BREAK/`. O conteúdo e a regra matemática são preservados nesta atualização; a alteração atual normaliza o cabeçalho documental e explicita rastreabilidade e governança.

## Estado

- **Estado técnico:** EXPERIMENTAL.
- **Estado da apuração:** PENDENTE_OHLC.
- **Validação numérica:** não realizada; os preços OHLC correspondentes não foram fornecidos.
- **Testes NTSL/Profit, replay, backtest e ordens:** não realizados nem declarados.
- **Produção:** não aprovado.

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

## 4. Estado da apuração e resultados

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
- Revisar cada ocorrência sinalizada e guardar a origem dos dados e o procedimento da apuração.
- Não combinar amostras nem extrapolar resultados para outros períodos ou ativos sem declarar e validar essa mudança de escopo.

## 7. Dependências, riscos e limitações

- Os números de candles visíveis nas imagens não provam que as séries sejam contínuas ou que não haja candles ocultos.
- A contagem numérica continua pendente até obter os preços OHLC correspondentes.
- O critério foi definido conforme a instrução explícita do utilizador.
- As contagens elegíveis (n-N) pressupõem uma série consecutiva e completa; isso ainda depende de verificação.
- Uma contagem correta, isoladamente, não prova força preditiva nem garante resultado operacional.

## Evidências

- [Norma de cabeçalho GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md)
- [Governança técnica do BRICKMASTER](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/main/BRICKMASTER_ARQUITETURA/GOVERNANCA.md)
- [Commit de correção da regra original](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/aeee3925a4cae60ca1823ead5ccc536cf1398bbf)
- [Commit de migração para FORCE_BREAK](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/a76a7d453ccddbbdf5126160ee46d1b2658fe279)

## Validação

Revisão documental preliminar em 2026-10-17: o conjunto de condições e as tabelas foram preservados; foi acrescentada a governança documental e o estado de validação. O resultado estatístico permanece desconhecido por ausência de OHLC. O cabeçalho de integridade será concluído com SHA-256 canónico após a normalização, sem confundir esse valor com o SHA do blob Git.

## Resultado

Regra matemática documentada; nenhuma contagem numérica validada. Não utilizar como estatística comprovada, backtest, recomendação financeira ou regra de produção antes da validação apropriada.

## Próxima Ação

1. Obter as exportações OHLC idênticas às duas amostras.
2. Executar a contagem reproduzível e revisar os eventos.
3. Calcular e conferir o SHA-256 canónico de cada documento segundo a norma GOV.
4. Rever a aceitação e atualizar o estado apenas com evidência.

## Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.0 | 2026-10-16 | Documento original migrado para FORCE_BREAK | Responsável técnico do projeto | [Commit a76a7d4](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/a76a7d453ccddbbdf5126160ee46d1b2658fe279) |
| 1.0.1 | 2026-10-17 | Cabeçalho normalizado e metadados/rastreabilidade GOV acrescentados; regra e amostras preservadas | Responsável técnico do projeto | Commit desta atualização |
