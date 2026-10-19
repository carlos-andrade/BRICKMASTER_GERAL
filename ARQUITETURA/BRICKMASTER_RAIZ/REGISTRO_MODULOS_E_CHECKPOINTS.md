---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "REGISTRO"
fase: "GOVERNANCA_DOCUMENTAL"
id_documento: "BM-DOC-ARQUITETURA-BRICKMASTER-RAIZ-REGISTRO-MODULOS-E-CHECKPOINTS"
titulo: "BRICKMASTER RAIZ — Registo de módulos e checkpoints"
status: "PLANEJADO"
versao: "1.0.4"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-19"
sha256_canonico: "SELF_HASH"
commit_referencia: "c0740f9fd4d1485b3c3a1b8568053b8cd077e688"
origem: "Conteúdo preexistente; ver histórico Git e referências internas"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR de padronização documental; commit a registar após criação"
escopo: "Documento existente em ARQUITETURA/BRICKMASTER_RAIZ/REGISTRO_MODULOS_E_CHECKPOINTS.md"
objetivo: "Preservar o conteúdo original com identificação, estado e rastreabilidade padronizados"
dependencias: "N/A"
---
# BRICKMASTER RAIZ — Registo de módulos e checkpoints

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Tipo:** REGISTRO  
> **Fase:** GOVERNANÇA DOCUMENTAL  
> **ID:** BM-DOC-ARQUITETURA-BRICKMASTER-RAIZ-REGISTRO-MODULOS-E-CHECKPOINTS  
> **Status:** PLANEJADO  
> **Versão:** 1.0.4  
> **Criação:** 2026-10-11  
> **Atualização:** 2026-10-19  
> **Origem:** Conteúdo preexistente; ver histórico Git e referências internas  
> **Autoridade:** GOVERNANÇA  
> **Rastreabilidade:** PR de padronização documental; commit a registar após criação

Data: 2026-10-11  
Estado inicial: DOCUMENTAÇÃO CRIADA; inventário completo dos arquivos ainda não executado.  
Documento associado: ARQUITETURA/BRICKMASTER_RAIZ/ARQUITETURA_MODULAR_BASELINE_2026-10-11.md

## 1. Registo mestre de módulos

Este registo é um índice de trabalho. Os estados abaixo descrevem o que está confirmado neste checkpoint documental, não a existência ou inexistência de código em outros caminhos.

