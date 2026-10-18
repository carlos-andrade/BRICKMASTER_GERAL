<!--
PROJETO: BRICKMASTER GERAL
DOCUMENTO: Giroscópio — Núcleo de Estado do Mercado
IDENTIFICADOR: BM-001
VERSÃO: 1.2.0
ESTADO: DOCUMENTADO — PROPOSTA EM EVOLUÇÃO; NÃO VALIDADA EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-17
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
DIRETÓRIO: MODULOS/01_GIROSCOPIO
HISTÓRICO:
- 2026-10-11 | v1.0.0 | Estrutura inicial modular e regras de governança.
- 2026-10-17 | v1.1.0 | Referência de abertura e bandas percentuais, analogia do monotrilho e regra de persistência.
- 2026-10-17 | v1.2.0 | Modelo formal de inclinação, níveis discretos, métricas dinâmicas e Índice de Resposta Corretiva (IRC) como proposta.
FONTE DA VERDADE: documentação e código versionados neste repositório.
SHA-256 (conteúdo canónico): 7e609c0cb892546fe652dc3956c1cb4992b2573067a44f34aba22c4d1ceb6688
Commit de referência (versão anterior): https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/057065d4f742f4a329f5bfbe99188b2ddad0db00
-->

# Giroscópio — Núcleo de Estado do Mercado

**Identificador:** BM-001  
**Versão:** 1.2.0  
**Estado:** DOCUMENTADO — proposta em evolução; não validada em produção.  
**Última revisão:** 2026-10-17

## 1. Missão

Produzir uma representação explícita do estado do mercado e da posição do operador no gráfico. O Giroscópio não deve ser um “voto da maioria” de indicadores: deve preservar conflitos entre evidências, expor incerteza, listar condições de invalidação e degradar a confiança quando existirem dados ausentes ou desatualizados.

O módulo atua como camada de contexto e leitura de estado. Não substitui automaticamente a lógica central já definida para o BRICKMASTER — incluindo a utilização de AVGPRICE e a configuração do gráfico de 60K trades — sem decisão formal, teste comparativo e validação.

## 2. Conceito de engenharia

O nome “Giroscópio” inspira-se no princípio de controle ativo de estabilidade associado ao monotrilho de Louis Brennan: observar um desvio, medir a resposta do sistema e aplicar controle com realimentação.

No mercado, isso é uma **analogia de arquitetura**, não uma equivalência física. O preço não obedece às leis de um giroscópio. O módulo deve observar localização, deslocamento, continuidade, resposta do preço e evidências independentes de fluxo; nenhuma dessas variáveis, isoladamente, prova absorção ou garante uma reversão.

## 3. Referência central e níveis de inclinação

A abertura da sessão é tratada como o trilho central. As quatro bandas superiores (+0,5%, +1%, +2%, +3%) representam níveis de inclinação de um lado; as quatro inferiores (−0,5%, −1%, −2%, −3%) representam o lado oposto. O mapa possui nove linhas no total, incluindo a abertura.

Definindo A como o preço de abertura validado para o ativo e para a sessão, e P como o preço observado:

- Desvio absoluto: D = P − A.
- Desvio percentual assinado: Dpct = 100 × (P − A) / A.
- Escala normalizada candidata: Z = (P − A) / ATR, se a série e o ATR estiverem adequados ao gráfico.
- Nível discreto: maior banda positiva ou negativa alcançada.

O desvio percentual descreve o afastamento em relação à abertura; a normalização por volatilidade descreve o afastamento relativo ao movimento típico. São medidas diferentes.

### Artefatos detalhados

- [Especificação do monotrilho, bandas percentuais, protótipo NTSL e prompt visual](./BRICKMASTER_GIROSCOPE_MONOTRILHO_BANDAS_ABERTURA.md)
- [Modelo de inclinação, dinâmica e força corretiva](./MODELO_INCLINACAO_FORCA_RETORNO_ABERTURA.md)

O segundo documento propõe medir velocidade, aceleração e um **Índice de Resposta Corretiva (IRC)**. O IRC será uma pontuação de evidências observáveis de retorno, não uma força física nem uma medida direta de intenção institucional.

## 4. Entradas candidatas

- Estado do gráfico e estrutura de preço;
- abertura da sessão e bandas percentuais;
- FVG e liquidez;
- VWAP/TWAP;
- fluxo e volume;
- volatilidade;
- contexto intermercado, incluindo IBOV quando a fonte estiver disponível e for apropriada;
- calendário econômico;
- qualidade, atualização e disponibilidade dos dados.

Cada entrada deve ter origem, temporalidade, momento de atualização e estado de qualidade documentados. Proxies não devem ser rotulados como dados reais: por exemplo, ATR não é VIX e um delta estimado pelo corpo do candle não é delta real de agressão.

