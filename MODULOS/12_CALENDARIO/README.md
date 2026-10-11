<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Calendário Econômico
IDENTIFICADOR: BM-012
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

# Calendário Econômico

## Missão
Classificar janelas de risco de eventos (por exemplo, inflação, emprego, decisões de juros e comunicados do Banco Central) e aplicar regras explícitas de cautela/bloqueio.

## Campos
Evento; fonte; horário local e UTC; país/moeda; impacto esperado conforme fonte; horário de publicação efetiva; revisão; janela pré/pós-evento.

## Regra
Não usar horário previsto como se fosse publicação confirmada. Se calendário estiver indisponível ou desatualizado, sinalizar incerteza.
