---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "GOVERNANCA_DOCUMENTAL"
id_documento: "BM-DOC-ARQUITETURA-BRICKMASTER-RAIZ-ARQUITETURA-MODULAR-BASELINE-2026-10"
titulo: "BRICKMASTER RAIZ — Estrutura Arquitetural e Plano de Evolução"
status: "EM_DESENVOLVIMENTO"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Conteúdo preexistente; ver histórico Git e referências internas"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR de padronização documental; commit a registar após criação"
escopo: "Documento existente em ARQUITETURA/BRICKMASTER_RAIZ/ARQUITETURA_MODULAR_BASELINE_2026-10-11.md"
objetivo: "Preservar o conteúdo original com identificação, estado e rastreabilidade padronizados"
dependencias: "N/A"
---
# BRICKMASTER RAIZ — Estrutura Arquitetural e Plano de Evolução

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Tipo:** DOCUMENTO TÉCNICO  
> **Fase:** GOVERNANÇA DOCUMENTAL  
> **ID:** BM-DOC-ARQUITETURA-BRICKMASTER-RAIZ-ARQUITETURA-MODULAR-BASELINE-2026-10  
> **Status:** EM_DESENVOLVIMENTO  
> **Versão:** 0.1.0  
> **Criação:** 2026-10-11  
> **Atualização:** 2026-10-11  
> **Origem:** Conteúdo preexistente; ver histórico Git e referências internas  
> **Autoridade:** GOVERNANÇA  
> **Rastreabilidade:** PR de padronização documental; commit a registar após criação

Projeto: BRICKMASTER RAIZ  
Documento: Arquitetura modular — baseline de continuidade  
Versão: 0.1.0  
Data: 2026-10-11  
Estado: PROPOSTA ESTRUTURAL — não significa código implementado nem estratégia validada  
Referência NTSL prioritária: Manual NTSL — Versão 4.4, 03/08/2026  
Repositório central: https://github.com/carlos-andrade/BRICKMASTER_GERAL

## 1. Objetivo do sistema

O BRICKMASTER é concebido como um sistema operacional modular para reduzir o problema de o operador não saber com precisão onde está no gráfico, qual é o contexto estrutural e que evidências sustentam uma decisão. A arquitetura separa leitura de contexto, deteção de eventos, validação, visualização, gestão de risco e execução.

A meta de referência de 1% a partir da abertura diária é um objetivo de projeto a testar, não uma promessa de rentabilidade nem uma obrigação de operar. A arquitetura deve permitir ausência de operação quando não houver condições verificáveis.

O sistema foi idealizado para gráficos atemporais baseados em ticks, incluindo a referência operacional de 60K ticks. Cada módulo deve declarar os tipos de gráfico suportados e as diferenças entre histórico, replay, backtest e tempo real.

## 2. Princípios arquiteturais

1. Modularidade: cada módulo tem responsabilidade, entradas, saídas, estados, dependências e testes próprios.
2. Separação entre sinal e ordem: detetar um evento não autoriza automaticamente uma operação.
3. Evidência rastreável: cada classificação expõe os dados que a sustentam e a razão de aprovação/rejeição.
4. Sem indicadores opacos: privilegiar cálculos e regras explícitas, testáveis e documentados.
5. Não repintar silenciosamente: declarar dependência de candle/tick em formação ou de dados confirmados.
6. Fail-safe: dados ausentes, inválidos, atrasados ou contraditórios bloqueiam decisões dependentes deles.
7. Testes independentes antes do acoplamento: novos módulos são testados isoladamente antes da integração.
8. NTSL documentada como contrato: confirmar sintaxe, funções e limitações no Manual 4.4 antes de declarar compatibilidade.
9. Sem alegações de lucro garantido: métricas históricas não garantem resultados futuros.
10. Checkpoint verificável: cada etapa termina com artefacto, teste, resultado, limitações e próximo passo.

## 3. Camadas do sistema

