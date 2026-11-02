<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: IFNC ATLAS — Especificação Técnica
IDENTIFICADOR: BM-020-SPEC
VERSÃO: 0.1.0
ESTADO: DOCUMENTADO — EXPERIMENTAL — NÃO VALIDADO
CRIADO EM: 2026-11-02
ÚLTIMA REVISÃO: 2026-11-02
SHA-256: PENDENTE — calcular no checkpoint de validação, antes do merge
COMMIT DE REFERÊNCIA: 4f5b5ad608fd045e6b5d48d8603239264843e719
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-11-02 | v0.1.0 | Arquitetura e especificação inicial.
FONTE DA VERDADE: repositório oficial e fontes B3 versionadas.
-->

# SPEC — BRICKMASTER IFNC ATLAS

## 1. Problema e hipótese

Problema: o operador pode interpretar o IBOV/WIN sem medir a participação do setor financeiro, mesmo quando esse setor influencia materialmente o índice.

Hipótese testável: variáveis derivadas do IFNC e de seus constituintes podem acrescentar informação incremental à previsão/explicação de retornos, volatilidade ou regime do IBOV e do WIN, condicionadas ao contexto já disponível.

A hipótese será rejeitada se não superar benchmarks simples fora da amostra, após custos e controle de múltiplos testes.

## 2. Arquitetura lógica

1. **Ingestion:** captura IFNC, IBOV, constituintes, calendário e metadados da carteira.
2. **Canonicalization:** normalização de símbolos, timestamps, timezone, sessões, preços e unidades.
3. **Quality Gate:** validação de atraso, lacunas, duplicidade, sequência temporal e coerência.
4. **Historical Registry:** armazenamento append-only de observações e versões de carteiras.
5. **Feature Engine:** cálculo de retornos, força relativa, breadth, dispersão, contribuição e alinhamento VWAP quando houver dados intradiários compatíveis.
6. **Research Engine:** testes de associação, incrementalidade, estabilidade e previsão.
7. **Atlas State:** classificação descritiva do contexto setorial.
8. **Gyroscope Adapter:** entrega de estado, evidências, confiança e invalidações ao BM-001.
9. **Observability:** logs, métricas, replay, auditoria e watchdog.

## 3. Fluxo

Fontes -> Ingestion -> Canonicalization -> Quality Gate -> Historical Registry
-> Feature Engine -> Research/Atlas State -> Gyroscope Adapter
-> BM-001 Giroscópio -> BM-014 Risco / BM-017 Watchdog.

O IFNC ATLAS não se conecta diretamente ao adaptador de execução.

## 4. Universo e relógios

- IFNC: índice setorial financeiro da B3.
- IBOV: benchmark amplo de ações brasileiras.
- WIN: contrato futuro de mini-índice identificado por vencimento/símbolo, sem misturar contratos.
- Constituintes: composição oficial válida em cada data, com pesos e vigência histórica.
- Timezone canônico: America/Sao_Paulo; guardar também timestamp UTC.
- Calendário: pregões, leilões, feriados, horário especial e eventos macroeconômicos.
- Cada observação deve conter event_time, ingest_time e source_time quando disponíveis.
- Sincronização deve usar somente informação efetivamente disponível no instante de decisão.

## 5. Features — definições iniciais

Sejam P_X(t) níveis de índice/preço válidos e sincronizados. Retornos simples:
r_X(t,h) = P_X(t) / P_X(t-h) - 1.
Usar log-retorno em análises estatísticas quando especificado no protocolo.

### 5.1 Força relativa IFNC/IBOV
FR(t,h) = [P_IFNC(t)/P_IFNC(t-h)] / [P_IBOV(t)/P_IBOV(t-h)] - 1.
FR positiva indica desempenho relativo do IFNC superior ao IBOV no horizonte h. Não é previsão nem sinal direcional automático.

### 5.2 Divergência setorial
DIV(t,h) = r_IFNC(t,h) - r_IBOV(t,h).
Reportar em pontos percentuais, com horizonte e timestamps.

