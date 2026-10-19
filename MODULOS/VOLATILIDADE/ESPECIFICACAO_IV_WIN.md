---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA_INDICADOR"
fase: "F2 — Requisitos e desenho"
id_documento: "BM-VOL-IV-WIN-001"
titulo: "Especificação do indicador de volatilidade implícita para contexto do Mini Índice"
status: "EXPERIMENTAL — ESPECIFICAÇÃO EM REVISÃO"
versao: "1.0.0"
data_criacao: "2026-10-19"
data_atualizacao: "2026-10-19"
origem: "Discussão técnica do BRICKMASTER RAIZ; fontes de mercado de opções a validar"
autoridade_documental: "Governação BRICKMASTER; especificações oficiais B3 e metodologia da fonte de dados quando validadas"
cadeia_autoridade: "Governança > documentação oficial do instrumento/fonte > especificação aprovada > implementação > evidências de validação"
rastreabilidade: "Documento novo; não altera RV-60K; SHA-256 e commit de referência registados após publicação"
escopo: "Especificar um módulo de volatilidade implícita para análise contextual do Mini Índice WIN em gráficos de 60K trades"
objetivo: "Definir requisitos, contratos, fórmulas candidatas, controlos de qualidade e critérios de validação para estudar o valor informativo da volatilidade implícita"
dependencias: "Dados de opções B3; dados WIN de 60K trades; calendário e horários de negociação; fonte/metodologia IV documentadas; governança e risco soberano"
---

# Especificação do Indicador de Volatilidade Implícita para WIN — IV-WIN

| Campo | Valor |
|---|---|
| ID documental | BM-VOL-IV-WIN-001 |
| Identificador candidato no Profit/NTSL | `ID: BM_VOL_IV_WIN_001` |
| Tipo | Indicador/contextualizador quantitativo; sem ordens |
| Estado | EXPERIMENTAL — requisitos em revisão |
| Versão | 1.0.0 |
| SHA-256 (conteúdo canónico) | 98c75bc732a07fd51de301c438b246c4682455f664d63f5a134b2cd8b07ed17d |
| Commit de referência | O próprio commit de criação será registado na referência Git |
| Ativo operacional de interesse | Mini Índice B3 — WIN |
| Gráfico-alvo | 60K trades |
| Data de criação | 2026-10-19 |
| Data de atualização | 2026-10-19 |

## Contexto Histórico

O BRICKMASTER RAIZ já dispõe do protótipo RV-60K, indicador de volatilidade realizada acumulada intradiária, cuja implementação e documentação foram integradas em `develop` pelo PR #32. Este documento especifica um módulo distinto, destinado a investigar se a informação de volatilidade implícita derivada de opções relacionadas com o mercado acionista brasileiro acrescenta contexto útil à leitura do Mini Índice.

O indicador nativo denominado “Volatilidade Implícita” na lista do Profit foi observado pelo utilizador. A metodologia exata desse indicador — instrumento subjacente, série de opções, vencimento, strikes, modelo de avaliação, fonte de preços e convenções — **não está confirmada**. Não assumir equivalência entre o indicador nativo, a volatilidade implícita de uma opção individual, uma superfície de volatilidade e um índice agregado de volatilidade.

A relação económica entre opções sobre o Ibovespa, ETFs associados e o futuro WIN justifica a investigação, mas não prova que uma medida específica produza vantagem preditiva. A adequação dependerá dos dados acessíveis, da liquidez, da sincronização e de testes fora da amostra.

## Estado

O documento define uma especificação experimental de requisitos e desenho. Não representa implementação, compilação, teste empírico, validação preditiva, integração com o Giroscópio ou aprovação para produção.

O RV-60K mantém-se independente e inalterado. O indicador IV-WIN não deve substituir a volatilidade realizada, determinar a direção do mercado isoladamente nem emitir ordens.

## 1. Problema a resolver

