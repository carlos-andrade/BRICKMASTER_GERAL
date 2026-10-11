# Ciclo de Desenvolvimento e Promoção

- Versão: 1.0.0
- Estado: PROPOSTA PARA REVISÃO
- Data: 2026-10-11

## Fluxo padrão

`feature/<escopo> → develop → validação → principal`

### Feature — experimental
- Confirmar branch-base e commit inicial.
- Declarar objetivo, escopo, não objetivos e critérios de aceitação.
- Identificar arquivos afetados e dependências.
- Definir contrato e testes antes da integração.
- Registrar limitações e evidências.

### Integração em develop
- Revisar código e documentação.
- Verificar contratos e compatibilidade.
- Executar testes unitários, integração e falhas aplicáveis.
- Registrar regressões e riscos residuais.

### Validação
Registrar ambiente, versão, configuração, conjunto de dados, período, comandos, esperado, observado e artefatos. Para módulos de mercado, avaliar dados ausentes/atrasados/duplicados/contraditórios, sessão, instrumento, divergência entre fontes, reinício, perda de conexão e recuperação. Incluir gráficos de ticks, inclusive 60K, quando aplicável.

Não declarar PASS sem saída ou artefato verificável. Sem evidência, o resultado é PENDING.

### Promoção para principal
Exigir critérios cumpridos, evidências vinculadas ao checkpoint, risco residual aceito, compatibilidade verificada, rollback definido, aprovação registrada e commit/tag identificável.

## Versionamento

Mudanças incompatíveis exigem versão principal do contrato ou migração explícita. Mudanças compatíveis de capacidade podem incrementar versão menor; correções compatíveis podem incrementar patch. Nunca alterar retrospectivamente resultados de validação: emitir novo registro que supersede o anterior.

## Pull request

Descrever problema, mudanças, contratos afetados, testes e evidências, riscos, limitações, rollback e atualização do checkpoint. Declarar se o estado permanece experimental.

## Hotfix

Limitar escopo, preservar estado anterior, documentar risco de agir/não agir e realizar revisão posterior com evidências.