| ID | Módulo | Responsabilidade | Estado do inventário | Próxima ação |
|---|---|---|---|---|
| BM-CORE-001 | GIROSCÓPIO | Contexto central e localização do operador no gráfico | Contrato inicial e plano de testes criados em `MODULOS/003-GIROSCOPIO/`; sem código nem testes executados | Implementar localização/contexto mínimo e executar testes de qualidade, conflito, bloqueio e 60K ticks |
| BM-DATA-001 | Relógio/Sessão/Abertura | Identificar sessão e referência diária | Política B aprovada em 2026-10-12: preço oficial da plataforma/fonte oficial validada; implementação pendente | Identificar e validar campo/fonte por instrumento, confirmar sessão/fuso/frescura, implementar máquina de estados e executar testes |
| BM-STRUCT-001 | Estrutura de preço | Swings, deslocamento e rompimento | A inventariar | Mapear código e documentação |
| BM-FVG-001 | FVG Atlas | Identificar FVGs, dimensão e ciclo de vida | Inventário externo inicial concluído: FVG-ATLAS `main` tem 249 blobs; roadmap externo aponta V2.1.33 como regressão integrada aprovada | Congelar contrato; validar Manual NTSL 4.4/Profit e testes de contrato antes de integração BRICKMASTER |
| BM-LIQ-001 | Liquidez | Níveis, varredura e reação | Não localizado por nome de ficheiro na árvore atual; auditoria semântica ainda parcial | Recuperar especificações anteriores e formalizar nível, sweep, confirmação e invalidação |
| BM-TOUCH-001 | Contador de toques | Contagem e invalidação de contactos com níveis | Não localizado por nome de ficheiro na árvore atual; auditoria semântica ainda parcial | Recuperar desenho anterior e identificar tolerância, separação temporal e invalidação |
| BM-FLOW-001 | Fluxo | Delta, volume financeiro e VWAP/TWAP | Candidatos legados identificados em `ROBÔ_TRADE/` e `BRICKMASTER_CLAUDE/CÓDIGO NTSL/`; não validados nem canónicos | Comparar variantes; verificar funções no Manual NTSL 4.4, fontes, sincronização e compatibilidade com ticks/60K |
| BM-MACRO-001 | Calendário económico | Contexto macro e janelas de risco | A inventariar | Inventariar fontes e regras de horário |
| BM-REF-001 | Referências externas | VIX e IBOV como contexto | A inventariar | Definir proveniência, atraso e regra de uso |
| BM-MDNA-001 | Market DNA | Responsabilidade funcional por definir a partir dos artefactos anteriores | Não consta como módulo identificado na árvore `main` consultada; especificação/código a localizar ou criar após inventário | Recuperar decisões anteriores, delimitar entradas/saídas e criar contrato sem duplicar módulos existentes |
| BM-RISK-001 | Gestão de risco | Limites, exposição e interrupção | Contrato inicial e plano de testes criados em `MODULOS/004-RISCO-SOBERANO/`; limites numéricos por aprovar | Aprovar política versionada sem defaults inventados; testar veto, limite diário, exposição e reconciliação |
| BM-EXEC-001 | Adaptador NTSL | Implementação e execução controlada | Contrato inicial em `MODULOS/005-EXECUCAO-CONCILIADA/`; sem implementação nem teste Profit | Implementar dry-run/simulação, mapear estados Profit e validar idempotência/reconciliação; LIVE permanece desativado |
| BM-OBS-001 | Watchdog/Auditoria | Saúde dos dados, logs e alertas | Contrato inicial em `MODULOS/006-WATCHDOG/`; sem implementação nem teste de recuperação | Medir freshness, definir heartbeat/timeouts e testar bloqueio/recuperação fail-closed |

## 2. Modelo obrigatório de checkpoint

### Identificação
- ID do checkpoint:
- Data/hora e fuso:
- Fase:
- Responsável:
- Branch/commit de referência:

### Escopo
- Pedido:
- Caminhos inspecionados:
- Fontes e versões consultadas:
- Dependências:

### Alterações
- Arquivos criados:
- Arquivos alterados:
- Arquivos removidos (evitar; justificar e aprovar):
- Resumo do diff:
- Motivo da alteração:

### Verificação
- Comandos/testes executados:
- Ambiente:
- Resultado: PASS / FAIL / BLOCKED / NOT_RUN / PROPOSED
- Evidência reproduzível:
- O que não foi testado:
- Riscos/regressões:
- Plano de rollback:

### Fecho
- Decisão:
- Próxima ação única:
- Critério objetivo de conclusão:
- Artefatos anexos:

## 3. Critérios para declarar um módulo integrado

Um módulo só muda para INTEGRATED quando:
1. A interface de entrada/saída está documentada.
2. As dependências e incompatibilidades estão registadas.
3. Os testes unitários passam.
4. Os casos de dados ausentes e de fronteira são tratados.
5. O comportamento em gráficos de ticks, incluindo 60K quando aplicável, foi observado.
6. A comparação histórico/replay/tempo real está documentada, quando suportada.
7. Existe evidência do teste no repositório.
8. A integração pode ser revertida sem apagar o módulo isolado.

A compilação isolada não satisfaz, por si só, estes critérios.

## 4. Política de segurança para desenvolvimento

- Não enviar ordens reais durante desenvolvimento, depuração ou teste inicial.
- Não alterar módulos existentes antes de inventariar as versões e preservar uma referência reversível.
- Não afirmar que uma fórmula/função NTSL existe sem conferir o Manual 4.4 ou validar no editor da plataforma.
- Não inferir que dados de delta, agressão, livro de ofertas, VIX ou TWAP estão disponíveis só porque são desejáveis na estratégia.
- Separar resultados de backtest, replay, simulação e execução real.
- Documentar limitações e condições de bloqueio como parte do comportamento esperado.

