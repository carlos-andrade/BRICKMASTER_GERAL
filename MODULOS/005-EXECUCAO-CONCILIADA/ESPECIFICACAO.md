---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "FASE_06_EXECUCAO_CONCILIADA"
id_documento: "BM-EXEC-001-ESPECIFICACAO"
titulo: "Contrato técnico — Execução conciliada"
status: "CONTRATO_INICIAL; IMPLEMENTACAO_PENDENTE"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Baseline arquitetural BRICKMASTER RAIZ"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase06-exec-watchdog-contracts"
escopo: "Estados de ordem/posição, reconciliação e idempotência"
objetivo: "Impedir duplicações e divergências entre estado local e estado reportado pelo Profit"
dependencias: "BM-RISK-001; BM-OBS-001; interface Profit; Manual NTSL 4.4"
---

# Contrato técnico — Execução conciliada

## Contexto Histórico

A arquitetura determina que só uma decisão aprovada pelo motor e pelo risco soberano pode chegar ao adaptador. Compilar ou passar em backtest não prova execução real.

## Estado

CONTRATO INICIAL — NÃO IMPLEMENTADO. Ordens reais desativadas por padrão.

## Contrato

### Entradas obrigatórias
- decision_id e resultado ALLOW do risco soberano.
- Instrumento/contrato, lado, quantidade, tipo de ordem e parâmetros aprovados.
- client_order_id idempotente e versão da política de execução.
- Estado atual de ordens/posição e saúde do Watchdog.
- Modo DRY_RUN, SIMULATION ou LIVE; LIVE não é permitido por defeito.

### Estados mínimos
CREATED, SUBMIT_PENDING, ACKNOWLEDGED, PARTIALLY_FILLED, FILLED, CANCEL_PENDING, CANCELED, REJECTED, EXPIRED, UNKNOWN, RECONCILIATION_REQUIRED.

### Invariantes
- Sem ALLOW explícito do risco, não criar ordem.
- SUBMIT_PENDING não significa aceitação da plataforma; exigir confirmação.
- Timeout/desconexão durante envio resulta em UNKNOWN/reconciliação, nunca reenvio cego.
- client_order_id deve prevenir duplicação em retries.
- Divergência entre estado local e Profit bloqueia novas ordens até reconciliação.
- Reinício com estado incerto inicia bloqueado; reconstruir estado pela plataforma.
- Cancelamento, fill parcial, rejeição, expiração e ordem manual externa são estados distintos.
- LIVE exige aprovação explícita fora deste módulo, release aprovado e política de risco ativa.
- Sem autorização explícita, não enviar ordens reais.

### Saídas
Estado da ordem, identificador da plataforma, timestamps, quantidades executadas/restantes, posição reconciliada, motivo de divergência e trilha auditável correlacionada por IDs.

### Dependências
Risco soberano, Watchdog, identidade do instrumento/contrato, sessão válida e interface real do Profit documentada.

## Evidências

Baseline arquitetural L8: execução recebe decisão aprovada por motor e risco; automação fica desativada durante testes de lógica.

## Validação

Contrato estático. Sem compilação, envio de ordens, simulação ou teste de integração. Aceitação exige idempotência, desconexão, estados parciais e reconciliação.

## Resultado

Fronteira de execução definida sem permitir que um sinal envie ordens automaticamente.

## Próxima Ação

Implementar dry-run/simulação, mapear estados reais do Profit e validar reconciliação antes de qualquer proposta de modo live.

## Histórico de versões

- 0.1.0 — 2026-10-11 — primeiro contrato de execução conciliada.
