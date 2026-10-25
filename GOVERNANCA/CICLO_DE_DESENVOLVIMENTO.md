---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "NORMA_CICLO_DESENVOLVIMENTO"
fase: "GOVERNANCA"
id_documento: "BM-GOV-CICLO-001"
titulo: "Ciclo de Desenvolvimento e Promoção"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; branch feature/pr3-governanca-mainline-reconciliation; main-base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "Ciclo de Desenvolvimento e Promoção"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "b1d4d27096b57d247e726d68dbedac17436e3ef931667757af487e84adc3cbc1"
commit_referencia: "PENDENTE_APOS_COMMIT"
---

# Ciclo de Desenvolvimento e Promoção

- Versão: 1.0.1
- Estado: PROPOSTA PARA REVISÃO
- Data: 2026-10-25

## Fluxo padrão

`feature/<escopo> → develop → validação → main`

### Feature — experimental

- Confirmar branch-base e commit inicial.
- Declarar objetivo, escopo, não objetivos e critérios de aceitação.
- Identificar arquivos afetados e dependências.
- Definir contrato e testes antes da integração.
- Registar limitações e evidências.

### Integração em develop

- Rever código e documentação.
- Verificar contratos e compatibilidade.
- Executar testes unitários, integração e falhas aplicáveis.
- Registar regressões e riscos residuais.

### Validação

Registar ambiente, versão, configuração, conjunto de dados, período, comandos, esperado, observado e artefactos. Para módulos de mercado, avaliar dados ausentes/atrasados/duplicados/contraditórios, sessão, instrumento, divergência entre fontes, reinício, perda de conexão e recuperação. Incluir gráficos de 60K trades quando aplicável.

Não declarar PASS sem saída ou artefacto verificável. Sem evidência, o resultado é PENDING.

### Promoção para main

Exigir critérios cumpridos, evidências vinculadas ao checkpoint, risco residual aceite, compatibilidade verificada, rollback definido, aprovação registada e commit/tag identificável.

## Versionamento

Mudanças incompatíveis exigem versão principal do contrato ou migração explícita. Mudanças compatíveis de capacidade podem incrementar versão menor; correções compatíveis podem incrementar patch. Nunca alterar retroativamente resultados de validação: emitir novo registo que supersede o anterior.

## Pull request

Descrever problema, mudanças, contratos afetados, testes e evidências, riscos, limitações, rollback e atualização do checkpoint. Declarar se o estado permanece experimental.

## Hotfix

Limitar escopo, preservar estado anterior, documentar risco de agir/não agir e realizar revisão posterior com evidências.

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
