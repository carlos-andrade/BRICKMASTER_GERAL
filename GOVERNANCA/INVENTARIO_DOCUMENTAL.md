---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "INVENTARIO_DOCUMENTAL"
fase: "GOVERNANCA"
id_documento: "BM-GOV-INVENTARIO-001"
titulo: "Inventário Documental e Plano de Migração"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; branch feature/pr3-governanca-mainline-reconciliation; main-base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "Inventário Documental e Plano de Migração"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "a3f40030e9ae10cd2274b9693b0d8f2ab46ec8a04dec3c552c0f6159bf8d8ff7"
commit_referencia: "PENDENTE_APOS_COMMIT"
---

# Inventário Documental e Plano de Migração

- Estado: INVENTÁRIO INICIAL EXECUTADO; classificação semântica final ainda requer revisão.
- Data: 2026-10-25
- Base examinada: main em `3db0c88f27fec4c6ea2418749de09ebba8130fe7` e proposta histórica do PR #3.
- Método: comparação das árvores Git e identificação de caminhos; não representa leitura semântica integral de todos os documentos do repositório.

## Critério de classificação

1. Governança: regras, autoridade, risco, decisões, checkpoints, contratos transversais e padrões documentais.
2. Arquitetura: desenho técnico e organização de camadas; permanece na pasta de arquitetura salvo quando o documento é um registo operacional de governança.
3. Módulo: especificações e testes próprios; permanecem junto ao módulo.
4. Evidência/referência: permanece na localização funcional original, com referência na governança quando necessário.

## Documentos recuperados pelo PR #41

| ID | Caminho | Estado |
|---|---|---|
| REC-0001 | `GOVERNANCA/CARTA_GOVERNANCA.md` | PROPOSTO |
| REC-0002 | `GOVERNANCA/CHECKPOINTS_E_EVIDENCIAS.md` | PROPOSTO |
| REC-0003 | `GOVERNANCA/CICLO_DE_DESENVOLVIMENTO.md` | PROPOSTO |
| REC-0004 | `GOVERNANCA/HISTORICO.md` | PROPOSTO |
| REC-0005 | `GOVERNANCA/INVENTARIO_DOCUMENTAL.md` | PROPOSTO |
| REC-0006 | `GOVERNANCA/MODELO_CHECKPOINT.md` | PROPOSTO |
| REC-0007 | `GOVERNANCA/MODELO_DECISAO.md` | PROPOSTO |
| REC-0008 | `GOVERNANCA/PADRAO_DE_MODULOS_E_CONTRATOS.md` | PROPOSTO |
| REC-0009 | `GOVERNANCA/README.md` | PROPOSTO |
| REC-0010 | `GOVERNANCA/REGISTRO_DE_DECISOES.md` | PROPOSTO |
| REC-0011 | `GOVERNANCA/RISCO_E_SEGURANCA.md` | PROPOSTO |
| REC-0012 | `GOVERNANCA/ROADMAP_MESTRE.md` | PROPOSTO |

## Documentos preexistentes preservados

- `GOVERNANCA/NORMA-CABECALHO-PADRAO.md`.
- `GOVERNANCA/REGISTRO_MODULOS_E_CHECKPOINTS.md`, mantido no caminho e conteúdo de `main`.
- Inventários, auditorias e planos específicos já presentes em `main`.
- `README.md` principal já presente em `main`.

## Verificações e limitações

- `main` consultado em `3db0c88f27fec4c6ea2418749de09ebba8130fe7`.
- A proposta histórica do PR #3 estava 19 commits à frente e 300 commits atrás de `main`, portanto não foi fundida diretamente.
- Foram identificados 12 documentos recuperados e 2 documentos de governança preexistentes explicitamente preservados.
- A classificação semântica integral de todos os documentos não está concluída.
- O validador de estrutura deve ser executado após normalização de metadados; esse validador não comprova conteúdo, hash ou validade técnica.
- Não foram executados testes NTSL, compilação Profit, backtest ou validação operacional.

## Próximo passo

Validar a estrutura documental, conferir os SHA-256 canónicos dos artefactos finalizados, rever as referências cruzadas e só depois considerar integração.

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
