<!--
PROJETO: BRICKMASTER GERAL
MÓDULO: MODULOS/01_GIROSCOPIO
DOCUMENTO: Modelo de inclinação e força corretiva em torno da abertura
IDENTIFICADOR: BM-GIRO-003
VERSÃO: 1.0.0
ESTADO: ESPECIFICAÇÃO CONCEITUAL — MODELO E NTSL AINDA NÃO VALIDADOS
CRIADO EM: 2026-10-17
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
-->

# Modelo de inclinação e força corretiva em torno da abertura

## 1. Hipótese de modelagem

A linha de abertura da sessão é representada como o trilho central do monotrilho. As bandas percentuais definem níveis discretos de inclinação:

- Lado direito/superior: +0,5%, +1%, +2% e +3%.
- Centro: abertura da sessão (0%).
- Lado esquerdo/inferior: −0,5%, −1%, −2% e −3%.

O sinal do desvio determina o lado; a magnitude determina o nível alcançado. Essa é uma metáfora quantitativa para classificar o afastamento do preço, não uma afirmação de que o mercado tenha uma força física restauradora ou de que retornará à abertura.

## 2. Variáveis a estimar

### Inclinação geométrica

Se A for a abertura de sessão e P o preço observado:

- Desvio absoluto: D = P − A.
- Desvio percentual assinado: Dpct = 100 × (P − A) / A.
- Inclinação normalizada: Z = (P − A) / escala, onde escala pode ser ATR ou outra medida de volatilidade validada.
- Nível discreto: banda mais distante alcançada no lado positivo ou negativo.

O desvio percentual responde “quão longe da abertura?”. A normalização por volatilidade responde “quão grande é esse deslocamento em relação ao movimento habitual?”. São medidas diferentes e devem ser preservadas separadamente.

### Velocidade e aceleração do preço

Em barras uniformes, uma aproximação pode ser construída por:

- Velocidade: V = (P[t] − P[t−1]) / duração da barra.
- Aceleração: Acc = V[t] − V[t−1].

Em Renko, as barras não representam durações uniformes; portanto, diferenças entre tijolos não devem ser tratadas como velocidade por unidade de tempo sem usar timestamps e medir o intervalo real.

### Força corretiva — proxy observável, não força física

O mercado não possui um “torque giroscópico” literal. O código pode calcular uma pontuação de evidências de retorno, usando variáveis observáveis, por exemplo:

- redução do afastamento em relação à abertura;
- reversão da variação do preço;
- diminuição da continuidade do movimento de afastamento;
- volume e agressão compatíveis com a resposta, quando disponíveis e validados;
- confirmação de que o preço se deslocou efetivamente na direção central.

Uma pontuação composta deve ser denominada **Índice de Resposta Corretiva (IRC)**, não força institucional real. Os componentes devem ser normalizados, documentados e testados para evitar dupla contagem de evidências correlacionadas.

## 3. Estados sugeridos

1. CENTRO: preço dentro da faixa de ±0,5% da abertura.
2. INCLINAÇÃO LEVE: desvio de 0,5% a menos de 1%.
3. INCLINAÇÃO MODERADA: desvio de 1% a menos de 2%.
4. INCLINAÇÃO FORTE: desvio de 2% a menos de 3%.
5. INCLINAÇÃO EXTREMA: desvio igual ou superior a 3%.
6. RESPOSTA CORRETIVA: o preço começa a reduzir o desvio absoluto.
7. EXPANSÃO: o preço continua a aumentar o desvio absoluto.
8. INDETERMINADO: dados insuficientes ou conflitantes.

Os limiares são categorias descritivas iniciais, não probabilidades de reversão. Uma banda tocada não implica que a banda seguinte será atingida nem que ocorrerá retorno ao centro.

## 4. O que o indicador deve demonstrar

- Abertura e oito bandas percentuais.
- Desvio assinado e percentual atual.
- Maior nível positivo e negativo atingido na sessão.
- Desvio máximo da sessão em cada direção.
- Variação do desvio entre barras e redução/aumento do afastamento.
- Estado atual (centro, inclinação, expansão, resposta corretiva ou indeterminado).
- IRC separado das métricas geométricas.
- Dados indisponíveis e limitações da estimativa.

## 5. Requisitos para implementação NTSL

A implementação deve ser incremental:

- **Etapa A — Geometria:** calcular abertura, bandas, desvio percentual e nível discreto.
- **Etapa B — Dinâmica:** medir variação do desvio e extremos de sessão, com tratamento específico para gráficos temporais e Renko.
- **Etapa C — Resposta:** identificar redução do afastamento sem antecipar reversão antes de o preço demonstrá-la.
- **Etapa D — Fluxo:** integrar delta/agressão real apenas quando as funções e fontes forem confirmadas para a versão do Profit.
- **Etapa E — Avaliação:** backtest/replay, custos, slippage, comportamento por ativo e teste fora da amostra.

O código NTSL deve começar como indicador visual e analítico, não como robô de execução automática. A estratégia não deve abrir posições só porque uma banda foi tocada.

## 6. Limitações e validação

- A abertura diária deve ser confirmada para o ativo, horário de sessão e tipo de gráfico.
- As bandas percentuais podem ser pouco relevantes para instrumentos com escalas e volatilidades diferentes; avaliar também normalização por ATR.
- Um movimento de retorno pode ser ruído ou pausa, não absorção.
- Volume agregado não revela, sozinho, a intenção de compradores ou vendedores.
- Não inferir VIX a partir de ATR; são medidas distintas.
- Não declarar o modelo preditivo antes de definir rótulos, métricas e validação fora da amostra.
- Não alegar rentabilidade garantida.

## 7. Critérios de aceitação

- Fórmulas conferidas com valores de teste conhecidos.
- Nove linhas visualmente corretas e ancoradas à sessão esperada.
- Níveis e extremos atualizados sem reinicializações indevidas.
- Separação clara entre medida de deslocamento e proxy de resposta corretiva.
- Compilação documentada na versão real do Profit.
- Testes em replay e fora da amostra com resultados registrados.
- Revisão de falsos sinais, custos, slippage e sensibilidade a regime.

## 8. Próxima etapa

Construir primeiro o indicador NTSL de geometria e dinâmica, sem ordens: desvio percentual, nível de inclinação, extremos da sessão e variação do afastamento. Depois, desenvolver o Índice de Resposta Corretiva como camada separada, com componentes explícitos e avaliação empírica.

## Histórico

- 2026-10-17 | v1.0.0 | Especificação inicial do modelo de inclinação, níveis e resposta corretiva.
