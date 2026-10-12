---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "CHECKPOINT_MESTRE_DE_EXECUCAO"
fase: "GOVERNANCA_E_ROADMAP_00_08"
id_documento: "BM-CKPT-ROADMAP-2026-10-11-001"
titulo: "Checkpoint mestre — execução do roadmap BRICKMASTER 00–08"
status: "CHECKPOINT_ATUAL; FASES_TECNICAS_AINDA_NAO_VALIDADAS"
versao: "1.7.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-12"
origem: "Execução GitHub e auditorias registadas nesta sessão"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/checkpoint-mestre-roadmap"
escopo: "Estado das fases 00–08, evidências, limitações e próxima decisão bloqueante"
objetivo: "Permitir continuidade a partir de estado verificável, sem repetir trabalho nem promover fases sem evidência"
dependencias: "ROADMAP_EXECUCAO_FASES_00_08.md; REGISTRO_MODULOS_E_CHECKPOINTS.md; GitHub Actions"
---

# Checkpoint mestre — execução do roadmap BRICKMASTER 00–08

## Contexto Histórico

O repositório oficial foi auditado e a sequência feature → develop → validação → main foi estabelecida. A branch develop foi criada a partir de main; as alterações documentais abaixo foram integradas em develop após o workflow documental passar. A branch main permaneceu no commit `ac61750ca0e1413d127759b592a0bd296cf9f83e` durante esta sequência, sem promoção dos artefactos experimentais.

## Estado

**Estado geral:** execução documental avançada; nenhuma fase técnica de trading foi certificada. O CI verde prova apenas que o validador documental passou, não que código NTSL compilou ou que o Profit foi testado.

| Fase | Estado atual | Evidência publicada | Bloqueio principal |
|---|---|---|---|
| 00 — Inventário | PARCIAL | Inventário recursivo de 212 blobs, hashes/caminhos e reconciliação 209 + 3 = 212 | Auditoria semântica integral dos artefactos ainda incompleta |
| 01 — Arquitetura/governança | PARCIAL | Roadmap, norma documental, mapeamento dos seis domínios lógicos às camadas L0–L9; branch develop e CI | Contratos técnicos e integração ainda não validados |
| 02 — Dados/sessão/abertura | POLÍTICA B APROVADA; IMPLEMENTAÇÃO PENDENTE | Módulo 002 v0.2.0 e 17 casos de teste planeados | Fonte/campo oficial por instrumento e sessão/fuso por confirmar; seis símbolos selecionados (INDFUT, DOFUT, IND, DOL, WIN e WDO); validação apenas com dados históricos armazenados; 44 casos planeados e NOT_RUN |
| 03 — Giroscópio | CONTRATO INICIAL | Módulo 003 com contrato de contexto e 13 casos de teste | Implementação e testes de localização/conflito/60K NOT_RUN |
| 04 — Estrutura/módulos de mercado | PARCIAL | FVG-ATLAS inventariado (249 blobs, V2.1.33 referenciada); candidatos VWAP/TWAP/delta/volume listados | Contratos, compatibilidade e testes BRICKMASTER pendentes; Market DNA e outros módulos por localizar/recuperar |
| 05 — Risco soberano | CONTRATO INICIAL | Módulo 004 e plano de 12 testes | Limites de perda/exposição/tentativas e política versionada por aprovar; testes NOT_RUN |
| 06 — NTSL/Profit/execução/Watchdog | CONTRATOS INICIAIS + REVISÃO ESTÁTICA | Módulos 005/006; auditoria CumulativeVolume vs Manual 4.4 | Sem compilação Profit, simulação ou reconciliação real; limites de freshness por medir |
| 07 — Testes/replay/backtest | PLANO DOCUMENTADO | Matriz de evidências definida em PLANO_VALIDACAO_FASE07_08.md | Datasets/configuração e execução de testes ainda não registados |
| 08 — Integração/produção | PORTÕES DOCUMENTADOS; BLOQUEADA | Critérios de release/rollback definidos | Portões anteriores não passaram por validação técnica; aprovação live ausente |

### Correções e conclusões verificadas