## 5. Saídas do Giroscópio

- **Regime:** tendência, rotação, compressão, expansão, transição ou indeterminado.
- **Localização:** posição relativa à abertura, bandas, VWAP, zonas estruturais e extremos da sessão.
- **Inclinação:** desvio absoluto, desvio percentual assinado, nível discreto e extremos de sessão.
- **Dinâmica:** variação do desvio e, quando o tipo de gráfico permitir, velocidade e aceleração estimadas.
- **Resposta corretiva:** IRC com componentes explícitos, normalizados e testados; não equivale a torque físico.
- **Evidências:** fatores favoráveis, contrários, ausentes e potencialmente correlacionados.
- **Invalidação e qualidade:** condições que contradizem a classificação, dados stale/ausentes e módulos indisponíveis.
- **Estado de execução:** separado da leitura analítica; um estado do mercado não envia ordem automaticamente.

## 6. Regras de decisão e segurança

1. Nenhum score isolado autoriza entrada.
2. Dados ausentes, desatualizados ou inválidos devem reduzir a confiança ou bloquear a saída dependente deles.
3. Correlação entre módulos não pode ser contabilizada como evidência independente sem ajuste.
4. Volume agregado não comprova, sozinho, absorção institucional.
5. Rompimento, toque de banda e retorno à abertura são observações, não garantias de continuidade ou reversão.
6. No gráfico de 60K trades, a duração de cada barra pode variar conforme a atividade de mercado: não tratar variação por barra como velocidade por unidade de tempo sem timestamps e duração temporal real.
7. A estratégia de execução exige regras próprias de risco, limites de exposição, stops, custos, tratamento de falhas e validação em replay/backtest antes de qualquer uso real.
8. O núcleo existente do BRICKMASTER não deve ser alterado implicitamente por este módulo de contexto.

## 7. Roadmap

| Fase | Objetivo | Estado |
|---|---|---|
| G1 — Referência visual | Abertura e oito bandas percentuais | Documentado; protótipo pendente de compilação e teste visual |
| G2 — Inclinação dinâmica | Desvio assinado, níveis, extremos e variação do afastamento | Especificado; implementação pendente |
| G3 — Resposta corretiva | Definir e testar componentes do IRC sem dupla contagem | Especificado conceitualmente; implementação pendente |
| G4 — Fluxo e contexto | Agressão/delta confiável, VWAP/TWAP, volatilidade, calendário, intermercado e qualidade | Planejado |
| G5 — Validação | Compilação, replay, custos, risco e teste fora da amostra | Pendente |

### Critérios mínimos de aceitação

- Compilar no Editor de Estratégias da versão de Profit em uso.
- Confirmar a referência de abertura correta para o ativo e sessão.
- Confirmar a geometria e os valores das nove linhas.
- Testar histórico, sessões consecutivas, replay e gráfico de 60K trades.
- Validar extremos, estados e reinicialização por sessão.
- Definir rótulos, métricas e baseline antes de afirmar capacidade preditiva.
- Registrar versão, instrumento, configuração, resultados e evidências verificáveis.

## 8. Persistência e governança

Todos os artefatos produzidos para esta linha de trabalho do Giroscópio devem ser persistidos em:

- [Diretório oficial do módulo](https://github.com/carlos-andrade/BRICKMASTER_GERAL/tree/main/MODULOS/01_GIROSCOPIO)
- [Regra de persistência de artefatos](./REGRA_PERSISTENCIA_ARTEFATOS.md)

Procedimento obrigatório: consultar os arquivos existentes, respeitar a nomenclatura e a governança, gravar por commit descritivo, verificar o conteúdo no GitHub e relatar com precisão o estado real. Se a gravação falhar, informar que o material não foi persistido. Não declarar código compilado ou sistema validado sem evidência.

## 9. Inventário do módulo

- README.md — índice, arquitetura, roadmap e estado.
- BRICKMASTER_GIROSCOPE_MONOTRILHO_BANDAS_ABERTURA.md — conceito, bandas, protótipo NTSL e prompt visual.
- MODELO_INCLINACAO_FORCA_RETORNO_ABERTURA.md — variáveis de inclinação, estados, IRC e requisitos de implementação.
- REGRA_PERSISTENCIA_ARTEFATOS.md — persistência, versionamento e verificação.

## 10. Próxima etapa

Implementar primeiro o indicador NTSL de geometria e dinâmica, sem ordens: desvio percentual, nível de inclinação, extremos da sessão e variação do afastamento. Compilar e validar no Profit. Só depois implementar o IRC e integrar dados de fluxo com semântica confirmada.