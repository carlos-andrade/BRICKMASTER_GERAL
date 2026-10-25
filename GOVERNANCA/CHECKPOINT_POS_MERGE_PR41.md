<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Relatório de checkpoint pós-merge da recuperação de governança
IDENTIFICADOR: BM-CP-GOV-POSTMERGE-0001
TIPO DOCUMENTAL: CHECKPOINT / AUDITORIA DE INTEGRIDADE
FASE DO ROADMAP: FASE 00 — INVENTÁRIO E GOVERNANÇA
VERSÃO: 1.0.0
ESTADO: BLOQUEADO PARA DECLARAÇÃO DE VALIDAÇÃO — CORREÇÕES PENDENTES
CRIADO EM: 2026-10-25
ÚLTIMA REVISÃO: 2026-10-25
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
BRANCH: fix/governanca-validator-include-frontmatter
PULL REQUEST: A CRIAR
OBJETIVO: Registar a causa demonstrada da falha do validador após PR #41 e definir correções mínimas verificáveis sem modificar main diretamente.
ESCOPO: Auditoria documental e correção do validador / metadados de inventário; não valida módulos de trading.
REFERÊNCIAS: PR #3; PR #41; workflow validar-cabecalhos-documentais.yml; scripts/validar_cabecalhos_markdown.sh.
DEPENDÊNCIAS: GitHub Actions; bash; árvore Markdown do repositório.
HISTÓRICO:
- 2026-10-25 | v1.0.0 | Checkpoint criado a partir da evidência do workflow do PR #41.
SHA-256 CANÓNICO: CALCULAR APÓS GRAVAÇÃO FINAL
COMMIT DE REFERÊNCIA: PENDENTE APÓS COMMIT
LIMITAÇÕES: Não foram executados NTSL, Profit, replay, backtest ou validação operacional.
FONTE DA VERDADE: Repositório oficial e logs de GitHub Actions.
-->

# Checkpoint pós-merge — recuperação da governança

## Sumário

O PR #41 foi integrado em `main` pelo merge commit `6118e0b131e445723ab27018371af9ebb01cddaa`. A integração documental ocorreu, mas o workflow `Validar cabeçalhos documentais` associado ao commit da PR #41 terminou em **FAIL**.

## Evidência verificável

- PR original fechado sem merge: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR de recuperação integrado: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Workflow falhado da PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144
- Job: `validar-markdown`, ID `121161093504`.
- Script chamado pelo workflow: `bash scripts/validar_cabecalhos_markdown.sh`.
- Resultado do log: múltiplas ocorrências de `Falta Front Matter YAML no início.` e saída final `Validação documental FALHOU.`

## Causa técnica demonstrada

O script percorre todos os Markdown rastreados com `git ls-files -z '*.md'` e exige que a primeira linha de cada arquivo seja `---`. O inventário atual contém ficheiros Markdown legados que começam com comentário HTML (`<!--`) em vez de Front Matter YAML. Por exemplo, o `README.md` na raiz de `main` começa com comentário HTML. O validador aplica, portanto, uma regra universal incompatível com parte do corpus atual.

O log prova falhas de formato do cabeçalho para muitos ficheiros, mas a evidência disponível não identifica por nome todos os ficheiros falhados nem demonstra que todos os documentos tenham o mesmo problema. Não declarar o número exato de ficheiros sem um relatório detalhado.

## Integridade documental adicional

1. Os documentos recuperados ainda carregam `commit_referencia: PENDENTE_APOS_COMMIT` e declaram SHA-256 canónico, mas a integridade desses hashes não foi recalculada independentemente neste checkpoint.
2. O inventário documental afirma que a PR #3 estava 300 commits atrás de `main`; a comparação real da PR #3 feita em 2026-10-25 retornou `ahead_by=19`, `behind_by=337`, `total_commits=19`, status `diverged`. Corrigir esse registo para 337, com indicação da hora/data da comparação.
3. O histórico de governança diz que o PR de recuperação “deve passar” pelo validador e pela revisão de hashes antes de merge, mas a PR foi integrada apesar do workflow ter falhado. Acrescentar uma entrada de supersessão pós-merge, sem apagar a entrada anterior, explicitando que a integração aconteceu com gate vermelho.
4. O estado documental continua proposta/revisão; o merge não deve ser interpretado como aprovação semântica de governança, validação técnica, produção ou aprovação de risco.

## Plano de correção na branch

- [ ] Ajustar o validador para suportar explicitamente os formatos permitidos pela norma canónica e pelo corpus legado. Uma alternativa é migrar, de forma controlada, os Markdown legados, preservando conteúdo e histórico. Não relaxar a verificação silenciosamente.
- [ ] Produzir lista dos ficheiros que falham, com regra e motivo por arquivo.
- [ ] Corrigir a contagem da divergência no inventário (337 commits atrás na comparação consultada).
- [ ] Atualizar o histórico com a falha do workflow pós-merge.
- [ ] Recalcular independentemente SHA-256 canónico para cada documento criado/alterado, conforme a regra de normalização definida, e atualizar o commit de referência em novo commit posterior.
- [ ] Reexecutar o workflow; registrar resultado real e links dos logs.
- [ ] Não alterar diretamente `main` nesta correção; submeter nova PR derivada do main atual.

## Testes e estado

| Verificação | Resultado |
|---|---|
| Estado da PR #3 | CLOSED, MERGED=false |
| Estado da PR #41 | CLOSED, MERGED=true |
| Workflow de validação da PR #41 | FAIL |
| Compilação NTSL / Profit | NOT_RUN |
| Replay / backtest | NOT_RUN |
| Validação em produção | NOT_RUN |

## Contexto Histórico

A recuperação dos documentos da PR #3 foi realizada por uma branch derivada do `main` corrente e integrada por PR #41. A branch original da PR #3 não foi fundida diretamente por estar divergente.

## Estado

BLOQUEADO para declarar validação documental concluída até o validador ser corrigido e o workflow passar com evidência.

## Evidências

- PR #3: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Workflow: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144
- Merge commit: `6118e0b131e445723ab27018371af9ebb01cddaa`
- Comparação atual da PR #3: `main...feature/governanca-fundacao` — 19 commits à frente, 337 atrás, divergente.

## Validação

A evidência de falha foi consultada no log do GitHub Actions. As restantes ações deste plano ainda não foram executadas.

## Resultado

A recuperação foi integrada; o gate de cabeçalhos falhou. A governança não deve ser declarada validada nem aprovada com base no merge isolado.

## Próxima Ação

Corrigir o validador em branch baseada no `main`, listar as falhas por arquivo, atualizar o inventário e o histórico, recalcular hashes e abrir uma nova PR.
