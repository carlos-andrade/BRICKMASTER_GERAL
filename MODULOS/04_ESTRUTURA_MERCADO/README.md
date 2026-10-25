<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Estrutura de Mercado
IDENTIFICADOR: BM-004
VERSÃO: 1.0.0
ESTADO: PROPOSTA INICIAL — NÃO VALIDADA EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-11
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-10-11 | v1.0.0 | Estrutura inicial modular e regras de governança.
FONTE DA VERDADE: documentação e código versionados neste repositório.
-->

# Estrutura de Mercado

## Missão
Identificar swings, deslocamentos, rompimentos, falhas de rompimento e transições estruturais com regras explícitas.

## Definições a fechar
Confirmação de swing; tolerância por tick; critérios de rompimento; distinção entre evento intrabar e confirmado; tratamento de gaps e sessões.

## Saídas
Evento estrutural, nível, timestamp de confirmação, direção, magnitude e condição de invalidação. Nenhum pivô futuro pode ser retroativamente tratado como conhecido no passado.