Avaliar se os preços das opções relacionadas com o mercado acionista brasileiro fornecem informação incremental sobre o regime e a amplitude dos movimentos do WIN, para além da informação disponível no preço do WIN, na volatilidade realizada e noutros dados de contexto já validados.

Perguntas verificáveis:
1. É possível obter uma medida de IV com instrumento de referência, timestamps, modelo e convenções conhecidos?
2. A medida é atual, líquida e suficientemente estável para análise intradiária?
3. O nível e a variação da IV acrescentam informação sobre a volatilidade realizada futura do WIN?
4. A estrutura temporal e a assimetria das opções acrescentam informação além do nível geral de IV?
5. O ganho permanece em períodos fora da amostra, após controlar custos, atrasos, dados ausentes e vieses de seleção?

## 2. Escopo e exclusões

### Incluído
- Inventário e avaliação das fontes de opções e volatilidade implícita.
- Especificação de métricas, unidades, horizonte e timestamps.
- Cálculo ou consumo de IV apenas quando a metodologia estiver documentada.
- Análise exploratória de nível, mudança, estrutura temporal e assimetria.
- Alinhamento temporal com barras WIN de 60K trades.
- Qualidade, atualidade, confiança e estado de indisponibilidade.
- Testes isolados e comparação com um modelo-base sem IV.
- Especificação de saídas para futura integração através de contrato explícito.

### Excluído
- Envio, alteração ou cancelamento de ordens.
- Sinal autónomo de compra/venda.
- Promessa de previsão direcional ou rentabilidade.
- Limiares operacionais considerados validados antes de testes.
- Alterar RV-60K ou redefinir a sua fórmula.
- Assumir que o indicador nativo do Profit corresponde a uma série agregada específica.
- Confundir IV com volatilidade realizada, probabilidade objetiva ou certeza sobre movimentos futuros.
- Integração automática com Giroscópio, decisão soberana de risco ou execução.

## 3. Instrumentos candidatos e hierarquia de investigação

A ordem seguinte é uma prioridade inicial para investigação, não um ranking de capacidade preditiva comprovada.

### 3.1 Opções sobre o Ibovespa
Candidata inicial pela ligação económica ao índice acionista de referência do WIN. Antes de utilizá-la, verificar disponibilidade na janela necessária, liquidez, bid/ask, vencimentos, strikes, estilo de exercício, multiplicador, liquidação e documentação da metodologia IV.

### 3.2 Opções sobre ETF associado ao Ibovespa, como BOVA11
Candidata complementar. Verificar base e diferenças entre ETF e índice, liquidez própria, horários e efeito de distribuições/rendimentos. A sua IV não é idêntica, por definição, à IV das opções sobre o Ibovespa ou ao comportamento do WIN.

### 3.3 Índice agregado de volatilidade do mercado brasileiro, se disponível e adequado
Pode servir como variável contextual de regime. Confirmar metodologia, subjacentes, tenor, frequência de atualização, fonte oficial, licenciamento e horário de publicação. Não assumir atualização em tempo real nem adequação a decisões dentro de uma barra de 60K trades.

### 3.4 Indicador nativo “Volatilidade Implícita” do Profit
Investigar separadamente e registar:
- nome exato exibido e versão do Profit;
- parâmetros disponíveis;
- ativo/série à qual se aplica;
- se o cálculo depende do instrumento gráfico, de uma opção específica ou de outra fonte;
- modelo, convenções e periodicidade, se documentados;
- comportamento com dados sem atualização e fora do horário regular.

Sem metodologia comprovada, o valor pode ser observado exploratoriamente, mas não será input canónico do modelo nem evidência suficiente de validação.

## 4. Definição financeira

A volatilidade implícita (IV) é a volatilidade que, introduzida num modelo de avaliação de opção com os restantes inputs definidos, permite reproduzir o prémio observado. É uma quantidade implícita no preço e no modelo, não uma observação direta da volatilidade futura.

