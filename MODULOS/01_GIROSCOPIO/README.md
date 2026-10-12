<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Giroscópio — Núcleo de Estado
IDENTIFICADOR: BM-001
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

# Giroscópio — Núcleo de Estado do Mercado

**Estado:** DOCUMENTADO — proposta inicial.

## Missão
Produzir uma representação explícita do estado atual do mercado e da posição do operador no gráfico. Não é um “voto da maioria” de indicadores: deve preservar conflito entre evidências e expor incerteza.

## Entradas candidatas
Estado do gráfico, estrutura, FVG, liquidez, VWAP/TWAP, fluxo/volume, volatilidade, IBOV, calendário e qualidade dos dados.

## Saídas
- Regime: tendência, rotação, compressão, expansão, transição ou indeterminado.
- Localização: posição relativa a abertura, VWAP, zonas estruturais e extremos da sessão.
- Confiança calibrável e lista de evidências favoráveis/contrárias.
- Condições de invalidação e módulos indisponíveis.

## Regras
Nenhum score isolado autoriza entrada. Dados stale/ausentes degradam confiança. Correlação entre módulos não pode ser contada como evidência independente sem ajuste.

## Próxima etapa
Definir esquema de estado, normalização e pesos somente após baseline e validação empírica.
