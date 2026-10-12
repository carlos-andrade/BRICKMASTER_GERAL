---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "AUDITORIA_DE_COBERTURA_DE_DADOS"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-002-AUDITORIA-B3-COBERTURA-2026-10-12"
titulo: "Auditoria de cobertura B3 — COTAHIST, Git LFS e market data"
status: "AUDITORIA_DA_ARVORE_CONCLUIDA; COBERTURA_SEMANTICA_DOS_SEIS_SIMBOLOS_NAO_CONFIRMADA"
versao: "1.6.0"
data_criacao: "2026-10-12"
data_atualizacao: "2026-10-12"
origem: "Inspeção de diretórios, manifests, metadados Git LFS e documentação no repositório público carlos-andrade/B3"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase02-auditoria-b3-cobertura"
escopo: "Verificar materialização, integridade declarada e limites de cobertura de dados históricos necessários ao Módulo 002"
objetivo: "Separar arquivos RAW, dados normalizados, manifests, objetos Git LFS e cobertura semântica comprovada"
dependencias: "B3 issue #6; AUDITORIA_FONTE_ABERTURA_OFICIAL_NTSL44.md; PLANO-DE-TESTES.md"
---

# Auditoria de cobertura B3 — COTAHIST, Git LFS e market data

## Contexto Histórico

Em 2026-10-12, após a política operacional determinar que as validações do BRICKMASTER devem usar apenas dados históricos armazenados em `carlos-andrade/B3`, foi feita uma inspeção adicional das árvores RAW, normalizada, manifests e Market Data. Esta auditoria complementa a auditoria inicial; não substitui os artefactos históricos nem afirma que os datasets foram integralmente descarregados ou processados neste passo.

## Estado

**Auditoria estrutural da árvore: CONCLUÍDA.**  
**Cobertura por instrumento/contrato e campo de abertura para INDFUT, DOFUT, IND, DOL, WIN e WDO: NÃO CONFIRMADA.**  
**Execução dos 44 testes anteriores do Módulo 002: NÃO REALIZADA.**  
**Testes adicionais DS-45/DS-46: planeados, NOT_RUN.**

## Evidências verificadas

### 1. COTAHIST RAW anual

A listagem de `dados/cotahist/raw/anual/` contém 41 arquivos ZIP anuais, de 1986 a 2026, além de `.gitkeep`. Os nomes e tamanhos dos objetos são visíveis na API do repositório. A presença do arquivo não certifica por si só a cobertura dos instrumentos-alvo nem a semântica da abertura para futuros.

### 2. Manifests e normalizados anuais

A listagem de `dados/cotahist/normalized/manifests/` contém 41 manifests de qualidade `COTAHIST_AYYYY_quality.json`, de 1986 a 2026. O documento `docs/ingestao/CERTIFICACAO_ANUAL_COTAHIST_1986_2026_V1.0.md` declara 41/41 manifests com estado `VALIDADO`, parser 1.1.0, 25 campos, zero datas inválidas e zero datas fora do ano. Esta é a certificação estrutural definida por esse projeto; não equivale à certificação semântica do BRICKMASTER.

A listagem de `dados/cotahist/normalized/anual/`, porém, contém apenas 20 CSVs: 1986–2004 e 2026. Os CSVs anuais de 2005–2025 não aparecem nessa pasta, embora existam os respetivos manifests de qualidade e os RAW ZIPs anuais. Esta é uma divergência concreta entre os artefactos listados e deve ser resolvida no repositório B3: materializar/restaurar os normalizados em falta ou ajustar a certificação e documentar a decisão. Não presumir que os manifests substituem os arquivos normalizados.

### 3. Interpretação correta de Git LFS

Um item listado pela API de Contents com tamanho 133/134 bytes pode ser um **ponteiro Git LFS**, não um CSV vazio nem um arquivo ausente. Foram inspecionados os conteúdos dos ponteiros para:

- `COTAHIST_A1986.csv`: objeto SHA-256 `fbd00ff5b24075813132193dc794e29015df20b7dc6bedadba7e896b30406329`, tamanho declarado 21.854.078 bytes; o manifest declara 177.981 linhas normalizadas.
- `COTAHIST_A1988.csv`: objeto SHA-256 `d4d9ae5cd4106967a195567278b44a9a71d788203d10a7372b98ce6fb1691a03`, tamanho declarado 19.387.364 bytes; o manifest declara 167.674 linhas normalizadas.
- `COTAHIST_A2026.csv`: objeto SHA-256 `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`, tamanho declarado 392.044.266 bytes; o manifest declara 2.919.760 linhas, período 2026-01-02 a 2026-09-23.

Os hashes e tamanhos acima são metadados declarados nos ponteiros/manifests. **Não foi descarregado nem re-hashado o conteúdo binário LFS nesta execução**; portanto, a igualdade entre conteúdo efetivo e hash declarado ainda requer verificação independente. Esta auditoria corrige qualquer interpretação anterior que tenha tratado automaticamente o tamanho do ponteiro como ausência de dados.

### 4. COTAHIST RAW/normalizado diário

Foram listados 15 pares de ZIP RAW e CSV normalizado para datas selecionadas entre 2026-09-21 e 2026-10-09. A seleção não é uma série diária contínua; não usar os dias presentes como prova de cobertura dos pregões em falta.

### 5. Catálogo de instrumentos

O repositório contém `ativos/catalogo/INVENTARIO_B3_2026-09-22.csv` (listagem de 18.202.864 bytes) e o arquivo bruto `ativos/catalogo/raw/IN260922.zip` (20.151.525 bytes). Os dados são relevantes para resolver identidade, tipo e vencimento do instrumento. A inspeção desta sessão não extraiu o ZIP nem analisou integralmente as linhas do CSV; logo, nenhum mapeamento entre aliases Profit e instrumentos B3 foi certificado.

### 6. Market Data e microestrutura

A árvore inspecionada de `dados/market_data/` contém README, matriz de provedores/granularidade, inventário da Pesquisa por Pregão e README nas subpastas `historico/` e `microestrutura/`. Não foram encontrados arquivos de dados BVBG.086.01/BVBG.187.01 ou datasets intraday/negócio a negócio nessas pastas. Os contratos de ingestão do próprio repositório registam captura intraday e negócio a negócio como pendente.

### 7. Consequência para os seis símbolos

| Símbolo utilizado | Mapeamento B3/contrato | Campo de abertura histórico aplicável | Estado |
|---|---|---|---|
| INDFUT | Não demonstrado nesta auditoria | Não confirmado | UNKNOWN/BLOCKED |
| DOFUT | Não demonstrado nesta auditoria | Não confirmado | UNKNOWN/BLOCKED |
| IND | Não demonstrado por linha/contrato | Não confirmado | UNKNOWN/BLOCKED |
| DOL | Não demonstrado por linha/contrato | Não confirmado | UNKNOWN/BLOCKED |
| WIN | Não demonstrado por linha/contrato | Não confirmado | UNKNOWN/BLOCKED |
| WDO | Não demonstrado por linha/contrato | Não confirmado | UNKNOWN/BLOCKED |

Não presumir que `INDFUT=IND` nem `DOFUT=DOL`. COTAHIST é uma fonte EOD; só pode ser usada para um instrumento se o registo real, o código de mercado e a semântica do campo demonstrarem que se aplica ao contrato. Não substitui intraday/tick quando a validação requer essa granularidade.

## Validação e limitações

A validação executada neste passo foi uma inspeção de diretórios, nomes, tamanhos, metadados de ponteiros LFS, manifests e documentação. Não houve download/extração de objetos LFS, leitura integral dos CSVs anuais, extração do catálogo BVBG.028.02, cálculo independente de SHA-256 dos objetos grandes, compilação NTSL, execução no Profit, replay, backtest ou envio de ordens.

A ausência de prova de cobertura não é prova de que o instrumento não exista nos arquivos; significa que a cobertura ainda não foi extraída e demonstrada com evidência reproduzível.

## Resultado