### 5.3 Breadth dos constituintes
BREADTH(t) = (N_up - N_down) / N_valid.
N_up e N_down são contagens de constituintes com retorno positivo/negativo no horizonte definido. N_valid é o número de constituintes válidos e sincronizados. Empates em zero ficam fora do numerador. Publicar cobertura N_valid/N_expected.

### 5.4 Participação ponderada
PART(t) = soma_i [w_i(t0) * s_i(t,h)] / soma_i [w_i(t0)] sobre constituintes válidos, com s_i definido como sinal do retorno (+1, 0, -1).
Usar pesos oficiais válidos no instante t0, sem retroagir carteira futura. Se cobertura ponderada for insuficiente, saída inválida.

### 5.5 Dispersão
DISP(t,h) = desvio-padrão transversal dos retornos dos constituintes válidos. Publicar N e método de ponderação. Não confundir dispersão alta com direção.

### 5.6 Volatilidade relativa
VOL_REL = RV_IFNC(h) / RV_IBOV(h), com retornos sincronizados e estimador explicitado. Se denominador zero/ausente, inválido.

### 5.7 Alinhamento intradiário
Quando dados intradiários comparáveis existirem: distância do IFNC e IBOV às respectivas VWAPs, em unidades de volatilidade ou basis points. Não fabricar VWAP de tick a partir de candles agregados sem declarar a perda de informação.

### 5.8 Relação com WIN
Calcular correlação, beta rolling e resposta futura do WIN a features IFNC, com janelas pré-registradas (5m, 30m e diário). WIN e IBOV devem usar relógio, sessão, contrato e convenção de retorno coerentes. Correlação não implica causalidade.

## 6. Estado do Atlas

Estados descritivos:
- FINANCIAL_SECTOR_STRONG: força relativa e breadth positivos, com cobertura adequada.
- FINANCIAL_SECTOR_WEAK: força relativa e breadth negativos, com cobertura adequada.
- MIXED: sinais contraditórios ou dispersão elevada sem direção consistente.
- NEUTRAL: evidência próxima de zero.
- DEGRADED: dados incompletos, atrasados ou cobertura insuficiente.
- BLOCKED: dados críticos inválidos, relógio inconsistente ou histórico/carteira indisponível.

O estado deve incluir evidências e regras que o produziram. Limiares numéricos serão calibrados somente no protocolo de pesquisa e congelados antes da validação fora da amostra.

## 7. Confiança

Confidence não é probabilidade de acerto. É escore de qualidade da evidência, inicialmente [0,1], derivado de:
- freshness;
- coverage;
- timestamp alignment;
- source integrity;
- constituent-weight coverage;
- cross-source consistency.

Se qualquer gate crítico falhar, Confidence = 0 e status DEGRADED/BLOCKED, conforme severidade. Não compensar falha crítica com média ponderada.

## 8. Regras de histórico e anti-bias

- Armazenar snapshots de carteira por vigência e data de publicação, incluindo pesos, free float quando disponível, versão da metodologia e fonte.
- Não usar composição atual para reconstruir períodos passados.
- Guardar revisões e correções como novos registos; nunca sobrescrever o original.
- Persistir dado bruto, dado normalizado, feature, versão do código e parâmetros.
- Backtest usa o timestamp de disponibilidade, não apenas o timestamp de referência.
- Corporate actions, mudanças de ticker, proventos e ajustes de índice devem ser rastreáveis.
- Separar data de publicação da carteira, data de vigência e data de captura.

## 9. Segurança operacional

O módulo é somente leitura. Não gera ordem, quantidade, preço de ordem nem autorização de execução. O BM-014 permanece soberano. Em indisponibilidade do IFNC, o sistema não deve inferir estado setorial: deve sinalizar DEGRADED/BLOCKED e permitir que o Giroscópio aplique sua política de contexto ausente.

## 10. Limitações

- Disponibilidade e granularidade intradiária do IFNC precisam ser verificadas na fonte de dados contratada.
- Pesos e carteiras podem ser revistos.
- A composição setorial muda ao longo do tempo.
- O WIN é derivativo com basis, rolagem, vencimento e dinâmica própria.
- O IFNC pode ser redundante com seus constituintes ou com o próprio IBOV.
- Relações variam por regime e evento macro.
