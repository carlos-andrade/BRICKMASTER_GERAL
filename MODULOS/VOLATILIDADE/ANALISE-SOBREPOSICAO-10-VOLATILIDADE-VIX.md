# Análise de sobreposição — VOLATILIDADE e VOLATILIDADE_VIX

| Campo | Valor |
|---|---|
| **ID** | BM-VOL-ANALISE-001 |
| **Projeto** | BRICKMASTER RAIZ |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | ANALISE_ARQUITETURAL |
| **Fase** | F1 — Levantamento e adoção documental |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | A_CALCULAR |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-18 |
| **Data de atualização** | 2026-10-18 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente de decisão arquitetural |
| **Origem** | Inspeção documental dos READMEs existentes no repositório |
| **Autoridade superior** | [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) e [índice modular](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/main/MODULOS/README.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | [README VOLATILIDADE](README.md); [README 10_VOLATILIDADE_VIX](../10_VOLATILIDADE_VIX/README.md) |
| **Escopo** | Comparação inicial das responsabilidades documentadas |
| **Objetivo** | Evitar duplicação e preservar o histórico dos dois diretórios até uma decisão formal |
| **Dependências** | F2 — requisitos e desenho; decisão do responsável técnico |

## Contexto Histórico

A pasta `MODULOS/VOLATILIDADE/` foi criada como espaço de trabalho geral para o módulo. Existe também `MODULOS/10_VOLATILIDADE_VIX/`, criada anteriormente para contexto de volatilidade e aversão ao risco com referência externa VIX. Foi consultado o README de ambos os diretórios.

## Comparação documental observada

| Aspeto | `VOLATILIDADE` | `10_VOLATILIDADE_VIX` |
|---|---|---|
| Foco documentado | Estrutura ampla para medir e classificar volatilidade, contratos, qualidade e testes | Contexto de volatilidade e aversão ao risco, com distinção entre volatilidade realizada do ativo e VIX |
| Papel do VIX | Fonte externa possível, sujeita a validação | Tema central explícito |
| Estado | EM_REVISAO; documentação ainda em desenvolvimento | Proposta inicial — não validada em produção |
| Código/testes | Não confirmados nesta análise | Não confirmados nesta análise; README inspecionado |
| Decisão arquitetural | Pendente | Pendente |

## Conclusão provisória

Há sobreposição temática, mas os READMEs, isoladamente, não provam duplicação de código nem definem completamente as responsabilidades. A decisão segura por enquanto é **manter os dois diretórios sem migração, eliminação ou alteração do conteúdo do VIX**.

Hipótese para avaliação em F2: `VOLATILIDADE` poderá tornar-se o domínio geral de métricas, classificação e contrato de regime; `10_VOLATILIDADE_VIX` poderá ser mantido como componente/adaptador especializado de dados VIX e contexto intermercado. Esta é apenas uma hipótese de arquitetura, não uma decisão aprovada.

## Critérios para fechar a decisão

1. Inspecionar todos os ficheiros, código, testes e referências de ambos os diretórios.
2. Identificar consumidores e imports/referências cruzadas no repositório.
3. Mapear responsabilidades únicas e sobrepostas, sem apagar histórico.
4. Propor a arquitetura-alvo e plano reversível de transição.
5. Obter decisão explícita antes de mover, renomear, fundir ou deprecar ficheiros.

## Evidências

- [Diretório VOLATILIDADE](https://github.com/carlos-andrade/BRICKMASTER_GERAL/tree/main/MODULOS/VOLATILIDADE)
- [README VOLATILIDADE_VIX](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/main/MODULOS/10_VOLATILIDADE_VIX/README.md)
- [Índice modular](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/main/MODULOS/README.md)

## Validação

Concluída apenas a comparação inicial dos dois READMEs. Ainda não foi feita inspeção integral de todos os ficheiros, referências de código, consumidores, testes, workflows ou histórico de commits; portanto, a ausência de duplicação não está comprovada.

## Resultado

Sobreposição temática confirmada nos documentos introdutórios. Duplicação de implementação e fronteira final continuam UNKNOWN até inspeção integral. Nenhum ficheiro foi removido ou migrado.

## Próxima Ação

Inventariar ambos os diretórios e pesquisar referências no repositório. Critério de conclusão: mapa de ficheiros, consumidores e responsabilidades com referências verificáveis, seguido de decisão arquitetural explícita.

## Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.0 | 2026-10-18 | Registo inicial da sobreposição documental | Responsável técnico do projeto | READMEs consultados; commit desta criação no histórico Git |
