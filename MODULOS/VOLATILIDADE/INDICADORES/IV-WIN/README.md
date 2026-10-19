<!--
PROJETO: BRICKMASTER RAIZ
REPOSITORIO: carlos-andrade/BRICKMASTER_GERAL
TIPO_DOCUMENTO: README_INDICADOR
FASE: ORGANIZACAO_DOCUMENTAL
ID_DOCUMENTO: BM-VOL-IVWIN-README-001
TITULO: Indicador Contextual de Volatilidade Implicita IV-WIN
STATUS: ESPECIFICACAO_EXPERIMENTAL
VERSAO: 1.0.0
DATA_CRIACAO: 2026-10-19
DATA_ATUALIZACAO: 2026-10-19
ORIGEM: ESPECIFICACAO_IV_WIN.md existente
AUTORIDADE_DOCUMENTAL: BRICKMASTER_GERAL
CADEIA_AUTORIDADE: REQUISITOS -> ESPECIFICACAO -> CONTRATO -> IMPLEMENTACAO -> VALIDACAO
RASTREABILIDADE: commit de criacao e historico Git
ESCOPO: Investigacao de volatilidade implicita contextual para WIN
OBJETIVO: Separar especificacao IV-WIN dos demais indicadores
DEPENDENCIAS: Dados de opcoes e cadeia temporal apropriada, ainda por confirmar
SHA-256-CANONICO: PENDENTE_DE_CALCULO_APOS_CONGELAMENTO
COMMIT-DE-REFERENCIA: PENDENTE_DE_COMMIT_FINAL
-->
# IV-WIN — Volatilidade Implícita

## Contexto Histórico

A especificação IV-WIN existente descreve uma linha de investigação para contexto de volatilidade implícita aplicável ao Mini Índice WIN. Ela não comprova que exista um feed disponível nem que cálculos, cadeia de opções ou testes empíricos tenham sido implementados.

## Estado

**EXPERIMENTAL — ESPECIFICAÇÃO DOCUMENTAL.** Não há alegação de série histórica de IV observada, testes empíricos, integração ou produção.

## Objetivo

Investigar se métricas de volatilidade implícita de opções relevantes para o mercado brasileiro podem acrescentar contexto ao Giroscópio, quando forem encontradas fontes autorizadas, consistentes, sincronizadas e tecnicamente adequadas.

## Famílias de métricas candidatas

Conforme especificação canónica movida para este diretório:
- nível de IV;
- variação de IV;
- estrutura a termo;
- skew;
- prémio de volatilidade.

São candidatos de investigação. Não representam métricas disponíveis ou validadas.

## Contrato preliminar

Toda observação deve incluir origem, instrumento/opção, timestamp do evento e receção, unidade, metodologia, validade, frescura e qualidade. Se a cadeia de opções, timestamp ou fonte estiver ausente ou incompatível, a saída deve ficar desconhecida/bloqueada e não alimentar decisão operacional.

## Limites

- Não envia ordens.
- Não prevê por si só a direção do WIN.
- Não substituir IV por VIX nem tratar VIX como medição direta da IV do ativo operado.
- Sem feed de opções identificado e testes reproduzíveis, o módulo permanece apenas uma especificação.
- Nenhum limiar ou peso de confiança é considerado aprovado por este README.

## Evidências

- [ESPECIFICACAO.md](ESPECIFICACAO.md)
- [Especificação IV-WIN de origem preservada](ESPECIFICACAO-IV-WIN-ORIGEM.md)

## Validação

A reorganização documental não executa testes de opções, estimação IV, sincronização, backtest nem validação empírica.

## Resultado

Diretório próprio para desenvolver e rever o conceito IV-WIN sem misturá-lo com RV-60K ou contexto VIX.

## Próxima Ação

Confirmar disponibilidade e licenças de dados de opções; definir método completo, convenções de vencimento e critérios de qualidade; só depois elaborar implementação e protocolo de teste.
