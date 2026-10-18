# CARTA-CONTRATO — MÓDULO VOLATILIDADE B3
### BRICKMASTER RAIZ

| Campo | Valor |
|---|---|
| **ID** | BM-VOL-CARTA-001 |
| **Projeto** | BRICKMASTER RAIZ |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | CARTA_CONTRATO_MODULAR |
| **Fase** | F2 — Requisitos e desenho |
| **Estado** | PROPOSTA_PARA_APROVACAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 39376f7c7c7fb635fccc9edf50b2c18adf92c730c52e4e300b86b79e5de010ec |
| **Commit de referência (versão anterior)** | [9e452d000992630c54fa0ca274cb4fd433aff9a0](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/9e452d000992630c54fa0ca274cb4fd433aff9a0) |
| **Data de criação** | 2026-10-18 |
| **Responsável técnico** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [Constituição da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Normas aplicáveis** | [Carta/Contrato padrão de roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md); [Roadmap padrão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md); [Norma de cabeçalho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Prompt especializado** | [PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md](PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md) |
| **Base conceptual** | [BASE PARA PROMPT.md](BASE%20PARA%20PROMPT.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

---

## 1. Objeto e compromisso

Esta Carta/Contrato define o mandato, os limites, as responsabilidades, os critérios de decisão e os gates de evolução do módulo **VOLATILIDADE** do BRICKMASTER RAIZ, com foco na investigação quantitativa da volatilidade dos instrumentos negociados na B3.

O módulo deve transformar dados de mercado verificáveis em contexto de volatilidade mensurável, rastreável e adequado ao consumo pelo Giroscópio. Deve ajudar a caracterizar regimes e condições de risco, investigar hipóteses operacionais e identificar quando a informação é insuficiente para uma conclusão segura.

A Carta é o contrato de governação do módulo. Não representa, por si só, especificação quantitativa concluída, código implementado, validação de mercado, autorização de integração ou aprovação para produção.

## 2. Objetivos

1. Distinguir volatilidade realizada/histórica, implícita e indicadores externos de contexto.
2. Descrever regimes, expansão, compressão, transições, extremos e incerteza com definições mensuráveis e testáveis.
3. Garantir proveniência, qualidade, sincronização, atualidade e rastreabilidade dos dados.
4. Investigar se a informação de volatilidade melhora a caracterização de risco ou o desempenho de métodos existentes, comparada com baselines e após custos realistas.
5. Fornecer ao Giroscópio contexto com estado, confiança, timestamps, divergências e motivos de bloqueio.
6. Preservar a separação entre dados, cálculo, interpretação, decisão, risco soberano, execução conciliada e watchdog.
7. Manter resultados negativos, limitações, alterações e decisões no histórico do repositório.

## 3. Âmbito

### Incluído

- Investigação de volatilidade dos instrumentos B3 para os quais existam dados adequados e uso autorizado.
- Estudo inicial de WIN e WDO, sem excluir outros instrumentos quando houver dados e requisitos aprovados.
- Métricas intradiárias, históricas/realizadas, relativas, de cauda, expansão/compressão e transição de regime.
- Volatilidade implícita somente quando existirem dados de opções e metodologia apropriada.
- Contexto intermercado, incluindo VIX, apenas como variável externa a testar; não como substituto direto da volatilidade de um ativo brasileiro.
- Gráficos temporais e gráfico de 60K trades, respeitando as diferenças de amostragem. O BRICKMASTER não usa gráficos de ticks nem Renko.
- Qualidade e reconciliação de dados, especificação de contratos, testes isolados, evidências e monitorização de falhas.

### Excluído

- Envio, alteração ou cancelamento de ordens.
- Substituição ou enfraquecimento da autoridade soberana do módulo Risco.
- Promessas de rentabilidade, previsões garantidas ou alegações de vantagem sem evidência reproduzível.
- Definição de limiares numéricos sem especificação e validação.
- Promoção direta de resultados experimentais para validação ou produção.
- Assumir disponibilidade de feeds, dados históricos, cadeia de opções ou interfaces de outros módulos sem confirmação.

## 4. Princípios obrigatórios

### 4.1 Evidência antes de conclusão
Cada conclusão quantitativa deve apontar para dados, método, período, amostra, versão e artefacto reproduzível. Ficheiro criado ou código escrito não prova que o teste foi executado nem que o resultado foi validado.

### 4.2 Fail-closed
Dados críticos ausentes, atrasados, inválidos, dessincronizados ou contraditórios devem reduzir confiança, produzir `DESCONHECIDO` ou bloquear a conclusão dependente deles. Nunca converter silêncio ou falta de dados em confirmação.

### 4.3 Separação de responsabilidades
O módulo calcula e contextualiza volatilidade. Não decide autonomamente a exposição final, não executa operações e não substitui Risco, Execução ou Watchdog.

### 4.4 Risco acima da meta
A hipótese de **1% desde a abertura do dia** é apenas uma hipótese de investigação. Não é promessa, objetivo obrigatório de cada sessão nem fundamento para aumentar risco ou relaxar controlos.

### 4.5 Histórico preservado
Não apagar silenciosamente resultados desfavoráveis, versões, hipóteses rejeitadas, exceções ou decisões anteriores. Correções devem ser registadas no histórico Git e no changelog pertinente.

### 4.6 Comparabilidade
Não equiparar diretamente métricas por barra temporal e por barra do gráfico de 60K trades: a duração de uma barra de 60K trades não é fixa. Registar instrumento, contrato, unidade, sessão, método de amostragem e normalização aplicada.

### 4.7 VIX e fontes externas
Não apresentar VIX como medição direta da volatilidade realizada do WIN, WDO, IBOV ou de ações brasileiras. Qualquer utilidade preditiva ou contextual deve ser testada com sincronização temporal e ganho incremental demonstrável.

### 4.8 Sem progresso inventado
Percentuais de conclusão só podem ser publicados segundo a norma da GOVERNANCA, a partir de critérios definidos e evidências. Enquanto não houver scorecard válido, usar estado qualitativo e listar pendências.

## 5. Contrato funcional preliminar

### Entradas

Quando disponíveis e necessários, os dados devem identificar:

- instrumento e contrato/vencimento;
- fonte e permissão de utilização;
- preço/retorno e unidade, granularidade e método de amostragem;
- timestamp do evento e timestamp da receção, com timezone;
- sessão/calendário, ajustes, leilões, gaps e rollover;
- estado de qualidade, idade do dado e transformações aplicadas;
- versão/identificador da série ou dataset e evidência de reconciliação.

### Saídas

A saída proposta deve transportar, no mínimo:

- instrumento, contrato e timestamps;
- estado dos dados e idade/atualidade;
- métrica, valor, unidade, janela e método;
- regime preliminar: `DESCONHECIDO`, `BAIXO`, `NORMAL`, `ELEVADO` ou `EXTREMO`;
- tendência da volatilidade e transição de regime, apenas quando calculáveis;
- confiança, divergências, limitações e motivo de bloqueio;
- estado de validação e referências às evidências.

Os rótulos de regime são uma taxonomia inicial, não limiares aprovados. O esquema, os tipos, os enums e as regras de validade só se tornam contrato estável depois da aprovação de `CONTRATOS.md`.

## 6. Responsabilidades e fronteiras

| Componente | Responsabilidade do módulo VOLATILIDADE | Limite obrigatório |
|---|---|---|
| Dados/Qualidade | Consumir dados identificados e expor problemas detetados | Não mascarar dados ausentes ou contraditórios |
| Cálculo/Estimadores | Calcular métricas especificadas e reproduzíveis | Não inventar parâmetros nem mudar método silenciosamente |
| Classificação | Produzir regime e confiança segundo regras aprovadas | Não forçar rótulo quando a evidência divergir |
| Giroscópio | Receber contexto resumido e rastreável | Interface real pendente de confirmação |
| Estado Gráfico | Considerar tipo/granularidade, incluindo o gráfico de 60K trades | Não presumir equivalência entre tipos de gráfico |
| FVG, Fluxo/Volume, VWAP/TWAP, Market DNA | Possíveis consumidores/fontes contextuais | Integração apenas após contratos explícitos |
| Risco soberano | Receber informação de contexto quando aplicável | Mantém autoridade sobre bloqueios e exposição |
| Execução conciliada | Sem execução por este módulo | Nenhuma ordem pode ser emitida por esta Carta |
| Watchdog | Detetar falhas, atraso e divergências através de interface definida | Integração pendente de contrato e testes |
| `MODULOS/10_VOLATILIDADE_VIX/` | Possível especialização relacionada | Não migrar, duplicar ou eliminar antes da análise de fronteiras |

## 7. Método de investigação e aceitação

Cada hipótese deve ser escrita antes do teste e conter:

1. Pergunta falsificável, hipótese nula e hipótese alternativa.
2. Instrumento, contrato, período, fonte e critérios de qualidade.
3. Definição matemática, unidade, janela e baseline.
4. Momento em que cada variável estaria disponível, evitando look-ahead.
5. Divisão cronológica de desenvolvimento, validação e teste final.
6. Custos, spread, slippage e premissas realistas de execução quando o resultado incluir desempenho operacional.
7. Métricas de risco e estabilidade além do retorno bruto.
8. Critérios de aceitação/rejeição definidos antes da execução.
9. Análise de sensibilidade, subperíodos e risco de sobreajuste.
10. Logs, versões, dados e artefactos que permitam reproduzir o resultado.

Uma hipótese não é aceite apenas porque melhora um backtest isolado. Deve demonstrar robustez, ganho incremental em relação à baseline e limitações conhecidas. Correlação não será apresentada como causalidade.

## 8. Estados e promoção

Usar os estados do ciclo de vida definidos pela GOVERNANCA e mapear os estados locais de forma explícita:

- `PLANEADA`: trabalho ainda não iniciado.
- `EM_EXECUCAO`: trabalho em curso, sem implicar validação.
- `AGUARDANDO_EVIDENCIA`: artefacto ou teste necessário ainda não comprovado.
- `BLOQUEADA`: dependência crítica ou condição de segurança não satisfeita.
- `EM_REVISAO`: material disponível para revisão, ainda sem aceitação.
- `CONCLUIDA`: critérios do gate satisfeitos com evidência verificável.
- `ACEITE_COM_EXCECAO`: apenas com exceção explícita, limitada, justificada, aprovada e rastreável.

Para maturidade técnica, distinguir `EXPERIMENTAL`, `EM_VALIDACAO`, `VALIDADO` e `PRODUCAO_AUTORIZADA`. A promoção exige revisão e evidências correspondentes. A criação desta Carta não promove código ou estratégia.

## 9. Roadmap e gates

| Gate | Objetivo/entregáveis | Critério de saída | Estado atual |
|---|---|---|---|
| F0 — Estrutura inicial | Pasta e documentação inicial | Artefactos recuperáveis no histórico Git | CONCLUIDA — evidência no repositório |
| F1 — Adoção documental e levantamento | Cabeçalhos, normas, inventário e análise de sobreposição | Documentos conferidos; fronteiras e pendências registadas | EM_REVISAO |
| F2 — Requisitos e desenho | `ESPECIFICACAO.md`, `CONTRATOS.md`, inventário de dados e critérios de aceitação | Métricas, unidades, janelas candidatas, fontes, qualidade, regimes e falhas especificados e revistos | EM_EXECUCAO — início documental; critérios ainda pendentes |
| F3 — Construção isolada | Implementação isolada dos cálculos e classificação aprovados | Revisão técnica e análise estática apropriada | BLOQUEADA até fechar F2 |
| F4 — Testes e evidências | Testes sintéticos, dados históricos, robustez e replay/backtest quando aplicável | Execução demonstrada, resultados reproduzíveis e critérios satisfeitos | BLOQUEADA até existir implementação |
| F5 — Revisão e integração | Revisão de contratos com Giroscópio, Dados/Qualidade e Risco | Aprovação explícita, compatibilidade e rollback documentados | BLOQUEADA até F2–F4 |
| F6 — Prontidão/produção | Observabilidade, watchdog, recuperação e autorização | Gate de prontidão aprovado com evidência e autorização formal | BLOQUEADA até gates anteriores |

Os estados acima descrevem o estado documental conhecido nesta versão; não são percentuais de conclusão. Atualizar o roadmap após cada mudança material, sempre com evidência.

## 10. Ações prioritárias

1. **P1 — Levantamento arquitetural:** inspecionar `MODULOS/10_VOLATILIDADE_VIX/` e documentar fronteiras, diferenças e possíveis reutilizações; não presumir duplicação.
2. **P1 — Inventário de dados:** identificar fontes efetivamente acessíveis, permissões, instrumentos, granularidade, calendário, timestamps e qualidade.
3. **P1 — Especificação quantitativa:** criar `ESPECIFICACAO.md` com métricas candidatas, fórmulas, unidades, janelas candidatas, pressupostos e baselines, separando candidatos de parâmetros aprovados.
4. **P1 — Contratos:** criar `CONTRATOS.md` com schema, semântica, enums, frescura, confiança, bloqueios e compatibilidade com consumidores.
5. **P2 — Plano de testes:** criar `TESTES.md` com casos sintéticos, dados inválidos, transições de regime, look-ahead, robustez e critérios mensuráveis.
6. **P2 — Checkpoint e histórico:** manter `CHECKPOINTS.md` e `CHANGELOG.md` com decisões, bloqueios, commits e evidências.
7. **P3 — Construção:** iniciar código apenas após revisão dos requisitos e contratos.

## 11. Riscos e bloqueios

| Risco/bloqueio | Impacto | Ação de desbloqueio | Estado |
|---|---|---|---|
| Sobreposição possível com `10_VOLATILIDADE_VIX` | Fronteiras e responsabilidades podem ficar ambíguas | Inventariar ambos os módulos e aprovar decisão arquitetural | ABERTO |
| Fontes e licenças dos dados não confirmadas | Resultados podem não ser reproduzíveis ou autorizados | Identificar origem, termos de uso, timestamps e acesso | ABERTO |
| Fórmulas, janelas e limiares ainda não aprovados | Classificação não pode ser considerada quantitativamente definida | Especificar e testar alternativas contra baselines | ABERTO |
| Contratos de dependências não verificados | Integração pode interpretar campos de modo incompatível | Inspecionar contratos reais e acordar schema | ABERTO |
| Sem testes de cálculo/replay/backtest nesta fase | Não há evidência de desempenho ou validade operacional | Executar testes após F2/F3 e arquivar artefactos | ABERTO |
| Possível sobreajuste e look-ahead | Vantagem aparente pode não sobreviver fora da amostra | Protocolo cronológico, baseline, custos e teste final isolado | ABERTO |

Enquanto existir bloqueio crítico relevante, não promover o módulo nem declarar validade operacional.

## 12. Evidências e rastreabilidade

Artefactos de referência:

- [BASE PARA PROMPT.md](BASE%20PARA%20PROMPT.md) — base conceptual original, com limites explícitos.
- [PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md](PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md) — prompt de investigação proposto.
- [README.md](README.md) — âmbito, dependências, regras e roadmap local.
- [Análise de sobreposição com 10_VOLATILIDADE_VIX](ANALISE-SOBREPOSICAO-10-VOLATILIDADE-VIX.md) — levantamento preliminar; não prova duplicação de código.
- [GOVERNANCA — Carta/Contrato padrão de roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md).
- [GOVERNANCA — Roadmap padrão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md).

Cada resultado futuro deve ligar-se ao commit do código, versão dos dados, parâmetros, teste, logs/relatórios e decisão de revisão. Checksums só serão registados depois de calculados sobre uma definição canónica explícita; não preencher campos com valores estimados.

## 13. Decisões, exceções e alterações

- Decisões de arquitetura, métricas, limiares, fontes e interfaces devem ser registadas antes da implementação correspondente.
- Exceções devem conter motivo, âmbito, risco, controlos compensatórios, aprovador e validade.
- Alterações materiais à Carta exigem nova versão, entrada no histórico e revisão dos documentos dependentes.
- A Carta não autoriza ordens nem elimina a necessidade de aprovação humana para promoção de fase.

## 14. Critérios de aceitação desta Carta

- [x] Documento criado com objeto, âmbito, limites e responsabilidades explícitos.
- [x] Roadmap com gates, dependências, estados e critérios de saída.
- [x] Riscos, bloqueios e ações prioritárias identificados.
- [x] Prompt especializado e base conceptual referenciados.
- [ ] Aprovação formal do responsável/aprovador registada.
- [ ] Ligação da Carta adicionada ao README do módulo e verificada.

A criação do documento satisfaz apenas os critérios assinalados. A Carta permanece proposta até à aprovação formal; os gates técnicos continuam sujeitos à evidência descrita.

## 15. Próximo marco verificável

Fechar F1/F2 documental: inventariar a pasta VIX e as fontes de dados, aprovar fronteiras do módulo, e produzir `ESPECIFICACAO.md` e `CONTRATOS.md` revistos. Não iniciar construção de produção antes destes critérios.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-18 | Criação da Carta/Contrato do módulo VOLATILIDADE B3 com âmbito, responsabilidades, gates, riscos e critérios de aceitação | Commit Git a confirmar após publicação |