A IV pode refletir expectativas de variabilidade, prémio de risco, procura de proteção, oferta e procura, liquidez e especificidades do contrato. Assim:
- IV a subir não implica que o WIN vá cair;
- IV a descer não implica que o WIN vá subir;
- IV elevada face ao histórico não demonstra, por si só, sobrevalorização;
- IV não é automaticamente uma medida de probabilidade direcional;
- divergências entre IV e RV podem refletir diferentes horizontes, prémios de risco, liquidez ou erros de medição.

## 5. Métricas candidatas

Todas as métricas são propostas para avaliação. Janelas, tenor-alvo, frequência e thresholds devem ser definidos com dados disponíveis e avaliação empírica.

### 5.1 Nível de IV — IV_LEVEL
Volatilidade anualizada implícita de uma opção ou métrica construída a partir de conjunto definido de opções. Especificar subjacente, tipo, tenor, moneyness/delta, seleção, modelo, timestamp e interpolação. Unidade recomendada: percentagem anualizada conforme convenção documentada.

### 5.2 Variação da IV — IV_CHANGE
Variação absoluta entre duas observações válidas e temporalmente comparáveis:

`ΔIV_t = IV_t − IV_(t−Δt)`

Unidade: pontos percentuais de volatilidade anualizada, se IV estiver expressa em percentagem. Documentar Δt, tratamento de cotações repetidas e idade máxima.

### 5.3 Variação relativa ou padronizada — IV_CHANGE_NORM
Usar variação relativa apenas com escala e tratamento de zero definidos. Como alternativa, padronizar com estatísticas calculadas apenas a partir de dados históricos disponíveis até ao instante da previsão. Não usar estatísticas de toda a amostra incluindo o futuro.

### 5.4 Estrutura temporal — IV_TERM_STRUCTURE
Comparar IVs com horizontes de vencimento diferentes, mantendo moneyness e metodologia comparáveis. Preferir tenores constantes/interpolados de forma documentada a comparações entre contratos com dias até vencimento diferentes. Se os pontos não forem comparáveis, devolver desconhecido.

### 5.5 Assimetria — IV_SKEW
Diferença entre IV de puts e calls selecionadas por delta ou moneyness comparáveis, mesmo subjacente e vencimento ou tenor harmonizado. Definir explicitamente o sinal e guardar os componentes. Assimetria mais inclinada pode refletir proteção de cauda relativamente mais cara, mas não prova queda iminente.

### 5.6 Prémio de volatilidade — VOL_PREMIUM
Diferença entre IV e estimativa de RV futura para horizonte compatível. É observável ex post, depois do horizonte terminar. Em tempo real, IV menos RV passada é apenas uma diferença descritiva e não deve ser chamada prémio ex post de volatilidade futura.

Para avaliação, alinhar horizonte e anualização, usar IV observável no instante t, calcular RV futura apenas como rótulo de avaliação e impedir que essa RV futura entre nas features.

## 6. Contrato de dados de entrada

| Campo | Semântica | Obrigatoriedade |
|---|---|---|
| source_id | Identificador estável da fonte | Obrigatório |
| instrument_id | Identificador do contrato/subjacente | Obrigatório |
| underlying_id | Índice, ETF ou outro subjacente | Obrigatório |
| option_type | Call/put | Para opção individual |
| strike | Preço de exercício | Para opção individual |
| expiry | Vencimento segundo convenção oficial | Para opção individual |
| bid / ask | Preços e unidades | Se a IV for reconstruída de cotações |
| last_price | Último negócio; não substitui automaticamente bid/ask | Opcional |
| implied_volatility | IV da fonte com convenção documentada | Se consumida diretamente |
| model_id | Modelo e versão | Para IV calculada |
| event_timestamp | Hora do evento de mercado | Obrigatório |
| receive_timestamp | Hora de receção | Obrigatório |
| currency / price_unit | Moeda e escala | Obrigatório |
| volume / open_interest | Métricas de atividade, se disponíveis | Recomendado |
| data_status | Válido, ausente, atrasado, inválido, cruzado ou contraditório | Obrigatório |
| quality_reason | Motivo de rejeição/limitação | Se não válido |

