---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "FASE_06_WATCHDOG_E_OBSERVABILIDADE"
id_documento: "BM-OBS-001-ESPECIFICACAO"
titulo: "Contrato técnico — Watchdog e observabilidade"
status: "CONTRATO_INICIAL; LIMITES_PENDENTES"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Baseline arquitetural BRICKMASTER RAIZ"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase06-exec-watchdog-contracts"
escopo: "Heartbeat, frescura, ligação, divergência e recuperação segura"
objetivo: "Reduzir confiança ou bloquear quando o sistema não tem estado fiável"
dependencias: "BM-DATA-001; BM-CORE-001; BM-RISK-001; BM-EXEC-001"
---

# Contrato técnico — Watchdog e observabilidade

## Contexto Histórico

A baseline define L9 como observabilidade/auditoria e prevê códigos como DATA_INVALID, CONTEXT_UNKNOWN, EVENT_UNCONFIRMED, RISK_BLOCK, NO_CONFLUENCE e SESSION_CLOSED.

## Estado

CONTRATO INICIAL — NÃO IMPLEMENTADO. Timeouts e limites de atraso serão configurados por fonte/componente após medição; não são inventados aqui.

## Contrato

### Sinais monitorizados
- Heartbeat de dados e timestamp da última atualização por fonte.
- Estado de sessão/abertura.
- Estado do Giroscópio e validade das entradas essenciais.
- Ligação ao Profit e última confirmação recebida.
- Diferença entre ordens/posição local e plataforma.
- Falhas de componente e tempo de processamento, quando disponíveis.

### Saídas
- watchdog_state: HEALTHY, DEGRADED, BLOCKED ou HALT.
- Fonte/componente afetado, última atualização, política aplicada e códigos de motivo.
- Evento de recuperação e condição que permitiu retomar.
- Log correlacionado com session_id, decision_id e client_order_id, quando existentes.

### Regras fail-closed
- Dado mais antigo que o limite configurado reduz confiança; se essencial, bloqueia.
- Perda de ligação durante envio torna o resultado UNKNOWN e exige reconciliação.
- Divergência de posição/ordens gera HALT até reconciliar com a plataforma.
- Retoma só após condição de recuperação explícita; não limpar falha silenciosamente.
- Alertas não são autorização para operar.
- Watchdog não produz sinais nem envia ordens.

### Dependências
BM-DATA-001, BM-CORE-001, BM-RISK-001, BM-EXEC-001 e canais reais de estado/heartbeat da plataforma.

## Evidências

Baseline arquitetural L9, registo mestre e contrato de execução conciliada.

## Validação

Contrato estático. Sem heartbeat implementado, teste de desconexão ou evidência de recuperação. Aceitação exige bloqueio em falha crítica e recuperação após reconciliação verificável.

## Resultado

Interface inicial do Watchdog definida; limites e comportamento real da plataforma continuam pendentes.

## Próxima Ação

Medir frescura/latência por fonte, escolher timeouts explícitos, implementar logs e testar perda de dados, ligação e divergência.

## Histórico de versões

- 0.1.0 — 2026-10-11 — primeiro contrato conceptual do Watchdog.