1. COTAHIST RAW anual: 41 ZIPs listados (1986–2026).
2. Manifests de qualidade anuais: 41 listados.
3. CSVs normalizados anuais listados: 20 (1986–2004 e 2026); falta materialização listada para 2005–2025.
4. COTAHIST diário: 15 datas selecionadas, sem continuidade diária demonstrada.
5. Objetos LFS: ponteiros identificados; conteúdo binário e hashes não revalidados independentemente nesta execução.
6. Market Data intraday/negócio a negócio: captura continua pendente na documentação consultada.
7. Cobertura dos seis símbolos e campo de abertura: não certificada.
8. Testes Módulo 002: manter NOT_RUN até que os dados necessários sejam extraídos, verificados e associados aos contratos corretos.

## Próxima Ação

1. Acompanhar B3 issue #6 e pedir a reconciliação dos 41 manifests com os 20 CSVs normalizados anuais atualmente listados.
2. Restaurar/materializar os normalizados de 2005–2025 ou corrigir a certificação para refletir a ausência; preservar RAW, histórico e checksums.
3. Extrair o catálogo BVBG.028.02 e gerar uma matriz por símbolo, código B3, tipo de instrumento, contrato/vencimento e data de referência.
4. Produzir cobertura COTAHIST por `CODNEG`, `TPMERC`, `CODBDI`, datas e campos relevantes, com amostras e hashes de entrada; não inferir cobertura dos futuros pelo ticker.
5. Verificar independentemente o conteúdo e SHA-256 dos objetos LFS quando disponíveis num ambiente de ingestão.
6. Só então executar DS-18–DS-46 com resultados e artefactos reproduzíveis. Não promover testes por existência de manifests.
7. Manter `main` sem alterações até revisão da PR desta auditoria.

## Histórico de versões

- 1.0.0 — 2026-10-12 — auditoria estrutural da árvore B3; identificada divergência entre 41 RAW/manifests anuais e 20 CSVs normalizados anuais listados; distinção explícita entre ponteiro Git LFS e conteúdo verificado; cobertura dos seis símbolos permanece UNKNOWN/BLOCKED.


## Atualização de estado após workflows B3 — 2026-10-12 13:07 UTC

A auditoria estrutural inicial registou 20 CSVs normalizados anuais e identificou 2005–2025 como lacuna. A árvore mudou durante o acompanhamento: o ficheiro anual de 2005 foi materializado/versionado após a sequência de workflows B3 de 2005.