### L0 — Dados e integridade
- Dados OHLC/negócios disponíveis no gráfico.
- Data/hora, ativo, vencimento/contrato e tipo de gráfico.
- Verificação de dados ausentes, valores impossíveis e mudanças de sessão.
- Proveniência e grau de confiança de cada campo.
- Não presumir que todo dado de fluxo (agressor, delta, book, volume financeiro) está disponível em NTSL; verificar suporte real da plataforma e da fonte.

### L1 — Relógio e estado da sessão
- Identificar abertura, sessão atual, mudança de dia e encerramento.
- Guardar a referência da abertura diária.
- Calcular distância absoluta e percentual desde a abertura.
- Distinguir horário de negociação, horário do dado e horário local da máquina.
- Bloquear decisões com abertura indefinida ou sessão incorretamente identificada.

### L2 — Contexto e localização no gráfico: GIROSCÓPIO
O GIROSCÓPIO é o núcleo de orientação contextual, não um indicador isolado. Deve responder:
- Em que regime/contexto o mercado está?
- Onde está o preço relativamente à abertura, estrutura recente e referências habilitadas?
- Há expansão, compressão, equilíbrio, deslocamento ou possível exaustão?
- Quais evidências concordam e quais divergem?
- Qual é o estado de confiança e porquê?

Saída conceptual: estado de contexto, direção/neutralidade, referências relevantes, qualidade dos dados, evidências favoráveis/contrárias e motivo de bloqueio. A definição matemática dos estados permanece por validar empiricamente.

### L3 — Estrutura de preço
- Swing highs/lows e estrutura local.
- Deslocamentos e rompimentos com regras explícitas.
- FVG Atlas: deteção, dimensão, origem, direção, idade e estado de mitigação.
- Liquidez: níveis observáveis, varredura potencial e reação posterior.
- Contador de toques: nível, número de toques, distância mínima entre toques e invalidação.
- Cada evento tem identificador estável e ciclo de vida documentado.

### L4 — Fluxo e confirmação
- Cumulative Delta, apenas se houver fonte confiável e definição verificável de agressão.
- Volume financeiro e variação relativa ao contexto.
- VWAPs diárias e gap entre VWAPs; TWAP apenas quando definição e dados estiverem disponíveis.
- VIX como contexto externo, com fonte, timestamp, atraso e sincronização documentados.
- IBOV como referência contextual, sem presumir correlação constante com WIN/WDO.
- Divergência entre preço e fluxo gera evidência, não conclusão automática de reversão.

### L5 — Calendário macroeconómico
- Eventos relevantes, como decisões de juros, inflação e emprego.
- Registar fonte, horário, fuso, consenso, valor divulgado e hora de atualização, quando disponíveis.
- Definir janelas pré-evento/pós-evento configuráveis e testáveis.
- Se calendário ou horário forem duvidosos, marcar contexto como desconhecido; não inventar eventos.

### L6 — Motor de hipóteses e confluência
- Recebe eventos dos módulos anteriores.
- Aplica regras explícitas e versionadas.
- Separa evidência observada, hipótese e condição de invalidação.
- Não somar pontos arbitrários sem calibração; pesos só entram após análise empírica.
- Saídas: LONG, SHORT, NEUTRO ou BLOQUEADO, com explicação auditável.

### L7 — Risco e objetivo diário
- Definir risco por operação, limite diário de perda, exposição máxima, número máximo de tentativas e regra de interrupção.
- A meta de 1% desde a abertura não substitui stop, limite de perda ou validação estatística.
- Ao atingir limite de risco ou detetar dados inconsistentes, bloquear novas entradas.
- Considerar custos, slippage, spread, liquidez e diferenças entre backtest e execução real.

### L8 — Execução NTSL
- Só recebe decisão aprovada pelo motor e pelo módulo de risco.
- Estado de posição, ordens pendentes, cancelamento, saída e reversão devem ser tratados explicitamente.
- Automação desativada durante testes de lógica.
- Usar funções NTSL após validação na versão 4.4 e no ambiente real da plataforma.
- Compilar ou passar no backtest não prova que ordens reais foram testadas.

