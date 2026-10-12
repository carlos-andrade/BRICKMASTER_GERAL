---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "AUDITORIA_DE_FONTE"
fase: "FASE_02_DADOS_SESSAO_ABERTURA"
id_documento: "BM-DATA-001-AUDITORIA-FONTE-NTSl44"
titulo: "Auditoria documental — candidatos à abertura oficial no Manual NTSL 4.4"
status: "REVISAO_DOCUMENTAL; VALIDACAO_PROFIT_PENDENTE"
versao: "0.1.0"
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

REVISÃO DOCUMENTAL CONCLUÍDA; validação no Profit, confirmação do instrumento prioritário e testes de sessão/ticks pendentes.

## Achados suportados pelo Manual 4.4

1. **Série `Open`:** a secção 4.2, página impressa 6, define Abertura/Open como o valor de abertura de cada candle. Isso é uma abertura de candle, não uma declaração geral de que o valor corresponde ao preço oficial de abertura da sessão.
2. **`OpenD(DaysAgo)`:** secção 16.45, página impressa 156, descreve o valor de abertura de um número de dias atrás. O manual apresenta `OpenD(0)` noutro exemplo como abertura do dia atual, mas essa ocorrência isolada não prova, por si só, a equivalência à abertura oficial para todos os instrumentos, sessões, leilões e tipos de gráfico.
3. **`OpenDaily(DaysBack)`:** secção 20.90, página impressa 357, descreve um valor de abertura diário segundo o deslocamento e exemplifica a abertura do dia anterior. A semântica exata para o dia atual e o contexto de execução tem de ser testada na versão concreta do Profit.
4. **Séries de ativo com período diferente:** a secção 4.4, páginas impressas 6–7, alerta que dados obtidos via `Asset` com período divergente podem não coincidir com o valor esperado. Recomenda especificar explicitamente a série desejada, por exemplo `itDaily`. Mesmo essa recomendação não substitui a validação empírica da política B.
5. **`Time()`:** a secção 16.55 define a hora de abertura do candle atual. Não é uma fonte do preço oficial de abertura da sessão.

## Conclusão técnica

O Manual 4.4 oferece candidatos para investigação — `OpenD(0)`, `OpenDaily(0)` e uma série diária explícita — mas a documentação consultada não permite declarar qualquer um deles como fonte oficial universal já validada. Não codificar a escolha como facto confirmado.

## Plano de verificação no Profit

Registar para um instrumento prioritário e data de pregão:
- ticker/contrato e vencimento, plataforma/feed e versão do Profit;
- nome e semântica do campo de abertura exibido pela plataforma, com captura ou exportação;
- sessão/fuso e tratamento de leilão, se aplicável;
- valores de `OpenD(0)`, `OpenDaily(0)`, `Open` e série diária explicitamente configurada, sem assumir equivalência;
- valor oficial de referência disponível na plataforma ou numa fonte oficial aprovada;
- comparação dos valores em gráfico temporal e gráfico de ticks, incluindo 60K, no início da sessão e após carregar/reprocessar o gráfico;
- timestamp, modo (histórico/replay/tempo real), discrepâncias e evidências anexadas ao repositório.

Critério: aprovar uma combinação fonte/campo/instrumento apenas após equivalência demonstrada em casos repetíveis e tratamento explícito de ausências, atrasos e divergências. Até lá, a referência mantém-se `UNKNOWN`/pendente e o Módulo 001 não deve tratar níveis como confirmados.

## Evidências

- Manual NTSL 4.4, secção 4.2, página impressa 6: definição da série `Open`.
- Manual NTSL 4.4, secção 4.4, páginas impressas 6–7: ressalva sobre `Asset` com período divergente.
- Manual NTSL 4.4, secção 16.45, página impressa 156: `OpenD`.
- Manual NTSL 4.4, secção 16.55: `Time()`.
- Manual NTSL 4.4, secção 20.90, página impressa 357: `OpenDaily`.

## Validação

Revisão documental estática apenas. Não houve execução de código, compilação, replay ou teste no Profit.

## Resultado

A política B está documentada. A fonte/campo oficial ainda não foi certificada. Não existem evidências para marcar o Módulo 002 como validado.

## Próxima Ação

Executar a comparação controlada no Profit e guardar os resultados como evidências antes de selecionar a função/campo de implementação.

## Histórico de versões

- 0.1.0 — 2026-10-12 — primeira auditoria documental de candidatos à abertura oficial.
