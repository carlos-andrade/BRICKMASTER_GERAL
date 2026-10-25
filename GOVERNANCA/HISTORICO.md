---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "HISTORICO_GOVERNANCA"
fase: "GOVERNANCA"
id_documento: "BM-GOV-HIST-001"
titulo: "Histórico da Governança"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.3"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; PR #42; workflow 40191746933; branch fix/governanca-validator-include-frontmatter"
escopo: "Histórico de propostas e eventos de governança"
objetivo: "Preservar decisões, falhas, recuperações e supersessões"
dependencias: "GOVERNANCA/README.md; INVENTARIO_DOCUMENTAL.md; checkpoints relacionados"
sha256_canonico: "1b5d3ea42847a47a4470e008d93b25f92082983d31d12930e0de3a61afd44787"
commit_referencia: "62026c8b7436eb36ca71c50dbe3f8e4e15da7102"
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

- O workflow `40191746933` concluiu com sucesso no commit testado `1d3737423f48cd33d7fbf2c56c431916772c0b88`.
- O log reportou 169 Markdown rastreados, 55 documentos com Front Matter YAML verificados, 32 cabeçalhos HTML legados e 82 outros formatos legados.
- O PASS aplica-se somente à validação estrutural dos documentos YAML. Os 114 documentos sem YAML permanecem classificados como legados pendentes, não como conformes.
- A PR #42 continua aberta; esta entrada não afirma merge, aprovação semântica, integridade de SHA-256, compilação NTSL/Profit, backtest ou produção.
- Evidência: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40191746933

## Contexto Histórico

Histórico recuperado da proposta original do PR #3 e atualizado para registar eventos posteriores sem apagar os registos anteriores.

## Estado

PROPOSTA PARA REVISÃO; o estado documental não representa aprovação operacional.

## Evidências

- PR #3: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Workflow falhado: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144

## Validação

Atualização redacional do histórico com base em metadados e logs consultados. SHA-256 canónico e commit de referência precisam ser atualizados após a gravação final.

## Resultado

O histórico conserva tanto a recuperação integrada quanto a falha do gate que não impediu o merge.

## Próxima Ação

Auditar os SHA-256 canónicos e commits de referência; depois definir a migração controlada dos 114 documentos legados antes de qualquer promoção.
