<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Gap entre VWAPs e TWAP
IDENTIFICADOR: BM-008
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

# VWAP/TWAP Gap

## Missão
Medir o posicionamento do preço e a divergência entre VWAPs de âncoras distintas e TWAP, preservando diferenças de definição e fonte.

## Não confundir
VWAP pondera preço por volume; TWAP pondera ao longo do tempo conforme implementação. Uma diferença numérica não prova desequilíbrio nem oferece, sozinha, direção de trade.

## Saídas
VWAP por âncora; TWAP; gap absoluto e normalizado; inclinação; preço relativo; janela, sessão, fonte de volume e qualidade dos dados.
