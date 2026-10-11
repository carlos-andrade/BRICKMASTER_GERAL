# Registro de Decisões Arquiteturais

Uma proposta não é uma decisão aprovada apenas por estar registrada aqui.

## ADR-0001 — Governança documental centralizada
- Estado: PROPOSTA
- Data: 2026-10-11
- Contexto: regras e decisões distribuídas dificultam continuidade e auditoria.
- Proposta: centralizar governança em GOVERNANÇA/, com índice, inventário, histórico e checkpoints.
- Alternativas: documentação dispersa ou arquivo único.
- Consequências: maior rastreabilidade; exige inventário inicial e manutenção contínua.
- Evidência: branch feature/governanca-fundacao. Aprovação e merge ainda não comprovados.

## ADR-0002 — Promoção por etapas
- Estado: PROPOSTA
- Proposta: usar feature → develop → validação → principal, com critérios explícitos, evidências e rollback.
- Consequência: revisão mais rigorosa e menor risco de promover trabalho não comprovado.
- Validação pendente: confirmar fluxo e regras reais do repositório.

## ADR-0003 — Risco soberano
- Estado: PROPOSTA
- Proposta: camada de risco independente pode bloquear decisões e execução; estado desconhecido não é seguro.
- Consequência: alguns sinais serão bloqueados; limites precisam ser definidos antes de produção.

## Novas decisões
Use MODELO_DECISAO.md e registre alternativas, consequências, evidências e autoridade de aprovação.