Não confundir nulo, zero, preço sem negócio, observação repetida e dado ausente. Preservar fonte e transformações para auditoria.

## 7. Contrato de saída IV-WIN

A saída é exclusivamente contextual, sem execução.

| Campo | Descrição |
|---|---|
| module_id | `BM_VOL_IV_WIN_001` |
| as_of_timestamp | Instante da avaliação |
| source_timestamp | Timestamp de mercado mais recente utilizado |
| underlying_id | Subjacente usado |
| iv_method | Método/série identificada |
| iv_level | Nível, se válido |
| iv_change | Variação na janela validada |
| term_structure | Valor/estado, se calculável |
| skew | Valor/estado, se calculável |
| realized_vol_reference | Referência RV e horizonte |
| quality_state | `VALID`, `STALE`, `MISSING`, `INVALID`, `CONTRADICTORY` ou `UNKNOWN` |
| context_state | `UNKNOWN`, `LOW_VOL`, `NORMAL_VOL`, `HIGH_VOL` ou `EXTREME_VOL`, apenas após validação |
| confidence | Medida calibrada; não atribuir número arbitrário |
| reason_codes | Motivos de bloqueio/limitação |
| methodology_version | Versão de método e parâmetros |
| evidence_ref | Captura, ficheiro, query ou lote reproduzível |

Os regimes são categorias propostas. Não existem thresholds aprovados. Até os critérios serem definidos e validados, devolver `UNKNOWN` ou apenas a medida descritiva.

## 8. Qualidade, atualidade e fail-closed

1. Rejeitar observações sem instrumento ou fonte identificável.
2. Rejeitar ou assinalar cotações cruzadas, preços inválidos, IV não finita e inputs incompatíveis com o modelo.
3. Distinguir ausência de atualização de mercado fechado.
4. Definir idade máxima com base na frequência observada e no horizonte de uso; não inventar TTL universal.
5. Sincronizar timestamps de evento, receção e barras WIN; atrasos materiais invalidam a comparação.
6. Divergências materiais entre fontes/contratos resultam em `CONTRADICTORY` ou `UNKNOWN`, sem seleção arbitrária.
7. Dados críticos ausentes, atrasados, inválidos ou contraditórios bloqueiam classificação e recomendação derivada.
8. Guardar RAW e derivados separadamente, com proveniência e retenção documentadas.
9. Não inventar confidence score; calibrar com frescura, liquidez, dispersão e qualidade mensuráveis.
10. O módulo não substitui o controlo soberano de risco e não gera ordens.

## 9. Relação com RV-60K e gráfico de 60K trades

- **RV-60K:** volatilidade realizada acumulada a partir dos retornos das barras de 60K trades; pode manter-se ou aumentar durante a sessão até ao reset documentado.
- **IV-WIN:** estimativa implícita nos prémios das opções e no modelo; pode subir ou descer.
- **RV futura:** rótulo de avaliação posterior; não pode servir de input no instante de previsão.

Não comparar diretamente IV anualizada com o valor acumulado de RV-60K. Para compará-las, converter para horizontes e convenções compatíveis e documentar a transformação. A barra de 60K trades fixa o número de negócios, não a duração temporal.

A linha branca dos gráficos BRICKMASTER representa sempre o preço de abertura do mercado. Preservar esta regra nas leituras visuais; ela não integra a fórmula de IV.

## 10. Pipeline proposto

1. Identificar instrumento, fonte, metodologia, licença e canal de dados.
2. Preservar cotações/IV RAW, timestamps e metadados.
3. Normalizar unidades, timezone, vencimento, modelo e convenções sem eliminar originais.
4. Validar atualidade, spread, inputs e coerência temporal.
5. Selecionar contratos através de regras determinísticas documentadas.
6. Calcular nível, variação, estrutura temporal, assimetria e referência de RV quando possível.
7. Classificar apenas depois de aprovar métodos, thresholds e qualidade.
8. Publicar resultado com timestamps, versão e razões de qualidade.
9. Alinhar ao WIN 60K e medir atraso.
10. Registar parâmetros, evidências e exceções.

