---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "CHECKPOINT_AUDITORIA"
fase: "GOVERNANCA"
id_documento: "BM-CP-GOV-POSTMERGE-0001"
titulo: "Checkpoint Pós-Merge da Recuperação de Governança"
status: "VALIDACAO_ESTRUTURAL_PARCIAL"
versao: "1.0.4"
data_criacao: "2026-10-25"
data_atualizacao: "2026-10-25"
origem: "PR #41 integrada; gate documental corrigido parcialmente na PR #42"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; PR #42; workflow 40192045467; branch fix/governanca-validator-include-frontmatter"
escopo: "Validação estrutural de cabeçalhos Markdown e integridade documental"
objetivo: "Registar falhas históricas, correção do validador e limites do resultado observado"
dependencias: "GitHub Actions; scripts/validar_cabecalhos_markdown.sh; INVENTARIO_DOCUMENTAL.md; HISTORICO.md"
sha256_canonico: "5542818f19c7189d009c41a40427bbfc392476456aaa7e2c0f7c6fd3ed1c1d00"
commit_referencia: "62026c8b7436eb36ca71c50dbe3f8e4e15da7102"
---

# Checkpoint pós-merge — recuperação da governança

## Sumário

O PR #41 foi integrado em `main` pelo merge commit `6118e0b131e445723ab27018371af9ebb01cddaa`. O workflow de cabeçalhos da PR #41 falhou. A primeira iteração corretiva da PR #42 também falhou. Após nova alteração do validador e atualização deste checkpoint, o workflow `40192045467` concluiu com sucesso no commit testado `325092cb45efc132ce87691897a837dda9a3492d`, já com os metadados SHA-256 registados.

O resultado é **PASS estrutural parcial**: valida a estrutura dos 55 documentos com Front Matter YAML, não os 114 documentos legados sem YAML nem os seus conteúdos semânticos ou hashes.

## Evidências verificáveis

- PR #3 fechada sem merge: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR #41 integrada: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Workflow falhado da PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144
- PR #42, ainda aberta para revisão: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/42
- Primeira iteração falhada da PR #42: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40191285606
- Última execução com sucesso estrutural: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40192045467
- Job da última execução: `validar-markdown`, ID `121164904928`.

## Resultado medido

| Métrica do workflow | Resultado |
|---|---:|
| Markdown rastreados | 169 |
| Documentos com Front Matter YAML verificados | 55 |
| Cabeçalhos HTML legados reportados | 32 |
| Outros formatos legados reportados | 82 |
| Conclusão do job estrutural YAML | PASS |

As duas categorias legadas não são declaradas conformes. O script emite avisos e mantém pendente a migração controlada desses ficheiros. A norma exige tratamento explícito dos formatos, preservação do conteúdo e validação por lotes.

## Causa técnica observada

O workflow executa `bash scripts/validar_cabecalhos_markdown.sh` sobre todos os Markdown rastreados. A versão original exigia Front Matter YAML em todos os ficheiros, embora parte do corpus legado comece por comentário HTML e outra parte use formatos de cabeçalho diferentes. As primeiras correções também falharam. A versão corrente verifica campos e secções obrigatórias nos ficheiros YAML e contabiliza separadamente os Markdown legados sem YAML.

Esta alteração permite um resultado estrutural reproduzível para os 55 ficheiros YAML, mas não substitui a migração integral exigida pela norma documental.

## Integridade documental adicional

1. A comparação Git consultada para a PR #3 em 2026-10-25 indicou estado `diverged`, 19 commits à frente e 337 atrás. A branch histórica não foi fundida diretamente.
2. O PR #41 foi integrado apesar do workflow ter falhado. O histórico preserva esse facto.
3. Os documentos alterados por esta correção têm campos de SHA-256 e commit de referência pendentes de auditoria independente. A presença de um campo não prova a integridade do hash. Regra canónica adotada nesta correção: normalizar o conteúdo para UTF-8/LF e excluir somente as linhas `sha256_canonico` e `commit_referencia` do cálculo, evitando autorreferência.
4. A governança continua em proposta/revisão. Merge documental ou PASS estrutural parcial não prova aprovação semântica, validação de módulos, compilação NTSL, Profit, replay, backtest ou produção.

## Plano pendente

- [ ] Migrar os 114 documentos legados sem Front Matter YAML por lotes controlados, preservando conteúdo e histórico, ou formalizar exceções de formato por tipo documental.
- [ ] Validar links e referências cruzadas após cada lote.
- [ ] Recalcular independentemente SHA-256 dos artefactos novos/alterados e definir a normalização UTF-8/LF aplicada.
- [ ] Atualizar os campos de commit de referência em commit posterior ao conteúdo final.
- [ ] Revisar a PR #42 antes de qualquer merge.
- [ ] Executar validações NTSL/Profit e testes de estratégia apenas quando houver código e escopo aplicável; nada disso foi executado nesta tarefa.

## Testes e estado

| Verificação | Estado |
|---|---|
| PR #3 | CLOSED, MERGED=false |
| PR #41 | CLOSED, MERGED=true |
| Workflow da PR #41 | FAIL |
| Primeira iteração do workflow da PR #42 | FAIL |
| Última iteração estrutural YAML da PR #42 | PASS, escopo parcial |
| Migração dos 114 documentos legados | PENDING |
| Auditoria independente de SHA-256 | PENDING |
| NTSL / compilação Profit | NOT_RUN |
| Replay / backtest | NOT_RUN |
| Validação em produção | NOT_RUN |

## Contexto Histórico

A recuperação documental foi integrada por PR #41 numa branch derivada do `main` corrente. As falhas e a correção parcial foram registadas sem alterar o histórico da PR #3 nem converter retroativamente FAIL em PASS.

## Estado

VALIDAÇÃO ESTRUTURAL PARCIAL. Os documentos YAML verificados passaram no workflow mais recente; a migração dos documentos legados e a auditoria de hashes permanecem pendentes. Não declarar conformidade documental integral nem produção.

## Evidências

- PR #3: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- PR #42: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/42
- Workflow falhado da PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144
- Workflow falhado da primeira iteração da PR #42: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40191285606
- Workflow mais recente: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40191704776
- Merge commit da PR #41: `6118e0b131e445723ab27018371af9ebb01cddaa`
- Commit verificado na última execução: `325092cb45efc132ce87691897a837dda9a3492d`

## Validação

O log da última execução reporta 169 Markdown, 55 documentos YAML verificados, 32 cabeçalhos HTML legados e 82 outros formatos legados; o job terminou em SUCCESS. A validação é estrutural e não calcula SHA-256 nem verifica conteúdo semântico.

## Resultado

A PR #42 passou a verificação estrutural parcial. Continua aberta e não foi integrada.

## Próxima Ação

Rever o diff da PR #42, completar a auditoria de hashes e planear a migração controlada dos 114 documentos legados antes da promoção.
