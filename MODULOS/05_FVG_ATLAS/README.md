<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: FVG Atlas
IDENTIFICADOR: BM-005
VERSÃO: 1.0.0
ESTADO: PROPOSTA INICIAL — NÃO VALIDADA EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-11
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-10-11 | v1.0.0 | Estrutura inicial modular e regras de governança.
FONTE DA VERDADE: documentação e código versionados neste repositório.
SHA-256 (conteúdo canónico): 4ed0944a272d694df66d78f7f64a502f6abd1d2c6887bb327a36d3acb49011ae
Commit de referência (versão anterior): https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/057065d4f742f4a329f5bfbe99188b2ddad0db00
-->

# FVG Atlas

## Missão
Detectar e manter inventário de Fair Value Gaps, com tamanho, direção, idade, estado de preenchimento, toques e reação posterior.

## Campos de cada FVG
ID estável; ativo/gráfico; direção; limites; tamanho em pontos e ticks; instante de formação; primeiro toque; preenchimento percentual; estado; invalidação; origem e versão do detector.

## Estados iniciais
ABERTO, TOCADO, PARCIALMENTE_PREENCHIDO, PREENCHIDO, INVALIDADO. Formalizar transições e a diferença entre toque e preenchimento integral.

## Dependências
Definição da barra no gráfico de 60K trades e comportamento da amostragem por negócios; contrato com contador de toques e módulo de liquidez. Ver projeto FVG-ATLAS como fonte auxiliar, sem duplicar decisões sem reconciliação.