1. A contagem histórica de 209 ficheiros foi reconciliada com 212 blobs atuais pelos três ficheiros adicionados no PR #2: norma documental, workflow e script.
2. O roadmap inicial usava comentário HTML no cabeçalho e falhou o workflow; o cabeçalho foi corrigido e execuções posteriores passaram.
3. A notação percentual da especificação do Módulo 001 foi clarificada por tabela. Nenhum código NTSL do módulo foi alterado.
4. FVG-ATLAS V2.1.33 tem relatório documental de regressão integrada aprovado no repositório externo; isso não é validação independente no BRICKMASTER nem prova de compatibilidade Profit/NTSL 4.4.
5. O Manual NTSL 4.4 confirma que Volume é volume financeiro por candle, Date() retorna a data do candle e Time() a hora de abertura do candle.
6. A revisão estática do candidato CumulativeVolume identificou falta de limites explícitos de sessão, possível atribuição de volume a janela errada em candles que cruzam fronteiras e uso impreciso do termo Welford.
7. O objetivo de 1% desde a abertura permanece hipótese; não é garantia nem motivo para ultrapassar risco.
8. Não foram enviadas ordens reais. Nenhum resultado de backtest, replay, compilação NTSL ou teste Profit foi declarado como executado nesta sequência.

## Evidências

### Pull requests integrados em develop

- PR #4 — roadmap e inventário estrutural: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/4
- PR #5 — reconciliação de contagem e checkpoint de arquitetura: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/5
- PR #6 — inventário FVG-ATLAS: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/6
- PR #7 — candidatos de fluxo/VWAP/TWAP/volume: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/7
- PR #8 — revisão estática versus Manual NTSL 4.4: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/8
- PR #9 — contratos de sessão/abertura e Giroscópio: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/9
- PR #10 — contrato de risco soberano: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/10
- PR #11 — execução conciliada, Watchdog e portões 07/08: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/11

### CI documental

- Último workflow de develop no checkpoint: https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/runs/38182191964
- Commit develop: `1e7409191a0b05846e80d0256954ac4357390d9f` — workflow documental concluído com SUCCESS.
- Commit main observado antes da sequência: `ac61750ca0e1413d127759b592a0bd296cf9f83e`.

## Validação

Este checkpoint foi consolidado a partir dos estados e artefactos GitHub consultados. A validação documental passou. As fases técnicas permanecem por validar porque ainda faltam implementação/testes no Profit, replay/backtest, confirmação da sessão/abertura, parâmetros de risco aprovados e reconciliação de execução.

## Resultado

Há contratos iniciais e planos de teste para as principais fronteiras de dados/sessão, Giroscópio, risco, execução e Watchdog; há inventários de FVG-ATLAS e de candidatos de fluxo; o fluxo de branches e a validação documental estão operacionais. O sistema não está pronto para produção.

## Próxima Ação

1. Auditar os dados históricos já armazenados em `carlos-andrade/B3` para INDFUT, DOFUT, IND, DOL, WIN e WDO; verificar cobertura por instrumento/contrato, hash, data, granularidade e campo de abertura. Não depender de Profit em tempo real nem simular outputs de funções NTSL.
2. Registar contrato/vencimento, data, sessão/fuso, versão/feed, timestamps, valores, discrepâncias e capturas/exports no repositório. Manter `UNKNOWN/INVALID` enquanto a fonte não for demonstrada.
3. Só após a base armazenada cobrir os instrumentos e campos necessários, executar testes offline repetíveis e aprovar a fonte histórica por instrumento. A semântica runtime NTSL/Profit continua fora do que pode ser comprovado offline.
4. Resolver os achados estáticos de CumulativeVolume numa variante separada, sem substituir o ficheiro histórico.
5. Recuperar/definir contratos para Liquidez, Contador de Toques e Market DNA.
6. Aprovar limites soberanos de risco antes de dimensionar ou autorizar qualquer ordem.
7. Executar testes no Profit e recolher evidências reproduzíveis antes de promover qualquer release.

## Histórico de versões

- 1.0.0 — 2026-10-11 — checkpoint mestre consolidado após PRs #4–#11 e validação documental em develop.


## Decisão nova — 2026-10-12

O utilizador aprovou a política B para o Módulo 002: preço oficial de abertura fornecido pela plataforma ou por fonte oficial validada. O Módulo 001 passa a exigir referência `CONFIRMED` do Módulo 002. A fonte concreta e o campo técnico continuam por validar; não há testes executados nem confirmação de disponibilidade no Profit/NTSL. A auditoria documental dos candidatos (`Open`, `OpenD(0)`, `OpenDaily(0)` e séries diárias) foi publicada em `GOVERNANCA/AUDITORIA_FONTE_ABERTURA_OFICIAL_NTSL44.md`; nenhum candidato foi certificado como fonte oficial universal.

