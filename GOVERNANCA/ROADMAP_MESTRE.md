---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ROADMAP_MESTRE"
fase: "FASE 00 — GOVERNANÇA"
id_documento: "BM-ROADMAP-MASTER-001"
titulo: "Roadmap Mestre do BRICKMASTER RAIZ"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "PR #3; conteúdo original preservado e normalizado"
autoridade_documental: "GOVERNANCA e responsável pelo projeto"
cadeia_autoridade: "PROMPT -> CARTA -> LAYOUT UNICO -> CODIGO"
rastreabilidade: "PR #3; branch feature/pr3-governanca-mainline-reconciliation"
escopo: "Roadmap Mestre do BRICKMASTER RAIZ"
objetivo: "Documentar governança sem declarar aprovação ou testes não executados"
dependencias: "GOVERNANCA/NORMA-CABECALHO-PADRAO.md; main base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
sha256_canonico: "e4cbf43ae20fcda865a1c6576641a30f454470ebdd0f32bd0f769a2dd2fd36e3"
commit_referencia: "3db0c88f27fec4c6ea2418749de09ebba8130fe7"
---
---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ROADMAP_MESTRE"
fase: "GOVERNANCA"
id_documento: "BM-ROADMAP-001"
titulo: "Roadmap Mestre do BRICKMASTER RAIZ"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Histórico de desenvolvimento e inventário preliminar do BRICKMASTER RAIZ"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feature/governanca-fundacao"
escopo: "Roadmap global, módulos, dependências, validação e promoção"
objetivo: "Organizar o desenvolvimento por fases e evidências sem apagar históricos ou declarar validações não comprovadas"
dependencias: "CARTA_GOVERNANCA.md; CICLO_DE_DESENVOLVIMENTO.md; PADRAO_DE_MODULOS_E_CONTRATOS.md; CHECKPOINTS_E_EVIDENCIAS.md; Manual NTSL 4.4"
---

# Roadmap Mestre — BRICKMASTER RAIZ

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL)  
> **Tipo:** ROADMAP MESTRE  
> **Fase:** GOVERNANÇA  
> **ID:** BM-ROADMAP-001  
> **Estado:** PROPOSTA PARA REVISÃO  
> **Versão:** 1.0.0  
> **Data de criação:** 2026-10-11  
> **Data de atualização:** 2026-10-11  
> **Rastreabilidade:** feature/governanca-fundacao

## Contexto Histórico

O desenvolvimento do BRICKMASTER RAIZ, dos módulos experimentais e dos componentes Profit/NTSL ocorreu ao longo de diferentes conversas e áreas de trabalho. Este roadmap centraliza a sequência de trabalho e os critérios de passagem entre fases. Não substitui especificações existentes, não elimina históricos e não declara que uma funcionalidade está implementada ou validada sem evidência.

## Estado

Roadmap inicial proposto. A arquitetura documental está em revisão no PR #3; esta versão deve ser integrada nessa revisão, não diretamente em `main`.

## Princípios de execução

1. Preservar histórico, decisões, artefatos e falhas.
2. Usar o ciclo `feature/* → develop → validação → principal`.
3. Separar EXPERIMENTAL, VALIDADO, PRODUÇÃO, BLOQUEADO e DEPRECADO.
4. Cada módulo deve ter contrato, dependências, testes, evidências, limitações e checkpoint.
5. Dados ausentes, inválidos, atrasados ou contraditórios reduzem confiança ou bloqueiam ações.
6. O Giroscópio consolida o estado contextual; não substitui a validação da fonte.
7. Risco soberano pode vetar a decisão e a execução.
8. Não enviar ordens por padrão; execução exige autorização explícita.
9. Gráficos de ticks, incluindo 60K ticks, são cenários essenciais de arquitetura e validação.
10. A meta de 1% desde a abertura é hipótese de pesquisa, não promessa nem prioridade sobre o risco.

## Fases do roadmap

| Fase | Objetivo | Entrega verificável | Estado inicial |
|---|---|---|---|
| 00 — Inventário e governança | Consolidar documentos, versões, decisões, módulos e evidências sem apagar históricos | Inventário rastreável, mapa de dependências, decisões e roadmap aprovado | EM ESTRUTURAÇÃO |
| 01 — Giroscópio | Definir o estado canônico e a localização contextual do operador no gráfico | Contrato versionado, estados, qualidade/confiança, bloqueios e fixtures | ESPECIFICAÇÃO PENDENTE |
| 02 — Dados, tempo e persistência | Padronizar instrumento, sessão, timestamp/fuso, validade, lacunas, armazenamento e replay | Contratos de dados, testes de qualidade e persistência reproduzível | VALIDAÇÃO PENDENTE |
| 03 — Módulos analíticos | Desenvolver e testar módulos independentes | Contrato e testes separados para FVG-ATLAS, contador de toques, liquidez, Market DNA, VWAP/TWAP, fluxo, VIX, IBOV e calendário económico | PARCIAL / EXPERIMENTAL |
| 04 — Inteligência e decisão | Combinar evidências sem contar sinais correlacionados como independentes | Regras explicáveis, conflitos, confiança, cenários e invalidação | ESPECIFICAÇÃO PENDENTE |
| 05 — Risco soberano | Aplicar limites e bloqueios independentes da estratégia | Matriz de risco, condições de bloqueio e testes de falha segura | ESPECIFICAÇÃO PENDENTE |
| 06 — Profit/NTSL, execução e Watchdog | Validar a estratégia, reconciliar ordens/posições e detetar falhas | Compilação documentada, testes no Profit, reconciliação e recuperação | NÃO VALIDADO |
| 07 — Replay e validação integrada | Medir comportamento histórico e operacional com custos e limitações | Relatório reproduzível, baseline, métricas, testes de regressão e cenários tick/60K | PENDENTE |
| 08 — Promoção controlada | Integrar somente componentes aprovados | Aprovação explícita, versão/tag, monitorização, rollback e checkpoint de produção | PENDENTE |

