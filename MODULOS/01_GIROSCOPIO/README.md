<!--
PROJETO: BRICKMASTER GERAL
DOCUMENTO: Giroscópio — Núcleo de Estado do Mercado
IDENTIFICADOR: BM-001
VERSÃO: 1.1.0
ESTADO: DOCUMENTADO — PROPOSTA EM EVOLUÇÃO; NÃO VALIDADA EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-17
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
DIRETÓRIO: MODULOS/01_GIROSCOPIO
HISTÓRICO:
- 2026-10-11 | v1.0.0 | Estrutura inicial modular e regras de governança.
- 2026-10-17 | v1.1.0 | Adicionadas referência de abertura e bandas percentuais, analogia de monotrilho, artefatos associados, regra de persistência e estado de validação.
FONTE DA VERDADE: documentação e código versionados neste repositório.
-->

# Giroscópio — Núcleo de Estado do Mercado

**Identificador:** BM-001  
**Versão:** 1.1.0  
**Estado:** DOCUMENTADO — proposta em evolução; não validada em produção.  
**Última revisão:** 2026-10-17

## 1. Missão

Produzir uma representação explícita do estado do mercado e da posição do operador no gráfico. O Giroscópio não deve ser um “voto da maioria” de indicadores: deve preservar conflitos entre evidências, expor incerteza, listar condições de invalidação e degradar a confiança quando existirem dados ausentes ou desatualizados.

O módulo atua como camada de contexto e leitura de estado. Não substitui automaticamente a lógica central já definida para o BRICKMASTER — incluindo a utilização de AVGPRICE e as regras dos tijolos Renko — sem decisão formal, teste comparativo e validação.

## 2. Conceito de engenharia

O nome “Giroscópio” inspira-se no princípio de controle ativo de estabilidade associado ao monotrilho de Louis Brennan: observar um desvio, medir a resposta do sistema e aplicar controle com realimentação.

No mercado, isso é uma **analogia de arquitetura**, não uma equivalência física. O preço não obedece às leis de um giroscópio. O módulo deve observar localização, deslocamento, continuidade, resposta do preço e evidências independentes de fluxo; nenhuma dessas variáveis, isoladamente, prova absorção ou garante uma reversão.

## 3. Referência de abertura e bandas percentuais

Um dos contextos visuais propostos é a abertura da sessão. Definindo A como o preço de abertura validado para o ativo e para a sessão pretendida, o mapa contém nove linhas:

| Referência | Fórmula |
|---|---:|
| +3% | A × 1,030 |
| +2% | A × 1,020 |
| +1% | A × 1,010 |
| +0,5% | A × 1,005 |
| Abertura | A |
| −0,5% | A × 0,995 |
| −1% | A × 0,990 |
| −2% | A × 0,980 |
| −3% | A × 0,970 |

Essas linhas definem localização e afastamento; não são sinais de compra ou venda por si só. Antes de uso operacional, é necessário confirmar a semântica da abertura diária na versão do Profit, o horário da sessão, o comportamento em gráficos Renko e a correção visual das nove linhas.

### Artefato detalhado

- [Especificação, protótipo NTSL e prompt visual do monotrilho com bandas](./BRICKMASTER_GIROSCOPE_MONOTRILHO_BANDAS_ABERTURA.md)

O documento detalhado identifica explicitamente o código NTSL como protótipo não compilado nem validado nesta etapa.

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
- **Evidências:** fatores favoráveis, contrários, ausentes e potencialmente correlacionados.
- **Confiança:** calibrável somente após definição de baseline e validação empírica.
- **Invalidação:** condições que contradizem a classificação atual.
- **Qualidade:** dados stale/ausentes, módulo indisponível ou fonte não validada.
- **Estado de execução:** separado da leitura analítica; um estado do mercado não envia ordem automaticamente.

## 6. Regras de decisão e segurança

1. Nenhum score isolado autoriza entrada.
2. Dados ausentes, desatualizados ou inválidos devem reduzir a confiança ou bloquear a saída dependente deles.
3. Correlação entre módulos não pode ser contabilizada como evidência independente sem ajuste.
4. Volume agregado não comprova, sozinho, absorção institucional.
5. Rompimento, toque de banda e retorno à abertura são observações, não garantias de continuidade ou reversão.
6. A estratégia de execução exige regras próprias de risco, limites de exposição, stops, custos, tratamento de falhas e validação em replay/backtest antes de qualquer uso real.
7. O núcleo existente do BRICKMASTER não deve ser alterado implicitamente por este módulo de contexto.

## 7. Roadmap

| Fase | Objetivo | Estado |
|---|---|---|
| G1 — Referência visual | Especificar abertura e oito bandas percentuais | Documentado; protótipo pendente de compilação e teste visual |
| G2 — Estado de preço | Medir distância, velocidade, permanência, expansão e retorno | Planejado |
| G3 — Fluxo | Integrar agressão/delta confiável e volume com semântica verificada | Planejado |
| G4 — Contexto | Integrar VWAP/TWAP, volatilidade, calendário, intermercado e qualidade de dados | Planejado |
| G5 — Validação | Testes de sessão, replay, custos, risco e fora da amostra | Pendente |

### Critérios mínimos para declarar G1 validada

- Compilar no Editor de Estratégias da versão de Profit em uso.
- Confirmar a referência de abertura correta para o ativo e sessão.
- Confirmar a geometria e os valores das nove linhas.
- Testar histórico, sessões consecutivas, replay e gráfico Renko relevante.
- Registrar versão, instrumento, configuração, resultados e evidências verificáveis.

## 8. Persistência e governança

Todos os artefatos produzidos para esta linha de trabalho do Giroscópio devem ser persistidos em:

- [Diretório oficial do módulo](https://github.com/carlos-andrade/BRICKMASTER_GERAL/tree/main/MODULOS/01_GIROSCOPIO)
- [Regra de persistência de artefatos](./REGRA_PERSISTENCIA_ARTEFATOS.md)

Procedimento obrigatório: consultar os arquivos existentes, respeitar a nomenclatura e a governança, gravar por commit descritivo, verificar o conteúdo no GitHub e relatar com precisão o estado real. Se a gravação falhar, informar que o material não foi persistido. Não declarar código compilado ou sistema validado sem evidência.

## 9. Inventário do módulo

- README.md — índice, missão, arquitetura, roadmap e estado do módulo.
- BRICKMASTER_GIROSCOPE_MONOTRILHO_BANDAS_ABERTURA.md — conceito, fórmulas das bandas, protótipo NTSL, prompt visual, critérios de aceitação e fases futuras.
- REGRA_PERSISTENCIA_ARTEFATOS.md — procedimento obrigatório de persistência/versionamento.

## 10. Próxima etapa

Validar o protótipo de abertura no Profit instalado. Corrigir eventuais incompatibilidades da NTSL e anexar evidências reproduzíveis antes de atualizar o estado de G1. Só depois avançar para a classificação dinâmica do preço e a integração de fluxo.