<!--
PROJETO: BRICKMASTER RAIZ
REPOSITORIO: carlos-andrade/BRICKMASTER_GERAL
TIPO_DOCUMENTO: README_INDICADOR_CANDIDATO
FASE: F2_REQUISITOS_E_DESENHO
ID_DOCUMENTO: BM-VOL-ATR-README-001
TITULO: True Range / Average True Range
STATUS: CANDIDATO_DOCUMENTAL_NAO_IMPLEMENTADO
VERSAO: 1.0.0
DATA_CRIACAO: 2026-10-19
DATA_ATUALIZACAO: 2026-10-19
ORIGEM: REGRAS-E-FORMULAS-CALCULO-VOLATILIDADE-B3.md, secao de estimadores
AUTORIDADE_DOCUMENTAL: BRICKMASTER_GERAL e GOVERNANCA
CADEIA_AUTORIDADE: REQUISITOS -> ESPECIFICACAO -> CONTRATO -> IMPLEMENTACAO -> VALIDACAO
RASTREABILIDADE: pasta criada por PR #37; commit de referência da estrutura: 8f69fba6e8abf8fb5db748755705552d92f5d0b9
ESCOPO: Organizar a documentação deste método/indicador de volatilidade
OBJETIVO: Definir requisitos e evidências sem presumir implementação
DEPENDENCIAS: Dados OHLC/retornos adequados ao método; disponibilidade e qualidade por confirmar
SHA-256-CANONICO: PENDENTE_DE_CALCULO_APOS_CONGELAMENTO
COMMIT-DE-REFERENCIA: 8f69fba6e8abf8fb5db748755705552d92f5d0b9
-->
# True Range / Average True Range

## Contexto Histórico

O método está identificado como estimador candidato no documento global de regras e fórmulas de volatilidade B3. Este diretório isola a sua futura especificação, contrato, código e validação, sem duplicar por ora a definição matemática canónica.

## Estado

**CANDIDATO DOCUMENTAL — NÃO IMPLEMENTADO NESTE DIRETÓRIO.** A existência desta pasta não comprova código, cálculo executado, desempenho ou aprovação.

## Fonte canónica

[Regras e fórmulas de cálculo de volatilidade B3](../../REGRAS-E-FORMULAS-CALCULO-VOLATILIDADE-B3.md)

A definição matemática, notação, limitações e estado de candidatura devem ser extraídos da secção relevante desse documento antes de uma implementação. Até essa revisão, não adotar parâmetros, janelas ou thresholds operacionais.

## Contrato a definir

- Instrumento, tipo de gráfico e granularidade.
- Campos de entrada e unidade, origem, timestamps e qualidade.
- Fórmula/algoritmo, janelas e tratamento de lacunas.
- Semântica de saída, estado desconhecido e regras fail-closed.
- Baseline, critérios de aceitação e protocolo anti-look-ahead.
- Dependências e forma de consumo pelo Giroscópio, sempre subordinada ao risco soberano.

## Evidências

Não existem evidências específicas de implementação ou validação neste diretório no momento da criação. Usar apenas dados e relatórios cuja origem e execução sejam verificáveis.

## Validação

Esta alteração cria estrutura documental. Não executa cálculo, teste, backtest, replay, compilação NTSL ou avaliação de rentabilidade.

## Resultado

Diretório individual de organização para o método candidato, sem promoção de estado técnico.

## Próxima Ação

Rever a definição canónica; decidir se o método é necessário para o BRICKMASTER; só depois criar ESPECIFICACAO.md e CONTRATOS.md com fórmulas, dados, critérios mensuráveis e testes.
