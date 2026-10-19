---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "REGISTRO"
fase: "GOVERNANCA_DOCUMENTAL"
id_documento: "BM-DOC-ARQUITETURA-BRICKMASTER-RAIZ-REGISTRO-MODULOS-E-CHECKPOINTS"
titulo: "BRICKMASTER RAIZ — Registo de módulos e checkpoints"
status: "PLANEJADO"
versao: "1.0.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
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
> **Versão:** 1.0.0  
> **Criação:** 2026-10-11  
> **Atualização:** 2026-10-11  
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
| BM-CORE-001 | GIROSCÓPIO | Contexto central e localização do operador no gráfico | A inventariar | Localizar versões existentes e consolidar definições |
| BM-DATA-001 | Relógio/Sessão/Abertura | Identificar sessão e referência diária | A inventariar | Localizar cálculos existentes; definir testes de transição |
| BM-STRUCT-001 | Estrutura de preço | Swings, deslocamento e rompimento | A inventariar | Mapear código e documentação |
| BM-FVG-001 | FVG Atlas | Identificar FVGs, dimensão e ciclo de vida | Repositório relacionado conhecido; código a inventariar | Comparar com FVG-ATLAS e localizar versões no repositório central |
| BM-LIQ-001 | Liquidez | Níveis, varredura e reação | A inventariar | Localizar especificações existentes e formalizar condições |
| BM-TOUCH-001 | Contador de toques | Contagem e invalidação de contactos com níveis | A inventariar | Recuperar desenho anterior e identificar parâmetros |
| BM-FLOW-001 | Fluxo | Delta, volume financeiro e VWAP/TWAP | A inventariar | Confirmar campos reais, fonte e sincronização |
| BM-MACRO-001 | Calendário económico | Contexto macro e janelas de risco | A inventariar | Inventariar fontes e regras de horário |
| BM-REF-001 | Referências externas | IBOV e, opcionalmente, VIX como contexto externo | A inventariar | Validar proveniência, atraso, sincronização e evidência estatística; a pasta VIX autónoma foi retirada por decisão do responsável |
| BM-RISK-001 | Gestão de risco | Limites, exposição e interrupção | A inventariar | Identificar regras anteriores e propor contrato testável |
| BM-EXEC-001 | Adaptador NTSL | Implementação e execução controlada | A inventariar | Verificar código e compatibilidade com Manual NTSL 4.4 |
| BM-OBS-001 | Watchdog/Auditoria | Saúde dos dados, logs e alertas | A inventariar | Localizar watchdog e definir heartbeat e falhas |

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
- Inventário integral do repositório: NOT_RUN.
- Código NTSL alterado: NÃO.
- Testes de estratégia executados: NÃO.
- Rentabilidade validada: NÃO.
- Próximo passo: inventariar os arquivos reais e atualizar este registo com caminhos, versões e evidências verificáveis.


## Contexto Histórico

Contexto histórico preservado no conteúdo preexistente e no histórico Git. Em 2026-10-19, foi tomada a decisão explícita de retirar `MODULOS/10_VOLATILIDADE_VIX/`, que continha apenas um README de proposta inicial. A remoção será submetida por branch/PR porque a pasta existe em `main` e não na linha atual de `develop`; não se faz alteração direta em `main`.


## Estado

Estado documental no momento da padronização: PLANEJADO. Este estado não comprova execução nem validação técnica.


## Evidências

O conteúdo original deste arquivo e o histórico de versões do Git são as fontes de evidência disponíveis. Evidências externas ou testes não foram presumidos.


## Validação

Validação estrutural do cabeçalho realizada nesta alteração; a validação funcional/técnica do conteúdo não é declarada por esta padronização.


## Resultado

Cabeçalho documental padronizado sem intenção de alterar as regras ou o conteúdo técnico preexistente.


## Próxima Ação

Validar o PR de retirada da pasta VIX e, depois, reconciliar a linha de desenvolvimento com `main` conforme a governança.
