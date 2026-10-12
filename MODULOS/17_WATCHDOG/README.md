<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Watchdog e Observabilidade
IDENTIFICADOR: BM-017
VERSÃO: 1.0.0
ESTADO: DOCUMENTADO — NÃO VALIDADO EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-11
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO: 2026-10-11 | v1.0.0 | Documentação inicial.
FONTE DA VERDADE: repositório oficial.
-->

# Watchdog e Observabilidade

## Missão
Monitorar saúde do feed, atualização de preço, latência, erros, posição e reconciliação de ordens.

## Alertas mínimos
Feed congelado; timestamps fora de ordem; dado stale; desconexão; divergência de posição; erro de execução; limite de risco atingido; calendário indisponível.

## Segurança
Definir mecanismo de interrupção e estado independente. Alertar não equivale a corrigir automaticamente. Registrar eventos com timestamp e evidência.
