<!--
PROJETO: BRICKMASTER GERAL
DOCUMENTO: BRICKMASTER GIROSCOPIO — MONOTRILHO E BANDAS DE ABERTURA
IDENTIFICADOR: BM-GIRO-002
VERSAO: 1.0.0
ESTADO: RASCUNHO TECNICO — NTSL NAO VALIDADO EM COMPILACAO
CRIADO EM: 2026-10-17
RESPONSAVEL: Carlos Andrade
REPOSITORIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
MODULO: MODULOS/01_GIROSCOPIO
HISTORICO:
- 2026-10-17 | v1.0.0 | Registo da concepcao, especificacao visual e prototipo NTSL.
FONTE DA VERDADE: documentos e codigo versionados neste repositorio.
-->

# BRICKMASTER GIROSCOPIO — Monotrilho, abertura e bandas percentuais

**Identificador:** BM-GIRO-002  
**Versão:** 1.0.0  
**Estado:** Rascunho técnico. O código não foi compilado nem validado no Profit nesta etapa.  
**Tipo de artefato de código:** indicador visual, não estratégia de execução.

## 1. Objetivo

Traduzir o princípio de estabilidade ativa ilustrado pelo monotrilho giroscópico de Louis Brennan para uma arquitetura de observação do mercado BRICKMASTER.

A abertura da sessão é a referência geométrica central. O mapa exibe quatro níveis percentuais acima e quatro abaixo. O conceito de “giroscópio” é uma metáfora de engenharia para um módulo que observa deslocamento, velocidade, resposta do preço e evidências de fluxo; não significa que um mecanismo físico governe o mercado.

## 2. Princípio físico e analogia com o mercado

O monotrilho de Brennan empregava rotores giroscópicos e mecanismos de controle para estabilizar um veículo sobre um único trilho. O momento angular de um rotor pode ser representado por:

\[
L = I \omega
\]

em que \(L\) é o momento angular, \(I\) o momento de inércia e \(\omega\) a velocidade angular.

A analogia de mercado deve ser tratada com rigor: o preço não obedece às leis de um giroscópio. A aplicação útil é arquitetural — observar o desvio em relação a uma referência, identificar evidências de resposta/continuidade e aplicar regras explícitas de risco e invalidação.

| Conceito de engenharia | Analogia de análise de mercado |
|---|---|
| Inclinação do veículo | Afastamento do preço em relação à abertura |
| Sensor de inclinação | Métrica de deslocamento e velocidade do preço |
| Rotor e momento angular | Capacidade de resposta do sistema; não corresponde literalmente ao volume |
| Torque corretivo | Resposta do preço após o movimento |
| Controle de malha fechada | Processo de observar, decidir, executar e verificar |
| Falha de estabilidade | Invalidação do cenário e aplicação de regras de risco |

**Limite da analogia:** volume alto não prova absorção institucional; delta estimado pelo sinal do candle não é delta real de agressão; ATR crescente não é o VIX. Essas variáveis não devem ser apresentadas como equivalentes.

## 3. Geometria BRICKMASTER

Seja \(A\) o preço de abertura definido para a sessão e o ativo em questão. As linhas são calculadas sobre essa referência:

| Linha | Fórmula | Multiplicador |
|---|---:|---:|
| Superior +0,5% | \(A \times 1,005\) | 1,005 |
| Superior +1% | \(A \times 1,010\) | 1,010 |
| Superior +2% | \(A \times 1,020\) | 1,020 |
| Superior +3% | \(A \times 1,030\) | 1,030 |
| Abertura | \(A\) | 1,000 |
| Inferior −0,5% | \(A \times 0,995\) | 0,995 |
| Inferior −1% | \(A \times 0,990\) | 0,990 |
| Inferior −2% | \(A \times 0,980\) | 0,980 |
| Inferior −3% | \(A \times 0,970\) | 0,970 |

