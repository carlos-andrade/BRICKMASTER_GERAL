---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-TESTES"
titulo: "Plano de testes — Relógio, sessão e abertura"
status: "49_CASOS; DS-45_PARTIAL_PASS_BLOCKED_2006_2025; DS-46_PARTIAL_PASS_2005; DS-47_DS-48_DS-49_PASS_COM_LIMITES"
versao: "1.0.7"
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
| DS-45 | Reconciliação anual B3 | Inventário estrutural parcial: 41 RAW ZIPs/manifests e 21 CSVs anuais listados; 2006–2025 sem CSV canónico listado, com 2006 manifesto presente mas CSV ausente. Falta reconciliar integralmente conteúdo/hash de todos os anos | PARTIAL_PASS_BLOCKED_2006_2025 |
| DS-46 | Integridade de objeto Git LFS | Obter o objeto real, recalcular SHA-256 e comparar com o ponteiro LFS e manifest; não aceitar metadados como hash recalculado | PARTIAL_PASS_2005 |
| DS-47 | Extração do catálogo BVBG.028.02 | Processar o CSV versionado, confirmar 120.973 registos/32 campos, extrair contratos futuros datados, verificar IDs e campos mínimos; evidência no relatório de mapeamento | PASS |
| DS-48 | Guardrail de aliases | Procurar correspondência exata de IND, INDFUT, DOL, DOFUT, WIN e WDO em TckrSymb; não inferir alias a partir de família de contrato. Resultado: zero correspondências exatas; aliases permanecem UNKNOWN/BLOCKED | PASS |
| DS-49 | Probe COTAHIST EOD — 15 pregões armazenados | Processar os 15 CSVs de 2026-09-21 a 2026-10-09; verificar 25 campos/contagens, CODNEG exato e candidatos por padrão. Resultado: 253.156 registos, zero aliases exatos; 15 candidatos regex-only DOLX11, não confirmados como futuros pelos campos do registo | PASS |

## Histórico de versões

- 1.0.0 — 2026-10-12 — acrescentados DS-47 (extração real do catálogo) e DS-48 (guardrail de aliases); ambos PASS com evidência de parsing, mas mapeamento de aliases permanece UNKNOWN/BLOCKED e DS-45/DS-46 continuam NOT_RUN.
- 0.9.0 — 2026-10-12 — acrescentados DS-45 e DS-46 após auditoria da árvore B3: reconciliação RAW/normalizado/manifests e verificação independente de objetos Git LFS; total de 46 casos, todos NOT_RUN.
- 0.8.0 — 2026-10-12 — reorientado para dados históricos armazenados, sem Profit em tempo real; DS-18–DS-23 reespecificados para cobertura e determinismo offline; DS-27–DS-38 reespecificados; DS-39–DS-44 adicionados para integridade, cobertura e lacunas.
- 0.7.0 — 2026-10-12 — matriz ampliada a INDFUT, DOFUT, IND, DOL, WIN e WDO; adicionados DS-27–DS-38 para configuração, comparação de candidatos e persistência em IND/DOL/WIN/WDO; todos os casos permanecem NOT_RUN.
- 0.6.0 — 2026-10-12 — acrescentado DS-26 para validar o mapeamento entre aliases Profit e códigos oficiais B3 IND/DOL; todos os casos permanecem NOT_RUN.
- 0.5.0 — 2026-10-12 — escopo corrigido para INDFUT/DOFUT sem requisito de gráfico de 60.000 ticks; mapeamento de código B3/contrato explicitamente pendente; todos os testes NOT_RUN.
- 0.4.0 — 2026-10-12 — incorporada verificação cruzada do repositório B3; adicionados DS-24/DS-25 para adequação EOD/intraday; todos continuam NOT_RUN.
- 0.3.0 — 2026-10-12 — matriz explícita WINFUT/DOLFUT em 60.000 ticks e seis casos específicos adicionados; testes continuam não executados.
- 0.2.0 — 2026-10-12 — casos acrescentados para política B e validação de fontes oficiais; testes não executados.