### L9 — Observabilidade e auditoria
- Log por ciclo: timestamp, ativo, contexto, eventos, decisão, motivo, posição/ordens e resultado.
- Códigos de motivo: DATA_INVALID, CONTEXT_UNKNOWN, EVENT_UNCONFIRMED, RISK_BLOCK, NO_CONFLUENCE, SESSION_CLOSED.
- Métricas: falsos positivos, eventos não detetados, latência, excursão adversa/favorável e resultado líquido após custos.
- Watchdog monitoriza atualização, estado de sessão e falhas; alerta não equivale a autorização para operar.

## 4. Contrato mínimo de cada módulo

Todo módulo novo deve incluir:
1. Identificador e versão.
2. Problema que resolve e o que explicitamente não resolve.
3. Entradas, unidades, fonte e pressupostos.
4. Regras matemáticas ou pseudocódigo determinístico.
5. Saídas e significado de cada estado.
6. Tratamento de dados inválidos, início de sessão e histórico insuficiente.
7. Dependências e compatibilidade de gráfico, incluindo ticks/60K quando aplicável.
8. Testes unitários com casos positivos, negativos, limítrofes e dados ausentes.
9. Comparação entre histórico, replay, backtest e tempo real.
10. Critérios de aceitação e evidência anexada.
11. Limitações conhecidas e riscos de repintura.
12. Instruções de integração e rollback.

## 5. Sequência recomendada de desenvolvimento

| Fase | Entrega | Critério de saída |
|---|---|---|
| 00 | Inventário do repositório e fontes | Arquivos classificados; duplicados e lacunas identificados |
| 01 | Contratos de dados, relógio e sessão | Abertura diária e transição de sessão testadas |
| 02 | GIROSCÓPIO contextual mínimo | Estados explicáveis e testes determinísticos |
| 03 | Estrutura de preço | Swings e eventos reproduzíveis |
| 04 | FVG Atlas isolado | Deteção, dimensão, estado e ciclo de vida testados |
| 05 | Liquidez e contador de toques | Regras de varredura/toque e invalidação testadas |
| 06 | Fluxo e confirmações | Apenas campos realmente disponíveis; sincronização medida |
| 07 | Calendário macro | Fuso, fonte e janelas de bloqueio validados |
| 08 | Confluência e hipóteses | Decisões explicáveis, incluindo NEUTRO/BLOQUEADO |
| 09 | Risco e objetivo diário | Limites testados em cenários de perda e falha |
| 10 | Integração NTSL em observação | Sem envio de ordens; logs coerentes |
| 11 | Backtest/replay e robustez | Custos, slippage, amostras e regimes documentados |
| 12 | Simulação/paper trading | Execução simulada comparada com sinais |
| 13 | Ativação gradual | Apenas após critérios de aceitação e aprovação explícita |

A sequência é uma proposta de controlo de risco; o inventário real do repositório pode exigir reordenamento.

## 6. Plano de validação quantitativa

Para qualquer setup, reportar:
- Período, ativo/contrato, tipo de gráfico e fonte dos dados.
- Número de operações e distribuição por dia/regime.
- Resultado bruto e líquido de custos.
- Expectância por operação, profit factor, drawdown máximo e recuperação.
- Taxa de acerto acompanhada do ganho médio/perda média.
- MAE/MFE, exposição e perdas consecutivas.
- Sensibilidade a parâmetros e teste fora da amostra.
- Comparação com baseline simples e períodos de mercado diferentes.
- Evidência de ausência de look-ahead, repaint e leakage.
- Diferenças entre preço teórico e execução simulada/real.

Nenhuma métrica isolada comprova vantagem estatística. Um setup só pode ser considerado promissor após robustez fora da amostra e confirmação em simulação.

## 7. Estado documental inicial dos módulos