A linha de abertura e as oito bandas formam **nove linhas no total**. Confirmar a definição da sessão (horário, instrumento e tratamento de sessões estendidas) antes de usar o indicador operacionalmente. Em futuros e gráficos Renko, validar também como a plataforma disponibiliza a abertura diária do ativo.

## 4. Prototipo NTSL — indicador visual

O código abaixo é uma **versão candidata para validação no Editor de Estratégias**. Não foi possível confirmar a compilação nesta etapa. Confirmar a disponibilidade e a semântica de `OpenD(0)`, `Plot` a `Plot9`, `RGB`, `SetPlotColor`, `SetPlotStyle` e `SetPlotWidth` na versão instalada do Profit antes de marcar o módulo como validado.

Arquivo sugerido: `BRICKMASTER_GIROSCOPE_V1.pas` (ou nome/extensão adotado pelo fluxo de estratégias do projeto). No Profit, usar a extensão/formato aceito pelo Editor de Estratégias.

```pascal
{
  BRICKMASTER_GIROSCOPE_V1
  Tipo: indicador visual NTSL - prototipo para compilacao
  Referencia: abertura diaria da sessao
  Bandas: +/- 0.5%, 1%, 2% e 3%
  Nao envia ordens.
}

var
  abertura : Float;
  sup05    : Float;
  sup1     : Float;
  sup2     : Float;
  sup3     : Float;
  inf05    : Float;
  inf1     : Float;
  inf2     : Float;
  inf3     : Float;

begin

  // Referencia central: validar OpenD(0) no ativo/grafico escolhido.
  abertura := OpenD(0);

  // Bandas superiores
  sup05 := abertura * 1.005;
  sup1  := abertura * 1.010;
  sup2  := abertura * 1.020;
  sup3  := abertura * 1.030;

  // Bandas inferiores
  inf05 := abertura * 0.995;
  inf1  := abertura * 0.990;
  inf2  := abertura * 0.980;
  inf3  := abertura * 0.970;

  // Nove linhas: abertura + quatro superiores + quatro inferiores
  Plot(abertura);
  Plot2(sup05);
  Plot3(sup1);
  Plot4(sup2);
  Plot5(sup3);
  Plot6(inf05);
  Plot7(inf1);
  Plot8(inf2);
  Plot9(inf3);

  // Cores - confirmar constantes/funcoes na versao do Profit.
  SetPlotColor(1, clWhite);
  SetPlotColor(2, clYellow);
  SetPlotColor(3, RGB(255, 165, 0));
  SetPlotColor(4, clRed);
  SetPlotColor(5, RGB(180, 40, 40));
  SetPlotColor(6, clYellow);
  SetPlotColor(7, RGB(0, 200, 100));
  SetPlotColor(8, clGreen);
  SetPlotColor(9, RGB(0, 100, 60));

  // Estilos - confirmar mapeamento de estilos na documentacao instalada.
  SetPlotStyle(1, 0);
  SetPlotStyle(2, 2);
  SetPlotStyle(3, 2);
  SetPlotStyle(4, 1);
  SetPlotStyle(5, 1);
  SetPlotStyle(6, 2);
  SetPlotStyle(7, 2);
  SetPlotStyle(8, 1);
  SetPlotStyle(9, 1);

  SetPlotWidth(1, 3);

end;
```

### 4.1 Condições de aceitação do indicador

- Compilar sem erros no Editor de Estratégias do Profit instalado.
- Confirmar que a abertura permanece estável durante a sessão e reinicia na sessão prevista.
- Confirmar as nove linhas com a fórmula percentual correta em pelo menos dois ativos e dois tipos de gráfico relevantes.
- Verificar se cores e estilos correspondem ao esperado.
- Testar mudanças de sessão, histórico carregado, replay e períodos sem negociação.
- Registrar versão do Profit, ativo, tipo de gráfico, horário da sessão e evidência visual do teste.
- Não declarar validado com base apenas na leitura estática deste documento.

## 5. Interpretador de estado — proposta, não implementação validada

As bandas definem localização. A classificação de estado é uma camada posterior e não deve ser confundida com sinal de entrada.