## Atualização de evidência B3 — 2026-10-12

Após a sequência de workflows de 2005, `COTAHIST_A2005.csv` passou a constar na pasta anual. A árvore atual lista 21 CSVs (1986–2005 e 2026) e 41 manifests (1986–2026); `COTAHIST_A2006.csv` ainda não aparece. A lacuna atual é 2006–2025. O manifesto de 2005 declara 181.408 linhas, 25 campos, período 2005-01-03 a 2005-12-29 e SHA-256 normalizado `9fe7ee30e135223f5d414d7ed678f2973645c2f8779f7e94b7a148794e6a847c`; o objeto LFS não foi re-hashado independentemente nesta execução.

DS-45 permanece NOT_RUN porque a reconciliação de todos os anos não está concluída. DS-46 permanece NOT_RUN porque não houve download e SHA-256 independente dos objetos LFS. DS-47 e DS-48 continuam PASS com o escopo restrito descrito acima.

- 1.0.1 — 2026-10-12 — atualização do estado dos normalizados anuais após workflows B3; lacuna corrigida de 2005–2025 para 2006–2025; DS-45/DS-46 permanecem NOT_RUN.


## Bloqueio de reconciliação — ano 2006 — 2026-10-12

O manifesto `COTAHIST_A2006_quality.json` declara `VALIDADO`, 198.367 linhas, 25 campos e SHA-256 `d9025ebcc01413111c67a0bb573f4ff2676aae2105e8204f19d13f9a313ee69d`, mas o CSV `dados/cotahist/normalized/anual/COTAHIST_A2006.csv` não está listado e o caminho retorna 404. DS-45 continua NOT_RUN; não aceitar manifesto como prova do conteúdo físico. A issue B3 #6 solicita materialização e verificação do objeto ou correção do manifesto.

- 1.0.2 — 2026-10-12 — registada discrepância manifesto/CSV em 2006; cobertura anual mantém-se bloqueada até reconciliação.


## Evidência de integridade LFS — 2005 — 2026-10-12

