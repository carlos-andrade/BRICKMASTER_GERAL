---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "INVENTARIO_DOCUMENTAL"
fase: "GOVERNANCA"
id_documento: "BM-GOV-INVENTARIO-001"
titulo: "Inventário Documental e Plano de Migração"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.4"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; PR #42; workflow 40192045467; branch fix/governanca-validator-include-frontmatter"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "Inventário Documental e Plano de Migração"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "b247c0c5a83a782140b60ab9dfd72c69893c79fd958aa2baf552e462f64ecd72"
commit_referencia: "6470c5db9131fa57ece6b18badc6233604007b21"
---
# Inventário Documental e Plano de Migração

- Estado: INVENTÁRIO ESTRUTURAL INICIAL; classificação semântica final ainda requer revisão.
- Data de atualização: 2026-10-25
- Base de recuperação: `main` em `3db0c88f27fec4c6ea2418749de09ebba8130fe7`, integrada pelo merge commit `6118e0b131e445723ab27018371af9ebb01cddaa`.
- Método: comparação das árvores Git e identificação de caminhos. Não representa leitura semântica integral de todos os documentos do repositório.

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
- `GOVERNANCA/REGISTRO_MODULOS_E_CHECKPOINTS.md`, mantido no caminho e conteúdo existente em `main`.
- Inventários, auditorias e planos específicos já presentes em `main`.
- `README.md` principal já presente em `main`.

## Verificações e limitações

- A PR #3 foi fechada sem merge.
- A comparação Git consultada em 2026-10-25 entre `main` e `feature/governanca-fundacao` retornou: estado `diverged`, `ahead_by=19`, `behind_by=337`, `total_commits=19`. A branch histórica não foi integrada diretamente.
- A PR #41 recuperou os documentos numa linha derivada do `main` corrente e foi integrada no commit `6118e0b131e445723ab27018371af9ebb01cddaa`.
- O workflow de cabeçalhos da PR #41 falhou em 2026-10-25: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144. O log apontou múltiplos Markdown sem Front Matter YAML no início. O validador exige YAML universalmente, embora parte do corpus legado comece com comentário HTML.
- A correção estrutural da PR #42 passou no workflow `40192045467` em 2026-10-25, no commit testado `325092cb45efc132ce87691897a837dda9a3492d`: 169 Markdown rastreados, 55 documentos YAML verificados, 32 cabeçalhos HTML legados e 82 outros formatos legados. O PASS cobre apenas o subconjunto YAML; os 114 documentos legados continuam pendentes.
- Foram identificados 12 documentos recuperados e pelo menos 2 documentos de governança preexistentes explicitamente preservados; isso não equivale a inventário semântico integral.
- A regra de cabeçalho estrutural não valida o conteúdo semântico nem certifica hashes SHA-256.
- Não foram executados testes NTSL, compilação Profit, replay, backtest ou validação operacional.

## Próximos passos

1. Definir e executar a migração controlada dos 114 documentos legados ou aprovar exceções documentais explícitas por tipo.
2. Validar links e referências cruzadas após cada lote.
3. Recalcular independentemente SHA-256 canónico dos documentos adicionados/alterados, com normalização UTF-8/LF e exclusão apenas dos dois campos de integridade.
4. Atualizar as referências de commit em commit posterior ao conteúdo final.
5. Rever a PR #42 e integrar somente após revisão da integridade e dos limites da validação.

## Contexto Histórico

A proposta original do PR #3 foi recuperada por meio do PR #41 porque a branch antiga divergiu substancialmente do `main`. O merge da recuperação não prova que os documentos ou a governança foram semanticamente aprovados.

## Estado

PROPOSTA PARA REVISÃO. Inventário semântico integral, reconciliação de todos os documentos e auditoria independente de hashes permanecem pendentes.

## Evidências

- PR #3 fechado sem merge: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR #41 integrado: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Workflow de cabeçalhos falhado: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/40190767144
- Merge commit: `6118e0b131e445723ab27018371af9ebb01cddaa`
- Comparação da branch original: 19 commits à frente e 337 atrás no momento da consulta.

## Validação

CI estrutural parcial PASS no workflow `40192045467`. O SHA-256 canónico desta versão foi recalculado excluindo apenas as linhas `sha256_canonico` e `commit_referencia`; o valor registado será verificado novamente após a gravação dos metadados.

## Resultado

Inventário atualizado quanto à divergência da PR #3 e ao gate CI vermelho pós-merge. Sem declaração de validação técnica.

## Próxima Ação

Planear a migração controlada dos 114 documentos legados, verificar links e rever esta PR antes de qualquer promoção.