## 11. Plano de validação

### V0 — Verificação da fonte (gate obrigatório)
- comprovar metodologia do indicador nativo Profit ou escolher fonte alternativa documentada;
- confirmar disponibilidade histórica e intradiária;
- confirmar horários, atraso, granularidade, licença e limitações;
- decidir entre consumir IV da fonte ou reconstruí-la;
- estabelecer política para contratos ilíquidos ou sem bid/ask.

**Saída exigida:** fonte identificada, metodologia reprodutível e esquema documentado. Sem isto, não avançar para implementação operacional.

### V1 — Auditoria de dados
Verificar duplicados, timestamps invertidos, lacunas, cotações cruzadas e trocas de contrato; quantificar cobertura, atraso e spread; produzir relatório de exclusões.

**Saída exigida:** defeitos contabilizados, nenhuma correção silenciosa e transformação RAW→resultado reproduzível.

### V2 — Validação matemática
Testar limites do método usado, entradas inválidas, denominadores nulos, vencimento, falta de cotação, unidades e anualização. Comparar com referência independente ou valores documentados.

**Saída exigida:** resultados reprodutíveis dentro de tolerância justificada antes do teste.

### V3 — Validação temporal e valor incremental
Definir antecipadamente horizontes, alvo de volatilidade futura e features; separar cronologicamente desenvolvimento/validação/teste; usar walk-forward e purging/embargo se necessário.

Comparar:
- **Base:** dados WIN e RV-60K, sem IV;
- **Experimental:** base mais IV_LEVEL e IV_CHANGE;
- **Ablation:** adicionar term structure e skew individualmente.

Impedir leakage em features, normalização e seleção; registar períodos com mercado fechado ou dados desfasados.

**Saída exigida:** melhoria incremental fora da amostra, examinada estatisticamente e robusta. Resultados negativos permanecem no histórico.

### V4 — Replay e robustez
Executar replay cronológico, testar atraso/falha da fonte, avaliar por regime/vencimento/liquidez, analisar sensibilidade a horários/spreads/seleção de contratos e comparar com baselines simples.

**Saída exigida:** falhas definidas, limitações quantificadas e resultados reproduzíveis.

### V5 — Integração contextual (gate futuro)
Propor contrato para o Giroscópio, semântica UNKNOWN e redução de confiança, dependências com Risco e Dados/Qualidade, monitorização, rollback e aprovação humana. A integração não decorre automaticamente da existência deste documento.

## 12. Métricas de avaliação

Para previsão contínua de volatilidade futura: MAE, RMSE, erro escalado e calibração face a baseline. Para regimes: matriz de confusão, precisão/recall por classe e estabilidade. Para valor incremental: ganho fora da amostra e robustez temporal.

Se futuramente apoiar uma regra de trading, acrescentar custos, slippage, exposição e limites de risco. Boa previsão de amplitude não demonstra rentabilidade nem direção correta.

## 13. Riscos e limitações

- Liquidez baixa pode distorcer IV, sobretudo em strikes/vencimentos afastados.
- Bid/ask e último negócio podem gerar valores diferentes.
- IV pode subir devido à procura de proteção sem aumento imediato de RV.
- Diferentes vencimentos exigem normalização.
- Relações podem mudar em stress, abertura, leilões, eventos macro e mudanças de microestrutura.
- Dados de opções podem ser atrasados, licenciados ou incompletos.
- Prever amplitude não determina direção.
- Resultados no WIN não se extrapolam automaticamente para outros ativos, sessões ou gráficos.
- O objetivo de 1% desde a abertura é hipótese de investigação, nunca promessa nem prioridade sobre o risco.

## 14. Dependências e contratos

