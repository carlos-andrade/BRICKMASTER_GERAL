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
SHA-256-CANONICO: b65e026dbbe471161739fd0a44b9d742500f88737cb0ad169f92ad1a9094ff1f
COMMIT-DE-REFERENCIA: 8f69fba6e8abf8fb5db748755705552d92f5d0b9
-->
# Catálogo de indicadores de volatilidade

## Contexto Histórico

A pasta VOLATILIDADE continha documentos gerais, código NTSL para RV-60K, documentação de validação e especificação de IV-WIN. A reorganização cria um nível comum para separar os indicadores, preservando os ficheiros globais que governam o módulo como um todo.

## Estado

Em revisão. Esta árvore representa organização documental, não prova de implementação ou maturidade técnica de todos os indicadores.

## Indicadores e diretórios

| Diretório | Indicador/método | Estado atual |
|---|---|---|
| [RV-60K](RV-60K/README.md) | Volatilidade realizada acumulada intradiária | Experimental; código e comparação numérica documentados |
| [IV-WIN](IV-WIN/README.md) | Volatilidade implícita contextual do Mini Índice | Experimental; especificação documental, fonte ainda por confirmar |
| [DESVIO-PADRAO-HISTORICO](DESVIO-PADRAO-HISTORICO/README.md) | Desvio-padrão histórico | Candidato documental |
| [PARKINSON](PARKINSON/README.md) | Estimador Parkinson | Candidato documental |
| [GARMAN-KLASS](GARMAN-KLASS/README.md) | Estimador Garman–Klass | Candidato documental |
| [ROGERS-SATCHELL](ROGERS-SATCHELL/README.md) | Estimador Rogers–Satchell | Candidato documental |
| [YANG-ZHANG](YANG-ZHANG/README.md) | Estimador Yang–Zhang | Candidato documental |
| [ATR](ATR/README.md) | True Range / Average True Range | Candidato documental |
| [AMPLITUDE-GAP](AMPLITUDE-GAP/README.md) | Amplitude e gaps | Candidato documental |
| [EWMA](EWMA/README.md) | Volatilidade condicional EWMA | Candidato documental |
| [GARCH-1-1](GARCH-1-1/README.md) | Modelo GARCH(1,1) | Candidato documental |
| [HAR-RV](HAR-RV/README.md) | Modelo HAR-RV | Candidato documental |

VIX permanece fora desta lista de indicadores locais ativos: pode ser estudado apenas como fonte externa opcional, após validar origem, timestamps, atraso, licença e valor informativo.

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

Concluir revisão da migração, corrigir referências relativas e verificar SHA-256 canónico independente; distinguir indicadores existentes de candidatos documentais.
