<!--
PROJETO: BRICKMASTER RAIZ
REPOSITORIO: carlos-andrade/BRICKMASTER_GERAL
TIPO_DOCUMENTO: ESPECIFICACAO_INDICADOR
FASE: ORGANIZACAO_DOCUMENTAL
ID_DOCUMENTO: BM-VOL-RV60K-SPEC-001
TITULO: Especificacao do RV-60K
STATUS: EXPERIMENTAL
VERSAO: 1.0.0
DATA_CRIACAO: 2026-10-19
DATA_ATUALIZACAO: 2026-10-19
ORIGEM: Codigo NTSL e documentacao RV-60K existentes
AUTORIDADE_DOCUMENTAL: BRICKMASTER_GERAL
CADEIA_AUTORIDADE: ESPECIFICACAO -> CODIGO -> EVIDENCIA
RASTREABILIDADE: commit de criacao e historico Git
ESCOPO: Volatilidade realizada intradiaria em barras 60K trades
OBJETIVO: Registrar formula, comportamento e limites do indicador
DEPENDENCIAS: Close, Close[1], Date, Date[1] no ambiente NTSL documentado
SHA-256-CANONICO: 0fadc4e260e188a833caf12de74a7c94662dd0d6dcbbffde956ff30b8e621733
COMMIT-DE-REFERENCIA: 8f69fba6e8abf8fb5db748755705552d92f5d0b9
-->
# Especificação — RV-60K

## Contexto Histórico

A implementação de origem calcula retornos logarítmicos entre fechamentos e acumula os seus quadrados dentro da data civil.

## Estado

Experimental. Este documento especifica o comportamento pretendido; não constitui aprovação de produção.

## Fórmula

Para (C_i > 0) e (C_{i-1} > 0):

`r_i = ln(C_i/C_(i-1))`

`RV_t = 100 * sqrt(sum(r_i^2))`

A implementação usa `Log(Close / Close[1])`, acumula `retornoLog * retornoLog` e plota `Sqrt(rvAcumulada) * 100`.

## Reset de sessão

Se `Date <> Date[1]`, `retornoLog` e `rvAcumulada` são colocados em zero. Para preços não positivos, o retorno da barra é zero e o acumulador conserva o valor anterior. O comportamento perante gaps de dados ou reinicialização intradia precisa ser revisto em testes dedicados.

## Interpretação

- O valor sobe com a acumulação dos quadrados dos retornos e não tem sinal direcional.
- Não é previsão de volatilidade futura.
- Não é volatilidade anualizada.
- Não está normalizado pela duração real da sessão nem pelo tempo decorrido.
- Em gráfico de 60K trades, o número e a duração das barras podem variar com a atividade.

## Unidades e comparabilidade

O resultado é escalado por 100 e apresentado como métrica percentual da soma quadrática de retornos logarítmicos. Não comparar sem normalização adequada com ATR, desvio-padrão temporal, volatilidade implícita ou indicadores externos.

## Falhas e qualidade

A série precisa ter preços positivos e dados temporais consistentes. A implementação atual substitui retorno inválido por zero; essa política pode ocultar falhas e deve ser reconsiderada antes de qualquer uso como input de decisão. Dados em falta, desatualizados ou contraditórios não devem ser tratados como confirmação.

## Evidência e limitações

O repositório contém relatório de reconciliação numérica de exportações WIN/WDO com tolerância máxima declarada de 0,01. A evidência é limitada às amostras/exports documentados e não comprova desempenho operacional, ausência universal de erros, nem aprovação para produção.

## Resultado

Especificação documental inicial extraída do código e dos registos existentes, a rever antes de integração.

## Próxima Ação

Criar testes dirigidos a primeira barra, viragem de data, preço inválido, gaps, reset e série atrasada; compilar no Profit e registar evidências reproduzíveis.
