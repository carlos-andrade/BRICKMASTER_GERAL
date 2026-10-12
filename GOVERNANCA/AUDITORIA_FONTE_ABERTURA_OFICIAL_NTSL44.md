---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "AUDITORIA_DE_FONTE"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-AUDITORIA-FONTE-NTSl44"
titulo: "Auditoria documental — candidatos à abertura oficial no Manual NTSL 4.4"
status: "REVISAO_DOCUMENTAL; VALIDACAO_PROFIT_PENDENTE; DADOS_HISTORICOS_B3_SEIS_SIMBOLOS_SEM_PROFIT_TEMPO_REAL"
versao: "0.9.0"
data_criacao: "2026-10-12"
data_atualizacao: "2026-10-12"
origem: "Manual NTSL versão 4.4 — 03-08-2026, ficheiro fornecido no projeto"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/auditoria-fonte-abertura-ntsl44"
escopo: "Avaliar o que a documentação NTSL 4.4 prova e não prova sobre o preço oficial de abertura"
objetivo: "Evitar equiparar abertura de candle ou série diária ao preço oficial sem validação"
dependencias: "Manual NTSL 4.4; Módulo 002; plataforma Profit; fonte oficial validada"
---

# Auditoria documental — candidatos à abertura oficial no Manual NTSL 4.4

## Contexto Histórico

Em 2026-10-12 foi aprovada a política B: usar o preço oficial de abertura fornecido pela plataforma ou por uma fonte oficial validada. Esta auditoria verifica apenas o suporte documental do Manual NTSL 4.4; não demonstra comportamento observado no Profit.

## Estado

REVISÃO DOCUMENTAL CONCLUÍDA; validação deve usar somente dados históricos já armazenados no repositório B3; não usar Profit em tempo real. Símbolos abrangidos: INDFUT, DOFUT, IND, DOL, WIN e WDO. Cobertura de dados por símbolo/contrato ainda precisa ser verificada nos artefactos versionados; não há restrição a gráfico de 60.000 ticks.

## Achados suportados pelo Manual 4.4

1. **Série `Open`:** a secção 4.2, página impressa 6, define Abertura/Open como o valor de abertura de cada candle. Isso é uma abertura de candle, não uma declaração geral de que o valor corresponde ao preço oficial de abertura da sessão.
2. **`OpenD(DaysAgo)`:** secção 16.45, página impressa 156, descreve o valor de abertura de um número de dias atrás. O manual apresenta `OpenD(0)` noutro exemplo como abertura do dia atual, mas essa ocorrência isolada não prova, por si só, a equivalência à abertura oficial para todos os instrumentos, sessões, leilões e tipos de gráfico.
3. **`OpenDaily(DaysBack)`:** secção 20.90, página impressa 357, descreve um valor de abertura diário segundo o deslocamento e exemplifica a abertura do dia anterior. A semântica exata para o dia atual e o contexto de execução tem de ser testada na versão concreta do Profit.
4. **Séries de ativo com período diferente:** a secção 4.4, páginas impressas 6–7, alerta que dados obtidos via `Asset` com período divergente podem não coincidir com o valor esperado. Recomenda especificar explicitamente a série desejada, por exemplo `itDaily`. Mesmo essa recomendação não substitui a validação empírica da política B.
5. **`Time()`:** a secção 16.55 define a hora de abertura do candle atual. Não é uma fonte do preço oficial de abertura da sessão.

## Conclusão técnica

O Manual 4.4 oferece candidatos para investigação — `OpenD(0)`, `OpenDaily(0)` e uma série diária explícita — mas a documentação consultada não permite declarar qualquer um deles como fonte oficial universal já validada. Não codificar a escolha como facto confirmado.

## Plano de validação offline com dados históricos armazenados

Usar exclusivamente arquivos já versionados no repositório B3. Para cada símbolo — INDFUT, DOFUT, IND, DOL, WIN e WDO — e cada data coberta, registar:
- ticker/contrato e vencimento, plataforma/feed e versão do Profit;
- nome e semântica do campo de abertura presente no arquivo histórico oficial, quando fornecido;
- data de pregão, sessão/fuso apenas quando constarem da fonte ou de contrato documentado;
- campos OHLC efetivamente presentes no dataset e sua semântica documentada; não simular valores de `OpenD(0)`, `OpenDaily(0)` ou `Open` do Profit;
- valor de abertura disponível na fonte histórica armazenada e referência documental da fonte;
- comparação entre arquivos/camadas armazenadas apenas quando tiverem mesma data, instrumento, contrato e semântica;
- caminho, hash SHA-256, data de referência, versão do parser, cobertura e discrepâncias; anexar evidências ao repositório.

