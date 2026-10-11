---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-TESTES"
titulo: "Plano de testes — Relógio, sessão e abertura"
status: "PLANEADO; NAO_EXECUTADO"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Contrato BM-DATA-001-ESPECIFICACAO"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase02-03-contracts"
escopo: "Testes de estado temporal e referência de abertura"
objetivo: "Definir critérios reproduzíveis antes da implementação"
dependencias: "ESPECIFICACAO.md; Manual NTSL 4.4; configuração de sessão"
---

# Plano de testes — Relógio, sessão e abertura

## Contexto Histórico

Criado antes da implementação para impedir que o primeiro candle visível seja confundido automaticamente com a abertura real.

## Estado

PLANEADO — todos os casos NOT_RUN.

## Evidências

A produzir em execução real, com instrumento, contrato, gráfico, sessão, modo de dados, resultado observado e artefacto.

## Validação

Este plano não comprova testes executados.

## Resultado

Matriz de aceitação inicial pronta.

## Próxima Ação

Executar após aprovar a política de abertura e implementar o módulo.

| ID | Caso | Resultado esperado | Estado |
|---|---|---|---|
| DS-01 | Abertura confirmada | `ACTIVE`, referência única e origem registada | NOT_RUN |
| DS-02 | Carregamento a meio da sessão | Recupera abertura real, não o primeiro candle visível | NOT_RUN |
| DS-03 | Abertura ausente | `OPENING_PENDING/UNKNOWN`; sem substituição | NOT_RUN |
| DS-04 | Data/hora inválida | `INVALID`; consumidores bloqueados | NOT_RUN |
| DS-05 | Mudança de sessão | Novo `session_id`; uma reinicialização | NOT_RUN |
| DS-06 | Candle cruza limite de sessão em ticks | Regra determinística; sem dupla contagem | NOT_RUN |
| DS-07 | Gráfico de 60K ticks | Transição verificada sem barras temporais fixas | NOT_RUN |
| DS-08 | Fonte atrasada | Confiança reduzida ou bloqueio segundo contrato | NOT_RUN |
| DS-09 | Fontes contraditórias | `INVALID`; bloqueio explícito | NOT_RUN |
| DS-10 | Histórico/replay/tempo real | Diferenças documentadas | NOT_RUN |
| DS-11 | Reprocessamento do mesmo conjunto | Mesmo estado e referência | NOT_RUN |
| DS-12 | Efeitos colaterais | Nenhuma ordem/posição alterada | NOT_RUN |
