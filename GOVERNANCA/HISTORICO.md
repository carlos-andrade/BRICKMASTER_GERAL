---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "HISTORICO_GOVERNANCA"
fase: "GOVERNANCA"
id_documento: "BM-GOV-HIST-001"
titulo: "Histórico da Governança"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.4"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; PR #42; workflow 40192045467; branch fix/governanca-validator-include-frontmatter"
escopo: "Histórico de propostas e eventos de governança"
objetivo: "Preservar decisões, falhas, recuperações e supersessões"
dependencias: "GOVERNANCA/README.md; INVENTARIO_DOCUMENTAL.md; checkpoints relacionados"
sha256_canonico: "ccade5a91d03add143759077ae68262e080b512067e41cc47d3ab348d8cd9f71"
commit_referencia: "77a9dbee297535a00b0f6ee3bd5f6c0e4a2900e7"
---
# Histórico da Governança

Este registo preserva a trilha histórica. Correções e supersessões são acrescentadas como novas entradas; não apagar falhas ou decisões anteriores.

## 2026-10-11 — Fundação documental proposta

- Criada a branch `feature/governanca-fundacao` a partir de uma referência de `main`.
- Preparados documentos de carta, processo de desenvolvimento, contratos, risco, checkpoints, decisões, inventário e modelos.
- Estado inicial: proposta documental, sem aprovação nem merge em `main` comprovados.
- Evidência: commit de fundação `b9f54d0b479e0a727e6dec409152b129cd55a36e`; PR #3 aberto em modo draft.
- Limitação inicial: a árvore completa não tinha sido obtida naquela etapa; a afirmação foi revista após consulta posterior à API Git.

## 2026-10-25 — Recuperação controlada da proposta fechada

- O PR #3 foi encerrado sem merge; os seus commits não foram integrados diretamente.
- A branch antiga divergiu do `main` corrente: a comparação consultada indicou 19 commits à frente e 337 atrás.
- Foi aberta uma proposta de recuperação numa branch nova derivada do `main` corrente.
- A recuperação preservou a norma de cabeçalho e o registo de módulos preexistentes.
- O PR #41 foi integrado no commit `6118e0b131e445723ab27018371af9ebb01cddaa`.

## 2026-10-25 — Supersessão: gate de validação pós-merge falhado

- A versão anterior deste histórico dizia que o PR de recuperação devia passar pelo validador e pela revisão dos hashes antes do merge. Essa condição não foi satisfeita: o workflow da PR #41 terminou em FAIL.
- Evidência: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144
- O log do job `validar-markdown` reporta múltiplas falhas `Falta Front Matter YAML no início.`.
- A causa observada é a incompatibilidade entre a regra universal do validador e Markdown legado cujo primeiro elemento é comentário HTML. A correção deverá ser executada em branch e validada antes de novo merge.
- O merge da PR #41 não é prova de aprovação semântica de governança, integridade independente de hashes, validação NTSL/Profit, backtest ou produção.
- A integração com gate vermelho é preservada no histórico; não reescrever o resultado para PASS.

## 2026-10-25 — Correção estrutural parcial verificada na PR #42

- O workflow `40191746933` concluiu com sucesso; o registo de execução devolveu o commit de job `40b11f7ef7bd755403d3689b7fc5c736e80c6bed`.
- O log reportou 169 Markdown rastreados, 55 documentos com Front Matter YAML verificados, 32 cabeçalhos HTML legados e 82 outros formatos legados.
- O PASS aplica-se somente à validação estrutural dos documentos YAML. Os 114 documentos sem YAML permanecem classificados como legados pendentes, não como conformes.
- A PR #42 continua aberta; esta entrada não afirma merge, aprovação semântica, integridade de SHA-256, compilação NTSL/Profit, backtest ou produção.
- Evidência: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40191746933

## 2026-10-25 — Integridade SHA-256 e CI pós-metadados

- Foram gravados e recalculados os hashes canónicos para o inventário, este histórico e o checkpoint; o cálculo exclui somente as linhas `sha256_canonico` e `commit_referencia`, após normalização UTF-8/LF.
- O workflow `40192045467` terminou com sucesso no commit testado `325092cb45efc132ce87691897a837dda9a3492d`.
- O log regista 169 Markdown rastreados, 55 documentos com YAML verificados, 32 cabeçalhos HTML legados e 82 outros formatos legados. A validação permanece parcial; os 114 ficheiros sem YAML continuam pendentes.
- Evidência: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40192045467

## Contexto Histórico

Histórico recuperado da proposta original do PR #3 e atualizado para registar eventos posteriores sem apagar os registos anteriores.

## Estado

PROPOSTA PARA REVISÃO; o estado documental não representa aprovação operacional.

## Evidências

- PR #3: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Workflow falhado: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144

## Validação

SHA-256 canónico do inventário, deste histórico e do checkpoint foi recalculado e confirmado, usando UTF-8/LF e excluindo somente as linhas `sha256_canonico` e `commit_referencia`. Os commits de referência apontam para os commits que contêm as versões de conteúdo usadas no cálculo. Outros documentos do corpus ainda requerem auditoria.

## Resultado

O histórico conserva tanto a recuperação integrada quanto a falha do gate que não impediu o merge.

## Próxima Ação

Concluir a migração controlada dos 114 documentos legados ou aprovar exceções explícitas; auditar os restantes hashes; manter a aprovação documental separada da validação de produção.