Evidência atual consultada em `main`:
- `dados/cotahist/normalized/anual/COTAHIST_A2005.csv` existe como ponteiro Git LFS com SHA-256 declarado `9fe7ee30e135223f5d414d7ed678f2973645c2f8779f7e94b7a148794e6a847c`, tamanho declarado 23.748.257 bytes.
- `COTAHIST_A2005_quality.json` declara `VALIDADO`, 181.408 linhas, 25 campos, período 2005-01-03 a 2005-12-29 e o mesmo hash declarado para o normalizado.
- Workflows de recuperação, validação independente, certificação e transição de 2005 aparecem como `success`, incluindo [FASE10](https://github.com/carlos-andrade/B3/actions/runs/38253210219), [FASE11](https://github.com/carlos-andrade/B3/actions/runs/38253300794) e [FASE12](https://github.com/carlos-andrade/B3/actions/runs/38253381813).
- A pasta anual lista agora 21 CSVs: 1986–2005 e 2026. Os manifests continuam listados para 1986–2026 (41 anos).
- `COTAHIST_A2006.csv` ainda não aparece na pasta anual consultada; a FASE00 de 2006 terminou com sucesso, mas isso não significa que o normalizado de 2006 esteja concluído.
- O hash declarado para 2005 foi lido do ponteiro/manifeste; o objeto LFS físico não foi descarregado nem re-hashado independentemente neste ambiente.

**Estado corrigido:** a lacuna de materialização anual observada na consulta atual é 2006–2025 (20 anos), não 2005–2025. O número de CSVs versionados é 21, não 20. A cobertura dos instrumentos-alvo e a semântica EOD para futuros continuam por comprovar. A lista deve continuar a ser atualizada porque os workflows B3 estão a avançar por fases.

A solicitação foi atualizada em [B3 issue #6](https://github.com/carlos-andrade/B3/issues/6). Os testes DS-45 (reconciliação completa) e DS-46 (verificação física independente de LFS) permanecem `NOT_RUN`.


## Discrepância de 2006: manifesto sem CSV canónico — 2026-10-12

A reconsulta da árvore B3 encontrou uma divergência específica para 2006:

- O manifesto `dados/cotahist/normalized/manifests/COTAHIST_A2006_quality.json` declara `status=VALIDADO`, 198.367 linhas, 25 campos, período 2006-01-02 a 2006-12-28 e SHA-256 normalizado declarado `d9025ebcc01413111c67a0bb573f4ff2676aae2105e8204f19d13f9a313ee69d`.
- A consulta ao caminho `dados/cotahist/normalized/anual/COTAHIST_A2006.csv` devolve 404 e o ficheiro não aparece na listagem da pasta anual.
- A FASE00 de governança 2006 concluiu com `success`, mas não certifica a existência física do CSV.

Classificação: `MANIFEST_PRESENTE / CSV_CANÓNICO_AUSENTE / UNKNOWN-BLOCKED`. Não aceitar o estado do manifesto como substituto do arquivo. A B3 issue #6 foi atualizada para pedir materialização/prova física do CSV, ou correção do manifesto se prematuro.

O estado atual observado é: 21 CSVs listados (1986–2005 e 2026), 41 manifests anuais (1986–2026), com 2006–2025 sem CSV canónico listado. Em 2006 há evidência de manifesto mas falta o artefacto no caminho esperado. Hashes declarados por ponteiro/manifesto não foram recalculados fisicamente neste ambiente.

DS-45 continua NOT_RUN porque a reconciliação anual completa não está concluída; DS-46 continua NOT_RUN porque não houve download LFS e verificação independente do SHA-256. A lacuna de abertura para futuros permanece separada desta auditoria COTAHIST.


## Matriz operacional por símbolo — 2026-10-12

Foi criada a matriz CSV de cobertura dos seis símbolos, com uma linha por símbolo e campos para correspondência exata do catálogo, família de contratos datados, estado COTAHIST EOD, lacunas de anos, presença de intraday/tick, campo de abertura, estado do alias e próxima ação:

`MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/MATRIZ_COBERTURA_SEIS_SIMBOLOS_2026-10-12.csv`

A matriz distingue família de contrato da resolução do alias Profit. Todos os seis permanecem `UNKNOWN/BLOCKED` para validação de abertura; `INDFUT` e `DOFUT` não são associados a IND/DOL por inferência. A situação de COTAHIST 2006 continua `MANIFEST_PRESENTE / CSV_CANÓNICO_AUSENTE`.

- 1.3.0 — 2026-10-12 — adicionada matriz operacional CSV dos seis símbolos, com fonte, granularidade, cobertura e bloqueios.


## Prova física de Git LFS — COTAHIST 2005 — 2026-10-12

A verificação dos logs da execução [B3 FASE10 — Validação Independente Integral 2005](https://github.com/carlos-andrade/B3/actions/runs/38253210219) encontrou uma prova física bem-sucedida do objeto LFS de 2005. O workflow usa checkout com `lfs: true`, calcula SHA-256 dos bytes de RAW e NORMALIZED e compara o NORMALIZED com manifesto e sidecar.

Resultado registado no log:
- `status=VALIDADO`; `decision=LIBERADO_PARA_FASE11`
- RAW SHA-256: `41eac6d743d9c3e812bb001c4d327582fa7c408dbc99ff4a1734698da8b18f52`
- NORMALIZED SHA-256: `9fe7ee30e135223f5d414d7ed678f2973645c2f8779f7e94b7a148794e6a847c`
- 181.408 registos RAW e 181.408 normalizados; 25 campos verificados; zero divergências.

**Correção de escopo:** o objeto NORMALIZED de 2005 tem prova de integridade via CI; não foi recalculado localmente nesta sessão. Isto constitui progresso parcial do requisito LFS, não certifica todos os objetos anuais. DS-46 fica `PARTIAL_PASS_2005`; os restantes objetos LFS continuam sem prova independente. DS-45 continua NOT_RUN e o problema 2006 persiste: manifesto `VALIDADO` sem CSV canónico listado.

- 1.4.0 — 2026-10-12 — incorporada evidência CI de SHA-256 físico e validação independente de COTAHIST 2005; DS-46 passa parcialmente apenas para 2005.


## Probe offline de cobertura COTAHIST — pregão 2026-10-09

Foi processado o CSV diário versionado `dados/cotahist/normalized/diario/COTAHIST_D09102026.csv`, identificado pelo Git blob SHA `ec8c33a699f2ef5b1bb88b919b30852b904a069b` (SHA Git, não SHA-256). O manifesto correspondente declara `VALIDADO`, 19.213 registos, 25 campos, data 2026-10-09 e SHA-256 normalizado `f39ec9919b27aa5716a2aa4cebea852f38849389067627238bf2bcf8e17eeed2`.

Resultado do parsing do conteúdo armazenado:
- 19.213 registos de dados e 25 campos.
- Correspondências exatas em `CODNEG` para `IND`, `INDFUT`, `DOL`, `DOFUT`, `WIN` e `WDO`: zero.
- Tickers que começam por `IND`, `WIN` ou `WDO`: zero.
- Quatro tickers começam por `DOL`: `DOLA11`, `DOLB11`, `DOLX11`, `DOLL39`. `DOLX11` também corresponde a uma expressão regular frouxa de ticker futuro, mas os campos disponíveis mostram `NOMRES=TREND DOLAR`, `ESPECI=CI`, `TPMERC=010`, `CODBDI=14`; não é um futuro confirmado. Tanto o prefixo como a expressão regular isolada podem gerar falsos positivos.
- Nenhum contrato futuro foi confirmado nesta data; foi identificado um candidato regex-only (`DOLX11`) que não pode ser classificado como futuro sem atributos oficiais adicionais.

A evidência foi persistida em `MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/PROBE_COTAHIST_D09102026_COBERTURA_SIMBOLOS.csv`; DS-49 fica PASS apenas para este probe negativo de uma data. Não prova ausência em todos os dias, anos ou fontes. COTAHIST é EOD e este resultado não valida a abertura dos seis símbolos. DS-45 continua NOT_RUN; DS-46 é PARTIAL_PASS_2005 apenas para o objeto COTAHIST 2005.

- 1.5.0 — 2026-10-12 — probe offline de 2026-10-09 executado e registado; DS-49 PASS com escopo de uma data; prefixos DOL não tratados como contratos automaticamente.


## Correção e ampliação do probe diário — 15 pregões — 2026-10-12

Uma revisão da regra do probe identificou que a expressão regular `^(IND|DOL|WIN|WDO)[FGHJKMNQUVXZ]\d{2}$` é insuficiente: `DOLX11` corresponde à expressão, mas o CSV diário apresenta `NOMRES=TREND DOLAR`, `ESPECI=CI`, `TPMERC=010`, `CODBDI=14`. A evidência disponível não confirma que esse registo seja um contrato futuro. O probe foi corrigido para separar **candidato sintático** de **contrato futuro confirmado**.

Foram processados todos os 15 CSVs diários listados em `dados/cotahist/normalized/diario/` para datas entre 2026-09-21 e 2026-10-09:
- 15 ficheiros; 253.156 registos no total; 25 campos por ficheiro.
- Correspondências exatas em `CODNEG` para os seis símbolos-base: zero.
- Candidatos regex-only: 15 no total, um por ficheiro, todos `DOLX11`.
- Contratos futuros confirmados por esta fonte/probe: zero.
- Prefixos DOL também incluem `DOLA11`, `DOLB11` e `DOLL39`; prefixo não é identidade de contrato.

Artefactos:
- `MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/PROBE_COTAHIST_D09102026_COBERTURA_SIMBOLOS.csv` — resumo dos seis símbolos no pregão 2026-10-09, corrigido.
- `MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/PROBE_COTAHIST_DIARIO_SELECIONADO_20260921_20261009.csv` — resumo por cada um dos 15 CSVs e identificação do candidato regex-only.

DS-49 PASS passa a significar que a leitura dos 15 ficheiros, a contagem e o guardrail contra falsos positivos foram executados. Não significa ausência universal de futuros no COTAHIST: o resultado limita-se aos 15 ficheiros armazenados. A cobertura dos seis símbolos e a fonte de abertura continuam UNKNOWN/BLOCKED.

- 1.6.0 — 2026-10-12 — probe ampliado a 15 ficheiros; corrigido falso positivo DOLX11; distinção explícita entre regex-only e futuro confirmado.