## 5. Estado deste checkpoint

- Arquitetura modular de alto nível: DOCUMENTADA.
- Registo mestre de módulos: DOCUMENTADO.
- Inventário estrutural de `BRICKMASTER_GERAL/main`: 212 blobs, árvore sem truncamento; diferença histórica 209 → 212 reconciliada com três ficheiros adicionados no PR #2.
- Inventário estrutural inicial de `FVG-ATLAS/main`: 249 blobs, árvore sem truncamento; V2.1.33 e o respetivo relatório de regressão foram identificados por hash.
- Auditoria semântica integral de todos os artefactos: PARCIAL.
- Código NTSL alterado por estes checkpoints: NÃO.
- Testes de estratégia executados nesta tarefa: NÃO; o relatório FVG externo contém evidência histórica do próprio projeto.
- Rentabilidade validada: NÃO.
- Próximo passo: concluir o inventário de versões e contratos de Giroscópio, sessão/abertura, liquidez, Market DNA, risco, execução e Watchdog.


## Contexto Histórico

Contexto histórico preservado no conteúdo preexistente e no histórico Git. Não foram inferidas datas ou decisões que não estivessem documentadas. Em 2026-10-19, a pasta autónoma `MODULOS/10_VOLATILIDADE_VIX/` foi retirada de `main` pelo PR #33 (commit `d1f91fdcae5d92ac56449b570022011ae7857e6b`). O VIX permanece opcional como referência externa sujeita a validação; a pasta não é restaurada nesta reconciliação.


## Estado

Estado documental no momento da padronização: PLANEJADO. Este estado não comprova execução nem validação técnica.


## Evidências

O conteúdo original deste arquivo e o histórico de versões do Git são as fontes de evidência disponíveis. Evidências externas ou testes não foram presumidos.


## Validação

Validação estrutural do cabeçalho realizada nesta alteração; a validação funcional/técnica do conteúdo não é declarada por esta padronização.


## Resultado

Cabeçalho documental padronizado sem intenção de alterar as regras ou o conteúdo técnico preexistente.


## Próxima Ação

Manter este registo como índice de trabalho; atualizar cada módulo somente com caminho, versão, estado e evidência verificáveis. Priorizar contratos isolados para FVG-ATLAS e candidatos de fluxo; recuperar a especificação de Market DNA e dos módulos não localizados antes de criar código.


## Histórico de versões

- 1.0.0 — 2026-10-11 — registo inicial dos módulos.
- 1.0.1 — 2026-10-11 — inventário estrutural do FVG-ATLAS registado e Market DNA incluído como lacuna de inventário, sem presumir implementação.


- 1.0.2 — 2026-10-11 — inventário de candidatos de fluxo/VWAP/TWAP/volume acrescentado; lacunas por nome de ficheiro registadas sem declarar inexistência absoluta.

- 1.0.6 — 2026-10-11 — contrato e plano de testes do risco soberano registados; parâmetros e execução permanecem pendentes.

- 1.0.7 — 2026-10-11 — contratos iniciais de execução conciliada e Watchdog registados; implementação e testes pendentes.

- 1.0.3 — 2026-10-12 — registo atualizado com a política B de abertura oficial; fonte concreta e validação pendentes.


## Histórico de reconciliação — 2026-10-19

- `main` e `develop` foram comparadas e identificadas como divergentes a partir do commit comum `ac61750ca0e1413d127759b592a0bd296cf9f83e`.
- A reconciliação preserva os conteúdos exclusivos de `main` e incorpora, em branch derivada de `main`, os documentos exclusivos e as versões evoluídas de `develop`.
- Esta atualização é documental. Não declara testes de estratégia, NTSL, replay, backtest ou produção.