Critério: aprovar a fonte histórica para cálculo offline apenas após confirmar arquivo armazenado, integridade, cobertura do instrumento/contrato, semântica do campo e repetibilidade. Se o campo ou instrumento não existir na base, registar lacuna e manter `UNKNOWN`/`BLOCKED`. Esta validação offline não certifica o comportamento de funções NTSL no runtime do Profit; isso exigirá posteriormente um teste específico quando houver exportação/evidência armazenada do Profit.

## Matriz de validação offline — seis símbolos e dados armazenados

A validação abrangerá INDFUT, DOFUT, IND, DOL, WIN e WDO usando apenas dados históricos armazenados. A declaração do operador confirma os símbolos usados no Profit, mas não prova mapeamento entre eles. Cada linha deve identificar fonte, caminho de arquivo, hash, data de pregão, código B3/ativo, contrato/vencimento quando disponível e cobertura. A periodicidade de gráfico não é dependência da validação offline.

| Símbolo | Estado da identificação | Verificação obrigatória na base armazenada |
|---|---|---|
| `INDFUT` | Símbolo usado pelo operador; mapeamento histórico não provado | Procurar cobertura/mapeamento em cadastro e datasets B3 armazenados; se ausente, lacuna explícita |
| `DOFUT` | Símbolo usado pelo operador; mapeamento histórico não provado | Procurar cobertura/mapeamento em cadastro e datasets B3 armazenados; se ausente, lacuna explícita |
| `IND` | Símbolo usado pelo operador; contrato/vencimento pendentes | Localizar código/contrato e campo de abertura em dados armazenados adequados a futuros |
| `DOL` | Símbolo usado pelo operador; contrato/vencimento pendentes | Localizar código/contrato e campo de abertura em dados armazenados adequados a futuros |
| `WIN` | Símbolo usado pelo operador; contrato/vencimento pendentes | Localizar código/contrato e campo de abertura em dados armazenados adequados a futuros |
| `WDO` | Símbolo usado pelo operador; contrato/vencimento pendentes | Localizar código/contrato e campo de abertura em dados armazenados adequados a futuros |

Para cada um dos seis símbolos, preencher os seguintes campos independentemente:

| Dimensão | Evidência requerida | Regra de aceitação |
|---|---|---|
| Gráfico utilizado | Tipo e periodicidade reais do Profit | Não exigir 60.000 ticks |
| Referência histórica | Campo de abertura/OHLC no arquivo armazenado, quando existente | Não inferir campo que não esteja no layout/dataset |
| Campo `open` da fonte | Valor armazenado e semântica documentada | Não confundir com abertura de candle do Profit |
| `OpenD(0)` | Não executável offline sem output armazenado do Profit | Manter sem validação runtime; não sintetizar valor |
| `OpenDaily(0)` | Não executável offline sem output armazenado do Profit | Manter sem validação runtime; não sintetizar valor |
| Série histórica diária | Fonte, caminho, hash e campos presentes | Comparar somente com outra fonte de semântica compatível |
| Reprocessamento | Mesmo arquivo/hash e mesma versão do parser | Resultado determinístico; sem alterações silenciosas |
| Resultado | PASS/FAIL/BLOCKED com evidência | Sem arquivo/campo/contrato comprovado: `UNKNOWN/BLOCKED` |

### Procedimento de recolha

1. Inventariar apenas arquivos já armazenados em `carlos-andrade/B3`, começando por manifestos, COTAHIST normalizado, cadastro BVBG.028.02 e diretórios `dados/market_data`/`dados/bdi`.
2. Para cada arquivo candidato, verificar existência do conteúdo efetivo, SHA-256, data de referência, layout e status do manifesto.
3. Inspecionar o layout do arquivo armazenado e identificar se contém preço de abertura, OHLC, instrumento, contrato/vencimento e granularidade necessários.
4. Cruzar cada símbolo com o cadastro histórico de instrumentos. Não mapear INDFUT/DOFUT para IND/DOL por suposição.
5. Comparar fontes armazenadas apenas quando instrumento, contrato, data e semântica forem compatíveis. Separar EOD de intraday/tick.
6. Reprocessar os mesmos arquivos e confirmar determinismo. Registar datas ausentes, campos ausentes e discrepâncias.
7. Se a base não cobrir um símbolo/contrato/campo, não criar dados substitutos: registar a lacuna e solicitar a atualização no repositório B3. A execução de `OpenD`/`OpenDaily` no Profit fica fora do escopo offline.

