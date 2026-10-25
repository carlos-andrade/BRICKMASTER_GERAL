---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "NORMA_CHECKPOINT_EVIDENCIAS"
fase: "GOVERNANCA"
id_documento: "BM-GOV-EVID-001"
titulo: "Checkpoints e Evidências"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; branch feature/pr3-governanca-mainline-reconciliation; main-base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "Checkpoints e Evidências"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "f9393464c4914b65e95810b54e9ac3f367c36c36d299befa3b586c9dbd55d7ea"
commit_referencia: "PENDENTE_APOS_COMMIT"
---

# Checkpoints e Evidências

Estado: PROPOSTA PARA REVISÃO. Data: 2026-10-25.

Um checkpoint deve permitir retomar o trabalho sem adivinhar. Relatos como “continuar” ou “funcionou” não são evidência suficiente.

## Campos obrigatórios

- ID e data/hora com fuso.
- Repositório, branch e commit-base.
- Objetivo, escopo e estado inicial.
- Arquivos criados, alterados ou movidos.
- Ambiente, comandos e configuração.
- Testes planejados e executados.
- Resultado esperado e observado.
- Links para logs, artefactos e commits.
- Limitações, riscos e bloqueios.
- Decisão e próximo passo com critério objetivo.

## Níveis de evidência

- E0: declaração sem artefacto; não comprova validação.
- E1: artefacto identificável, como log, saída, arquivo ou commit.
- E2: procedimento e ambiente reproduzíveis.
- E3: revisão ou reprodução independente.
- E4: histórico operacional monitorizado.

## Resultados

PASS significa que todos os critérios foram cumpridos e as evidências estão referenciadas. FAIL indica critério violado. BLOCKED indica dependência ou risco que impediu execução. PENDING significa não executado ou sem evidência. NOT_APPLICABLE exige justificação. Nunca converter PENDING em PASS por ausência aparente de erro.

## Evidências de mercado

Registar dados/fixture, fonte, timestamp, instrumento, sessão, configuração, parâmetros, commit, resultado, custos e limitações. Distinguir backtest OHLC de tick a tick; incluir gráficos de 60K trades quando fizer parte do cenário alegado.

## Encerramento de etapa

Guardar evidências, atualizar checkpoint, registar decisão e risco residual, e indicar exatamente o próximo passo. Nunca incluir segredos em logs.

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
