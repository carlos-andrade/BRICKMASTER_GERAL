---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "MATRIZ_DE_COBERTURA_E_MAPEAMENTO"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-003-MAPEAMENTO-CATALOGO-B3-2026-10-12"
titulo: "Extração do catálogo BVBG.028.02 — famílias de futuros e aliases"
status: "EXTRACAO_CATALOGO_PASS; MAPEAMENTO_ALIAS_PROFIT_UNKNOWN_BLOCKED"
versao: "1.0.1"
data_criacao: "2026-10-12"
data_atualizacao: "2026-10-12"
origem: "CSV versionado em carlos-andrade/B3, snapshot de cadastro BVBG.028.02 de 2026-09-22"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase02-catalogo-b3-mapeamento"
escopo: "Extração reproduzível das famílias de contratos futuros presentes no catálogo armazenado e verificação de correspondência exata dos seis símbolos operacionais"
objetivo: "Provar presença de famílias de contratos datados sem inferir que um alias Profit corresponda a uma série ou contrato específico"
dependencias: "B3 issue #6; INVENTARIO_B3_2026-09-22.csv; ESTATISTICAS_BVBG028_2026-09-22.json"
---

# Extração do catálogo BVBG.028.02 — famílias de futuros e aliases

## Contexto Histórico

Em 2026-10-12, foi processado o conteúdo integral do CSV versionado `ativos/catalogo/INVENTARIO_B3_2026-09-22.csv` no repositório `carlos-andrade/B3`. A extração foi feita a partir do objeto Git blob identificado pelo SHA Git `5d88fa0e319d8398e992537de51bda691dc4a5ab`. Esse identificador é um Git blob SHA (SHA-1), não deve ser rotulado como SHA-256 do conteúdo.

## Estado

**Extração do catálogo: PASS.** O mapeamento dos aliases da plataforma continua `UNKNOWN/BLOCKED`.

## Evidências

| Verificação | Resultado | Estado |
|---|---:|---|
| Linhas de dados no CSV | 120.973 | PASS |
| Campos do cabeçalho | 32 | PASS |
| Correspondência entre linhas e contagem publicada | 120.973 / 120.973 | PASS |
| Contratos futuros datados extraídos | 70 | PASS |
| IDs de instrumento duplicados entre os 70 contratos extraídos | 0 | PASS |
| Contratos extraídos sem ID, vencimento, multiplicador ou CFI | 0 | PASS |
| Correspondências exatas para os seis símbolos-base consultados | 0 | PASS como teste de não-inferência; mapeamento permanece bloqueado |

## Matriz dos seis símbolos operacionais

A extração procurou correspondência exata em `TckrSymb` e também famílias de contratos datados com ticker que começa por uma das famílias IND/WIN/DOL/WDO e CFI de futuro.

| Símbolo informado pelo operador | Ticker exato encontrado? | Família de contratos datados no catálogo | Evidência de família | Estado do alias Profit |
|---|---|---|---|---|
| `IND` | Não | `IND*` | 12 contratos com CFI `FFICSX` | UNKNOWN/BLOCKED: o catálogo lista contratos, não o alias nu |
| `INDFUT` | Não | Possível relação com família `IND*`, mas não provada | Nenhum `TckrSymb=INDFUT` | UNKNOWN/BLOCKED |
| `DOL` | Não | `DOL*` | 24 contratos com CFI `FFCCSX` | UNKNOWN/BLOCKED: o catálogo lista contratos, não o alias nu |
| `DOFUT` | Não | Possível relação com família `DOL*`, mas não provada | Nenhum `TckrSymb=DOFUT` | UNKNOWN/BLOCKED |
| `WIN` | Não | `WIN*` | 11 contratos com CFI `FFICSX` | UNKNOWN/BLOCKED: o catálogo lista contratos, não o alias nu |
| `WDO` | Não | `WDO*` | 23 contratos com CFI `FFCCSX` | UNKNOWN/BLOCKED: o catálogo lista contratos, não o alias nu |