- 1.0.1 — 2026-10-12 — checkpoint atualizado com a decisão de abertura oficial.

- 1.0.3 — 2026-10-12 — instrumentos INDFUT e DOFUT definidos para validação prática, sem exigência de gráfico de 60.000 ticks; execução Profit e evidências continuam pendentes.
- 1.0.2 — 2026-10-12 — referência à auditoria documental da fonte de abertura acrescentada; validação Profit continua pendente.


## Verificação cruzada B3 — 2026-10-12

O repositório `carlos-andrade/B3` foi consultado para a fonte de abertura. O contrato COTAHIST documenta `preabe` como preço de abertura EOD; a camada Market Data classifica BVBG.186.01/BVBG.187.01 como EOD e não tick-by-tick; a documentação intraday/negócio a negócio consultada ainda marca a captura dos binários como pendente. Isso não certifica a abertura usada pelo Profit em INDFUT/DOFUT. O tipo de gráfico não é restringido a 60.000 ticks. Mantêm-se os testes práticos `NOT_RUN` e a fonte do Módulo 002 não certificada.

- 1.0.4 — 2026-10-12 — verificação cruzada do B3 registada; dados EOD distinguidos da validação Profit.
- 1.0.5 — 2026-10-12 — correção do escopo para INDFUT/DOFUT; gráfico de 60.000 ticks desconsiderado; mapeamento B3/contrato pendente.
- 1.0.8 — 2026-10-12 — regra operacional alterada para usar apenas dados históricos armazenados; registada lacuna de cobertura B3 e issue #6; plano Módulo 002 ampliado para 44 casos, todos NOT_RUN.
- 1.0.7 — 2026-10-12 — âmbito ampliado aos seis símbolos utilizados no Profit (INDFUT, DOFUT, IND, DOL, WIN e WDO); plano Módulo 002 ampliado para 38 casos, todos NOT_RUN.
- 1.0.6 — 2026-10-12 — acrescentada verificação de códigos oficiais B3 IND/DOL versus aliases Profit INDFUT/DOFUT; teste de mapeamento permanece NOT_RUN.


## Correção de escopo — 2026-10-12

O utilizador confirmou que utiliza no Profit seis símbolos: INDFUT, DOFUT, IND, DOL, WIN e WDO, e determinou que a validação use sempre dados históricos já armazenados, sem depender do Profit em tempo real. A identificação operacional dos seis símbolos está registada; instrumento/código B3 efetivo, contrato/vencimento e fonte histórica de abertura devem ser resolvidos a partir do cadastro e dos arquivos versionados, sem presumir equivalência. A auditoria inicial da árvore B3 encontrou COTAHIST anual via Git LFS e datas diárias selecionadas, mas não encontrou RAW BVBG.086.01/BVBG.187.01 nem dados intraday/negócio a negócio em `dados/market_data`; a documentação B3 também declara esses dados pendentes. Foi criada a solicitação de atualização https://github.com/carlos-andrade/B3/issues/6. O plano Módulo 002 tem 44 casos, todos NOT_RUN; esta alteração não certifica a fonte de abertura.


## Política operacional — dados históricos armazenados — 2026-10-12

