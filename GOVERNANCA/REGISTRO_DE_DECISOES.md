---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "REGISTRO_DECISOES"
fase: "FASE 00 — GOVERNANÇA"
id_documento: "BM-GOV-DECISIONS-001"
titulo: "Registo de Decisões Arquiteturais"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "PR #3; conteúdo original preservado e normalizado"
autoridade_documental: "GOVERNANCA e responsável pelo projeto"
cadeia_autoridade: "PROMPT -> CARTA -> LAYOUT UNICO -> CODIGO"
rastreabilidade: "PR #3; branch feature/pr3-governanca-mainline-reconciliation"
escopo: "Registo de Decisões Arquiteturais"
objetivo: "Documentar governança sem declarar aprovação ou testes não executados"
dependencias: "GOVERNANCA/NORMA-CABECALHO-PADRAO.md; main base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
sha256_canonico: "c883ba7772b8772d021e49ab38144f54d3a1cfa572d6a43e72098540cb0c1ddc"
commit_referencia: "3db0c88f27fec4c6ea2418749de09ebba8130fe7"
---
# Registro de Decisões Arquiteturais

Uma proposta não é uma decisão aprovada apenas por estar registrada aqui.

## ADR-0001 — Governança documental centralizada
- Estado: PROPOSTA
- Data: 2026-10-11
- Contexto: regras e decisões distribuídas dificultam continuidade e auditoria.
- Proposta: centralizar governança em GOVERNANCA/, com índice, inventário, histórico e checkpoints.
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

## Contexto Histórico

Conteúdo preservado da proposta de governança do PR #3.


## Estado

PROPOSTA PARA REVISÃO; não representa aprovação nem produção.


## Evidências

- PR #3 e histórico Git do BRICKMASTER_GERAL.


## Validação

Revisão documental; não comprova testes de trading, compilação NTSL ou validação operacional.


## Resultado

Documento em proposta, sujeito a revisão e critérios de aceitação.


## Próxima Ação

Rever conteúdo e executar o validador documental antes da promoção.