| Módulo | Estado nesta arquitetura | Próxima validação necessária |
|---|---|---|
| GIROSCÓPIO | Conceito central definido | Especificar estados, variáveis observáveis e transições |
| FVG Atlas | Módulo independente previsto | Inventariar código existente e formalizar ciclo de vida |
| Liquidez | Módulo previsto | Definir sweep, nível de referência e confirmação |
| Contador de toques | Módulo previsto | Definir tolerância, separação temporal e invalidação |
| VWAP/TWAP | Requisito de contexto | Confirmar cálculo, dados e sincronização |
| Cumulative Delta | Requisito condicional | Confirmar disponibilidade e semântica da fonte |
| VIX | Filtro contextual condicional | Definir fonte, atraso e sincronização |
| IBOV | Referência contextual | Definir cálculo e validar relação com o ativo |
| Calendário económico | Módulo de contexto | Fonte oficial, fuso e política de bloqueio |
| Watchdog | Observabilidade | Especificar heartbeat, timeouts, alertas e recuperação |
| Execução NTSL | Posterior à validação | Consultar Manual 4.4 e testar sem ordens reais |

Esta tabela regista estado documental, não prova que módulos não existam noutros arquivos do repositório.

## 8. Checkpoint obrigatório por etapa

Cada checkpoint responde:
- O que foi pedido?
- O que foi inspecionado? Listar caminhos e versões.
- O que foi alterado? Arquivos e diffs.
- O que foi executado? Comando e ambiente, sem alegar execução não realizada.
- Qual foi o resultado? PASS, FAIL ou BLOCKED, com evidência.
- O que não foi verificado?
- Há regressões ou riscos?
- Qual é o próximo passo único e objetivo?
- Como reverter?

Estados padronizados:
- PASS: critério executado e comprovado.
- FAIL: teste executado e falhou.
- BLOCKED: não foi possível executar ou falta pré-requisito.
- NOT_RUN: ainda não executado.
- PROPOSED: desenho/documentação sem implementação.

## 9. Próximo passo imediato

Fase 00 — Inventário real do repositório. Mapear diretórios e arquivos existentes, identificar documentação de arquitetura, módulos FVG Atlas, Liquidez, Market DNA, Contador de Toques, Watchdog e manuais NTSL. Não substituir nem apagar material existente. Produzir um índice com caminho, função, versão, estado, dependências, duplicidade provável e ação recomendada. Só depois selecionar o primeiro módulo a implementar.

## 10. Fontes e limites

- Repositório central indicado pelo projeto: https://github.com/carlos-andrade/BRICKMASTER_GERAL
- Manual NTSL fornecido: Versão 4.4, datado de 03/08/2026 — referência primária para validar linguagem e funcionalidades NTSL.
- Repositório relacionado FVG Atlas: https://github.com/carlos-andrade/FVG-ATLAS
- Consultar diretamente as referências antes de alegar que uma implementação existe, compila ou foi testada.
- Este documento é uma proposta arquitetural inicial; não constitui validação de rentabilidade nem confirmação de execução de código.


## Contexto Histórico

Contexto histórico preservado no conteúdo preexistente e no histórico Git. Não foram inferidas datas ou decisões que não estivessem documentadas.


## Estado

Estado documental no momento da padronização: EM_DESENVOLVIMENTO. Este estado não comprova execução nem validação técnica.


## Evidências

O conteúdo original deste arquivo e o histórico de versões do Git são as fontes de evidência disponíveis. Evidências externas ou testes não foram presumidos.


## Validação

Validação estrutural do cabeçalho realizada nesta alteração; a validação funcional/técnica do conteúdo não é declarada por esta padronização.


## Resultado

Cabeçalho documental padronizado sem intenção de alterar as regras ou o conteúdo técnico preexistente.


## Próxima Ação

Rever os metadados, preencher datas/versões desconhecidas com evidência verificável e executar os testes específicos quando aplicável.