O utilizador determinou que todas as validações devem usar os dados históricos já armazenados em `carlos-andrade/B3`; não é possível consumir dados do Profit em tempo real neste fluxo. A execução deve ser offline e reproduzível, com fonte, caminho, data de referência, SHA-256, granularidade, parser e cobertura registados. Uma auditoria inicial identificou documentação de Market Data e contratos de ingestão, mas não encontrou arquivos brutos BVBG.086.01/BVBG.187.01 nem datasets intraday/negócio a negócio armazenados em `dados/market_data`; a captura está pendente na documentação de ingestão. Foi aberta a issue [B3 #6](https://github.com/carlos-andrade/B3/issues/6) para completar e documentar a cobertura histórica dos seis símbolos. COTAHIST/EOD só pode ser usado para os instrumentos/campos que sua cobertura e semântica realmente comprovarem. O comportamento runtime de `Open`, `OpenD(0)` e `OpenDaily(0)` no Profit não pode ser certificado apenas com documentação ou datasets externos; permanece explicitamente fora da validação offline.


## Auditoria complementar de cobertura B3 — 2026-10-12

A inspeção detalhada da árvore B3 identificou uma divergência que deve ser resolvida antes da execução dos testes de cobertura:

- `dados/cotahist/raw/anual/`: 41 ZIPs anuais listados, 1986–2026.
- `dados/cotahist/normalized/manifests/`: 41 manifests anuais de qualidade listados.
- `dados/cotahist/normalized/anual/`: apenas 20 CSVs listados — 1986–2004 e 2026. Os CSVs normalizados de 2005–2025 não aparecem nessa pasta apesar de existirem os manifests e os RAW ZIPs.
- `dados/cotahist/raw/diario/` e `dados/cotahist/normalized/diario/`: 15 datas selecionadas, sem série diária contínua demonstrada.
- `dados/market_data/`: documentação e inventário; não foram encontrados datasets brutos BVBG.086.01/BVBG.187.01 nem intraday/negócio a negócio nas pastas inspecionadas.
- Ponteiros de 133/134 bytes podem ser ponteiros Git LFS. Foram confirmados exemplos que declaram objetos reais grandes; não se deve classificar esses ponteiros como ficheiros ausentes. Nesta execução, o conteúdo binário LFS não foi descarregado nem teve o SHA-256 recalculado independentemente.
- O catálogo BVBG.028.02 está armazenado, mas ainda não foi extraído/analisado integralmente para mapear os seis símbolos a códigos e contratos.

Foi publicada a auditoria `GOVERNANCA/AUDITORIA_COBERTURA_B3_MERCADOS_E_LFS_2026-10-12.md` e acrescentada uma atualização à [B3 issue #6](https://github.com/carlos-andrade/B3/issues/6). A issue passa a solicitar reconciliação dos 41 manifests com os 20 CSVs normalizados, matriz por instrumento/contrato e verificação dos hashes LFS.

**Correção de interpretação:** tamanho 133/134 bytes na resposta da API pode representar apenas o ponteiro LFS; não é evidência de que o conteúdo esteja vazio ou ausente. A lacuna comprovada é a ausência de listagem dos CSVs normalizados anuais de 2005–2025, que precisa ser reconciliada com os manifests.

O plano de testes passa de 44 para 46 casos com DS-45 (reconciliação RAW/normalizado/manifests) e DS-46 (verificação independente do conteúdo LFS). Os 46 permanecem `NOT_RUN`. Nenhuma compilação NTSL, execução Profit, replay, backtest ou ordem foi realizada.

### Próxima decisão bloqueante

1. Aguardar a atualização B3 para a lacuna de normalização anual e a matriz de cobertura dos seis símbolos.
2. Verificar os objetos LFS por download e SHA-256 independente em ambiente apropriado.
3. Extrair o cadastro BVBG.028.02 e confirmar código, tipo e vencimento de cada contrato sem equivalências presumidas.
4. Só depois executar DS-18–DS-46 com evidências reproduzíveis. Manter `UNKNOWN/BLOCKED` enquanto faltar fonte/campo/contrato comprovado.
5. Não promover para `main` até revisão e validação dos portões.

- 1.0.9 — 2026-10-12 — auditoria complementar B3; identificada divergência entre 41 RAW/manifests anuais e 20 CSVs normalizados listados; esclarecido o tratamento de ponteiros Git LFS; plano ampliado para 46 casos NOT_RUN.


## Extração efetiva do catálogo B3 — 2026-10-12

Foi processado o conteúdo do CSV versionado `ativos/catalogo/INVENTARIO_B3_2026-09-22.csv`, Git blob SHA `5d88fa0e319d8398e992537de51bda691dc4a5ab` (identificador Git SHA-1, não SHA-256). A extração verificou 120.973 linhas de dados, 32 campos, e 70 contratos futuros datados com ID único, vencimento, multiplicador e CFI preenchidos: 12 IND, 11 WIN, 24 DOL e 23 WDO. Nenhum `TckrSymb` corresponde exatamente aos símbolos `IND`, `INDFUT`, `DOL`, `DOFUT`, `WIN` ou `WDO`.

Evidências:
- `GOVERNANCA/MAPEAMENTO_CATALOGO_B3_ALIASES_E_CONTRATOS_2026-10-12.md`
- `MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/MATRIZ_CONTRATOS_FUTUROS_BVBG028_2026-09-22.csv`
- B3 issue #6: https://github.com/carlos-andrade/B3/issues/6

DS-47 e DS-48 foram executados com resultado PASS, com escopo restrito ao parsing e ao guardrail de não-inferência. **Isto não valida o mapeamento de aliases Profit**: `INDFUT`/ `DOFUT` permanecem UNKNOWN/BLOCKED; os símbolos-base também não são contratos exatos no campo `TckrSymb`. O catálogo não contém preços de abertura nem dados de OHLC/negócios.

O plano passa a 48 casos: DS-47 e DS-48 PASS; DS-45 (reconciliação dos anos normalizados) e DS-46 (download e SHA-256 independente de objetos LFS) continuam NOT_RUN. Não houve execução NTSL/Profit, replay, backtest ou ordens.

- 1.1.0 — 2026-10-12 — catálogo BVBG.028.02 processado; 70 contratos extraídos; DS-47/48 PASS com limites explícitos; aliases sem correspondência exata permanecem bloqueados.


## Correção dinâmica da cobertura COTAHIST — 2026-10-12 13:07 UTC

A auditoria B3 foi reconsultada após a sequência automática de workflows de 2005. O estado mudou: `COTAHIST_A2005.csv` agora está listado em `dados/cotahist/normalized/anual/` e o respetivo manifesto declara `VALIDADO`, 181.408 linhas, 25 campos e período 2005-01-03 a 2005-12-29. O ponteiro LFS declara SHA-256 `9fe7ee30e135223f5d414d7ed678f2973645c2f8779f7e94b7a148794e6a847c` e tamanho 23.748.257 bytes; o conteúdo físico não foi re-hashado independentemente neste ambiente.

A pasta anual lista 21 CSVs (1986–2005 e 2026) e 41 manifests (1986–2026). `COTAHIST_A2006.csv` ainda não aparece no caminho canónico; a FASE00 de 2006 concluiu com sucesso, mas não certifica a normalização. A lacuna atual é 2006–2025. A issue [B3 #6](https://github.com/carlos-andrade/B3/issues/6) foi atualizada com esta correção.

Não marcar DS-45 ou DS-46 como PASS: a reconciliação anual completa e a verificação física independente de LFS continuam pendentes. Os dados COTAHIST permanecem EOD; não demonstram abertura oficial dos seis símbolos de futuros nem substituem dados intraday. DS-47/DS-48 continuam PASS apenas para extração do catálogo/guardrail de não-inferência. Nenhum teste NTSL/Profit, replay, backtest ou ordem foi executado.

- 1.2.0 — 2026-10-12 — atualização dinâmica da cobertura após materialização de COTAHIST 2005; lacuna atual 2006–2025; hashes LFS continuam declarados, não recalculados localmente.


## Bloqueio adicional de integridade anual — COTAHIST 2006 — 2026-10-12

O manifesto `COTAHIST_A2006_quality.json` declara `VALIDADO`, 198.367 linhas, 25 campos, período 2006-01-02 a 2006-12-28 e SHA-256 normalizado `d9025ebcc01413111c67a0bb573f4ff2676aae2105e8204f19d13f9a313ee69d`; contudo, `dados/cotahist/normalized/anual/COTAHIST_A2006.csv` não aparece na árvore e o caminho devolve 404. O estado correto é `MANIFEST_PRESENTE / CSV_CANÓNICO_AUSENTE / UNKNOWN-BLOCKED` até que o artefacto físico seja materializado e verificado ou o manifesto corrigido. A issue [B3 #6](https://github.com/carlos-andrade/B3/issues/6) foi atualizada.

A cobertura atual observada é 21 CSVs anuais (1986–2005 e 2026), 41 manifests (1986–2026), e ausência de CSV canónico listado para 2006–2025. A FASE00 de 2006 com sucesso não certifica a normalização. Não declarar DS-45/DS-46 concluídos. Nenhum teste NTSL/Profit, replay, backtest ou ordem.

- 1.3.0 — 2026-10-12 — registada discrepância entre manifesto VALIDADO e CSV normalizado ausente para 2006; estado bloqueado até prova física.


## Matriz consolidada dos seis símbolos — 2026-10-12

Artefacto persistido:
`MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/MATRIZ_COBERTURA_SEIS_SIMBOLOS_2026-10-12.csv`

A matriz regista, para INDFUT, DOFUT, IND, DOL, WIN e WDO, a correspondência exata observada no BVBG.028.02, a família de contratos datados encontrada, o estado das fontes EOD/intraday, a lacuna anual COTAHIST e o estado do campo de abertura. A extração do catálogo encontrou 70 contratos (IND 12, WIN 11, DOL 24, WDO 23), mas zero correspondências exatas dos seis símbolos-base em `TckrSymb`. Todos os símbolos permanecem `UNKNOWN/BLOCKED` para validação de abertura.

O estado COTAHIST foi atualizado dinamicamente: 21 CSVs anuais listados (1986–2005 e 2026), 41 manifests; 2006–2025 sem CSV canónico listado, e 2006 tem manifesto `VALIDADO` sem o CSV no caminho canónico. B3 issue #6 foi atualizada para solicitar a reconciliação.

- 1.4.0 — 2026-10-12 — publicada matriz operacional de cobertura dos seis símbolos; mantém os bloqueios de alias, abertura, anos normalizados e LFS.


## Evidência CI de Git LFS — COTAHIST 2005 — 2026-10-12

A execução [B3 FASE10 2005](https://github.com/carlos-andrade/B3/actions/runs/38253210219) terminou com success. O log comprova checkout com Git LFS ativo e cálculo independente de SHA-256 dos bytes de RAW e NORMALIZED, com correspondência ao manifesto/sidecar e comparação integral de 25 campos.

- RAW SHA-256: `41eac6d743d9c3e812bb001c4d327582fa7c408dbc99ff4a1734698da8b18f52`.
- NORMALIZED SHA-256: `9fe7ee30e135223f5d414d7ed678f2973645c2f8779f7e94b7a148794e6a847c`.
- Contagem RAW/NORMALIZED: 181.408/181.408; divergências: 0.
- Estado de teste: DS-46 = `PARTIAL_PASS_2005`; não se generaliza para os outros objetos LFS.
- DS-45 permanece NOT_RUN; a reconciliação anual não terminou. O CSV 2006 continua ausente apesar do manifesto VALIDADO.
- A abertura dos seis símbolos permanece UNKNOWN/BLOCKED; esta prova é apenas da integridade do dataset COTAHIST 2005, não da sua aplicabilidade a futuros.

- 1.5.0 — 2026-10-12 — evidência CI LFS/RAW/NORMALIZED de 2005 incorporada; DS-46 parcialmente aprovado apenas para esse objeto.


## Probe offline COTAHIST 2026-10-09 — 2026-10-12

Foi processado o CSV diário `COTAHIST_D09102026.csv` armazenado em B3. O manifesto declara VALIDADO, 19.213 registos e 25 campos. No conteúdo lido, as correspondências exatas de `CODNEG` para os seis símbolos foram zero. Os quatro prefixos DOL (`DOLA11`, `DOLB11`, `DOLX11`, `DOLL39`) não bastam para mapear contratos. Uma expressão regular frouxa também encontra `DOLX11`, mas os campos (`NOMRES=TREND DOLAR`, `ESPECI=CI`, `TPMERC=010`, `CODBDI=14`) não confirmam um futuro.

Evidência: `MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/PROBE_COTAHIST_D09102026_COBERTURA_SIMBOLOS.csv`. DS-49 = PASS apenas para o probe de uma data; não prova ausência em outros pregões ou fontes. DS-45 continua NOT_RUN; DS-46 PARTIAL_PASS_2005. A abertura dos seis símbolos permanece UNKNOWN/BLOCKED.

- 1.6.0 — 2026-10-12 — acrescentado probe offline de um pregão e guardrail contra falsos positivos por prefixo.


## Correção do probe COTAHIST — 15 pregões selecionados — 2026-10-12

A auditoria foi ampliada aos 15 CSVs diários versionados entre 2026-09-21 e 2026-10-09: 253.156 registos, 25 campos por ficheiro. Foram encontradas zero correspondências exatas para IND/INDFUT/DOL/DOFUT/WIN/WDO. Uma expressão regular frouxa encontrou 15 ocorrências de `DOLX11`, uma por ficheiro; o registo apresenta `NOMRES=TREND DOLAR`, `ESPECI=CI`, `TPMERC=010`, `CODBDI=14` e não está confirmado como futuro. **Candidatos sintáticos não são contratos futuros confirmados.** Não foram confirmados contratos futuros das famílias-alvo neste conjunto diário.

Artefacto por pregão: `MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/PROBE_COTAHIST_DIARIO_SELECIONADO_20260921_20261009.csv`. O artefacto de 2026-10-09 também foi corrigido para registar o candidato regex-only.

DS-49 PASS significa que a leitura e o guardrail foram executados nos 15 ficheiros; o resultado não prova ausência em datas não armazenadas. DS-45 continua NOT_RUN; DS-46 PARTIAL_PASS_2005; abertura dos seis símbolos UNKNOWN/BLOCKED.

- 1.7.0 — 2026-10-12 — ampliado probe a 15 ficheiros e corrigido falso positivo DOLX11.