## Evidências

- Manual NTSL 4.4, secção 4.2, página impressa 6: definição da série `Open`.
- Manual NTSL 4.4, secção 4.4, páginas impressas 6–7: ressalva sobre `Asset` com período divergente.
- Manual NTSL 4.4, secção 16.45, página impressa 156: `OpenD`.
- Manual NTSL 4.4, secção 16.55: `Time()`.
- Manual NTSL 4.4, secção 20.90, página impressa 357: `OpenDaily`.

## Verificação cruzada do repositório B3

Repositório consultado: https://github.com/carlos-andrade/B3, branch `main`.

Achados documentais:

- `docs/ingestao/PARTE01_CONTRATO_NORMALIZED_COTAHIST_V1.0.md` define o COTAHIST como série histórica de cotações EOD e documenta o campo `preabe` (posições 57–69) como preço de abertura diário.
- `dados/market_data/README.md` declara que `BVBG.186.01` e `BVBG.187.01` são relatórios simplificados EOD e não devem ser tratados como feed tick a tick.
- `docs/ingestao/PARTE03_B3_INTRADAY_CONTRATO_V1.0.md` e `docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_CONTRATO_V1.1.md` indicam que a captura dos binários intraday/negócio a negócio e a validação do dataset continuam pendentes no estado documentado.
- O ficheiro COTAHIST diário de 2026-10-09 tem manifesto `VALIDADO`, 19.213 linhas e 25 campos. A leitura pesquisável do CSV não encontrou linhas com os símbolos `WIN` ou `WDO`; este resultado não prova ausência em todas as datas, mas não fornece uma abertura de contrato para os instrumentos-alvo.

Conclusão da auditoria da árvore: há COTAHIST RAW anual e diário selecionado, manifestos de qualidade e dataset anual 2026 via Git LFS; a cobertura de futuros/símbolos-alvo ainda precisa ser medida a partir do conteúdo efetivo. `dados/market_data/` contém READMEs/inventário, mas não foram encontrados arquivos RAW BVBG.086.01/BVBG.187.01 nem arquivos tick/negócio a negócio nessa camada. `dados/bdi/2026/` apresenta README sem datasets de negócio a negócio na árvore inspecionada. A documentação de intraday/negócio a negócio já declara a captura pendente. Assim, não há base evidencial suficiente para validar offline a abertura dos seis símbolos; o gap foi formalmente solicitado em https://github.com/carlos-andrade/B3/issues/6.

A consulta às páginas oficiais B3 indica `IND` e `DOL` para futuros cheios e `WIN`/`WDO` para minicontratos. O operador confirmou que usa também os símbolos `INDFUT` e `DOFUT`. Esta confirmação define o escopo, mas não prova que sejam aliases equivalentes nem identifica o vencimento. O cadastro BVBG.028.02 armazenado deve ser usado para mapear o instrumento quando houver correspondência verificável.

Fontes oficiais adicionais:
- https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/futuro-de-ibovespa.htm
- https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/mercado-de-acoes/mercado-futuro.htm

Referências B3:
- https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/PARTE01_CONTRATO_NORMALIZED_COTAHIST_V1.0.md
- https://github.com/carlos-andrade/B3/blob/main/dados/market_data/README.md
- https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/PARTE03_B3_INTRADAY_CONTRATO_V1.0.md
- https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_CONTRATO_V1.1.md
- https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/normalized/manifests/diario/COTAHIST_D09102026_quality.json

## Validação

Revisão estática da árvore e dos manifestos armazenados. Não houve download/extração dos binários Git LFS neste passo, análise completa de todas as linhas COTAHIST, compilação NTSL, replay, backtest ou teste no Profit. Os dados necessários para validar os seis instrumentos ainda não estão demonstrados como disponíveis em forma diretamente utilizável.

## Adenda — cobertura física e Git LFS — 2026-10-12

A auditoria complementar está documentada em [AUDITORIA_COBERTURA_B3_MERCADOS_E_LFS_2026-10-12.md](AUDITORIA_COBERTURA_B3_MERCADOS_E_LFS_2026-10-12.md). Os resultados que afetam esta auditoria são:

- Existem 41 RAW ZIPs anuais (1986–2026) e 41 manifests de qualidade; a pasta de normalizados anuais lista somente 20 CSVs (1986–2004 e 2026). Os CSVs de 2005–2025 não estão listados em `dados/cotahist/normalized/anual/`, apesar de existirem manifests. Essa divergência exige atualização/reconciliação em B3.
- Os tamanhos de 133/134 bytes na API podem representar ponteiros Git LFS, não ausência de conteúdo. Foram verificados ponteiros de 1986, 1988 e 2026 com SHA-256 e tamanho declarado; os objetos grandes não foram descarregados nem re-hashados nesta execução.
- O catálogo BVBG.028.02 está armazenado, mas a extração integral e o mapeamento de `INDFUT`, `DOFUT`, `IND`, `DOL`, `WIN` e `WDO` para código/contrato continuam pendentes.
- A presença de RAW e manifestos COTAHIST não demonstra, por si só, cobertura semântica dos futuros ou aplicabilidade do campo de abertura. O campo real por instrumento/contrato continua não confirmado.
- O plano do Módulo 002 foi ampliado para 46 casos com DS-45 e DS-46. Todos permanecem `NOT_RUN`.

A validação continua offline. Nenhum teste NTSL/Profit, replay, backtest ou ordem foi executado nesta adenda.

## Adenda — extração efetiva do catálogo BVBG.028.02 — 2026-10-12

O CSV `ativos/catalogo/INVENTARIO_B3_2026-09-22.csv` foi processado integralmente a partir do Git blob `5d88fa0e319d8398e992537de51bda691dc4a5ab` (Git SHA-1, não SHA-256). Foram contados 120.973 registos e 32 campos; a extração encontrou 70 contratos futuros datados com ID único e campos mínimos completos: IND=12, WIN=11, DOL=24, WDO=23.

Nenhum `TckrSymb` corresponde exatamente a `IND`, `INDFUT`, `DOL`, `DOFUT`, `WIN` ou `WDO`. O resultado comprova famílias de contratos datados, mas não o mapeamento dos aliases da plataforma. Em particular, não autoriza assumir `INDFUT=IND` ou `DOFUT=DOL`; estes aliases permanecem `UNKNOWN/BLOCKED`.

A matriz completa foi guardada em `MODULOS/002-RELOGIO-SESSAO-ABERTURA/data/MATRIZ_CONTRATOS_FUTUROS_BVBG028_2026-09-22.csv`, e a metodologia/limites em `GOVERNANCA/MAPEAMENTO_CATALOGO_B3_ALIASES_E_CONTRATOS_2026-10-12.md`. DS-47 e DS-48 passaram apenas como testes de extração/guardrail. A fonte não contém preços históricos de abertura; DS-45 e DS-46 continuam NOT_RUN.

## Resultado

A política de validação offline por dados armazenados está definida. A cobertura de dados por símbolo e a fonte histórica de abertura ainda não estão certificadas. O Módulo 002 permanece não validado; a lacuna foi registada na issue B3 #6.

## Próxima Ação

Aguardar/acompanhar a atualização solicitada em B3 issue #6; quando os arquivos históricos necessários estiverem armazenados, executar a matriz offline e registrar cobertura, integridade e resultados. Não depender do Profit em tempo real. A semântica runtime de funções NTSL continuará explicitamente não validada até existir evidência armazenada apropriada.

## Histórico de versões

- 0.7.0 — 2026-10-12 — política ajustada para validação offline com dados já armazenados; auditoria identificou ausência de datasets brutos intraday/derivativos na camada market_data e criou-se B3 issue #6 para completar cobertura; nenhum teste Profit é alegado.
- 0.6.0 — 2026-10-12 — escopo ampliado a seis símbolos utilizados pelo operador: INDFUT, DOFUT, IND, DOL, WIN e WDO; testes de abertura continuam pendentes e cada instrumento/contrato deve ser validado separadamente.
- 0.5.0 — 2026-10-12 — verificação em páginas oficiais B3: códigos genéricos documentados são IND/DOL, distintos de WIN/WDO; aliases INDFUT/DOFUT precisam de mapeamento no Profit.
- 0.4.0 — 2026-10-12 — correção do escopo para INDFUT e DOFUT, sem requisito de gráfico de 60.000 ticks; correspondência dos símbolos com código/contrato B3 exigida.
- 0.3.0 — 2026-10-12 — verificação cruzada do B3; identificada abertura EOD no COTAHIST, mas sem evidência suficiente para certificar WINFUT/DOLFUT em Profit 60K; testes práticos continuam pendentes.
- 0.2.0 — 2026-10-12 — matriz operacional definida para WINFUT e DOLFUT em gráficos de 60.000 ticks; nenhuma execução no Profit declarada.
- 0.1.0 — 2026-10-12 — primeira auditoria documental de candidatos à abertura oficial.
