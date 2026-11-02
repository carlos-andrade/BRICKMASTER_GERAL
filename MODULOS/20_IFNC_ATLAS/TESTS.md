<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: IFNC ATLAS — Plano de Testes
IDENTIFICADOR: BM-020-TESTS
VERSÃO: 0.1.0
ESTADO: PLANEADO — NÃO EXECUTADO
CRIADO EM: 2026-11-02
ÚLTIMA REVISÃO: 2026-11-02
SHA-256: ver CHECKSUMS.sha256 (SHA-256 do conteúdo integral)
COMMIT DE REFERÊNCIA: 4f5b5ad608fd045e6b5d48d8603239264843e719
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-11-02 | v0.1.0 | Plano de testes inicial.
FONTE DA VERDADE: repositório oficial.
-->

# TESTS — IFNC ATLAS

## 1. Estado
Nenhum teste foi executado neste checkpoint. Todos os itens abaixo são casos planeados.

## 2. Testes unitários
- Retorno simples e log-retorno em séries sintéticas conhecidas.
- Força relativa: IFNC supera, iguala e fica abaixo do IBOV.
- Divergência com retornos positivos, negativos e mistos.
- Breadth: todos sobem, todos caem, empate, universo vazio.
- Participação ponderada: pesos normalizados, peso ausente e carteira incompleta.
- Dispersão e volatilidade relativa; tratamento de denominador zero.
- Estados: STRONG, WEAK, MIXED, NEUTRAL, DEGRADED e BLOCKED.
- Confidence limitada a [0,1]; falha crítica força bloqueio.

## 3. Testes de dados e qualidade
- Duplicidade de eventos.
- Eventos fora de ordem.
- Timestamp sem timezone.
- Defasagem IFNC/IBOV/WIN.
- Buracos de sessão, leilão e horário especial.
- Fonte atrasada, congelada ou indisponível.
- Mudança de ticker e contrato WIN.
- Carteira sem vigência ou publicada após o instante de decisão.
- Peso total fora da tolerância definida pela metodologia.

## 4. Testes anti-look-ahead e histórico
- Replay ponto-a-ponto: feature no instante t só usa eventos disponíveis até t.
- Simular revisão de dado publicada após t: não pode alterar decisão histórica original.
- Simular alteração de carteira: carteira futura não pode contaminar observações anteriores.
- Reproduzir resultado com mesma versão, dados e parâmetros.
- Verificar append-only e trilha de correção.
- Testar rolagem WIN sem concatenar contratos de forma silenciosa.

## 5. Testes de integração
- BM-018 fornece qualidade e proveniência.
- BM-011 fornece IBOV com relógio compatível.
- BM-020 publica contexto ao BM-001.
- BM-001 preserva divergência entre IFNC, IBOV, fluxo e estrutura.
- BM-014 não recebe autorização de ordem do IFNC.
- BM-017 detecta heartbeat perdido e dados stale.
- BM-016 reproduz o mesmo estado no replay.

## 6. Pesquisa estatística
Protocolo pré-registado:
- Alvos: retornos futuros do IBOV e WIN em 5m, 30m e diário.
- Benchmarks: persistência/retorno passado, IBOV isolado, features existentes sem IFNC.
- Modelos: baseline linear regularizado e modelos simples interpretáveis antes de modelos complexos.
- Divisão temporal: treino, validação e teste fora da amostra; walk-forward.
- Purge/embargo quando horizontes e rótulos se sobrepõem.
- Métricas: IC, MAE/RMSE quando regressão; AUC/Brier apenas quando classificação probabilística; estabilidade por regime; turnover e custo quando convertido em regra.
- Controlo de múltiplos testes e reporte de intervalos de confiança.
- Custos, slippage, spread, latência e horários de leilão no teste de estratégia.
- Reportar incrementalidade contra benchmark e não somente resultado bruto.
- Testar períodos de stress, baixa liquidez, eventos macro e mudanças de composição.

## 7. Critérios de aceite
A. Dados: proveniência e sincronização auditáveis; sem lacunas críticas silenciosas.
B. Histórico: snapshots de carteira e revisões reproduzíveis.
C. Matemática: testes unitários passam e fórmulas documentadas.
D. Temporalidade: zero look-ahead nos testes automatizados.
E. Integração: Giroscópio recebe estado, confiança e invalidações; nenhum caminho para execução.
F. Pesquisa: só declarar informação incremental se superar benchmarks fora da amostra com robustez e custos realistas.
G. Produção: exige gates de risco e aprovação independente; fora do escopo desta versão.

## 8. Evidência exigida
Cada execução deve guardar commit, hash do dataset, parâmetros, versão do código, intervalo temporal, logs, resultado, falhas e relatório. Não declarar PASS sem artefato verificável.
