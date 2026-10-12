---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "AUDITORIA_DE_FONTE"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-AUDITORIA-FONTE-NTSl44"
titulo: "Auditoria documental — candidatos à abertura oficial no Manual NTSL 4.4"
status: "REVISAO_DOCUMENTAL; VALIDACAO_PROFIT_PENDENTE; MATRIZ_INDFUT_DOFUT_SEM_RESTRICAO_60K"
versao: "0.4.0"
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

REVISÃO DOCUMENTAL CONCLUÍDA; instrumentos solicitados: INDFUT e DOFUT; não há restrição a gráfico de 60.000 ticks; execução no Profit e evidências ainda pendentes. A correspondência dos símbolos com códigos B3 e contrato/vencimento deve ser registada antes da aceitação.

## Achados suportados pelo Manual 4.4

1. **Série `Open`:** a secção 4.2, página impressa 6, define Abertura/Open como o valor de abertura de cada candle. Isso é uma abertura de candle, não uma declaração geral de que o valor corresponde ao preço oficial de abertura da sessão.
2. **`OpenD(DaysAgo)`:** secção 16.45, página impressa 156, descreve o valor de abertura de um número de dias atrás. O manual apresenta `OpenD(0)` noutro exemplo como abertura do dia atual, mas essa ocorrência isolada não prova, por si só, a equivalência à abertura oficial para todos os instrumentos, sessões, leilões e tipos de gráfico.
3. **`OpenDaily(DaysBack)`:** secção 20.90, página impressa 357, descreve um valor de abertura diário segundo o deslocamento e exemplifica a abertura do dia anterior. A semântica exata para o dia atual e o contexto de execução tem de ser testada na versão concreta do Profit.
4. **Séries de ativo com período diferente:** a secção 4.4, páginas impressas 6–7, alerta que dados obtidos via `Asset` com período divergente podem não coincidir com o valor esperado. Recomenda especificar explicitamente a série desejada, por exemplo `itDaily`. Mesmo essa recomendação não substitui a validação empírica da política B.
5. **`Time()`:** a secção 16.55 define a hora de abertura do candle atual. Não é uma fonte do preço oficial de abertura da sessão.

## Conclusão técnica

O Manual 4.4 oferece candidatos para investigação — `OpenD(0)`, `OpenDaily(0)` e uma série diária explícita — mas a documentação consultada não permite declarar qualquer um deles como fonte oficial universal já validada. Não codificar a escolha como facto confirmado.

## Plano de verificação no Profit

Registar separadamente para INDFUT e DOFUT, em cada data de pregão, usando a configuração de gráfico efetivamente escolhida no Profit, sem requisito de 60.000 ticks:
- ticker/contrato e vencimento, plataforma/feed e versão do Profit;
- nome e semântica do campo de abertura exibido pela plataforma, com captura ou exportação;
- sessão/fuso e tratamento de leilão, se aplicável;
- valores de `OpenD(0)`, `OpenDaily(0)`, `Open` e série diária explicitamente configurada, sem assumir equivalência;
- valor oficial de referência disponível na plataforma ou numa fonte oficial aprovada;
- comparação dos valores na configuração de gráfico efetivamente usada no Profit, sem exigir 60.000 ticks, no início da sessão e após carregar/reprocessar o gráfico;
- timestamp, modo (histórico/replay/tempo real), discrepâncias e evidências anexadas ao repositório.

Critério: aprovar uma combinação fonte/campo/instrumento apenas após equivalência demonstrada em casos repetíveis e tratamento explícito de ausências, atrasos e divergências. Até lá, a referência mantém-se `UNKNOWN`/pendente e o Módulo 001 não deve tratar níveis como confirmados.

## Matriz de validação atual — INDFUT e DOFUT / gráfico sem restrição de periodicidade

A execução será feita nos dois símbolos solicitados, sem presumir que a mesma fonte/campo serve para ambos. Não é exigido gráfico de 60.000 ticks. Cada linha de evidência deve identificar o símbolo real no Profit, código de negociação B3, contrato/vencimento e data do pregão.

