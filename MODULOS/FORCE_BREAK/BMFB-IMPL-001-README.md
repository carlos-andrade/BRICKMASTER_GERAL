# BM_FORCE_BREAK — Primeiro código NTSL

| Campo | Valor |
|---|---|
| **ID** | BMFB-IMPL-001 |
| **Projeto** | BRICKMASTER RAIZ — BM_FORCE_BREAK |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | ESPECIFICACAO_TECNICA |
| **Fase** | FEATURE |
| **Estado** | EXPERIMENTAL |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular conforme GOV-CAB-NORMA-001 v1.0.3 |
| **Commit de referência (versão anterior)** | [76af18f16fd592809727b79890cdca800ba0aa35](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/76af18f16fd592809727b79890cdca800ba0aa35) |
| **Data de criação** | 2026-10-17 |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente |
| **Origem** | Requisito aprovado nesta conversa: alvo NTSL/Profit; indicador visual e contadores; módulo isolado e sem ordens |
| **Autoridade superior** | [GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Dependências** | Profit/NTSL; gráfico com candles OHLC; especificação BMFB-001 |
| **Rastreabilidade** | [Estudo BMFB-001](BMFB-001-FECHAMENTOS-MINIMAS-MAXIMAS.md) |

## 1. Objetivo

Entregar a primeira implementação experimental do BM_FORCE_BREAK para NTSL/Profit com dois indicadores independentes: marcação visual no gráfico e contadores cumulativos numa janela de indicador. Permanecem separados para evitar que os valores dos contadores alterem a escala de preços do gráfico principal.

## 2. Contrato funcional

Para candle atual i e distância N:

- Abaixo N: `Close[i] < Low[i-N]`.
- Acima N: `Close[i] > High[i-N]`.
- N ∈ {1, 2, 3}.
- Comparações estritas: igualdade não conta.
- A contagem começa apenas quando existe histórico suficiente para a distância comparada.
- Os contadores são cumulativos sobre as barras carregadas/recalculadas pelo Profit; não são contadores exclusivos do dia.
- O indicador visual usa etiquetas: B1/B2/B3 para fechamento abaixo da mínima e A1/A2/A3 para fechamento acima da máxima.

## 3. Artefactos

- `BMFB-001-INDICADOR-VISUAL.ntsl`: marcações B1–B3/A1–A3.
- `BMFB-002-CONTADORES.ntsl`: seis séries cumulativas, plots 0–5.
- `BMFB-IMPL-001-README.md`: este contrato e registo de validação.

## 4. Isolamento e segurança

- Não contém chamadas de compra, venda, cancelamento ou alteração de ordens.
- Não altera a estratégia central BRICKMASTER, AVGPRICE, stops ou gestão de posição.
- Não integra automaticamente no BRICKMASTER nem em automações.
- Deve ser importado como indicador, não como estratégia de execução.
- Não representa recomendação de entrada; apenas classifica relações entre OHLC.

## 5. Plano de validação

1. Importar cada ficheiro no editor NTSL do Profit como indicador separado.
2. Compilar e guardar o resultado da compilação (não presumir sucesso).
3. Conferir manualmente barras de teste para as seis desigualdades, incluindo igualdade exata e histórico insuficiente.
4. Verificar os seis contadores contra uma apuração independente sobre OHLC exportado.
5. Testar em gráfico de ticks, incluindo 60K, e em outro tipo de gráfico; registar plataforma, ativo, período, quantidade de barras e evidências.
6. Só após evidências, atualizar estado para VALIDADO; produção exige revisão e aprovação separadas.

## 6. Limitações conhecidas

- Ainda não compilado nem executado nesta sessão.
- A disponibilidade de nomes de cores, índice inicial de `CurrentBar`, persistência de variáveis e semântica de recálculo devem ser confirmadas no Profit.
- Os contadores podem variar conforme a quantidade de barras carregadas e o comportamento de recálculo da plataforma.
- As etiquetas de várias condições na mesma barra podem sobrepor-se visualmente; ajustar apenas após teste documentado.
- O SHA-256 canónico permanece pendente até cálculo determinístico.

## 7. Estado e próxima ação

Estado técnico: EXPERIMENTAL. Estado de validação: PENDENTE_COMPILACAO_PROFIT. Não declarar testado, validado ou pronto para produção até recolher evidência. Próxima ação: compilar os dois indicadores no Profit e registar os resultados, erros e capturas relevantes.

## 8. Histórico

- 2026-10-17 — versão inicial experimental criada para NTSL/Profit, com visualização e contadores separados; sem ordens e sem integração operacional.
