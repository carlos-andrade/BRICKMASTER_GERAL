<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Market DNA
IDENTIFICADOR: BM-003
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

# Market DNA

## Missão
Caracterizar o comportamento do mercado a partir de atributos mensuráveis: expansão/contração, persistência, reversão, eficiência direcional, intensidade de volume e resposta a zonas.

## Saídas
Classe de comportamento, atributos brutos, janela de cálculo, confiança, regime anterior e transição detectada.

## Regra de pesquisa
Definir classes e rótulos antes de otimizar parâmetros. Evitar classificador circular que define o regime usando a mesma variável que depois pretende explicar.