| Dimensão | INDFUT | DOFUT | Regra de aceitação |
|---|---|---|---|
| Gráfico utilizado | Configuração real no Profit | Configuração real no Profit | Registar tipo/periodicidade usados; não exigir 60.000 ticks |
| Referência da plataforma | Registar campo e valor visível | Registar campo e valor visível | Captura/exportação identificável, não valor inferido visualmente sem contexto |
| `Open` | Registar valor observado | Registar valor observado | Tratar como abertura do candle, não presumir abertura oficial |
| `OpenD(0)` | Registar valor observado | Registar valor observado | Candidato; não aprovar sem comparação repetível |
| `OpenDaily(0)` | Registar valor observado ou erro/indisponível | Registar valor observado ou erro/indisponível | Candidato; não aprovar sem comparação repetível |
| Série diária explícita | Registar configuração e valor | Registar configuração e valor | Documentar período/série usado e possíveis divergências |
| Momento de observação | Início da sessão e após recarregar/reprocessar | Início da sessão e após recarregar/reprocessar | Referência oficial não pode mudar silenciosamente durante a sessão |
| Resultado | PASS/FAIL/BLOCKED com evidência | PASS/FAIL/BLOCKED com evidência | Se não houver fonte oficial observável ou houver conflito, manter `UNKNOWN/INVALID` |

### Procedimento de recolha

1. Abrir o símbolo INDFUT no Profit e registar o código efetivo, contrato/vencimento, tipo de gráfico, data, feed, versão da plataforma, sessão e fuso. Confirmar a correspondência com o cadastro/código B3; não assumir equivalência pelo nome.
2. Registar o campo de abertura oficial apresentado pela plataforma e a evidência visual/exportada com timestamp.
3. Sem alterar o gráfico, observar e anotar separadamente `Open`, `OpenD(0)`, `OpenDaily(0)` e a série diária explícita disponível. Se a função não compilar, não estiver disponível ou não devolver valor, registar isso — não substituir silenciosamente.
4. Repetir no símbolo DOFUT, com os mesmos campos de metadados e confirmação de correspondência B3.
5. Comparar cada candidato com o campo de referência oficial no início da sessão e após recarregar/reprocessar o gráfico. Anotar diferenças em pontos, timestamp e contexto.
6. Repetir em outra sessão de pregão antes de aprovar uma fonte/campo por instrumento. Uma coincidência isolada não certifica equivalência.
7. Anexar capturas/exports e a tabela preenchida ao repositório antes de alterar o estado de qualquer teste para PASS.

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

Conclusão: o B3 contém metodologia e dados diários EOD, incluindo um campo de abertura diária, mas a evidência encontrada não fornece valores certificados de abertura para INDFUT/DOFUT no Profit. O tipo de gráfico de validação não é restringido a 60.000 ticks. COTAHIST/EOD não substitui a validação do campo de abertura efetivamente utilizado pelo Profit, nem comprova o comportamento de `Open`, `OpenD(0)` ou `OpenDaily(0)`. A documentação B3 consultada usa WIN/WDO como instrumentos-alvo noutro contrato de ingestão; a correspondência com INDFUT/DOFUT continua por confirmar.

Referências B3:
- https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/PARTE01_CONTRATO_NORMALIZED_COTAHIST_V1.0.md
- https://github.com/carlos-andrade/B3/blob/main/dados/market_data/README.md
- https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/PARTE03_B3_INTRADAY_CONTRATO_V1.0.md
- https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_CONTRATO_V1.1.md
- https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/normalized/manifests/diario/COTAHIST_D09102026_quality.json

## Validação

Revisão documental estática apenas. Não houve execução de código, compilação, replay ou teste no Profit.

## Resultado

A política B está documentada. A fonte/campo oficial ainda não foi certificada. Não existem evidências para marcar o Módulo 002 como validado.

## Próxima Ação

Executar a comparação controlada no Profit e guardar os resultados como evidências antes de selecionar a função/campo de implementação.

## Histórico de versões

- 0.4.0 — 2026-10-12 — correção do escopo para INDFUT e DOFUT, sem requisito de gráfico de 60.000 ticks; correspondência dos símbolos com código/contrato B3 exigida.\n- 0.3.0 — 2026-10-12 — verificação cruzada do B3; identificada abertura EOD no COTAHIST, mas sem evidência suficiente para certificar WINFUT/DOLFUT em Profit 60K; testes práticos continuam pendentes.
- 0.2.0 — 2026-10-12 — matriz operacional definida para WINFUT e DOLFUT em gráficos de 60.000 ticks; nenhuma execução no Profit declarada.
- 0.1.0 — 2026-10-12 — primeira auditoria documental de candidatos à abertura oficial.
