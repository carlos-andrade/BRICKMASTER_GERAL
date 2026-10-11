---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "FASE_03_GIROSCOPIO_ESTADO_DO_GRAFICO"
id_documento: "BM-CORE-001-ESPECIFICACAO"
titulo: "Contrato técnico — Giroscópio contextual"
status: "ESPECIFICACAO_INICIAL; REGIMES_EXPERIMENTAIS"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Baseline arquitetural BRICKMASTER RAIZ"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase02-03-contracts"
escopo: "Contrato de contexto operacional e localização do preço no gráfico"
objetivo: "Consolidar dados/evidências e explicar a posição operacional sem gerar ordens"
dependencias: "BM-DATA-001; Módulo 001; contratos de estrutura/fluxo"
---

# Contrato técnico — Giroscópio contextual

## Contexto Histórico

O Giroscópio foi concebido para resolver o problema de o operador não saber onde está no gráfico. A baseline exige explicação do contexto, localização do preço relativamente à abertura/estrutura, evidências concordantes/divergentes e motivos de bloqueio. Não se presume que existam classificadores ou limiares validados.

## Estado

ESPECIFICAÇÃO INICIAL — não implementada; estados de regime e limiares permanecem experimentais.

## Contrato

### Entradas obrigatórias
- Instrumento/contrato e tipo de gráfico, identificando explicitamente ticks/60K.
- Sessão e abertura de BM-DATA-001.
- Preço atual, timestamp, proveniência e frescura.
- Referências disponíveis e validadas, incluindo Módulo 001.
- Eventos FVG/estrutura/liquidez/fluxo somente se o produtor tiver contrato e evidência de validação.
- Estado de qualidade, atraso, ausência e contradição por fonte.

### Saídas
- `context_status`: `VALID`, `DEGRADED`, `CONFLICT`, `BLOCKED` ou `UNKNOWN`.
- `operator_location`: localização relativamente à abertura/referência (`ABOVE`, `AT`, `BELOW`, `INSIDE`, `OUTSIDE`, `UNAVAILABLE`).
- Sessão, instrumento, gráfico, timestamp e modo de dados.
- Evidências favoráveis, contrárias, indisponíveis e expiradas com fonte e timestamp.
- `confidence_class`: `HIGH`, `MEDIUM`, `LOW` ou `UNKNOWN`, com razões legíveis; sem score numérico até calibração.
- `block_reasons` com códigos explícitos.

### Precedência de estados
1. `BLOCKED`: identidade/sessão/abertura essencial inválida ou ausente, dados essenciais obsoletos ou contradição que impede determinar localização.
2. `UNKNOWN`: dados insuficientes sem contradição demonstrada; nunca apresentado como válido.
3. `CONFLICT`: fontes atuais e válidas apontam para leituras incompatíveis; expor a divergência, sem peso arbitrário.
4. `DEGRADED`: núcleo válido, mas fontes não essenciais ausentes/atrasadas.
5. `VALID`: identidade, sessão, abertura e preço válidos; fontes usadas atuais e coerentes.

A avaliação deve ser determinística e o bloqueio essencial prevalece sobre qualquer estado favorável.

### Invariantes
- Contexto/localização não é sinal de entrada/saída.
- O risco soberano pode vetar qualquer decisão posterior.
- Dados ausentes, atrasados ou contraditórios reduzem confiança ou bloqueiam.
- Fontes não validadas não podem tornar-se entradas essenciais silenciosamente.
- Histórico, replay e tempo real identificam o modo de dados; equivalência não é presumida.
- Mesmo conjunto de entradas, versão e configuração deve produzir o mesmo estado.
- Ticks, incluindo 60K, são alvo obrigatório de validação.
- Não emitir ordens nem alterar posições.

### Dependências
Obrigatórias: BM-DATA-001 e Módulo 001. Condicionais após validação: BM-FVG-001, BM-STRUCT-001, BM-LIQ-001, BM-FLOW-001, BM-MACRO-001 e BM-REF-001. Consumidores futuros: decisão e risco, com contratos próprios.

### Fora do âmbito
Classificar automaticamente expansão/compressão/exaustão/reversão sem regras objetivas; atribuir pesos estatísticos sem calibração; gerar sinais/ordens.

## Evidências

Baseline arquitetural L2 — Giroscópio; Manual NTSL 4.4 para data/hora de candle; roadmap com risco soberano e execução separados.

## Validação

Revisão estática inicial. Sem testes de transição, replay, backtest, compilação ou observação no Profit.

## Resultado

Contrato mínimo define entradas, saídas, estados de qualidade, precedência e dependências. Classificação de regimes e integração de fontes continuam pendentes.

## Próxima Ação

Implementar e testar primeiro a localização relativa à abertura/referências; adicionar classificadores somente após critérios objetivos e testes.

## Histórico de versões

- 0.1.0 — 2026-10-11 — primeiro contrato conceptual com bloqueios e confiança categórica.
