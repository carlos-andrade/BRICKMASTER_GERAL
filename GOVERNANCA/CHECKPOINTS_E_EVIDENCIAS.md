---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "POLITICA_EVIDENCIAS"
fase: "FASE 00 — GOVERNANÇA"
id_documento: "BM-GOV-CHECKPOINTS-001"
titulo: "Checkpoints e Evidências"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "PR #3; conteúdo anterior preservado e normalizado"
autoridade_documental: "GOVERNANCA e responsável pelo projeto"
cadeia_autoridade: "PROMPT -> CARTA -> LAYOUT UNICO -> CODIGO"
rastreabilidade: "PR #3; branch feature/pr3-governanca-mainline-reconciliation"
escopo: "Checkpoints e Evidências"
objetivo: "Documentar governança, sem declarar aprovação ou testes não executados"
dependencias: "GOVERNANCA/NORMA-CABECALHO-PADRAO.md; main base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
sha256_canonico: "103081317ca19cecc59ba20536ccf52c4993c31202612557caa43a9cec7d2915"
commit_referencia: "3db0c88f27fec4c6ea2418749de09ebba8130fe7"
---
# Checkpoints e Evidências

Estado: PROPOSTA PARA REVISÃO. Data: 2026-10-11.

Um checkpoint deve permitir retomar o trabalho sem adivinhar. Relatos como “continuar” ou “funcionou” não são evidência suficiente.

## Campos obrigatórios
- ID e data/hora com fuso.
- Repositório, branch e commit-base.
- Objetivo, escopo e estado inicial.
- Arquivos criados, alterados ou movidos.
- Ambiente, comandos e configuração.
- Testes planejados e executados.
- Resultado esperado e observado.
- Links para logs, artefatos e commits.
- Limitações, riscos e bloqueios.
- Decisão e próximo passo com critério objetivo.

## Níveis de evidência
- E0: declaração sem artefato; não comprova validação.
- E1: artefato identificável, como log, saída, arquivo ou commit.
- E2: procedimento e ambiente reproduzíveis.
- E3: revisão ou reprodução independente.
- E4: histórico operacional monitorado.

## Resultados
PASS significa que todos os critérios foram cumpridos e as evidências estão referenciadas. FAIL indica critério violado. BLOCKED indica dependência ou risco que impediu execução. PENDING significa não executado ou sem evidência. NOT_APPLICABLE exige justificativa. Nunca converter PENDING em PASS por ausência aparente de erro.

## Evidências de mercado
Registrar dados/fixture, fonte, timestamp, instrumento, sessão, configuração, parâmetros, commit, resultado, custos e limitações. Distinguir backtest OHLC de tick a tick; incluir gráficos de ticks, incluindo 60K, quando fizer parte do cenário alegado.

## Encerramento de etapa
Salvar evidências, atualizar checkpoint, registrar decisão e risco residual, e indicar exatamente o próximo passo. Nunca incluir segredos em logs.

## Contexto Histórico

Documento histórico de governança preservado e reconciliado a partir da proposta PR #3.


## Estado

PROPOSTA PARA REVISÃO; não representa aprovação ou produção.


## Validação

Apenas revisão documental; não foram executados testes de trading, compilação NTSL ou validação no Profit por esta alteração.


## Próxima Ação

Verificar referências, conteúdo e critérios de aceitação antes de aprovação.
