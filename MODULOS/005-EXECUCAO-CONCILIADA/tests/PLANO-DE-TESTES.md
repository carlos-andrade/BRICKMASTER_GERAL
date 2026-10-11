---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE_06_EXECUCAO_CONCILIADA"
id_documento: "BM-EXEC-001-TESTES"
titulo: "Plano de testes — Execução conciliada"
status: "PLANEADO; NAO_EXECUTADO"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Contrato BM-EXEC-001-ESPECIFICACAO"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase06-exec-watchdog-contracts"
escopo: "Estados, idempotência e reconciliação"
objetivo: "Impedir ordens duplicadas e ações em estado desconhecido"
dependencias: "ESPECIFICACAO.md; simulação; BM-RISK-001; Watchdog"
---

# Plano de testes — Execução conciliada

## Contexto Histórico

Plano criado antes da implementação. Modo live não está autorizado.

## Estado

PLANEADO — todos os casos NOT_RUN.

## Evidências

Registar IDs, estado Profit, modo, inputs, resultado esperado/observado e logs/capturas.

## Validação

Plano documental; não comprova testes executados.

## Resultado

Critérios mínimos de aceitação para o adaptador definidos.

## Próxima Ação

Executar em dry-run/simulação com dados reproduzíveis; não usar ordens reais.

| ID | Caso | Resultado esperado | Estado |
|---|---|---|---|
| EX-01 | Risco sem ALLOW | Ordem não criada | NOT_RUN |
| EX-02 | Retry com mesmo client_order_id | Sem duplicação | NOT_RUN |
| EX-03 | Timeout após envio | UNKNOWN; reconciliação antes de retry | NOT_RUN |
| EX-04 | Fill parcial | Quantidade executada/restante conciliada | NOT_RUN |
| EX-05 | Cancelamento pendente | Não marcar cancelado antes da confirmação | NOT_RUN |
| EX-06 | Rejeição da plataforma | REJECTED com motivo | NOT_RUN |
| EX-07 | Desconexão | Bloqueio e reconciliação | NOT_RUN |
| EX-08 | Reinício com posição aberta | Reconstrução a partir do Profit | NOT_RUN |
| EX-09 | Ordem manual externa | Divergência detetada; novas ordens bloqueadas | NOT_RUN |
| EX-10 | Estado local difere do Profit | RECONCILIATION_REQUIRED | NOT_RUN |
| EX-11 | Modo padrão | DRY_RUN/SIMULATION; sem LIVE | NOT_RUN |
| EX-12 | Logs correlacionados | IDs e timestamps por decisão/ordem | NOT_RUN |
