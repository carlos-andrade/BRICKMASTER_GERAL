---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-TESTES"
titulo: "Plano de testes — Relógio, sessão e abertura"
status: "PLANEADO; NAO_EXECUTADO; INDFUT_DOFUT_SEM_RESTRICAO_60K"
versao: "0.5.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-12"
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

Criado antes da implementação para impedir que o primeiro candle visível seja confundido com a abertura real. A política B foi aprovada em 2026-10-12: preço oficial de abertura da plataforma ou fonte oficial validada.

## Estado

PLANEADO — todos os casos NOT_RUN.

## Evidências

A produzir em execução real, com instrumento, contrato, gráfico, sessão, modo de dados, resultado observado e artefacto.

## Validação

Este plano não comprova testes executados.

## Resultado

Matriz de aceitação inicial pronta.

## Próxima Ação

Executar primeiro a matriz INDFUT e DOFUT na configuração de gráfico efetivamente usada no Profit, sem exigir 60.000 ticks; confirmar código B3/contrato/vencimento, anexar evidências e só então selecionar fonte/campo por instrumento. Depois implementar o módulo e executar os casos. Todos os casos continuam NOT_RUN.

| ID | Caso | Resultado esperado | Estado |
|---|---|---|---|
| DS-01 | Abertura confirmada | `ACTIVE`, referência única e origem registada | NOT_RUN |
| DS-02 | Carregamento a meio da sessão | Recupera abertura real, não o primeiro candle visível | NOT_RUN |
| DS-03 | Abertura ausente | `OPENING_PENDING/UNKNOWN`; sem substituição | NOT_RUN |
| DS-04 | Data/hora inválida | `INVALID`; consumidores bloqueados | NOT_RUN |
| DS-05 | Mudança de sessão | Novo `session_id`; uma reinicialização | NOT_RUN |
| DS-06 | Candle cruza limite de sessão em ticks | Regra determinística; sem dupla contagem | NOT_RUN |
| DS-07 | Tipo de gráfico utilizado | Registar configuração real; a validação da abertura não exige gráfico de 60.000 ticks | NOT_RUN |
| DS-08 | Fonte atrasada | Confiança reduzida ou bloqueio segundo contrato | NOT_RUN |
| DS-09 | Fontes contraditórias | `INVALID`; bloqueio explícito | NOT_RUN |
| DS-10 | Histórico/replay/tempo real | Diferenças documentadas | NOT_RUN |
| DS-11 | Reprocessamento do mesmo conjunto | Mesmo estado e referência | NOT_RUN |
| DS-12 | Efeitos colaterais | Nenhuma ordem/posição alterada | NOT_RUN |
| DS-13 | Fonte oficial configurada | Fonte/campo, instrumento, sessão e timestamp ficam auditáveis | NOT_RUN |
| DS-14 | Fonte primária indisponível | Não escolher alternativa não aprovada; manter UNKNOWN/BLOCKED | NOT_RUN |
| DS-15 | Fontes oficiais divergem | INVALID/BLOCKED até resolução documentada | NOT_RUN |
| DS-16 | Campo NTSL/Profit não equivale à abertura oficial | Rejeitar como substituto e manter UNKNOWN | NOT_RUN |
| DS-17 | Correção oficial da abertura | Evento auditável; nenhuma alteração silenciosa dos níveis | NOT_RUN |
| DS-18 | INDFUT — configuração real do Profit | Símbolo, código B3, contrato, sessão, campo oficial e candidatos registados com evidência | NOT_RUN |
| DS-19 | DOFUT — configuração real do Profit | Símbolo, código B3, contrato, sessão, campo oficial e candidatos registados com evidência | NOT_RUN |
| DS-20 | INDFUT — comparar candidatos | Comparar campo oficial com `Open`, `OpenD(0)`, `OpenDaily(0)` e série diária explícita | NOT_RUN |
| DS-21 | DOFUT — comparar candidatos | Comparar campo oficial com `Open`, `OpenD(0)`, `OpenDaily(0)` e série diária explícita | NOT_RUN |
| DS-22 | INDFUT — persistência da referência | Abertura não muda ao recarregar/reprocessar; diferenças ficam auditadas | NOT_RUN |
| DS-23 | DOFUT — persistência da referência | Abertura não muda ao recarregar/reprocessar; diferenças ficam auditadas | NOT_RUN |
| DS-24 | Adequação de COTAHIST/EOD | Não usar `preabe` como substituto automático da abertura confirmada do Profit; exigir correspondência de símbolo/código B3, contrato, data e semântica | NOT_RUN |
| DS-25 | Adequação de market data intraday B3 | Confirmar arquivo binário, granularidade e campos antes de usar como evidência de abertura/tick; documentação isolada não conta como dataset capturado | NOT_RUN |

## Histórico de versões

- 0.5.0 — 2026-10-12 — escopo corrigido para INDFUT/DOFUT sem requisito de gráfico de 60.000 ticks; mapeamento de código B3/contrato explicitamente pendente; todos os testes NOT_RUN.
- 0.4.0 — 2026-10-12 — incorporada verificação cruzada do repositório B3; adicionados DS-24/DS-25 para adequação EOD/intraday; todos continuam NOT_RUN.
- 0.3.0 — 2026-10-12 — matriz explícita WINFUT/DOLFUT em 60.000 ticks e seis casos específicos adicionados; testes continuam não executados.
- 0.2.0 — 2026-10-12 — casos acrescentados para política B e validação de fontes oficiais; testes não executados.
