<!--
PROJETO: BRICKMASTER RAIZ
REPOSITORIO: carlos-andrade/BRICKMASTER_GERAL
TIPO_DOCUMENTO: README_INDICADOR
FASE: ORGANIZACAO_DOCUMENTAL
ID_DOCUMENTO: BM-VOL-RV60K-README-001
TITULO: Indicador de Volatilidade Realizada RV-60K
STATUS: EXPERIMENTAL_COM_EVIDENCIA_NUMERICA
VERSAO: 1.0.0
DATA_CRIACAO: 2026-10-19
DATA_ATUALIZACAO: 2026-10-19
ORIGEM: Reorganizacao dos artefactos existentes em MODULOS/VOLATILIDADE
AUTORIDADE_DOCUMENTAL: GOVERNANCA e BRICKMASTER_GERAL
CADEIA_AUTORIDADE: PROMPTS -> CARTAS -> ESPECIFICACOES -> CODIGO -> VALIDACAO
RASTREABILIDADE: commit de criacao e historico Git
ESCOPO: Indicador intradiario de volatilidade realizada para grafico de 60K trades
OBJETIVO: Concentrar especificacao, codigo e evidencias do RV-60K
DEPENDENCIAS: Precos Close validos e sequencia de barras do grafico 60K trades
SHA-256-CANONICO: 1a75f3ae00920d8175e758f140f46148c731dc9b43ad5f920f3cbc16600c7720
COMMIT-DE-REFERENCIA: 8f69fba6e8abf8fb5db748755705552d92f5d0b9
-->
# RV-60K — Volatilidade Realizada

## Contexto Histórico

O indicador RV-60K foi criado como protótipo isolado para medir volatilidade realizada intradiária através da soma acumulada dos quadrados dos retornos logarítmicos entre barras. O alvo operacional/documental é o gráfico de **60K trades**; isto não deve ser confundido com gráfico de ticks nem com Renko.

## Estado

- Maturidade: **EXPERIMENTAL**.
- Código NTSL existente: `src/RV_60K_V1.0.src`.
- Não envia ordens, não decide direção e não está integrado ao Giroscópio.
- Evidência numérica independente anteriormente registada para exportações WIN/WDO; isso não equivale a backtest, prova de rentabilidade ou aprovação para produção.

## Definição

Forma documentada do cálculo:

`RV_t = 100 * sqrt(sum(ln(C_i/C_(i-1))^2))`

A soma reinicia quando muda a data civil indicada pelos dados do gráfico. O valor é uma métrica acumulada de volatilidade realizada, não uma previsão, não uma métrica direcional e não uma normalização por tempo.

## Contrato de entrada e saída

Entrada: Close atual/anterior válidos e data da barra. Valores de preço nulos, não positivos, ausentes ou inconsistentes não devem ser interpretados como movimento válido.

Saída: valor numérico acumulado da métrica, sujeito à disponibilidade e integridade da série. A interface atual não publica confiança, regime de mercado ou ação operacional.

## Estrutura

- `src/RV_60K_V1.0.src` — código NTSL.
- `ESPECIFICACAO.md` — fórmula, unidades, limites e comportamento.
- `VALIDACAO/` — documentos de evidência e política de reset.
- `CHECKPOINTS.md` — histórico de estado e próximos gates.

## Validação

O relatório de validação previamente existente indica comparação numérica contra exportações do Profit, com tolerância registada de 0,01. A verificação não equivale a compilação validada em todas as versões do Profit, replay, backtest ou validação de estratégia.

## Limitações e bloqueios

- A volatilidade acumulada depende do número de barras amostradas; barras 60K trades não têm duração temporal constante.
- Não usar diretamente como limiar de risco sem estudo quantitativo separado.
- Não inferir que uma meta de 1% desde a abertura será alcançada.
- Mudanças de sessão, dados ausentes, barra inicial e reconciliação de fontes exigem política explícita.
- A integração com Giroscópio, risco soberano e watchdog continua fora do escopo deste indicador.

## Evidências

- [Código RV_60K_V1.0.src](src/RV_60K_V1.0.src)
- [Relatório funcional](VALIDACAO/RELATORIO_VALIDACAO_FUNCIONAL_RV_60K.md)
- [Política de reset](VALIDACAO/POLITICA_SESSAO_RESET_RV_60K.md)
- [Manifesto SHA-256](VALIDACAO/MANIFESTO_SHA256_RV_60K.md)
- [README anterior do RV-60K](README-RV-60K-ORIGEM.md)

## Validação

Esta movimentação é organizacional. Não executa compilação NTSL, replay, backtest nem teste de trading. Os artefactos importados devem ser verificados após a publicação.

## Resultado

Diretório canónico proposto para o indicador RV-60K, mantendo os artefactos de origem e o seu histórico via Git.

## Próxima Ação

Rever contratos e hashes após publicação; confirmar a compilação no Profit em ambiente controlado e manter a maturidade experimental até haver evidência e aprovação explícita.
