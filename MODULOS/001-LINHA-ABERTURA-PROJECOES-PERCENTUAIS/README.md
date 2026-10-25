---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "README_MODULO"
fase: "MODULO_001"
id_documento: "BM-DOC-MODULO-001-README"
titulo: "MÓDULO 001 — Linha de abertura e projeções percentuais"
status: "PLANEJADO"
versao: "1.0.0"
data_criacao: "N/A"
data_atualizacao: "2026-10-11"
origem: "Conteúdo preexistente; histórico Git"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR feat/cabecalho-padrao-documental"
escopo: "Descrição funcional e estado do Módulo 001"
objetivo: "Documentar objetivo, critérios e limites sem presumir validação"
dependencias: "ESPECIFICACAO.md; tests/; evidencias/; Manual NTSL 4.4"
---

# MÓDULO 001 — Linha de abertura e projeções percentuais

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Tipo:** README DE MÓDULO  
> **Fase:** MÓDULO 001  
> **ID:** BM-DOC-MODULO-001-README  
> **Status:** PLANEJADO  
> **Versão:** 1.0.0  
> **Criação:** N/A  
> **Atualização:** 2026-10-11  
> **Origem:** Conteúdo preexistente; histórico Git  
> **Autoridade:** LAYOUT  
> **Rastreabilidade:** PR feat/cabecalho-padrao-documental

**Projeto:** BRICKMASTER RAIZ  
**Estado:** ESPECIFICAÇÃO INICIAL — NÃO APROVADO PARA INTEGRAÇÃO  
**Prioridade:** Fundacional  
**Isolamento:** Obrigatório

## Contexto Histórico

README preexistente do primeiro módulo; conteúdo funcional e limitações foram preservados nesta padronização.

## 1. Objetivo

No início de cada sessão de mercado, plotar uma linha horizontal de referência no preço de abertura definido para o ativo e projetar, acima e abaixo dessa linha, níveis de ±0,5%, ±1%, ±2% e ±3%.

Este é o primeiro módulo do BRICKMASTER RAIZ. A arquitetura posterior deverá poder referenciar os seus níveis, mas não deve misturar a lógica deste módulo com outros módulos antes da validação independente.

## 2. Saída visual esperada

- Uma linha-base no preço de referência da abertura: (P₀).
- Oito níveis percentuais simétricos:
  - Superior: +0,5%, +1%, +2%, +3%.
  - Inferior: −0,5%, −1%, −2%, −3%.
- Os níveis devem permanecer coerentes com a referência da sessão corrente.
- Na mudança de sessão, a referência deve ser atualizada uma única vez conforme a regra de abertura aprovada.
- O módulo não deve enviar ordens nem tomar decisões de entrada/saída.

## 3. Cálculo

Para cada variação percentual (p):

`Nível(p) = P₀ × (1 + p/100)`

Exemplos genéricos:
- `+0,5%`: `P₀ × 1,005`
- `−0,5%`: `P₀ × 0,995`
- `+1%`: `P₀ × 1,01`
- `−1%`: `P₀ × 0,99`
- `+2%`: `P₀ × 1,02`
- `−2%`: `P₀ × 0,98`
- `+3%`: `P₀ × 1,03`
- `−3%`: `P₀ × 0,97`

O arredondamento deve respeitar o incremento mínimo de preço (tick size) do instrumento. A regra exata de arredondamento será decidida e testada por ativo; não arredondar silenciosamente antes de confirmar o comportamento pretendido.

## 4. Decisão técnica em aberto

Antes de escrever a implementação NTSL, confirmar e registar:
- Instrumento inicial de teste (por exemplo, WIN, WDO ou ação).
- Qual preço é a “abertura”: primeiro negócio observado na sessão, abertura oficial ou outro campo disponível.
- Horário da sessão e fuso horário de referência.
- Como identificar a primeira barra/tick da sessão, inclusive em gráficos atemporais/de ticks.
- Comportamento quando o gráfico é carregado a meio da sessão ou recalculado.
- Precisão e arredondamento por instrumento.
- Se as linhas devem estender-se por toda a sessão e como são reinicializadas no pregão seguinte.

Não presumir que a primeira barra visível no gráfico equivale à abertura real do mercado.

## 5. Critérios de aceitação

- [ ] A linha-base coincide com o preço de referência documentado.
- [ ] Os oito níveis correspondem matematicamente a ±0,5%, ±1%, ±2% e ±3%.
- [ ] A referência não muda indevidamente durante a sessão.
- [ ] A reinicialização ocorre corretamente numa nova sessão.
- [ ] O comportamento foi verificado com histórico e com sessão em andamento.
- [ ] Foram testados recálculo, carregamento a meio da sessão e mudança de data/pregão.
- [ ] A precisão respeita o tick size do instrumento.
- [ ] Não há ordens ou efeitos colaterais de execução.
- [ ] Resultados e limitações foram registados em `tests/` e `evidencias/`.

## 6. Plano de testes isolados

1. Cálculo dos oito níveis com valores de abertura conhecidos.
2. Verificação de simetria percentual em relação a (P₀).
3. Mudança de sessão e atualização da referência.
4. Recarregamento do gráfico a meio do pregão.
5. Gráfico atemporal/de ticks, incluindo sequência sem barra temporal fixa.
6. Teste de arredondamento para o incremento mínimo do ativo.
7. Verificação visual dos níveis no Profit.
8. Regressão após cada correção.

Os testes devem separar resultado matemático, comportamento de plotagem e comportamento específico do Profit/NTSL.

## 7. Limites

Este módulo apenas estabelece uma referência visual e níveis percentuais. Os níveis não são, por si só, sinais de compra/venda, suportes ou resistências comprovados, nem garantem desempenho financeiro.

## 8. Estrutura da pasta

- `ESPECIFICACAO.md` — especificação técnica detalhada.
- `tests/PLANO-DE-TESTES.md` — casos de teste e critérios.
- `evidencias/README.md` — regras para registo de evidências.
- `CHANGELOG.md` — histórico de versões.
- `src/` — implementação isolada, a criar após fechar as decisões técnicas.

## 9. Estado de aprovação

**Estado atual:** especificação inicial registada. Implementação, execução e aprovação ainda pendentes. Não declarar o módulo testado até existirem evidências verificáveis.

## Estado

PLANEJADO — não aprovado para integração.

## Evidências

O próprio documento e os artefatos ligados na estrutura da pasta. Não foram adicionadas evidências de execução.

## Validação

A padronização documental não representa validação técnica do módulo.

## Resultado

README com cabeçalho rastreável e conteúdo original preservado.

## Próxima Ação

Fechar as decisões técnicas em aberto e executar o plano de testes isolados.
