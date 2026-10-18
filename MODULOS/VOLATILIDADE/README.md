# Módulo VOLATILIDADE — BRICKMASTER RAIZ

| Campo | Valor |
|---|---|
| **ID** | BM-VOL-README-001 |
| **Projeto** | BRICKMASTER RAIZ |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | README_MODULO |
| **Fase** | F1 — Levantamento e adoção documental |
| **Estado** | EM_REVISAO |
| **Versão** | 1.3.0 |
| **SHA-256 (conteúdo canónico)** | 12fabcce4887af38230028ec0a6fc8efe715003eb6ecf6a548936c355c2fb781 |
| **Commit de referência (versão anterior)** | [70f09f95cfbfdc2df8a0dfffaa6a4b157e367b86](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/70f09f95cfbfdc2df8a0dfffaa6a4b157e367b86) |
| **Data de criação** | 2026-10-18 |
| **Data de atualização** | 2026-10-18 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Evolução do README preexistente; adoção documental baseada no repositório GOVERNANCA |
| **Autoridade superior** | [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md), [Norma de cabeçalho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md), [Carta de roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Adoção documental registada no histórico Git; fontes e evidências ligadas nas secções próprias |
| **Escopo** | Estrutura, especificação, teste e validação isolada do módulo VOLATILIDADE |
| **Objetivo** | Definir governança rastreável para o módulo antes da integração com o BRICKMASTER |
| **Dependências** | Giroscópio, Estado Gráfico, Dados/Qualidade, Fluxo/Volume, VWAP/TWAP, Intermercado e Risco; contratos efetivos ainda por verificar |

## Contexto Histórico

A pasta foi criada para reunir a definição do módulo de volatilidade. O documento `BASE PARA PROMPT.md` preserva o texto conceitual fornecido para orientar o desenvolvimento. A revisão documental atual aplica os padrões de cabeçalho, rastreabilidade, roadmap, evidência e ciclo de vida consultados no repositório GOVERNANCA.

Foi identificada no repositório uma pasta separada, `MODULOS/10_VOLATILIDADE_VIX/`. A relação funcional entre essa pasta e `MODULOS/VOLATILIDADE/` ainda não foi determinada. Não migrar, eliminar nem duplicar implementação até concluir o levantamento.

## Objetivo e âmbito

Centralizar a especificação e a evolução dos componentes de volatilidade do BRICKMASTER RAIZ, produzindo contexto para o Giroscópio sem gerar ordens de negociação.

Incluído:
- métricas de volatilidade observada e sua variação;
- classificação de regimes, com fórmulas, janelas, unidades e limiares documentados;
- qualidade, proveniência, sincronização e atualidade dos dados;
- interfaces propostas com os módulos consumidores;
- testes isolados, evidências reproduzíveis, limitações, decisões e versões.

Excluído nesta fase:
- execução ou envio de ordens;
- afirmações de rentabilidade ou garantia de atingir 1% desde a abertura;
- declarar limiares como validados sem evidência;
- considerar VIX substituto direto da volatilidade realizada do ativo operado.

## Contrato preliminar

### Entradas

Dados de mercado identificados, quando aplicável, por ativo, fonte, horário do evento, horário de receção, unidade, janela, método de cálculo e estado de qualidade. Dados externos, inclusive VIX, só podem ser usados após verificação de origem, disponibilidade, sincronização e finalidade.

### Saídas

O contexto proposto deverá identificar:
- regime: `DESCONHECIDO`, `BAIXO`, `NORMAL`, `ELEVADO` ou `EXTREMO`;
- métrica, valor, unidade, método e janela;
- ativo e fonte de origem;
- timestamp do evento e da receção;
- qualidade, atualidade e confiança;
- motivo de bloqueio ou advertência, quando aplicável.

Esta interface é preliminar. O contrato não será considerado estável até ser confrontado com os módulos dependentes.

## Regras de governança e segurança

1. **Evidência antes de alegação:** não declarar testes, publicação técnica, integração, aceitação ou produção sem artefactos verificáveis.
2. **Fail-closed:** dado crítico ausente, atrasado, inválido ou contraditório deve produzir `UNKNOWN/DESCONHECIDO` e bloquear decisões que dependam dessa informação.
3. **Separação de responsabilidades:** dados, cálculo, interpretação, decisão soberana de risco e execução permanecem separados. Este módulo não envia ordens.
4. **Risco prevalece sobre metas:** a hipótese de 1% desde a abertura é objetivo de investigação, nunca promessa nem autorização para ultrapassar limites de risco.
5. **Rastreabilidade:** decisões, requisitos, alterações, testes, evidências, desvios e exceções devem apontar para referências verificáveis.
6. **Histórico preservado:** mudanças devem acrescentar contexto e não apagar resultados desfavoráveis ou decisões anteriores.
7. **Dados governados:** registar origem, qualidade, atualidade, unidade, transformação e limitações; não confundir zero, nulo, desconhecido e dado não recebido.
8. **Segurança:** não gravar segredos, tokens ou dados pessoais desnecessários no repositório.
9. **Revisão humana:** mudanças de alto impacto, alteração de limiares e promoção de estado exigem revisão e aprovação explícitas.
10. **Conformidade individual:** inserir cabeçalho ou citar GOVERNANCA não significa que o módulo esteja totalmente conforme, validado ou aprovado.

## Estrutura documental do módulo

- `README.md` — contexto, estado, contrato preliminar, regras e roadmap.
- `CARTA-CONTRATO-VOLATILIDADE-B3.md` — mandato, limites, responsabilidades, gates, riscos e critérios de aceitação do módulo.
- `PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md` — prompt especializado para investigação quantitativa, sujeito a revisão.
- `LAYOUT-UNICO-VOLATILIDADE-B3.md` — desenho lógico proposto, componentes, pipeline, contratos preliminares, falhas e gates; ainda sujeito a aprovação.
- `BASE PARA PROMPT.md` — base conceitual fornecida, preservada com a identificação documental.
- `ESPECIFICACAO.md` — métricas, fórmulas, unidades, janelas, regimes e decisões de desenho.
- `CONTRATOS.md` — interfaces, dependências e semântica dos campos.
- `TESTES.md` — casos, dados de teste, critérios de aceitação e evidências.
- `CHECKPOINTS.md` — histórico de fases, validações, decisões e pendências.
- `CHANGELOG.md` — resumo versionado das alterações.
- `tests/` e `evidencias/` — implementar quando existirem testes e artefactos reais, sem ficheiros vazios que sugiram validação inexistente.

Ficheiros previstos não são considerados entregáveis concluídos até serem efetivamente criados e verificados.

## Dependências previstas

- **Giroscópio:** consolidar contexto, qualidade e confiança; interface pendente de confirmação.
- **Estado Gráfico:** declarar o gráfico de 60K trades e a granularidade utilizada; a duração temporal de cada barra pode variar e a compatibilidade deve ser validada.
- **Dados/Qualidade:** garantir proveniência, sincronização, integridade e tratamento de dados ausentes/atrasados.
- **Fluxo/Volume e VWAP/TWAP:** possíveis fontes auxiliares para contexto, não pré-requisitos assumidos sem contrato.
- **Intermercado/VIX:** contexto externo sujeito à validação de origem e sincronização.
- **Risco:** autoridade soberana sobre bloqueios; o módulo VOLATILIDADE não substitui nem enfraquece esse controlo.
- `10_VOLATILIDADE_VIX`: possível sobreposição a investigar antes de definir a arquitetura final.

## Roadmap oficial do módulo

O progresso percentual só será publicado quando houver scorecard com critérios e evidências conforme a norma da GOVERNANCA. Não atribuir percentual estimado neste documento.

| Fase | Objetivo e entregáveis | Critério de saída | Estado |
|---|---|---|---|
| F0 — Estrutura inicial | Criar pasta e README inicial | Artefactos existentes e recuperáveis no GitHub | CONCLUIDA — evidência no histórico Git |
| F1 — Adoção documental e levantamento | Cabeçalho padronizado, regras aplicáveis documentadas e inspeção de sobreposição | Documentos conferidos, pendências e diferenças registadas | EM_REVISAO |
| F2 — Requisitos e desenho | Definir métricas, fórmulas, janelas, unidades, fontes, regimes, atualidade e falhas | Especificação revisada, contratos e critérios mensuráveis | PLANEADA |
| F3 — Construção isolada | Implementar somente após fechar os requisitos | Código isolado, revisão e análise estática apropriada | PLANEADA |
| F4 — Testes e evidências | Testes sintéticos, fronteira, dados inválidos, replay/backtest, reconciliação e limitações | Logs/relatórios reproduzíveis e critérios satisfeitos | PLANEADA |
| F5 — Revisão e integração | Rever compatibilidade e integração com o Giroscópio e Risco | Aprovação explícita, contratos conciliados e rollback definido | BLOQUEADA por F2–F4 |
| F6 — Prontidão/produção | Avaliar observabilidade, suporte, recuperação e autorização | Gate de prontidão e lançamento aprovados com evidência | BLOQUEADA por gates anteriores |

### Ações prioritárias

1. Inspecionar a documentação de `MODULOS/10_VOLATILIDADE_VIX/` e registar sobreposição, diferenças e decisão arquitetural.
2. Inventariar as métricas candidatas e distinguir volatilidade histórica/realizada, implícita e índices externos.
3. Definir contratos e critérios de dados antes de implementar a classificação dos regimes.
4. Criar testes isolados reproduzíveis e registar evidência antes de qualquer integração.

## Riscos e bloqueios

- **Sobreposição de módulos:** não resolvida; impede decisão final sobre fronteiras e reaproveitamento.
- **Fórmulas e janelas:** ainda não especificadas; qualquer regime numérico permanece por definir.
- **Fontes e dados externos:** feeds, timestamps, atraso permitido e reconciliação ainda por confirmar.
- **Contratos entre módulos:** interfaces dos consumidores ainda não verificadas.
- **Validação de plataforma:** nenhuma validação NTSL, replay, backtest ou tempo real é alegada neste checkpoint.

Sem resolver dependências críticas e cumprir os critérios de saída, as fases posteriores permanecem bloqueadas.

## Evidências

- [Repositório de governança](https://github.com/carlos-andrade/GOVERNANCA)
- [Constituição do sistema de governança](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md)
- [Norma de cabeçalho documental](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md)
- [Carta/Contrato de roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md)
- [Roadmap padrão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md)
- [Norma de estado e percentual](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md)
- [Índice modular do BRICKMASTER](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/main/MODULOS/README.md)
- [Carta/Contrato do módulo VOLATILIDADE B3](CARTA-CONTRATO-VOLATILIDADE-B3.md)
- [Prompt especializado de volatilidade B3](PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md)
- [Base conceptual para prompt](BASE%20PARA%20PROMPT.md)

## Validação

Verificações executadas nesta atualização documental:
- consultada a árvore e os documentos canónicos relevantes do repositório GOVERNANCA;
- inspecionados os ficheiros atuais de VOLATILIDADE e o índice modular;
- preservado o conteúdo conceptual de `BASE PARA PROMPT.md`;
- confirmada a existência da pasta distinta `MODULOS/10_VOLATILIDADE_VIX`;
- não foram executados testes de código, cálculos de volatilidade, replay, backtest ou testes de integração.

A normalização documental ainda requer verificação de integridade SHA-256 canónico após o conteúdo final ser fixado. Esta revisão não constitui certificação de conformidade integral nem aprovação para produção.

## Resultado

O módulo passa a documentar os controlos de governança aplicáveis, o estado real, as dependências, os bloqueios e a sequência de gates. Fica em revisão; não está validado para produção.

## Próxima Ação

Inspecionar `MODULOS/10_VOLATILIDADE_VIX/`, registar a análise de sobreposição e fechar os requisitos de F2. Critério de conclusão: comparação documentada, fronteiras do módulo decididas e evidência verificável ligada ao checkpoint.

## Documentos operacionais principais

- [Carta/Contrato — Módulo VOLATILIDADE B3](CARTA-CONTRATO-VOLATILIDADE-B3.md) — proposta para aprovação formal.
- [Prompt Especialista — Inteligência de Volatilidade B3](PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md) — investigação e desenho; estado experimental.
- [Layout Único — Módulo VOLATILIDADE B3](LAYOUT-UNICO-VOLATILIDADE-B3.md) — arquitetura lógica em revisão, sem implementação presumida.
- [Base conceptual](BASE%20PARA%20PROMPT.md) — origem conceptual e limites de interpretação.

## Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.0 | 2026-10-18 | Criação inicial do README do módulo | Responsável técnico do projeto | Histórico Git do repositório |
| 1.1.0 | 2026-10-18 | Adoção documental de regras de governança, roadmap por gates, riscos, dependências e evidências | Responsável técnico do projeto | Histórico Git |
| 1.2.0 | 2026-10-18 | Ligação à Carta/Contrato VOLATILIDADE B3 e ao prompt especializado | Responsável técnico do projeto | Histórico Git |
| 1.3.0 | 2026-10-18 | Ligação ao Layout Único e atualização do índice documental do módulo | Responsável técnico do projeto | Commit a confirmar após publicação |