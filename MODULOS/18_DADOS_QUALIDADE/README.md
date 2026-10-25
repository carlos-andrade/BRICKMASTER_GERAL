<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Dados e Qualidade
IDENTIFICADOR: BM-018
VERSÃO: 1.0.0
ESTADO: DOCUMENTADO — NÃO VALIDADO EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-11
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO: 2026-10-11 | v1.0.0 | Documentação inicial.
FONTE DA VERDADE: repositório oficial.
-->

# Dados e Qualidade

## Missão
Garantir proveniência, sincronização, consistência e rastreabilidade dos dados.

## Campos obrigatórios
Instrumento/contrato; fonte; timestamp de evento e recepção; timezone; granularidade; unidade; versão do esquema; transformações; atraso e qualidade.

## Verificações
Lacunas, duplicatas, valores impossíveis, timestamps atrasados, mudança de contrato e divergências entre fontes.

## Fail closed
Dados essenciais reprovados devem reduzir confiança ou bloquear ação; nunca preencher silenciosamente com valores inventados.
