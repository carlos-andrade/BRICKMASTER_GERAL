---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_VALIDACAO_E_RELEASE"
fase: "FASES_07_08_TESTES_E_INTEGRACAO"
id_documento: "BM-QA-RELEASE-001"
titulo: "Plano de validação, regressão e passagem a produção — fases 07/08"
status: "PLANO_INICIAL; EXECUCAO_PENDENTE"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Roadmap BRICKMASTER RAIZ e registo mestre de módulos"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase06-exec-watchdog-contracts"
escopo: "Portões de teste, replay, backtest, integração, release e rollback"
objetivo: "Impedir promoção por documentação isolada ou resultado não reproduzível"
dependencias: "Fases 00–06; contratos de módulos; datasets; CI"
---

# Plano de validação, regressão e passagem a produção — fases 07/08

## Contexto Histórico

O roadmap separa documentação, implementação, teste e validação. Aprovação em backtest não demonstra comportamento em tempo real nem rentabilidade futura.

## Estado

PLANO INICIAL — não há resultados de backtest/replay ou release candidate declarados por este documento.

## Evidências

Registar commit, versão/hash do código, dataset, configuração, ambiente e ID de teste no repositório.

## Validação

Os portões abaixo são critérios, não testes já executados.

## Resultado

Critérios mínimos para fases 07/08 definidos; promoção bloqueada até existirem evidências.

## Próxima Ação

Criar matriz de testes por módulo/dataset, executar testes isolados, regressão, replay/backtest e revisão; só então preparar release candidate.

## Fase 07 — Testes, replay e backtest

Para cada teste, registar ID, contrato/versão, instrumento/contrato, fonte e período dos dados, tipo de gráfico (incluindo ticks/60K quando aplicável), sessão/abertura, parâmetros, resultado esperado/observado, estado PASS/FAIL/BLOCKED/NOT_RUN e evidência. Quando medir resultado económico, registar custos, slippage, spread, latência e limitações. Distinguir histórico, replay, simulação e tempo real. Não declarar validade estatística com amostra insuficiente nem sem separar treino/validação quando aplicável.

## Fase 08 — Integração e produção

A passagem fica bloqueada até todos os portões serem PASS:
1. Fases 00–06 têm contratos, dependências, estado e limitações registados.
2. CI documental e testes de código relevantes aprovados no commit candidato.
3. Código NTSL validado contra Manual 4.4 e compilado no Profit da versão registada.
4. Testes de sessão/abertura e gráficos de ticks, incluindo 60K, com evidência reproduzível.
5. Risco soberano testado; política versionada e limites explicitamente aprovados.
6. Execução conciliada testada em simulação; sem divergências não resolvidas.
7. Watchdog testado para dados obsoletos, perda de ligação, reinício e recuperação.
8. Plano de rollback testado; release candidate identificada por commit/tag.
9. Aprovação explícita separada para qualquer ativação live.

## Regras de publicação

Desenvolvimento: feature → develop. Validação: workflows/testes e revisão sobre commit imutável. Principal: promoção separada após portões PASS e revisão. Ordens reais desativadas por padrão; documento ou CI verde não autoriza modo live.

## Histórico de versões

- 0.1.0 — 2026-10-11 — plano inicial de testes e portões de release.
