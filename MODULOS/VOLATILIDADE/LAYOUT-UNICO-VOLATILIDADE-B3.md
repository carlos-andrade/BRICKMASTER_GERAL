# LAYOUT ÚNICO — MÓDULO VOLATILIDADE B3
### BRICKMASTER RAIZ

| Campo | Valor |
|---|---|
| **ID** | BM-VOL-LAYOUT-001 |
| **Projeto** | BRICKMASTER RAIZ |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | LAYOUT_UNICO_ARQUITETURAL |
| **Fase** | F2 — Requisitos e desenho |
| **Estado** | PROPOSTA_EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 6ad7a9d7fd04e259a10feeb848c61b1575cc67bb0e4bb3a43070ae233989a555|
| **Commit de referência (versão anterior)** | [9958fede2156e4b035ee1a6a4aceb738b85ae814](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/9958fede2156e4b035ee1a6a4aceb738b85ae814) |
| **Data de criação** | 2026-10-18 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente de aprovação formal |
| **Origem normativa** | [GOVERNANCA — Constituição](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md); [Carta/Contrato padrão de roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md); [Norma de cabeçalho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Carta/Contrato** | [CARTA-CONTRATO-VOLATILIDADE-B3.md](CARTA-CONTRATO-VOLATILIDADE-B3.md) |
| **Prompt** | [PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md](PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md) |
| **Base conceptual** | [BASE PARA PROMPT.md](BASE%20PARA%20PROMPT.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

---

## 1. Objetivo e força documental

Este documento consolida num único desenho lógico a arquitetura proposta para o módulo VOLATILIDADE B3. Deve servir de referência entre a Carta/Contrato e qualquer futura implementação, evitando que cálculos, interfaces, estados de dados ou regras de segurança sejam inventados diretamente no código.

Este Layout Único é **proposta arquitetural em revisão**. Não é implementação, especificação quantitativa final, aprovação de integração ou autorização de produção. Em caso de conflito, prevalecem a lei e os contratos vinculativos, as políticas formalmente aprovadas e as normas superiores aplicáveis. Alterações devem ser rastreadas e aprovadas.

## 2. Problema a resolver

O BRICKMASTER RAIZ necessita de saber em que contexto de volatilidade se encontra o instrumento analisado, como esse contexto evolui e quando a qualidade da informação não permite uma conclusão confiável. O módulo deve produzir contexto verificável para o Giroscópio, sem confundir volatilidade com direção, liquidez, oportunidade ou probabilidade de lucro.

## 3. Objetivos de arquitetura

1. Separar ingestão, validação de dados, cálculo, classificação, publicação de contexto e monitorização.
2. Identificar a proveniência e a atualidade de cada dado utilizado.
3. Tornar métodos, unidades, janelas e versões explícitos e reproduzíveis.
4. Preservar o estado `DESCONHECIDO` e bloquear conclusões quando faltarem pré-condições críticas.
5. Permitir métricas múltiplas sem forçar uma classificação única quando existirem divergências.
6. Permitir avaliação separada por instrumento, contrato, sessão e granularidade do gráfico.
7. Respeitar a autoridade soberana do módulo Risco e impedir execução direta de ordens.
8. Permitir testes isolados antes de qualquer integração.

## 4. Arquitetura lógica proposta

```text
FONTES DE DADOS AUTORIZADAS
        |
        v
[M1 — ADAPTADORES / INGESTÃO]
        | dados brutos + proveniência
        v
[M2 — QUALIDADE / SINCRONIZAÇÃO]
        | válido / degradado / atrasado / contraditório / ausente
        +-----------------------> [M7 — WATCHDOG / EVENTOS DE FALHA]
        | dados aceites
        v
[M3 — NORMALIZAÇÃO / CONTEXTO DE SESSÃO]
        | instrumento, contrato, unidade, calendário, granularidade
        v
[M4 — MOTOR DE MÉTRICAS]
        | métricas versionadas + janela + método + evidência
        v
[M5 — CLASSIFICAÇÃO / TRANSIÇÃO DE REGIME]
        | regime candidato + confiança + divergências
        v
[M6 — PUBLICADOR DE CONTEXTO]
        | contrato versionado; sem ordens
        v
[GIROSCÓPIO — CONSUMO PROPOSTO]
        |
        +---- contexto para avaliação pelo sistema
              [RISCO SOBERANO mantém autoridade independente]
```

Este diagrama representa uma proposta lógica. Não prova que os adaptadores, APIs, filas, serviços ou interfaces descritos já existem. A integração efetiva depende de contratos aprovados e inventário técnico.

## 5. Módulos internos e responsabilidades

| ID | Componente | Responsabilidade | Não pode fazer | Estado |
|---|---|---|---|---|
| M1 | Adaptadores / Ingestão | Receber séries de fontes autorizadas, preservar campos de origem e timestamps | Inventar valores ou esconder lacunas | PROPOSTO |
| M2 | Qualidade / Sincronização | Verificar campos, ordem temporal, duplicados, atrasos, consistência e regras da fonte | Corrigir silenciosamente dados ambíguos | PROPOSTO |
| M3 | Normalização / Sessão | Uniformizar unidades, identificar instrumento/contrato, calendário, sessão e granularidade | Misturar contratos ou escalas sem regra explícita | PROPOSTO |
| M4 | Motor de Métricas | Calcular métricas documentadas e guardar método, janela, unidade e versão | Calcular métricas sem especificação aprovada | PROPOSTO |
| M5 | Classificação / Regime | Interpretar métricas segundo regras aprovadas e expor confiança/divergências | Forçar regime único sem evidência suficiente | PROPOSTO |
| M6 | Publicador de Contexto | Emitir payload versionado para consumidores autorizados | Enviar, alterar ou cancelar ordens | PROPOSTO |
| M7 | Watchdog / Falhas | Detetar ausência, atraso, erro de cálculo, divergência e recuperação | Declarar saúde sem evidência observável | PROPOSTO |
| M8 | Evidências / Auditoria | Relacionar inputs, versão, cálculo, saída, teste e decisão | Alterar ou apagar histórico desfavorável | PROPOSTO |

## 6. Contrato de dados entre componentes

### 6.1 Envelope mínimo de observação

Cada observação de mercado usada pelo motor deve, quando aplicável, ser identificável por:

- `instrumento` e `contrato`;
- `fonte` e referência/licença de uso;
- `timestamp_evento`, `timestamp_rececao` e `timezone`;
- `preco` ou `retorno`, com `unidade` e método de amostragem;
- `granularidade_grafico` e tipo de gráfico, quando relevantes;
- `sessao`/calendário e metadados de ajuste/rollover;
- `estado_dados` e lista de anomalias;
- `versao_dataset` ou identificador rastreável, quando disponível.

Os nomes são ilustrativos até à aprovação de `CONTRATOS.md`. Não são um schema implementado.

### 6.2 Envelope mínimo de métrica

Cada métrica calculada deve transportar:

- identificador e versão da métrica;
- instrumento e período observado;
- valor e unidade;
- método, parâmetros e janela;
- timestamp do último evento usado e timestamp de cálculo;
- estado de qualidade dos dados de entrada;
- limitações e referência aos dados/artefactos usados.

### 6.3 Envelope mínimo de contexto

A saída para consumo deve incluir:

- versão do schema;
- instrumento/contrato e timestamps;
- estado de qualidade e idade dos dados;
- métricas utilizadas e respetivas unidades/janelas;
- regime candidato (`DESCONHECIDO`, `BAIXO`, `NORMAL`, `ELEVADO`, `EXTREMO`);
- confiança, divergências e limitações;
- avisos e razões de bloqueio;
- estado de maturidade e evidências;
- indicação explícita de que o módulo não gera ordens.

Os rótulos de regime são taxonomia inicial. Fórmulas, janelas, critérios de atualidade, valores de corte e cálculo de confiança permanecem pendentes de especificação.

## 7. Pipeline operacional

1. **Receber:** obter dados apenas de fontes confirmadas e permitidas.
2. **Identificar:** associar instrumento, contrato, fonte, unidade, calendário e timestamps.
3. **Validar:** detetar ausência, atraso, duplicados, valores inválidos, desordem temporal e divergências.
4. **Bloquear ou degradar:** se falhar um requisito crítico, não avançar para uma conclusão dependente do dado; emitir estado e motivo.
5. **Normalizar:** aplicar apenas transformações documentadas, versionadas e reversíveis quando possível.
6. **Calcular:** executar métricas aprovadas com parâmetros e janelas explícitos.
7. **Classificar:** aplicar regras aprovadas, expondo divergências e confiança sem forçar resultados.
8. **Publicar:** disponibilizar contexto versionado para consumidores aprovados; não enviar ordens.
9. **Registar:** guardar referências aos dados, método, versão, resultado, erros e evidências.
10. **Monitorizar:** acompanhar atualidade, falhas e recuperação; nunca converter `UNKNOWN` em `PASS`.

## 8. Tratamento de falhas e estados

| Condição | Estado proposto | Comportamento |
|---|---|---|
| Dados completos, sincronizados e dentro dos critérios aprovados | `VALIDO` | Permitir cálculo das métricas autorizadas |
| Problema não crítico com impacto mensurável | `DEGRADADO` | Reduzir confiança, expor anomalia e aplicar política aprovada |
| Dado além do limite de atualidade aprovado | `ATRASADO` | Bloquear conclusões dependentes da atualidade |
| Fontes ou campos incompatíveis/contraditórios | `CONTRADITORIO` | Não reconciliar silenciosamente; bloquear ou marcar como desconhecido |
| Dado obrigatório não recebido | `AUSENTE` | Não inventar valor; emitir `DESCONHECIDO` e motivo |
| Falha interna de cálculo/schema | `FAIL` | Não publicar resultado como válido; gerar evento observável |
| Estado não demonstrável | `UNKNOWN` | Não considerar sucesso; requer diagnóstico |

Os limites numéricos de atraso, tolerâncias e severidades ainda não foram aprovados. A tabela descreve comportamento-alvo, não comprova implementação.

## 9. Tratamento da volatilidade e dos regimes

O motor deve suportar múltiplas famílias de métricas, desde que cada uma tenha especificação e teste:

- volatilidade realizada/histórica;
- volatilidade intradiária por sessão/horário;
- medidas absolutas e relativas;
- horizontes curtos e longos;
- expansão/compressão em relação a baseline comparável;
- amplitude e eficiência direcional, mantendo-as conceptualmente distintas;
- risco de cauda e saltos;
- volatilidade implícita, apenas com dados de opções adequados;
- relação com fatores externos, incluindo VIX, apenas como hipótese a testar.

Não selecionar agora um estimador, janela ou limiar único. F2 deve comparar candidatos, unidades, baselines, sensibilidade e limitações antes de aprovar o método.

### 9.1 Gráfico de 60K trades e referência temporal

Registar a definição real do gráfico de 60K trades na plataforma, instrumento e granularidade. O BRICKMASTER utiliza gráfico de 60K trades, não gráficos de ticks nem Renko. Uma barra baseada em 60K trades representa uma contagem de negócios, não um intervalo de tempo fixo; a duração varia com a atividade de mercado. Não comparar diretamente métricas por barra temporal e por barra de 60K trades sem método de normalização e validação explícitos.

## 10. Fronteiras com outros módulos

| Dependência | Relação proposta | Gate necessário |
|---|---|---|
| Giroscópio | Consumir contexto de volatilidade com timestamps, qualidade, confiança e divergências | Inspecionar e aprovar contrato real |
| Estado Gráfico | Fornecer tipo/granularidade do gráfico de 60K trades | Confirmar representação e fonte |
| Dados/Qualidade | Validar proveniência, integridade e atualidade | Definir critérios e integração |
| Fluxo/Volume, FVG, VWAP/TWAP, Market DNA | Possíveis inputs contextuais | Não ligar sem necessidade demonstrada e contrato explícito |
| Risco soberano | Receber contexto se aprovado; mantém decisão de limites/bloqueios | Revisão de segurança e autoridade |
| Execução conciliada | Sem chamada de execução a partir deste módulo | Proibição de ordens neste escopo |
| Watchdog | Receber eventos de saúde e falha conforme contrato | Definir observabilidade, alertas e recuperação |
| `MODULOS/10_VOLATILIDADE_VIX/` | Possível especialização de VIX | Inventariar diferenças antes de decidir fronteira ou reutilização |

## 11. Segurança, risco e controlo operacional

- O módulo opera em modo de pesquisa/produção de contexto, nunca de execução.
- Não contém credenciais, tokens, dados pessoais desnecessários ou segredos no repositório.
- A ausência do próprio cálculo ou do watchdog deve ser detetável por controlo independente nos âmbitos críticos, conforme a arquitetura geral de WATCHDOG.
- Remediação automática não é habilitada por este documento.
- Alterações de fórmula, janela, limiar, fonte ou schema exigem versão, testes e revisão.
- O módulo não pode sobrepor-se ao Risco soberano, nem usar a meta hipotética de 1% para relaxar bloqueios.
- A promoção para produção exige autorização formal, rollback definido e evidência de observabilidade/recuperação.

## 12. Estratégia de testes

Os testes devem ser planeados antes da implementação e executados isoladamente:

1. Séries sintéticas com volatilidade constante, crescente, decrescente e transições.
2. Dados ausentes, atrasados, duplicados, fora de ordem, contraditórios e inválidos.
3. Timestamps, timezone, sessões, feriados, abertura/fecho, leilões, gaps e rollover.
4. Preços constantes, retornos extremos, overflow e entradas fora do domínio.
5. Robustez a janelas, frequências e estimadores candidatos.
6. Comparação contra baselines simples e teste final cronológico isolado.
7. Controlo de look-ahead, leakage, seleção de parâmetros e survivorship bias.
8. Comparabilidade entre gráficos temporais e gráfico de 60K trades.
9. Falha de fonte, cálculo, schema, publicação e watchdog.
10. Reprodutibilidade, reconciliação e preservação dos resultados negativos.

Cada teste deve registar ID, requisito, entrada, versão do código, versão dos dados, resultado esperado/obtido, log/artefacto, estado e revisor. Até à execução observável, usar `NAO_EXECUTADO`.

## 13. Artefactos documentais e técnicos

Documentos previstos no diretório `MODULOS/VOLATILIDADE/`:

- `README.md` — índice, estado, roadmap e dependências;
- `BASE PARA PROMPT.md` — origem conceptual preservada;
- `PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md` — mandato de investigação;
- `CARTA-CONTRATO-VOLATILIDADE-B3.md` — compromissos, limites e gates;
- `LAYOUT-UNICO-VOLATILIDADE-B3.md` — este desenho arquitetural;
- `ESPECIFICACAO.md` — fórmulas, unidades, janelas e regras de regime aprovadas;
- `CONTRATOS.md` — schemas e interfaces aprovados;
- `TESTES.md` — testes, critérios e evidências;
- `CHECKPOINTS.md` — decisões, fases, bloqueios e revisões;
- `CHANGELOG.md` — histórico de alterações do módulo.

Os ficheiros futuros só contam como entregáveis quando existirem, forem revistos e tiverem evidência adequada. Não criar artefactos vazios para simular conclusão.

## 14. Roadmap e critérios de gate

| Gate | Entregável | Critério de saída | Estado |
|---|---|---|---|
| F2 — Requisitos e desenho | Inventário de dados, `ESPECIFICACAO.md`, `CONTRATOS.md`, decisões de fronteira | Métricas candidatas avaliadas; fórmulas/unidades/janelas e critérios de qualidade documentados; interfaces revisadas | EM_CURSO — pendente |
| F3 — Construção isolada | Implementação do motor aprovado | Revisão de código, análise estática e testes unitários básicos executados | BLOQUEADA por F2 |
| F4 — Testes e evidências | Relatórios e logs reproduzíveis | Critérios de aceitação satisfeitos, resultados negativos registados e limitações explícitas | BLOQUEADA por F3 |
| F5 — Integração | Adaptadores e consumidor Giroscópio/Risco com contratos aprovados | Compatibilidade verificada, testes de integração e rollback demonstrados | BLOQUEADA por F2–F4 |
| F6 — Prontidão | Observabilidade, watchdog, suporte, recuperação e autorização | Gate operacional aprovado e autorização formal documentada | BLOQUEADA por gates anteriores |

Não atribuir percentagem sem scorecard conforme a GOVERNANCA. O estado desta proposta não significa que qualquer componente esteja implementado.

## 15. Decisões pendentes

1. Confirmar inventário e fronteira com `MODULOS/10_VOLATILIDADE_VIX/`.
2. Confirmar fontes de dados, permissões, granularidade e disponibilidade histórica/tempo real.
3. Selecionar e justificar estimadores candidatos por pergunta de investigação.
4. Definir janelas, unidades, baselines, critérios de frescura e thresholds de regime por teste.
5. Aprovar o schema de entrada/saída e as interfaces com Giroscópio, Dados/Qualidade e Watchdog.
6. Definir critérios de aceitação e responsáveis pela revisão independente, conforme o risco.

## 16. Evidências, validação e limitações

### Evidência documental

- Carta/Contrato do módulo: [CARTA-CONTRATO-VOLATILIDADE-B3.md](CARTA-CONTRATO-VOLATILIDADE-B3.md).
- Prompt especializado: [PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md](PROMPT_ESPECIALISTA_VOLATILIDADE_B3.md).
- Base conceptual: [BASE PARA PROMPT.md](BASE%20PARA%20PROMPT.md).
- Normas superiores: [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).

### Validação executada nesta etapa

- [x] Consultados a Constituição e a norma de cabeçalho da GOVERNANCA.
- [x] Consultados a Carta/Contrato e o prompt especializados do módulo.
- [x] Produzido um desenho lógico com componentes, pipeline, fronteiras, falhas e gates.
- [ ] Aprovação formal do Layout Único.
- [ ] Validação contra contratos técnicos reais dos módulos dependentes.
- [ ] Testes de cálculo, replay, backtest ou integração.

Não foram executados cálculos quantitativos, testes de código, replay, backtests ou testes de integração. O desenho não prova que os componentes existem nem que a arquitetura foi aprovada.

## 17. Resultado e próxima ação

Resultado: proposta arquitetural única criada para orientar F2 e impedir implementação divergente dos requisitos e da Carta. Permanece em revisão.

Próxima ação: concluir o inventário das dependências e criar `ESPECIFICACAO.md` e `CONTRATOS.md`; só depois solicitar aprovação do desenho e iniciar construção isolada.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-18 | Criação do Layout Único arquitetural do módulo VOLATILIDADE B3 | Commit Git a confirmar após publicação |