<!--
PROJETO: BRICKMASTER RAIZ
REPOSITORIO: carlos-andrade/BRICKMASTER_GERAL
TIPO_DOCUMENTO: INDICE_INDICADORES
FASE: ORGANIZACAO_DOCUMENTAL
ID_DOCUMENTO: BM-VOL-IND-INDEX-001
TITULO: Catalogo de Indicadores de Volatilidade
STATUS: EM_REVISAO
VERSAO: 1.0.0
DATA_CRIACAO: 2026-10-19
DATA_ATUALIZACAO: 2026-10-19
ORIGEM: Levantamento de artefactos existentes em MODULOS/VOLATILIDADE
AUTORIDADE_DOCUMENTAL: GOVERNANCA e BRICKMASTER_GERAL
CADEIA_AUTORIDADE: CATALOGO -> INDICADOR -> CODIGO/ESPECIFICACAO -> VALIDACAO
RASTREABILIDADE: historico Git e commits referenciados
ESCOPO: Catalogar cada família de indicador de volatilidade em pasta própria
OBJETIVO: Separar ciclo de vida, código, especificação e evidências por indicador
DEPENDENCIAS: MODULOS/VOLATILIDADE/README.md
SHA-256-CANONICO: PREENCHER_APOS_HASH_CANONICO
COMMIT-DE-REFERENCIA: PREENCHER_APOS_COMMIT
-->
# Catálogo de indicadores de volatilidade

## Contexto Histórico

A pasta VOLATILIDADE continha documentos gerais, código NTSL para RV-60K, documentação de validação e especificação de IV-WIN. A reorganização cria um nível comum para separar os indicadores, preservando os ficheiros globais que governam o módulo como um todo.

## Estado

Em revisão. Esta árvore representa organização documental, não prova de implementação ou maturidade técnica de todos os indicadores.

## Estrutura proposta

| Diretório | Indicador/família | Conteúdo | Maturidade conhecida |
|---|---|---|---|
| `RV-60K/` | Volatilidade realizada RV-60K | NTSL, especificação, evidências e checkpoints | Experimental; comparação numérica documentada |
| `IV-WIN/` | Volatilidade implícita contextual IV-WIN | especificação e critérios de investigação | Experimental; especificação apenas |
| `VIX-EXTERNO/` | Contexto externo VIX | Não criado como módulo ativo; deve existir somente após decisão formal e contrato de dados | Opcional, não integrado |
| `ATR/` | Average True Range | Criar quando forem inventariados requisitos, implementação ou evidências reais | Por inventariar |
| `DESVIO-PADRAO/` | Desvio-padrão de retornos | Criar quando houver especificação aprovada e uso definido | Por inventariar |
| `RANGE-REALIZADO/` | Estimadores de range (ex.: Parkinson, Garman–Klass, Rogers–Satchell, Yang–Zhang) | Manter juntos apenas se contrato indicar que são variantes de um mesmo grupo; caso sejam indicadores independentes, separar | Candidatos documentais |

## Convenção de pasta por indicador

Cada pasta deve conter, apenas conforme existirem artefactos reais:
- `README.md` — identidade, estado, objetivo e limites;
- `ESPECIFICACAO.md` — fórmula, unidades, janelas, amostragem, tratamento de erros;
- `CONTRATOS.md` — entradas/saídas e dependências, quando definidos;
- código em `src/` ou subdiretório próprio por linguagem, sem misturar com documentos;
- `TESTES.md`, diretório `tests/` e `VALIDACAO/` somente quando existirem casos/resultados;
- `EVIDENCIAS/` e `CHECKPOINTS.md` para material verificável;
- `CHANGELOG.md` para mudanças materiais.
Não criar ficheiros vazios que sugiram implementação, teste ou validação inexistentes.

## Critérios de criação

Criar diretório dedicado quando houver indicador identificado com pelo menos uma necessidade rastreável (código, especificação, dados ou plano aprovado). Indicadores ainda hipotéticos ficam listados como candidatos no catálogo global; não são apresentados como componentes existentes.

## Segurança e governança

- Nenhuma pasta equivale a aprovação ou produção.
- Não misturar volatilidade realizada, implícita e índices externos.
- Não converter ausência de dados em zero ou em sinal neutro sem especificação.
- Dados atrasados/contraditórios reduzem confiança ou bloqueiam consumidores.
- Meta de +1% desde a abertura permanece hipótese, nunca promessa.
- A linha branca do gráfico continua a representar o preço da abertura do mercado.
- O gráfico-alvo do BRICKMASTER permanece 60K trades, não gráfico de ticks.

## Evidências

Organização baseada em ficheiros identificados na árvore do repositório e no inventário atual de VOLATILIDADE.

## Validação

A estrutura ainda precisa de ser confirmada após a cópia de todos os artefactos existentes e executada a revisão de referências relativas. A alteração não realiza testes de trading.

## Resultado

Catálogo e convenção inicial para separar indicadores existentes dos candidatos de pesquisa.

## Próxima Ação

Migrar os artefactos RV-60K e IV-WIN sem perda de conteúdo; rever ligações do README pai e calcular SHA-256 canónico independente após fixar o commit.
