# BASE PARA PROMPT — VOLATILIDADE

| Campo | Valor |
|---|---|
| **ID** | BM-VOL-BASE-001 |
| **Projeto** | BRICKMASTER RAIZ |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | BASE_CONCEITUAL |
| **Fase** | F1 — Levantamento e adoção documental |
| **Estado** | EM_REVISAO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | bae0431e743d6369adfd591af13c08bd13fbe7fe58bbed9fc6426581dae2d64a |
| **Commit de referência (versão anterior)** | [fcaa7464d8eb6610667caf803485e98d1519f9ef](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/fcaa7464d8eb6610667caf803485e98d1519f9ef) |
| **Data de criação** | 2026-10-18 |
| **Data de atualização** | 2026-10-18 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Texto conceitual fornecido pelo utilizador nesta conversa; conteúdo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) e [Norma de cabeçalho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Atualização documental após consulta à GOVERNANCA; commit desta alteração a registar no histórico Git |
| **Escopo** | Base conceitual para prompts e requisitos do módulo VOLATILIDADE |
| **Objetivo** | Preservar as definições iniciais sem as confundir com metodologia operacional validada |
| **Dependências** | Especificação, contratos de dados, critérios de teste e validação futura do módulo |

## Contexto Histórico

Este texto foi fornecido pelo utilizador para servir como ponto de partida para o desenvolvimento do módulo VOLATILIDADE. Nesta revisão, foi adicionado o cabeçalho documental e a rastreabilidade conforme a norma consultada no repositório GOVERNANCA. O conteúdo conceitual abaixo foi preservado.

## Conceito

A volatilidade é uma medida que indica a frequência e a intensidade com que o preço de um ativo financeiro oscila ao longo do tempo.

## O que significa na prática

**Alta volatilidade:** O preço do ativo sobe e desce com muita rapidez e amplitude. Representa maior risco, mas também abre espaço para potenciais lucros (ou perdas) acelerados. Exemplos: ações, criptomoedas e small caps.

**Baixa volatilidade:** O preço do ativo varia pouco, mantendo-se mais próximo da média e com maior estabilidade. Representa menor risco. Exemplos: renda fixa e Tesouro Selic.

## Como é medida

- **Desvio-padrão:** A métrica estatística mais utilizada para calcular o afastamento dos preços em relação à média.
- **Índice VIX:** Conhecido como o "índice do medo", mede a expectativa de volatilidade para o mercado de ações dos EUA (S&P 500).
- **Volatilidade histórica vs. implícita:** A primeira analisa dados do passado, enquanto a segunda baseia-se nas expectativas futuras do mercado.

## Limites de interpretação

Este material é uma base conceitual, não uma especificação quantitativa validada. Não define fórmulas operacionais, janelas estatísticas, limiares de classificação, fontes de dados aprovadas, critérios de atualidade ou regras de bloqueio. As referências a exemplos e instrumentos representam a formulação original do texto e não substituem a análise de risco específica de cada ativo. Estes elementos deverão ser especificados e testados separadamente antes de qualquer integração operacional.

## Evidências

- [README do módulo VOLATILIDADE](README.md)
- [Norma de cabeçalho documental da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md)

## Validação

Foi verificado que o conteúdo conceitual fornecido continua presente. Esta atualização não executou validação técnica de métricas nem testes quantitativos de mercado.

## Resultado

Documento conceptual padronizado para revisão, preservando as definições fornecidas e identificando explicitamente as limitações.

## Próxima Ação

Usar o texto como insumo de F2 — Requisitos e desenho. Critério de conclusão: cada conceito operacional pretendido deve ligar-se a uma definição mensurável, fonte aprovada e critério de teste.

## Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.0 | 2026-10-18 | Registo inicial do texto conceptual fornecido | Responsável técnico do projeto | Histórico Git do repositório |
| 1.1.0 | 2026-10-18 | Cabeçalho de governança, rastreabilidade, limites de interpretação e validação documental | Responsável técnico do projeto | Commit a confirmar após publicação |
