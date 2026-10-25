---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "CHECKPOINT_AUDITORIA"
fase: "GOVERNANCA"
id_documento: "BM-CP-GOV-POSTMERGE-0001"
titulo: "Checkpoint Pós-Merge da Recuperação de Governança"
status: "BLOQUEADO_PARA_VALIDACAO"
versao: "1.0.1"
data_criacao: "2026-10-25"
data_atualizacao: "2026-10-25"
origem: "PR #41 integrado; falha de validação pós-merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; PR #42; branch fix/governanca-validator-include-frontmatter"
escopo: "Validação documental, verificação de metadados e critérios de integridade"
objetivo: "Registar a causa e a evolução dos gates CI sem declarar PASS indevido"
dependencias: "GitHub Actions; scripts/validar_cabecalhos_markdown.sh; INVENTARIO_DOCUMENTAL.md; HISTORICO.md"
sha256_canonico: "PENDENTE_DE_RECALCULO"
commit_referencia: "PENDENTE_APOS_COMMIT"
---
# Checkpoint pós-merge — recuperação da governança

## Sumário

O PR #41 foi integrado em `main` pelo merge commit `6118e0b131e445723ab27018371af9ebb01cddaa`. O workflow de cabeçalhos da PR #41 terminou em FAIL. A primeira correção, enviada na PR #42, também terminou em FAIL; o segundo log indicou formatos de cabeçalho adicionais que o script não reconhecia. A PR #42 permanece aberta para revisão e ainda não foi integrada.

## Evidência verificável

- PR #3, fechada sem merge: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR #41, integrada: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Workflow falhado da PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144
- PR #42, correção em revisão: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/42
- Workflow falhado da primeira iteração da PR #42: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40191285606
- Job da PR #41: `validar-markdown`, ID `121161093504`.
- Job da primeira iteração da PR #42: `validar-markdown`, ID `121162633277`.

## Causa técnica observada

O workflow executa `bash scripts/validar_cabecalhos_markdown.sh` sobre todos os Markdown rastreados. A implementação original exige Front Matter YAML (`---`) em todos os ficheiros. Parte do corpus legado começa por comentário HTML e outra parte utiliza cabeçalhos sem YAML nem comentário HTML. A primeira correção distinguiu os dois primeiros formatos, mas o log da PR #42 continuou a falhar para o terceiro conjunto.

A correção seguinte na mesma branch passou a separar os Markdown com YAML dos ficheiros legados sem YAML, registando aviso e contagem agregada. Esta mudança é uma correção estrutural provisória; não equivale à migração completa de todos os documentos para a norma canónica.

## Integridade documental adicional

1. Os documentos recuperados contêm campos de SHA-256 e de commit de referência que exigem recálculo/auditoria independente. A presença do campo, por si só, não prova o hash.
2. A comparação Git consultada para a PR #3 em 2026-10-25 indicou estado `diverged`, 19 commits à frente e 337 atrás. A branch histórica não foi fundida diretamente.
3. A PR #41 foi integrada apesar do workflow ter falhado; o histórico deve preservar este facto sem reescrever o resultado como PASS.
4. A governança documental continua em proposta/revisão. Merge documental não prova aprovação semântica, validação de módulos, compilação NTSL, Profit, replay, backtest ou produção.

## Plano de correção

- [ ] Executar o workflow após a última atualização do validador na PR #42.
- [ ] Se o job falhar, usar o log atualizado para identificar os campos e secções obrigatórios que falham nos documentos YAML.
- [ ] Não confundir tolerância transitória aos formatos legados com conformidade integral da norma; planear migração por lotes com diff e preservação de conteúdo.
- [ ] Recalcular independentemente SHA-256 dos artefactos novos/alterados e documentar a regra de normalização.
- [ ] Atualizar o commit de referência num commit posterior ao commit de conteúdo.
- [ ] Só declarar PASS para o escopo efetivamente coberto pelo teste e seus logs.

## Testes e estado

| Verificação | Estado |
|---|---|
| PR #3 | CLOSED, MERGED=false |
| PR #41 | CLOSED, MERGED=true |
| Workflow da PR #41 | FAIL |
| Primeira iteração do workflow da PR #42 | FAIL |
| Última alteração do validador na PR #42 | PENDING — workflow ainda por verificar |
| NTSL / compilação Profit | NOT_RUN |
| Replay / backtest | NOT_RUN |
| Validação em produção | NOT_RUN |

## Contexto Histórico

A recuperação documental foi integrada por PR #41 numa branch derivada do `main` corrente. Os problemas de validação foram registados em alterações posteriores, sem modificar o histórico da PR #3 nem afirmar aprovação de produção.

## Estado

BLOQUEADO para declarar validação documental concluída. A última iteração do validador ainda precisa de evidência de execução e os hashes canónicos precisam de auditoria independente.

## Evidências

- PR #3: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- PR #42: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/42
- Workflow da PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144
- Workflow da primeira iteração da PR #42: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40191285606
- Merge commit da PR #41: `6118e0b131e445723ab27018371af9ebb01cddaa`

## Validação

As falhas foram confirmadas consultando os logs dos workflows. A última alteração do validador ainda não foi verificada por um workflow concluído. Não foi feita compilação nem teste de trading.

## Resultado

A PR #41 está integrada, mas os gates documentais falharam nas duas primeiras execuções aqui examinadas. Uma alteração adicional do validador está na PR #42, ainda sem resultado de CI comprovado nesta etapa.

## Próxima Ação

Confirmar o resultado do workflow mais recente da PR #42 e, depois, auditar SHA-256 e referências de commit antes de considerar a validação documental concluída.