**Interpretação estrita:** a existência de contratos datados com prefixos IND, DOL, WIN e WDO é comprovada neste snapshot. Não se provou que `INDFUT` seja alias de `IND`, que `DOFUT` seja alias de `DOL`, nem que qualquer símbolo nu selecione uma série contínua, contrato vigente ou regra de rolagem específica. O cadastro também não contém preços de abertura, OHLC, negócios ou barras intraday.

## Amostras de contratos encontrados

| Família | Ticker | Id do instrumento | CFI | Vencimento | Multiplicador |
|---|---|---|---|---|---:|
| IND | INDZ26 | 200001604742 | FFICSX | 2026-12-16 | 1 |
| WIN | WINV26 | 200001771168 | FFICSX | 2026-10-14 | 0,2 |
| DOL | DOLV26 | 200001266025 | FFCCSX | 2026-10-01 | 50 |
| WDO | WDOX26 | 400000108058 | FFCCSX | 2026-11-03 | 10 |

A matriz completa de 70 contratos extraídos foi gravada em:

`MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/MATRIZ_CONTRATOS_FUTUROS_BVBG028_2026-09-22.csv`

O CSV derivado conserva a data de referência, ticker, ID, família, descrições, CFI, datas de negociação, vencimento, multiplicador, mercado, caminho de origem, Git blob SHA e estado de mapeamento. O Git blob SHA da origem é uma identidade Git, não um SHA-256 do conteúdo.

## Validação

- A contagem integral do CSV e a extração dos 70 contratos foram executadas sobre o conteúdo retornado pelo objeto Git do repositório.
- A matriz extraída tem 70 IDs únicos e os quatro campos mínimos (ID, vencimento, multiplicador, CFI) preenchidos em todos os registos.
- O manifesto existente declara SHA-256 `4e29690d9ce9e226bb61da80a167c11c50f828565431351eaf1f8fbbdcfe0a49` e tamanho 20.151.525 bytes para o ZIP RAW `ativos/catalogo/raw/IN260922.zip`; esse hash do RAW é uma declaração do manifesto e não foi recalculado nesta execução.
- Os objetos Git LFS de COTAHIST não foram descarregados nem re-hashados independentemente nesta execução. DS-46 continua NOT_RUN.
- Não houve análise de preço histórico, COTAHIST por contrato, fonte de abertura, compilação NTSL, execução no Profit, replay, backtest ou ordens.

## Resultado

A extração de famílias de contratos e a validação do guardrail de aliases foram executadas. A disponibilidade de dados de abertura e a correspondência dos aliases não estão certificadas.

## Próxima Ação

1. Solicitar evidência documental de como os aliases `INDFUT` e `DOFUT` são resolvidos pela plataforma e qual a série/contrato escolhido; não deduzir isso apenas do cadastro B3.
2. Obter dados históricos de preço para contratos identificados e verificar a existência e semântica do campo de abertura.
3. Completar/reconciliar os CSVs normalizados anuais COTAHIST de 2005–2025 com os RAW ZIPs e manifests.
4. Descarregar objetos LFS num ambiente apropriado, recalcular SHA-256 e comparar com o ponteiro LFS.
5. Manter bloqueadas as validações que dependam de preços de abertura não disponíveis.

## Histórico de versões

- 1.0.0 — 2026-10-12 — extraídos 70 contratos futuros datados de 120.973 registos; zero correspondências exatas para os seis símbolos-base; mapeamento dos aliases Profit continua UNKNOWN/BLOCKED.


## Matriz consolidada por símbolo

Para consulta operacional por símbolo e fonte, ver `MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/MATRIZ_COBERTURA_SEIS_SIMBOLOS_2026-10-12.csv`. Esta matriz consolida a evidência do catálogo com as lacunas COTAHIST e intraday e mantém os seis símbolos em `UNKNOWN/BLOCKED` para abertura enquanto o alias/contrato e o campo de preço não forem comprovados.

- 1.0.1 — 2026-10-12 — referenciada matriz consolidada de cobertura por símbolo e fonte.
