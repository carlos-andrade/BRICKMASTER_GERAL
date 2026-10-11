<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Volatilidade e VIX
IDENTIFICADOR: BM-010
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

# Volatilidade e VIX

## Missão
Adicionar contexto de volatilidade e aversão a risco, separando volatilidade realizada do ativo e VIX como referência externa.

## Cuidados
O VIX refere-se a volatilidade implícita esperada do S&P 500, não é medição direta da volatilidade do WIN/WDO. Validar horário, fuso, defasagem, disponibilidade e relação estatística antes de usar como filtro.