| Observação | Estado candidato | Evidência necessária |
|---|---|---|
| Preço entre −0,5% e +0,5% | Próximo da abertura | Localização confirmada |
| Preço alcança uma banda externa | Afastamento | Toque/rompimento e distância |
| Rompimento com progresso persistente | Expansão direcional possível | Continuidade do preço e contexto |
| Fluxo elevado sem progresso proporcional | Candidato a absorção | Agressão confiável, volume e resposta do preço |
| Preço retorna para dentro da banda | Reentrada na região anterior | Fechamento/condição de retorno claramente definida |
| Preço regressa à abertura | Reaproximação da referência | Chegada observada; não implica reversão concluída |

Nenhuma condição isolada autoriza entrada. A classificação de absorção exige dados de fluxo adequados; volume agregado sozinho não revela quem absorveu nem a intenção de um participante.

## 6. Arquitetura proposta para as próximas versões

1. **V1 — Mapa:** calcular e desenhar as nove linhas da sessão.
2. **V2 — Estado de preço:** medir distância normalizada, velocidade, permanência, rompimento e retorno às bandas.
3. **V3 — Fluxo:** integrar delta real/agressão e volume financeiro somente por funções ou fontes cuja semântica esteja documentada.
4. **V4 — Contexto:** integrar VWAP/TWAP, volatilidade, calendário e referência intermercado em módulos separados e com degradação explícita quando os dados estiverem indisponíveis.
5. **V5 — Execução:** somente depois de especificar regras de entrada/saída, stops, exposição, limites de perda, custos e testes fora da amostra.

O núcleo original do BRICKMASTER — baseado na AVGPRICE e na lógica dos tijolos Renko definida no projeto — não deve ser substituído por este módulo de contexto sem decisão formal e teste comparativo.

## 7. Prompt para gerar a imagem conceitual

**Prompt:**

> Criar um infográfico cinematográfico técnico, em português, sobre “MONOTRILHO COM GIROSCÓPIO — BRICKMASTER”. Composição horizontal 16:9, fundo escuro industrial, visual de engenharia de alta qualidade. Na metade superior, representar um monotrilho histórico inspirado nos experimentos de Louis Brennan, equilibrado sobre um único trilho, com rotor giroscópico em corte técnico e setas que expliquem inclinação, momento angular e correção ativa. Não afirmar que existe um único rotor se a composição mostrar dois; manter a mecânica coerente e evitar rótulos ilegíveis.
>
> Na metade inferior, representar um gráfico de mercado com candles e nove linhas horizontais: abertura central branca, bandas superiores +0,5%, +1%, +2%, +3% e inferiores −0,5%, −1%, −2%, −3%. Destacar a abertura como referência geométrica. Acrescentar um módulo central identificado como “GIROSCÓPIO DE MERCADO” com as etapas “MEDIR DESLOCAMENTO”, “AVALIAR RESPOSTA”, “CONFIRMAR FLUXO” e “APLICAR CONTROLO DE RISCO”. Mostrar uma sequência de expansão e retorno como exemplo didático, sem sugerir lucro garantido. Tipografia legível, rótulos curtos, hierarquia visual clara, estética de blueprint misturada com renderização 3D fotorealista e gráficos financeiros precisos.
>
> Evitar texto miúdo, linhas percentuais duplicadas, bandas incorretas, alegações de rentabilidade garantida e afirmações de que volume sozinho prova absorção.

## 8. Estado e auditoria

**Estado atual: DOCUMENTADO; IMPLEMENTAÇÃO NÃO VALIDADA.**

Esta especificação regista a ideia e o protótipo. Ela não afirma que o código compila, que as bandas são exibidas corretamente no Profit ou que a lógica tem rentabilidade demonstrada.

Próxima ação de validação: compilar no Profit instalado, corrigir as incompatibilidades da versão da NTSL, testar a abertura da sessão e anexar evidências reproduzíveis antes de promover o estado deste documento.
