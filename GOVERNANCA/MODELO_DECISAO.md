---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "MODELO_DECISAO"
fase: "GOVERNANCA"
id_documento: "BM-GOV-MODELO-ADR-001"
titulo: "Modelo de Decisão Arquitetural"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; branch feature/pr3-governanca-mainline-reconciliation; main-base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "Modelo de Decisão Arquitetural"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "9bbcc8ac30e745d08c547e07a4c523968b75866af7867bf2d2ad49adb5365bf9"
commit_referencia: "PENDENTE_APOS_COMMIT"
---

# ADR-[NNNN] — [Título]

- Estado: PROPOSTA / ACEITA / REJEITADA / DEPRECADA / SUPERSEDIDA
- Data: [AAAA-MM-DD]
- Responsável pela decisão: [papel]
- Módulos afetados: [lista]
- Referências: [issues, PRs, commits e checkpoints]

## Contexto
Qual problema exige decisão? Quais factos e evidências são conhecidos?

## Restrições
Limites técnicos, operacionais, de segurança, dados, compatibilidade e risco.

## Alternativas
1. Alternativa A: vantagens, custos e riscos.
2. Alternativa B: vantagens, custos e riscos.
3. Não alterar: consequências.

## Decisão
Descrever a decisão em termos verificáveis e distinguir proposta de aprovação efetiva.

## Consequências
- Benefícios:
- Custos:
- Riscos residuais:
- Compatibilidade e migração:

## Validação
- Testes exigidos:
- Evidências:
- Critérios de aceitação:
- Plano de rollback:

## Histórico
- [data] — [alteração, papel responsável e evidência]

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
