---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "README_MODULO"
fase: "FASE_06_EXECUCAO_CONCILIADA"
id_documento: "BM-EXEC-001-README"
titulo: "Módulo 005 — Execução conciliada"
status: "CONTRATO_INICIAL; IMPLEMENTACAO_PENDENTE"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Baseline arquitetural BRICKMASTER RAIZ"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase06-exec-watchdog-contracts"
escopo: "Ordens/posições com reconciliação explícita ao Profit"
objetivo: "Impedir que intenção local seja confundida com execução confirmada"
dependencias: "BM-RISK-001; BM-OBS-001; Manual NTSL 4.4; estado Profit"
---

# Módulo 005 — Execução conciliada

## Contexto Histórico

A baseline separa decisão, risco soberano e execução. Este módulo define a fronteira de execução sem ativar ordens reais.

## Estado

Contrato inicial documentado; implementação e integração com Profit pendentes.

## Evidências

Baseline arquitetural L8, contrato de risco soberano e especificação técnica.

## Validação

Sem código, compilação ou ordens de teste nesta fase.

## Resultado

Execução é um adaptador com estado próprio e reconciliação obrigatória, não um efeito colateral do sinal.

## Próxima Ação

Implementar primeiro em modo simulado/dry-run e validar reconciliação, idempotência e recuperação.
