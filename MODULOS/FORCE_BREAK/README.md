# BRICKMASTER FORCE BREAK

| Campo | Valor |
|---|---|
| **ID** | BMFB-README-001 |
| **Projeto** | BRICKMASTER RAIZ — módulo FORCE BREAK |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | ESPECIFICACAO |
| **Fase** | DESCOBERTA_E_ESPECIFICACAO |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — cálculo determinístico ainda não executado nesta sessão |
| **Commit de referência (versão anterior)** | [83090e784663cdc1ff2313e628c986e83c066493](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/83090e784663cdc1ff2313e628c986e83c066493) |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente — aprovação deste documento não registada |
| **Origem** | Requisito do módulo e regras do estudo BMFB-001 versionadas neste repositório |
| **Autoridade superior** | [Norma de cabeçalho documental GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); [Governança técnica BRICKMASTER](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/main/BRICKMASTER_ARQUITETURA/GOVERNANCA.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | [Estudo BMFB-001](BMFB-001-FECHAMENTOS-MINIMAS-MAXIMAS.md); [commit de migração](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/b6b81bd551a2ae8e8b4769f337a5fb9cf374e49d) |
| **Escopo** | Pesquisa experimental de rompimentos por fechamento contra máximas/mínimas anteriores; sem execução de ordens |
| **Objetivo** | Estabelecer contrato documental e critérios para investigar a força de rompimentos |
| **Dependências** | Dados OHLC correspondentes às amostras; rastreabilidade da origem; validação reproduzível |

## 1. Missão

Investigar e quantificar a força de rompimentos em que o fechamento de um candle ultrapassa a mínima ou a máxima de candles anteriores, começando pelas referências de 1, 2 e 3 candles.

## 2. Princípios obrigatórios

- Preservar o histórico e a proveniência de cada estudo.
- Distinguir observação, hipótese, evidência e conclusão validada.
- Não declarar testes ou resultados sem evidências reproduzíveis.
- Manter estudos experimentais separados das regras validadas e de produção.
- Não emitir ordens nem alterar a lógica operacional do BRICKMASTER.
- Avaliar critérios, dependências, riscos e limitações antes de integrar descobertas.
- Aplicar a norma documental GOV-CAB-NORMA-001 v1.0.3 a cada ficheiro Markdown, incluindo cabeçalho visível, integridade canónica e referência ao commit anterior.

## 3. Estrutura obrigatória de cada estudo

1. Identificador único, pergunta investigada, escopo e exclusões.
2. Fonte dos dados, proveniência e contexto gráfico.
3. Definição matemática das condições e convenções.
4. Amostra, critérios de inclusão/exclusão e observações elegíveis.
5. Tabelas de resultados, controlos de consistência e forma de reprodução.
6. Dependências, riscos, limitações e evidências verificáveis.
7. Estado documental e estado técnico, sem confundi-los.
8. Histórico de alterações e decisão de integração.
9. Validação independente/proporcional ao risco e próxima ação.

## 4. Estado do módulo

- **Estado técnico:** EXPERIMENTAL.
- **Estado documental deste README:** EM_REVISAO.
- **Estado do estudo BMFB-001:** EXPERIMENTAL; contagens numéricas pendentes de OHLC.
- **Testes NTSL/Profit, replay, backtest ou execução de ordens:** não declarados nem presumidos neste documento.
- **Produção:** não aprovado.

## 5. Estudo inicial

O estudo [BMFB-001 — Fechamentos além da mínima/máxima de candles anteriores](BMFB-001-FECHAMENTOS-MINIMAS-MAXIMAS.md) investiga fechamentos abaixo da mínima e acima da máxima de candles situados 1, 2 e 3 posições atrás. A contagem exata permanece pendente de dados OHLC correspondentes às imagens. Não considerar o estudo validado até essa reconciliação.

## 6. Contexto histórico

O módulo foi migrado de `MODULOS/DESCOBERTA/` para `MODULOS/FORCE_BREAK/` em 2026-10-16. A migração preservou o histórico Git; os commits anteriores permanecem consultáveis. O identificador técnico do módulo é `BM_FORCE_BREAK`.

## 7. Evidências

- [Norma de cabeçalho GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md)
- [Governança técnica BRICKMASTER RAIZ](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/main/BRICKMASTER_ARQUITETURA/GOVERNANCA.md)
- [Commit de migração do README](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/b6b81bd551a2ae8e8b4769f337a5fb9cf374e49d)
- [Estudo BMFB-001](BMFB-001-FECHAMENTOS-MINIMAS-MAXIMAS.md)

## 8. Validação

Verificação documental iniciada em 2026-10-17. A atualização deste README corrige a referência antiga `DESC-001` para `BMFB-001` e torna explícita a aplicação da norma GOV. O SHA-256 canónico deve ser calculado conforme a norma após a redação; não confundir o checksum canónico com o SHA do blob Git. Não declarar conformidade integral sem cálculo/verificação do checksum e revisão dos critérios.

## 9. Resultado

Contrato documental atualizado. A pesquisa permanece experimental, sem resultados numéricos OHLC, sem aprovação para produção e sem envio de ordens.

## 10. Próxima ação

Aplicar o cabeçalho canónico e calcular o SHA-256 conforme GOV em todos os documentos Markdown da pasta. Em seguida, obter dados OHLC idênticos às amostras, executar a contagem reproduzível e registar evidências e revisão.

## 11. Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.0 | 2026-10-16 | Criação inicial do módulo após migração | Responsável técnico do projeto | [Commit b6b81bd](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/b6b81bd551a2ae8e8b4769f337a5fb9cf374e49d) |
| 1.0.1 | 2026-10-17 | Normalização preliminar segundo GOV; corrigida referência ao estudo atual | Responsável técnico do projeto | Commit desta atualização |
