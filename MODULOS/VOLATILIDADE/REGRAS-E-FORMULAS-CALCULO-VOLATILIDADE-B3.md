# Regras e fórmulas para cálculo da volatilidade — B3
### BRICKMASTER RAIZ | Especificação quantitativa do módulo VOLATILIDADE

| Campo | Valor |
|---|---|
| **ID** | BM-VOL-FORMULAS-001 |
| **Projeto** | BRICKMASTER RAIZ |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | ESPECIFICACAO_QUANTITATIVA |
| **Fase** | F2 — Requisitos e desenho |
| **Estado** | PROPOSTA_EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | A_CALCULAR |
| **Commit de referência (versão anterior)** | [437bb05811e7a860e7a53a9bbdec88795ef294c3](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/437bb05811e7a860e7a53a9bbdec88795ef294c3) |
| **Data de criação** | 2026-10-18 |
| **Data de atualização** | 2026-10-18 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Documentos relacionados** | [README](README.md); [Carta-Contrato](CARTA-CONTRATO-VOLATILIDADE-B3.md); [Layout Único](LAYOUT-UNICO-VOLATILIDADE-B3.md); [análise VOLATILIDADE/VIX](ANALISE-SOBREPOSICAO-10-VOLATILIDADE-VIX.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → ESPECIFICAÇÃO QUANTITATIVA → LAYOUT ÚNICO → CÓDIGO |

---

## 1. Mandato e limites

Este documento define as famílias de estimadores, regras de dados, unidades, regimes e validação para o módulo VOLATILIDADE do BRICKMASTER RAIZ. É uma especificação quantitativa **em revisão**, não uma declaração de implementação, validação ou produção.

Volatilidade não é um único número universal. É uma propriedade estatística estimada com dados, método, amostragem e horizonte específicos. O módulo deve distinguir:
- volatilidade histórica e realizada (variação observada);
- volatilidade intradiária acumulada e rolling;
- estimadores baseados em retornos e em amplitude OHLC;
- medidas operacionais em pontos/ticks, como ATR;
- previsão de volatilidade condicional;
- volatilidade implícita derivada de opções;
- métricas relativas, caudas, saltos e transições de regime.

Volatilidade mede magnitude/dispersão, não direção, probabilidade de lucro ou oportunidade por si só. O módulo fornece contexto ao Giroscópio; não emite ordens e não substitui o Risco soberano. A hipótese de 1% desde a abertura nunca sobrepõe a segurança.

## 2. Regras não negociáveis

1. Comparar apenas métricas com instrumento/contrato, sessão, unidade, método, horizonte e regra de amostragem compatíveis.
2. Preferir retornos logarítmicos para séries de preços positivos; se a fórmula não for válida, não substituir silenciosamente o método.
3. Separar medida observada, previsão, classificação e decisão.
4. Dados críticos ausentes, atrasados, inválidos, fora de ordem, contraditórios ou dessincronizados produzem DESCONHECIDO/DEGRADED e bloqueiam decisões dependentes.
5. Preservar RAW autorizado, proveniência, timestamps, lacunas, correções, versões, resultados negativos e histórico.
6. Não tratar maior frequência como automaticamente melhor: ruído de microestrutura, bid-ask bounce, baixa liquidez e timestamps imprecisos podem distorcer a estimativa.
7. Não assumir equivalência entre barras temporais, barras de ticks e Renko.
8. Não definir limiares de regimes sem calibração cronológica e teste fora da amostra.
9. Não promover resultados experimentais para VALIDADO/PRODUÇÃO sem evidência reproduzível e aprovação.
10. Não alegar testes, disponibilidade de feeds, rentabilidade ou vantagem operacional sem artefactos verificáveis.

## 3. Notação e unidades

\(P_i\): preço; \(r_i\): retorno; \(O_i,H_i,L_i,C_i\): abertura, máxima, mínima e fechamento; \(N\): número de observações válidas; \(\delta\): incremento mínimo do instrumento; \(RV\): variância realizada; \(RVol=\sqrt{RV}\): volatilidade realizada.

Retorno simples:
\[
R_i=P_i/P_{i-1}-1
\]
Retorno logarítmico:
\[
r_i=\ln(P_i/P_{i-1})
\]
Os retornos logarítmicos são aditivos no tempo. Não misturar retornos simples e logarítmicos sem conversão explícita.

Unidades:
- variância: retorno ao quadrado;
- volatilidade: desvio-padrão dos retornos; em percentagem, multiplicar por 100;
- pontos e ticks: escala operacional dependente do contrato;
- ATR: amplitude em unidade de preço, não volatilidade percentual por definição;
- volatilidade anualizada: exige convenção explícita de calendário e sessões, e não representa volatilidade observada no dia.

Nunca comparar diretamente percentagem, pontos, ticks, ATR bruto e VIX como a mesma grandeza.

## 4. Estimadores centrais

### 4.1 Desvio-padrão histórico

\[
\bar r=\frac1N\sum_{i=1}^{N}r_i,\qquad
s^2=\frac1{N-1}\sum_{i=1}^{N}(r_i-\bar r)^2,\qquad s=\sqrt{s^2}
\]

É um baseline simples para janelas comparáveis. É sensível a extremos e a mudanças de regime. Guardar tamanho amostral, janela, amostragem e tratamento de lacunas.

### 4.2 Variância realizada (RV)

\[
RV=\sum_{i=1}^{N}r_i^2,\qquad RVol=\sqrt{RV},\qquad RVol_{\%}=100\sqrt{RV}
\]

A RV é uma medida ex post da variação acumulada na janela. Durante a sessão, publicar como acumulada/parcial, nunca como sessão completa. A soma de retornos quadráticos não é idêntica à variância amostral centrada na média; registar a definição escolhida.

### 4.3 Parkinson — amplitude high-low

\[
\widehat{\sigma}_{P}^{2}=\frac{1}{4N\ln 2}\sum_{i=1}^{N}\left[\ln(H_i/L_i)\right]^2
\]

Usa máxima e mínima e pressupõe uma dinâmica específica de preços. Não incorpora diretamente todos os efeitos de gaps/saltos e exige OHLC corretos. Não aplicar automaticamente a barras de ticks/Renko.

### 4.4 Garman–Klass

\[
\widehat{\sigma}_{GK}^{2}=\frac1N\sum_{i=1}^{N}\left[\frac12\ln^2(H_i/L_i)-(2\ln2-1)\ln^2(C_i/O_i)\right]
\]

Estimador OHLC sob pressupostos específicos. Gaps, saltos, barras incompletas ou definição inconsistente de sessão podem prejudicar a interpretação.

### 4.5 Rogers–Satchell

\[
\widehat{\sigma}_{RS}^{2}=\frac1N\sum_{i=1}^{N}\left[
\ln(H_i/O_i)\ln(H_i/C_i)+
\ln(L_i/O_i)\ln(L_i/C_i)\right]
\]

Usa OHLC e pode acomodar deriva sob certas hipóteses; não elimina riscos de dados contaminados, saltos ou fronteiras de sessão incorretas.

### 4.6 Yang–Zhang

Forma resumida da família:
\[
\widehat{\sigma}_{YZ}^{2}=\sigma_o^2+k\sigma_c^2+(1-k)\sigma_{RS}^{2},\quad
k=\frac{0.34}{1.34+\frac{N+1}{N-1}}
\]
\(\sigma_o^2\) representa a componente open-to-open/overnight definida pelo método; \(\sigma_c^2\), a componente open-to-close; \(\sigma_{RS}^2\), Rogers–Satchell. Esta forma é apenas uma descrição da família. Antes de codificar, fixar definição completa de retornos, amostra, sessão, inicialização e tratamento de gaps e comparar com uma implementação de referência.

**Regra comum aos estimadores OHLC:** não presumir que as suas propriedades permanecem válidas em gráficos de ticks ou Renko. Adaptações são hipóteses experimentais separadas.

### 4.7 True Range e ATR

\[
TR_i=\max(H_i-L_i,\ |H_i-C_{i-1}|,\ |L_i-C_{i-1}|)
\]
ATR por média simples:
\[
ATR_n=\frac1n\sum_{i=1}^{n}TR_i
\]
ATR por suavização de Wilder:
\[
ATR_i=\frac{(n-1)ATR_{i-1}+TR_i}{n}
\]
As variantes diferem; o método e o período devem ser explícitos. ATR normalizado:
\[
NATR=100\frac{ATR_n}{C_i}
\]
quando \(C_i\) é válido. Para futuros, \(ATR_{ticks}=ATR_{pontos}/\delta\), apenas se o incremento mínimo estiver confirmado para o contrato.

### 4.8 Amplitude e gap

\[
Range_t=H_{0:t}-L_{0:t},\qquad RangeRel_t=Range_t/P_{ref}
\]
\[
Gap=(O_t-C_{t-1})/C_{t-1},\qquad Gap_{pts}=O_t-C_{t-1}
\]
Definir \(P_{ref}\), sessões e tratamento de rolagem/ajuste. Um gap numa série contínua sintética não é necessariamente um movimento negociável no contrato corrente.

## 5. Caudas, robustez e saltos

MAD:
\[
m_r=\operatorname{median}(r_i),\quad MAD=\operatorname{median}(|r_i-m_r|),\quad \sigma_{MAD}\approx1.4826\,MAD
\]
A escala 1.4826 torna MAD aproximadamente comparável ao desvio-padrão sob normalidade; não torna a distribuição normal nem remove risco de cauda.

Quantis absolutos:
\[
Q_{95}=Q_{0.95}(|r_i|),\qquad Q_{99}=Q_{0.99}(|r_i|)
\]
Quantis de cauda requerem amostra suficiente e devem ser calculados só com dados passados.

Diagnóstico de salto por bipower variation:
\[
BV=\mu_1^{-2}\sum_{i=2}^{N}|r_i||r_{i-1}|,\qquad \mu_1=\sqrt{2/\pi}
\]
\[
JumpProxy=\max(RV-BV,0)
\]
É um proxy, não teste formal de significância. Ruído de microestrutura e amostras curtas podem invalidar a interpretação; não classificar automaticamente todo RV−BV como salto real.

Assimetria e curtose podem complementar a análise, mas são instáveis em janelas curtas e sensíveis a extremos. Se usadas, registar fórmula, correção amostral e convenção de curtose (ordinária ou excesso).

## 6. Previsão condicional

### 6.1 EWMA

\[
h_t=\lambda h_{t-1}+(1-\lambda)r_{t-1}^{2},\quad 0<\lambda<1
\]
Registar \(\lambda\), inicialização, frequência, janela de aquecimento e horizonte. Validar fora da amostra; não assumir equivalência com a implementação de uma plataforma.

### 6.2 GARCH(1,1)

\[
r_t=\mu+\varepsilon_t,\quad \varepsilon_t=\sqrt{h_t}z_t
\]
\[
h_t=\omega+\alpha\varepsilon_{t-1}^{2}+\beta h_{t-1}
\]
Condições usuais: \(\omega>0\), \(\alpha,\beta\geq0\); \(\alpha+\beta<1\) é condição comum para variância incondicional finita sob hipóteses padrão. Avaliar resíduos, estabilidade e previsão fora da amostra. Ajuste bom no treino não é validação.

### 6.3 HAR-RV — candidato

\[
\log RV_{t+1}=\beta_0+\beta_d\log RV_t+\beta_w\overline{\log RV}_{t-4:t}+\beta_m\overline{\log RV}_{t-21:t}+\epsilon_{t+1}
\]
É um exemplo de especificação, não um modelo estimado. Adaptar horizontes à frequência e dados disponíveis; impedir leakage e avaliar por blocos cronológicos.

### 6.4 Avaliação

Comparar com baselines simples (persistência e média histórica, quando apropriados). Candidatos: MAE, RMSE, QLIKE quando aplicável, cobertura/calibração de intervalos e estabilidade por ativo, sessão e regime. Não comparar modelos com amostras ou horizontes diferentes. Guardar modelos rejeitados e razões.

## 7. Volatilidade implícita e VIX

Volatilidade implícita é inferida de preços de opções com modelo e convenções próprios. O VIX estima volatilidade esperada de 30 dias do S&P 500 a partir de opções SPX; não mede diretamente a volatilidade realizada de WIN, WDO ou outro ativo B3. citeturn715356search48turn715356search6

Regras:
1. Usar VIX como variável externa de contexto a testar, nunca como substituto direto de volatilidade local.
2. Guardar fonte, timestamp, atraso, sessão, unidade e validade.
3. Não converter VIX para volatilidade B3 por multiplicador fixo sem modelo validado.
4. Para volatilidade implícita de ativo B3, exigir cadeia de opções adequada, bid/ask válidos, vencimentos, taxas, ajustes e método de interpolação documentados.
5. Testar contribuição incremental de VIX face a baselines sem VIX, com sincronização temporal e sem informação futura.

## 8. Regimes relativos e transições

Razão contra baseline:
\[
VolRatio_t=VolMetric_t/Baseline_t
\]
Se o baseline for zero, ausente ou inválido, resultado DESCONHECIDO; nunca infinito ou zero artificial.

Escore robusto:
\[
RobustZ_t=(x_t-M)/(1.4826\,MAD)
\]
onde \(M\) e MAD são estimados no histórico elegível anterior ao instante atual. Definir a transformação de \(x_t\) antes de testar. Se MAD=0 ou a amostra for insuficiente, não publicar score.

Percentil:
\[
Percentile_t=F_{\text{past}}(VolMetric_t)
\]
O percentil descreve raridade relativa, não probabilidade de lucro. A distribuição de referência não pode incluir dados futuros.

Estados candidatos:
- DESCONHECIDO: pré-condições ou qualidade insuficientes;
- BAIXO: faixa inferior definida por estudo;
- NORMAL: faixa de referência definida por estudo;
- ELEVADO: expansão relativa relevante;
- EXTREMO: expansão/cauda que aciona cautela reforçada.

**Nenhum limite numérico está definido ou validado neste documento.** Calibrar apenas no treino/validação, congelar antes do teste final e realizar análise de sensibilidade. Se estimadores divergirem, publicar a divergência e reduzir confiança em vez de forçar um rótulo único.

Histerese (limites distintos de entrada/saída ou persistência por \(k\) observações) pode reduzir alternância excessiva. \(k\) e limites exigem validação; histerese nunca pode atrasar um bloqueio por dados inválidos.

## 9. Tempo, ticks de 60K e Renko

Manter três eixos separados: tempo de evento/receção; quantidade de negócios ou ticks; transformação gráfica. Uma barra de 60K ticks pode cobrir tempos de relógio muito diferentes. Renko depende do percurso de preço e dos parâmetros do construtor. Não anualizar nem comparar diretamente volatilidade por barra de ticks/Renko com volatilidade temporal.

Para cada barra de tick/Renko registar: definição e número de eventos, duração real, preços de referência, amplitude em pontos/ticks, negócio/volume se disponível e confiável, spread quando disponível, timestamps, lacunas, tipo de gráfico e versão do construtor. Testar cada granularidade separadamente e manter uma referência temporal paralela.

Dados de alta frequência podem sofrer ruído de microestrutura, amostragem irregular, saltos e dessincronização; realized kernel, two-scale/multi-scale e pre-averaging são famílias candidatas para determinados cenários, não soluções universais. A seleção de frequência deve ser empírica. citeturn715356search0turn715356search3turn715356search14

## 10. Qualidade, sincronização e confiança

Cada entrada deve conter instrumento/contrato, fonte, timestamp do evento e receção, unidade, método de amostragem, sessão/calendário, estado de qualidade e versão do adaptador.

Estados:
- VALID: verificações obrigatórias passaram;
- DEGRADED: utilizável somente em usos que tolerem a degradação;
- STALE: ultrapassou política de atualidade específica da fonte;
- MISSING: dado obrigatório ausente;
- CONTRADICTORY: valores/fontes incompatíveis sem resolução;
- INVALID: valor, sequência, unidade ou contrato inválido.

A idade máxima não é universal: definir por fonte e finalidade. Não usar um feed externo como atual sem evidência de timestamp/latência. Para confiança, expor separadamente qualidade, atualidade, suficiência amostral, estabilidade entre estimadores, estabilidade de regime e incerteza de previsão. Não somar componentes em score único até validar escalas e pesos.

## 11. Contrato de saída para o Giroscópio

Cada publicação deve incluir:
- schema_version e metric_version;
- instrumento, contrato, mercado e sessão;
- timestamps de evento, cálculo e publicação;
- fontes, proveniência e qualidade;
- métrica, estimador, unidade, valor, janela e número de observações;
- tipo/frequência de amostragem;
- baseline, percentil/escore quando aplicável;
- regime candidato, confiança por componente e divergências;
- alertas, motivo de bloqueio e validade temporal;
- estado EXPERIMENTAL/VALIDADO/PRODUÇÃO;
- IDs/hashes para recuperar dados e cálculo.

O módulo não emite ordens. Dados críticos inválidos ou stale bloqueiam conclusões dependentes. VALIDADO exige critérios e evidências reproduzíveis; PRODUÇÃO exige ainda aprovação formal, monitorização e rollback.

## 12. Protocolo de validação

**F0 — Dados:** inventariar fontes/licenças, calendário, contratos, timestamps, grão, cobertura, lacunas e RAW autorizado.

**F1 — Referência:** implementar fórmulas isoladas, unidades explícitas, testes sintéticos e comparação independente. Cobrir N insuficiente, zero/negativo, gaps, duplicados, fora de ordem e OHLC incompleto.

**F2 — Histórico cronológico:** separar treino/validação/teste por tempo, sem embaralhar; estimar normalizadores/quantis apenas no passado; incluir abertura, meio da sessão, fecho, eventos, baixa liquidez e diferentes regimes; fazer sensibilidade de janela, frequência e estimador.

**F3 — Regimes:** definir baseline, percentis, thresholds e histerese no treino; congelar antes do teste final; reportar estabilidade e falsos alertas.

**F4 — Previsão/incrementalidade:** comparar EWMA/GARCH/HAR-RV e contexto VIX contra baselines, fora da amostra e com erros segmentados.

**F5 — Shadow mode:** sem ordens; medir atraso, stale, falhas, divergências, reconciliação e recuperação.

**F6 — Gate:** fórmula e versão congeladas, dados identificados, testes automáticos aprovados, resultados reproduzíveis, baseline, análise de falhas, limites, revisão independente, monitorização e rollback. Sem evidência, estado EXPERIMENTAL.

## 13. Testes mínimos requeridos

| ID | Caso | Resultado esperado |
|---|---|---|
| VOL-UT-001 | Retornos todos zero | RV=0; tratar baseline zero sem divisão por zero |
| VOL-UT-002 | Um salto sintético | RV aumenta; diagnóstico não determina direção |
| VOL-UT-003 | Preço inválido/log indefinido | INVALID/DESCONHECIDO, sem substituição silenciosa |
| VOL-UT-004 | Eventos fora de ordem | Rejeitar/quarentena e auditar |
| VOL-UT-005 | Duplicados | Política determinística e contagem auditável |
| VOL-UT-006 | Feed parado | STALE, watchdog e bloqueio dependente |
| VOL-UT-007 | Contrato/rolagem diferente | Não comparar sem ajuste explícito |
| VOL-UT-008 | Granularidades diferentes | Não assumir equivalência temporal |
| VOL-UT-009 | MAD/baseline zero | Score desconhecido, sem infinito artificial |
| VOL-UT-010 | VIX atrasado | Contexto externo STALE |
| VOL-UT-011 | OHLC incompleto | Estimador OHLC não publica valor válido |
| VOL-UT-012 | Dado futuro face à decisão | Bloquear por leakage |
| VOL-UT-013 | Sessão parcial | Identificar como parcial |
| VOL-UT-014 | Reconexão | Reconciliar e preservar lacuna |
| VOL-UT-015 | Estimadores divergentes | Expor divergência e reduzir confiança |

Esta lista especifica testes a executar; não afirma que já foram executados.

## 14. Riscos e vantagens investigáveis

| Risco | Mitigação |
|---|---|
| Bid-ask bounce/ruído | Comparar frequências, trade vs midquote e estimadores robustos |
| Amostragem irregular | Registar durações e testar amostragem alternativa |
| Saltos/gaps | Métricas separadas e análise por sessão |
| Mudança de regime | Rolling baseline e monitorização de drift |
| Leakage/sobreajuste | Validação cronológica, congelamento de parâmetros e teste final intocado |
| Dessincronização | Timestamps comparáveis e gates de atualidade |
| Escalas distintas | Métricas normalizadas e contratos por instrumento |
| Confundir magnitude com direção | Separar volatilidade, direção, liquidez e sinal de estratégia |
| Confundir VIX com B3 | Variável explicativa externa, testada contra baseline |

Vantagens a investigar, não presumidas: detetar expansão/compressão; identificar sessões anormais; distinguir amplitude de ruído; adequar o contexto de risco; melhorar leitura de ticks/60K; detetar dados degradados antes de contaminarem o Giroscópio; medir se VIX acrescenta informação incremental.

## 15. Critério de escolha

- Baseline: desvio-padrão e RV, pela simplicidade.
- OHLC temporal: avaliar Parkinson, Garman–Klass, Rogers–Satchell e Yang–Zhang conforme pressupostos.
- Amplitude operacional: ATR em pontos/ticks.
- Alta frequência: estudar microestrutura, frequência e estimadores robustos.
- Previsão: EWMA/GARCH/HAR-RV contra baselines.
- Caudas: quantis, MAD e diagnósticos de salto.
- Opções/VIX: domínio separado com metodologia própria.
- Tick/60K/Renko: perfil próprio, sem equivalência presumida.

A seleção final deve considerar estabilidade, qualidade, atraso, custo computacional, calibração e utilidade incremental demonstrada — não complexidade matemática por si só.

## 16. Pendências de decisão

Fontes autorizadas e cobertura de WIN/WDO; preço representativo (negócio, midquote ou barra); frequência temporal; leilões/abertura/fecho/interrupções; ajustes e rolagem; janelas e baselines; definição da confiança; limites de regime e histerese; freshness por fonte; retenção/licenças RAW; fronteira com MODULOS/10_VOLATILIDADE_VIX; contrato técnico do Giroscópio. Até decisão formal, estes itens são PENDING/UNKNOWN e não podem ser inferidos no código.

## 17. Fontes metodológicas

1. McAleer & Medeiros, *Realized Volatility: A Review* (2008): https://doi.org/10.1080/07474930701853509
2. Wang et al., *Volatility analysis in high-frequency financial data* (2014): https://doi.org/10.1002/wics.1330
3. Aït-Sahalia & Mykland, *Estimating Volatility in the Presence of Market Microstructure Noise* (2009): https://doi.org/10.1007/978-3-540-71297-8_25
4. Barndorff-Nielsen et al., *Realized kernels in practice: trades and quotes* (2009): https://doi.org/10.1111/j.1368-423X.2008.00275.x
5. Cboe, metodologia oficial dos índices de volatilidade: https://cdn.cboe.com/api/global/us_indices/governance/Volatility_Index_methodology_VIXMO_only.pdf
6. Cboe, FAQ do VIX: https://www.cboe.com/tradable_products/vix/faqs

Estas fontes fundamentam famílias de métodos e riscos gerais. Não validam limiares, frequências ou performance específica para B3/WIN/WDO.

## 18. Evidência e limitações

- Especificação documental; não prova código implementado nem integração.
- Nenhum backtest, benchmark, teste B3 ou teste em tempo real é declarado.
- Não se afirma disponibilidade de feed intradiário, opções, bid/ask ou séries reconciliadas.
- Limiares e pesos de confiança permanecem por definir.
- Algumas famílias (em especial Yang–Zhang e testes formais de saltos) exigem especificação de implementação completa antes da codificação.
- Não há autorização de ordens, produção ou promessa de desempenho.
- Revisão e aprovação formal pendentes.

## 19. Histórico de alterações

| Versão | Data | Alteração | Estado |
|---|---|---|---|
| 1.0.0 | 2026-10-18 | Definição inicial de estimadores, fórmulas, qualidade, regimes, testes e roadmap | Proposta em revisão |

## 20. Integridade documental

Calcular SHA-256 canónico em UTF-8 com finais de linha LF, excluindo apenas as duas linhas de metadados que contêm SHA-256 (conteúdo canónico) e Commit de referência (versão anterior), conforme a norma do repositório GOVERNANCA. Após publicação, reler o ficheiro no GitHub, recalcular e comparar. Se houver divergência, não declarar a verificação concluída.