Os estados acima são uma linha de base de planejamento e devem ser atualizados quando houver evidências novas. Não equivalem a resultados de testes.

## Dependências arquiteturais

```text
Fontes de dados
  → Qualidade, tempo e persistência
  → Giroscópio / estado canônico
  → Módulos analíticos independentes
  → Inteligência e decisão
  → Risco soberano
  → Execução conciliada
  → Watchdog, auditoria e recuperação

Replay/backtest e evidências atravessam todas as camadas.
Interface do operador expõe contexto, estado, confiança, fonte e motivo de bloqueio.
```

### Regras de dependência

- Módulos analíticos não enviam ordens e não alteram diretamente o estado de produção.
- O Giroscópio recebe dados com proveniência e publica estado, confiança, divergências e motivos de bloqueio.
- A decisão consome resultados versionados e considera correlação/duplicação de sinais.
- Risco soberano tem autoridade de veto; nenhum score pode contorná-lo.
- Execução concilia intenção, ordem enviada, confirmação, negócios e posição real.
- Watchdog monitoriza saúde, atrasos, falhas, divergências e recuperação.
- Módulos experimentais podem operar em sandbox/observação, sem autoridade operacional.

## Contrato mínimo obrigatório por módulo

1. Identidade estável, versão e estado de maturidade.
2. Objetivo e não objetivos.
3. Entradas, tipos, unidades, fontes, timestamps e validade.
4. Saídas, semântica, unidades e garantias.
5. Dependências diretas/indiretas e comportamento quando indisponíveis.
6. Regras, parâmetros, pré-condições e pós-condições.
7. Erros, limites, dados ausentes, atrasados, duplicados e contraditórios.
8. Testes unitários, contrato, integração, regressão e falha segura.
9. Fixtures, logs, artefatos e método de reprodução.
10. Limitações, riscos residuais, compatibilidade e rollback.
11. Checkpoint e próximo passo com critério objetivo.

## Critérios para avançar de fase

Uma fase só pode ser marcada como concluída quando:
- os entregáveis estão versionados no repositório;
- os critérios de aceitação foram definidos antes da execução;
- os testes aplicáveis foram executados e os resultados observados estão registados;
- as evidências são identificáveis e reproduzíveis;
- limitações, bloqueios e riscos residuais estão explícitos;
- as dependências e compatibilidade foram verificadas;
- o checkpoint indica decisão e próximo passo;
- a promoção foi aprovada conforme a governança.

Sem evidência suficiente, o estado é PENDING ou BLOCKED — nunca PASS por omissão.

## Barra de conclusão

A percentagem global ainda **não está calculada**. Não atribuir percentagens por impressão, número de documentos ou quantidade de ideias. Após inventário por entregável, calcular a conclusão por critérios ponderados e evidências; apresentar separadamente:
- cobertura documental;
- implementação;
- testes executados;
- validação reproduzível;
- prontidão operacional.

Uma funcionalidade não recebe crédito de validação apenas por estar descrita, compilar ou ter sido mencionada numa conversa.

## Próximo checkpoint

**ID:** BM-CP-ROADMAP-0001  
**Objetivo:** rever o PR #3, incorporar este roadmap e reconciliar os estados com os artefatos reais.  
**Esperado:** roadmap no branch de governança, links cruzados válidos, fases e critérios consistentes.  
**Não executado nesta etapa:** testes de código, compilação NTSL, backtest, testes no Profit e validação operacional.  
**Critério de encerramento:** revisão documental concluída, links verificados, estados confirmados contra evidências e aprovação explícita antes do merge.

## Evidências

- Repositório central: https://github.com/carlos-andrade/BRICKMASTER_GERAL
- Pull request de governança em revisão: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- Manual NTSL 4.4, versão de 03/08/2026, fornecido no contexto do projeto.
- Histórico do projeto consultado para identificar módulos e limitações; a validação integral de cada artefato permanece pendente.

## Resultado

Roadmap consolidado como proposta de organização. A sua criação não demonstra que as fases ou módulos foram concluídos.

## Próxima Ação

Rever e integrar este documento na PR #3; em seguida executar o inventário técnico de fase 00 e construir o registo de módulos com estados baseados em evidências.


## Validação

Revisão documental; não comprova testes de trading, compilação NTSL ou validação operacional.
