---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-TESTES"
titulo: "Plano de testes — Relógio, sessão e abertura"
status: "PLANEADO; 46_CASOS_NOT_RUN; AUDITORIA_DE_COBERTURA_B3_EM_CURSO"
versao: "0.9.0"
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

PLANEADO — todos os casos NOT_RUN. A execução deste plano deve usar somente dados históricos já armazenados no repositório B3; não há acesso a Profit em tempo real neste fluxo.

## Evidências

A produzir em execução real, com instrumento, contrato, gráfico, sessão, modo de dados, resultado observado e artefacto.

## Validação

Este plano não comprova testes executados.

## Resultado

Matriz de aceitação inicial pronta.

## Próxima Ação

Usar somente arquivos já armazenados em `carlos-andrade/B3`. Primeiro verificar a cobertura real de cada símbolo/contrato, hash, manifesto, campos e semântica. A cobertura insuficiente de derivativos históricos foi solicitada em [B3 issue #6](https://github.com/carlos-andrade/B3/issues/6). Não simular resultados de funções NTSL nem depender do Profit em tempo real. Todos os casos continuam NOT_RUN.

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
| DS-18 | INDFUT — cobertura histórica armazenada | Localizar arquivos B3 armazenados e registar fonte, data, hash, campos e contrato; se ausente, documentar lacuna | NOT_RUN |
| DS-19 | DOFUT — cobertura histórica armazenada | Localizar arquivos B3 armazenados e registar fonte, data, hash, campos e contrato; se ausente, documentar lacuna | NOT_RUN |
| DS-20 | INDFUT — validar abertura offline | Validar apenas campo de abertura existente em fonte histórica armazenada e sua semântica; não executar funções NTSL offline | NOT_RUN |
| DS-21 | DOFUT — validar abertura offline | Validar apenas campo de abertura existente em fonte histórica armazenada e sua semântica; não executar funções NTSL offline | NOT_RUN |
| DS-22 | INDFUT — determinismo offline | Mesmo arquivo/hash e versão do parser produzem resultado repetível; diferenças ficam auditadas | NOT_RUN |
| DS-23 | DOFUT — determinismo offline | Mesmo arquivo/hash e versão do parser produzem resultado repetível; diferenças ficam auditadas | NOT_RUN |
| DS-24 | Adequação de COTAHIST/EOD | Não usar `preabe` como substituto automático da abertura confirmada do Profit; exigir correspondência de símbolo/código B3, contrato, data e semântica | NOT_RUN |
| DS-25 | Adequação de market data intraday B3 | Confirmar arquivo binário, granularidade e campos antes de usar como evidência de abertura/tick; documentação isolada não conta como dataset capturado | NOT_RUN |
| DS-26 | Identidade e metadados dos seis símbolos Profit/B3 | Usar cadastro e arquivos armazenados para mapear INDFUT, DOFUT, IND, DOL, WIN e WDO; não presumir equivalência entre símbolos | NOT_RUN |
| DS-27 | IND — configuração real do Profit | Registar símbolo, código efetivo, contrato, sessão, campo oficial e candidatos com evidência | NOT_RUN |
| DS-28 | IND — validar abertura offline | Validar campos históricos armazenados e semântica; funções NTSL não são executadas offline | NOT_RUN |
| DS-29 | IND — determinismo offline | Mesmo arquivo/hash e parser reproduzem resultado; auditar qualquer diferença | NOT_RUN |
| DS-30 | DOL — configuração real do Profit | Registar símbolo, código efetivo, contrato, sessão, campo oficial e candidatos com evidência | NOT_RUN |
| DS-31 | DOL — validar abertura offline | Validar campos históricos armazenados e semântica; funções NTSL não são executadas offline | NOT_RUN |
| DS-32 | DOL — determinismo offline | Mesmo arquivo/hash e parser reproduzem resultado; auditar qualquer diferença | NOT_RUN |
| DS-33 | WIN — configuração real do Profit | Registar símbolo, código efetivo, contrato, sessão, campo oficial e candidatos com evidência | NOT_RUN |
| DS-34 | WIN — validar abertura offline | Validar campos históricos armazenados e semântica; funções NTSL não são executadas offline | NOT_RUN |
| DS-35 | WIN — determinismo offline | Mesmo arquivo/hash e parser reproduzem resultado; auditar qualquer diferença | NOT_RUN |
| DS-36 | WDO — configuração real do Profit | Registar símbolo, código efetivo, contrato, sessão, campo oficial e candidatos com evidência | NOT_RUN |
| DS-37 | WDO — validar abertura offline | Validar campos históricos armazenados e semântica; funções NTSL não são executadas offline | NOT_RUN |
| DS-38 | WDO — determinismo offline | Mesmo arquivo/hash e parser reproduzem resultado; auditar qualquer diferença | NOT_RUN |

| DS-39 | Manifesto e integridade dos dados | Para cada arquivo usado, verificar SHA-256, data de referência, versão do parser e status de qualidade | NOT_RUN |
| DS-40 | Cobertura temporal | Identificar datas/pregões presentes e ausentes; não tratar uma amostra de dias como série contínua | NOT_RUN |
| DS-41 | Granularidade da fonte | Classificar cada fonte como EOD, barra, intraday ou negócio a negócio; não substituir granularidade ausente | NOT_RUN |
| DS-42 | Ausência de dados de Profit em tempo real | Confirmar que os testes offline não exigem feed/exportação live nem simulam saída de funções NTSL | NOT_RUN |
| DS-43 | Campo oficial de abertura armazenado | Verificar no layout e no arquivo real se existe campo de abertura aplicável ao contrato; se não existir, registrar lacuna | NOT_RUN |
| DS-44 | Lacuna de dados e bloqueio | Se não houver arquivo/campo/contrato comprovado, manter `UNKNOWN/BLOCKED` e encaminhar pedido de atualização para B3 issue #6 | NOT_RUN |
| DS-45 | Reconciliação anual B3 | Comparar anos/arquivos RAW, CSVs normalizados e manifests; bloquear anos com artefacto normalizado ausente ou divergente | NOT_RUN |
| DS-46 | Integridade de objeto Git LFS | Obter o objeto real, recalcular SHA-256 e comparar com o ponteiro LFS e manifest; não aceitar metadados como hash recalculado | NOT_RUN |

## Histórico de versões

- 0.9.0 — 2026-10-12 — acrescentados DS-45 e DS-46 após auditoria da árvore B3: reconciliação RAW/normalizado/manifests e verificação independente de objetos Git LFS; total de 46 casos, todos NOT_RUN.
- 0.8.0 — 2026-10-12 — reorientado para dados históricos armazenados, sem Profit em tempo real; DS-18–DS-23 reespecificados para cobertura e determinismo offline; DS-27–DS-38 reespecificados; DS-39–DS-44 adicionados para integridade, cobertura e lacunas.
- 0.7.0 — 2026-10-12 — matriz ampliada a INDFUT, DOFUT, IND, DOL, WIN e WDO; adicionados DS-27–DS-38 para configuração, comparação de candidatos e persistência em IND/DOL/WIN/WDO; todos os casos permanecem NOT_RUN.
- 0.6.0 — 2026-10-12 — acrescentado DS-26 para validar o mapeamento entre aliases Profit e códigos oficiais B3 IND/DOL; todos os casos permanecem NOT_RUN.
- 0.5.0 — 2026-10-12 — escopo corrigido para INDFUT/DOFUT sem requisito de gráfico de 60.000 ticks; mapeamento de código B3/contrato explicitamente pendente; todos os testes NOT_RUN.
- 0.4.0 — 2026-10-12 — incorporada verificação cruzada do repositório B3; adicionados DS-24/DS-25 para adequação EOD/intraday; todos continuam NOT_RUN.
- 0.3.0 — 2026-10-12 — matriz explícita WINFUT/DOLFUT em 60.000 ticks e seis casos específicos adicionados; testes continuam não executados.
- 0.2.0 — 2026-10-12 — casos acrescentados para política B e validação de fontes oficiais; testes não executados.
