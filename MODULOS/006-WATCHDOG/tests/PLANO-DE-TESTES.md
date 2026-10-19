---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE_06_WATCHDOG_E_OBSERVABILIDADE"
id_documento: "BM-OBS-001-TESTES"
titulo: "Plano de testes — Watchdog"
status: "PLANEADO; NAO_EXECUTADO"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Contrato BM-OBS-001-ESPECIFICACAO"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase06-exec-watchdog-contracts"
escopo: "Freshness, ligação, bloqueio e recuperação"
objetivo: "Demonstrar comportamento fail-closed e recuperação auditável"
dependencias: "ESPECIFICACAO.md; BM-DATA-001; BM-EXEC-001; ambiente simulado"
---

# Plano de testes — Watchdog

## Contexto Histórico

Plano criado antes da implementação para evitar que alertas sejam confundidos com autorização.

## Estado

PLANEADO — todos os casos NOT_RUN.

## Evidências

Registar componente, timestamp, timeout, falha injetada, estado esperado/observado e log.

## Validação

Plano documental; não comprova testes executados.

## Resultado

Casos mínimos de falha/recuperação definidos.

## Próxima Ação

Executar em ambiente simulado após implementar heartbeat e logging.

| ID | Caso | Resultado esperado | Estado |
|---|---|---|---|
| WD-01 | Fonte essencial obsoleta | BLOCKED/HALT | NOT_RUN |
| WD-02 | Fonte não essencial obsoleta | DEGRADED | NOT_RUN |
| WD-03 | Sessão/abertura inválida | BLOCKED | NOT_RUN |
| WD-04 | Ligação Profit perdida | BLOCKED/HALT; ordem pendente fica UNKNOWN | NOT_RUN |
| WD-05 | Posição local diverge da plataforma | HALT até reconciliação | NOT_RUN |
| WD-06 | Heartbeat de módulo ausente | DEGRADED/BLOCKED conforme criticidade | NOT_RUN |
| WD-07 | Dados recuperam após falha | Retoma após validação explícita | NOT_RUN |
| WD-08 | Reinício do processo | Revalida sessão, dados e posição | NOT_RUN |
| WD-09 | Log de evento crítico | Fonte, timestamp, estado e motivo | NOT_RUN |
| WD-10 | Alerta recebido | Não envia ordem automaticamente | NOT_RUN |