| Dependência | Contrato requerido | Estado |
|---|---|---|
| Fonte de opções/IV | Instrumento, método, schema, timestamps e licença | POR IDENTIFICAR/VALIDAR |
| WIN 60K | Barras, preço, timestamp e sessão | Dados específicos do estudo por alinhar |
| RV-60K | Métrica realizada com metodologia/reset documentados | Referência separada; não alterar |
| Dados/Qualidade | Atualidade, proveniência, integridade e rejeições | Contrato por formalizar |
| Giroscópio | Campos e semântica de contexto/confiança | NÃO INTEGRADO |
| Risco soberano | Regras de bloqueio e precedência | Não alterado por este módulo |
| NTSL/Profit | Capacidade de consumir/exibir a fonte e sintaxe válida | Não investigada neste checkpoint |

## 15. Roadmap e gates

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| F0 — Documento-base | Especificação versionada e hash | Ficheiro recuperável no GitHub | EM PUBLICAÇÃO |
| F1 — Descobrir a fonte | Relatório de método, acesso e limitações | Fonte e cobertura demonstradas | PENDENTE |
| F2 — Fechar requisitos | Contratos, unidades, janelas, filtros e métricas | Requisitos revisados | EM DEFINIÇÃO |
| F3 — Implementação isolada | Prova de conceito independente | Revisão e validação estática | BLOQUEADA por F1/F2 |
| F4 — Testes/evidências | Relatório de dados, matemática e replay | Evidência reproduzível | BLOQUEADA |
| F5 — Valor incremental | Comparação fora da amostra | Resultado, incluindo negativos | BLOQUEADA |
| F6 — Integração contextual | Contrato aprovado e rollback | Gate humano e fallback definidos | BLOQUEADA |

Não publicar percentagem de conclusão sem scorecard e evidências ligados a critérios objetivos.

## Evidências

- [Módulo VOLATILIDADE no BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL/tree/main/MODULOS/VOLATILIDADE)
- [README do RV-60K em develop](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/develop/MODULOS/VOLATILIDADE/NTSL/README-RV-60K.md)
- [Relatório de validação funcional RV-60K](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/develop/MODULOS/VOLATILIDADE/VALIDACAO/RELATORIO_VALIDACAO_FUNCIONAL_RV_60K.md)
- [PR #32 — RV-60K](https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/32)
- B3: a página inicial `https://www.b3.com.br/` é apenas ponto de partida. As páginas de produto, especificações dos contratos e metodologia da IV terão de ser registadas como fontes diretas durante F1.

Nenhuma série histórica de IV foi descarregada, nenhum cálculo IV foi executado e nenhum teste empírico foi realizado ao redigir esta especificação.

## Validação

Checklist documental:
- cabeçalho completo e coerente com a governança;
- separação explícita entre requisito, hipótese, dado observado e resultado validado;
- nenhuma alegação de implementação, compilação, backtest ou ganho preditivo sem evidência;
- entradas, saídas, falhas, dependências e gates descritos;
- RV-60K preservado sem alterações;
- SHA-256 canónico calculado após fixar conteúdo, em UTF-8 com finais LF, excluindo do material canonizado os campos SHA-256 e Commit de referência.

Não foram executados testes de código, cálculo de IV, replay, backtest ou integração.

## Resultado

Especificação preliminar para investigar a volatilidade implícita como variável contextual do WIN. O módulo permanece experimental. O primeiro gate é comprovar a metodologia e a disponibilidade da fonte antes da implementação.

## Próxima Ação

Executar F1: identificar exatamente o indicador do Profit ou uma fonte B3 alternativa com metodologia documentada; obter schema, frequência, histórico, timestamps e condições de acesso/licença; publicar relatório de fonte antes de escrever código.

## Histórico de alterações

| Versão | Data | Alteração | Estado |
|---|---|---|---|
| 1.0.0 | 2026-10-19 | Especificação técnica inicial IV-WIN: métricas candidatas, contratos, controlos de dados e plano de validação | EXPERIMENTAL — EM REVISÃO |
