---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "MODULO_001"
id_documento: "BM-DOC-MODULO-001-PLANO-TESTES"
titulo: "Plano de testes — Módulo 001"
status: "PLANEJADO"
versao: "1.0.0"
data_criacao: "N/A"
data_atualizacao: "2026-10-11"
origem: "Conteúdo preexistente; histórico Git"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR feat/cabecalho-padrao-documental"
escopo: "Testes isolados do Módulo 001"
objetivo: "Definir testes e evidências antes de aprovação"
dependencias: "ESPECIFICACAO.md; Profit/NTSL"
---

# Plano de testes — Módulo 001

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Tipo:** PLANO DE TESTES  
> **Fase:** MÓDULO 001  
> **ID:** BM-DOC-MODULO-001-PLANO-TESTES  
> **Status:** PLANEJADO  
> **Versão:** 1.0.0  
> **Criação:** N/A  
> **Atualização:** 2026-10-11  
> **Origem:** Conteúdo preexistente; histórico Git  
> **Autoridade:** LAYOUT  
> **Rastreabilidade:** PR feat/cabecalho-padrao-documental

**Estado:** PLANEADO — AINDA NÃO EXECUTADO

| ID | Teste | Resultado esperado | Evidência |
|---|---|---|---|
| T001 | Cálculo com preço de abertura conhecido | Oito níveis coincidem com a fórmula | Tabela de cálculo |
| T002 | Simetria percentual | Cada nível respeita a percentagem indicada em relação a P₀ | Cálculo independente |
| T003 | Congelamento da referência | P₀ não muda com a oscilação intrassessão | Registo de sessão |
| T004 | Nova sessão | A referência muda apenas para a nova sessão válida | Captura antes/depois |
| T005 | Carregamento a meio do pregão | Recupera a abertura real, não o primeiro preço visível | Captura e log |
| T006 | Gráfico de ticks | Deteção de sessão funciona sem barras temporais fixas | Captura e log |
| T007 | Tick size | Níveis plotados respeitam a regra aprovada | Tabela pré/pós-arredondamento |
| T008 | Plotagem | Linha-base e oito níveis são visíveis e corretos | Captura do Profit |
| T009 | Reprocessamento histórico | Referências diárias permanecem corretas | Capturas de dias diferentes |
| T010 | Efeitos colaterais | Nenhuma ordem é enviada e nenhuma posição é alterada | Verificação da estratégia |

## Registo por execução

Para cada teste, registar data/hora, instrumento, tipo de gráfico, configuração, resultado esperado, resultado observado, estado (PASS/FAIL/BLOCKED), evidência e defeito associado.

Não marcar PASS sem evidência observável. Testes não executados devem permanecer PLANEADO; bloqueios devem identificar a dependência em falta.

## Contexto Histórico

Plano preexistente do Módulo 001; conteúdo preservado.

## Estado

PLANEADO — testes ainda não executados.

## Evidências

A produzir durante a execução real de cada caso.

## Validação

A padronização do cabeçalho não representa execução dos testes.

## Resultado

Plano rastreável, com os testes ainda pendentes.

## Próxima Ação

Executar os testes e anexar evidências verificáveis.
