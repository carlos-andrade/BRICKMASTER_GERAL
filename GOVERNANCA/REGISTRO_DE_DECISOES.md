---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "REGISTO_DECISOES"
fase: "GOVERNANCA"
id_documento: "BM-GOV-DECISOES-001"
titulo: "Registo de Decisões Arquiteturais"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; branch feature/pr3-governanca-mainline-reconciliation; main-base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "Registo de Decisões Arquiteturais"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "a4763a99e269224330e7c4ab57d74e57884f381c65448830d5f81662737eec6d"
commit_referencia: "PENDENTE_APOS_COMMIT"
---

# Registo de Decisões Arquiteturais

Uma proposta não é uma decisão aprovada apenas por estar registada aqui.

## ADR-0001 — Governança documental centralizada
- Estado: PROPOSTA
- Data: 2026-10-11
- Contexto: regras e decisões distribuídas dificultam continuidade e auditoria.
- Proposta: centralizar governança em GOVERNANCA/, com índice, inventário, histórico e checkpoints.
- Alternativas: documentação dispersa ou arquivo único.
- Consequências: maior rastreabilidade; exige inventário inicial e manutenção contínua.
- Evidência: PR #3 fechado sem merge; recuperação proposta no PR #41.

## ADR-0002 — Promoção por etapas
- Estado: PROPOSTA
- Proposta: usar feature → develop → validação → main, com critérios explícitos, evidências e rollback.
- Consequência: revisão mais rigorosa e menor risco de promover trabalho não comprovado.
- Validação pendente: confirmar fluxo e regras reais do repositório.

## ADR-0003 — Risco soberano
- Estado: PROPOSTA
- Proposta: camada de risco independente pode bloquear decisões e execução; estado desconhecido não é seguro.
- Consequência: alguns sinais serão bloqueados; limites precisam ser definidos antes de produção.

## Novas decisões
Use MODELO_DECISAO.md e registe alternativas, consequências, evidências e autoridade de aprovação.

## Contexto Histórico

Documento recuperado da proposta histórica PR #3, fechada sem merge, e reconciliado numa branch derivada do main corrente.

## Estado

PROPOSTA PARA REVISÃO. Não equivale a aprovação da governança, implementação operacional ou produção.

## Evidências

- PR #3 fechado sem merge: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR de recuperação: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Main-base: 3db0c88f27fec4c6ea2418749de09ebba8130fe7

## Validação

Estrutura documental sujeita ao workflow do repositório. O SHA-256 canónico será calculado sobre o corpo normalizado UTF-8/LF, excluindo apenas este bloco de metadados; o commit de referência será atualizado após a gravação final. Não foram executados testes NTSL, Profit, backtest nem validação operacional.

## Resultado

Conteúdo preservado e adaptado para revisão sobre o main corrente, sem substituir os artefactos de governança preexistentes.

## Próxima Ação

Executar a validação documental, auditar o SHA-256 final, conferir links e referências cruzadas e rever o PR antes de qualquer integração.
