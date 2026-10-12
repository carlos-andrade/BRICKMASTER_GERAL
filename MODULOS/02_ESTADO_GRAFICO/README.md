<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Estado do Gráfico
IDENTIFICADOR: BM-002
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

# Estado do Gráfico

## Missão
Eliminar a ambiguidade operacional de “onde estou no gráfico”: posição do preço, estrutura próxima, zonas relevantes, distância aos níveis e contexto temporal.

## Saídas mínimas
Preço atual; abertura da sessão; máxima/mínima; localização relativa; distância em pontos e em unidades normalizadas; zonas acima/abaixo; regime e invalidação.

## Cuidados
Definir sessão e fuso explicitamente. Em gráficos atemporais/de ticks, não confundir número de barras com tempo cronológico. A referência +1% é um nível de pesquisa separado, não sinal automático.