A execução [B3 FASE10 — Validação Independente Integral 2005](https://github.com/carlos-andrade/B3/actions/runs/38253210219) terminou com `success` e o log registou `status=VALIDADO`, SHA-256 do RAW `41eac6d743d9c3e812bb001c4d327582fa7c408dbc99ff4a1734698da8b18f52`, SHA-256 do NORMALIZED `9fe7ee30e135223f5d414d7ed678f2973645c2f8779f7e94b7a148794e6a847c`, 181.408 registos em ambos, 25 campos e zero divergências. O workflow usou checkout com `lfs: true`.

DS-46 passa parcialmente apenas para o objeto NORMALIZED de 2005; os restantes objetos LFS continuam por verificar. DS-45 permanece NOT_RUN. A prova de integridade de COTAHIST 2005 não prova que COTAHIST cubra os contratos futuros-alvo ou o campo de abertura necessário.

- 1.0.3 — 2026-10-12 — DS-46 alterado para PARTIAL_PASS_2005 com evidência CI; restantes objetos LFS pendentes.


## Evidência DS-49 — probe limitado a 2026-10-09

Fonte: `dados/cotahist/normalized/diario/COTAHIST_D09102026.csv`; manifesto `COTAHIST_D09102026_quality.json` declara `VALIDADO`, 19.213 registos, 25 campos e SHA-256 normalizado `f39ec9919b27aa5716a2aa4cebea852f38849389067627238bf2bcf8e17eeed2`. Git blob SHA do CSV: `ec8c33a699f2ef5b1bb88b919b30852b904a069b` (não SHA-256).

Parsing executado: zero correspondências exatas em `CODNEG` para IND/INDFUT/DOL/DOFUT/WIN/WDO; zero prefixos IND/WIN/WDO; quatro prefixos DOL (`DOLA11`, `DOLB11`, `DOLX11`, `DOLL39`). `DOLX11` corresponde a uma regex frouxa de ticker, mas os campos `NOMRES=TREND DOLAR`, `ESPECI=CI`, `TPMERC=010`, `CODBDI=14` não confirmam um contrato futuro. DS-49 PASS significa que o probe executou e o guardrail contra falsos positivos foi aplicado; não certifica cobertura em outros pregões ou a fonte de abertura.

- 1.0.4 — 2026-10-12 — DS-49 PASS com escopo de uma data; DS-45 NOT_RUN e DS-46 PARTIAL_PASS_2005 mantidos.


## Correção DS-49 — candidatos regex-only versus futuros confirmados

O probe foi ampliado aos 15 CSVs diários versionados entre 2026-09-21 e 2026-10-09. Total: 253.156 registos, 25 campos por ficheiro, zero correspondências exatas em `CODNEG` para os seis símbolos-base. A expressão regular frouxa encontra `DOLX11` uma vez por ficheiro; o registo tem `NOMRES=TREND DOLAR`, `ESPECI=CI`, `TPMERC=010`, `CODBDI=14`, pelo que não foi confirmado como contrato futuro. Não foram confirmados contratos futuros das famílias-alvo neste conjunto.

Artefactos:
- `PROBE_COTAHIST_D09102026_COBERTURA_SIMBOLOS.csv` — resumo do pregão 2026-10-09, corrigido.
- `PROBE_COTAHIST_DIARIO_SELECIONADO_20260921_20261009.csv` — contagem por ficheiro, candidatos regex-only e campos de classificação.

DS-49 PASS refere-se à execução do probe e à aplicação do guardrail, não a uma afirmação de ausência universal em COTAHIST. DS-45 permanece NOT_RUN; DS-46 PARTIAL_PASS_2005.

- 1.0.5 — 2026-10-12 — escopo DS-49 ampliado e falso positivo DOLX11 corrigido.


## Atualização da recuperação COTAHIST 2006 — 2026-10-12

A auditoria da árvore B3 permanece: 41 RAW ZIPs anuais e 41 manifests listados; 21 CSVs normalizados anuais (1986–2005 e 2026); os CSVs canónicos de 2006–2025 não estão listados. Em 2006, o manifesto e sidecar declaram hash normalizado, mas o CSV canónico não existe no caminho esperado.

Foi preparada a branch B3 `feat/cotahist-2006-offline-recovery` com workflows FASE01–FASE11, Gate 06–08 e plano documental. A cadeia usa somente o RAW já armazenado, com validação independente de hash/contagem/campos/datas, e é sequenciada por evidência da fase anterior. **A branch não foi integrada nem executada.** A tentativa de criar PR via integração GitHub devolveu 403; a `main` B3 não foi alterada. Comparação: https://github.com/carlos-andrade/B3/compare/main...feat/cotahist-2006-offline-recovery.

DS-45 passa a `PARTIAL_PASS_BLOCKED_2006_2025`: o inventário estrutural confirmou a lacuna, mas a reconciliação integral dos conteúdos continua pendente. DS-46 permanece `PARTIAL_PASS_2005`, porque a evidência CI de 2005 existe, mas não se generaliza aos restantes objetos LFS.

Foram também registadas falhas dos workflows anuais: a certificação anual e o gerador de dataset oficial falharam por incompatibilidade de parser em 1998 (`1.1.1` no manifesto contra requisito `1.1.0`). Em 1998, o SHA-256 do sidecar diverge do hash declarado pelo manifesto/ponteiro LFS; é necessário reconciliar os bytes reais, sem corrigir hashes por suposição. A abertura dos seis símbolos continua `UNKNOWN/BLOCKED`.

- 1.0.7 — 2026-10-12 — DS-45 atualizado para aprovação parcial com bloqueio após inventário de 41 RAW/manifests versus 21 CSVs; registada proposta não integrada de recuperação offline de 2006 e bloqueios de certificação 1998.
