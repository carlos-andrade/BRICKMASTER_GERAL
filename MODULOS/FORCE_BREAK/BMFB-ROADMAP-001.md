# ROADMAP — BRICKMASTER FORCE BREAK (BM_FORCE_BREAK)

| Campo | Valor |
|---|---|
| **ID** | BMFB-ROADMAP-001 |
| **Projeto** | BRICKMASTER RAIZ — módulo FORCE BREAK |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | ROADMAP |
| **Fase** | DEVELOP |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular deterministicamente conforme GOV-CAB-NORMA-001 v1.0.3 |
| **Commit de referência (versão anterior)** | N/A — documento inicial do roadmap formal |
| **Data de criação** | 2026-10-17 |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Responsável técnico do BRICKMASTER RAIZ |
| **Aprovador** | Pendente |
| **Origem** | Requisitos registados nesta conversa e estado verificado dos ficheiros na branch feature/bm-force-break-001 |
| **Autoridade superior** | [Norma de cabeçalho GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); [Constituição GOV-001 — proposta para revisão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | [README do módulo](README.md); [estudo BMFB-001](BMFB-001-FECHAMENTOS-MINIMAS-MAXIMAS.md); [especificação técnica BMFB-IMPL-001](BMFB-IMPL-001-README.md) |
| **Escopo** | Primeiro indicador visual e contadores diários de rompimentos em NTSL/Profit; sem ordens e sem integração operacional |
| **Dependências** | Profit/NTSL, séries OHLC e Date, gráfico de ticks incluindo 60K, dados de validação reproduzíveis |

## 1. Propósito e limites

Entregar um módulo experimental que identifique as seis condições definidas no estudo BMFB-001:
- B1–B3: `Close < Low[N]`, para N=1, 2, 3.
- A1–A3: `Close > High[N]`, para N=1, 2, 3.

Só avaliar quando `Date = Date[N]`. Os seis contadores devem reiniciar quando muda `Date`. O módulo permanece independente do BRICKMASTER operacional; não contém funções de ordens. A hipótese de 1% diário não é promessa, métrica de aceitação nem prioridade sobre o risco.

## 2. Estado atual confirmado

- Branch de desenvolvimento: `feature/bm-force-break-001`.
- Indicador visual BMFB-001: versão 0.2.0 gravada; o utilizador reportou anteriormente que a versão inicial compilou, mas a versão filtrada por data ainda requer confirmação atual.
- Contadores BMFB-002: versão 0.3.0 gravada, com índices PlotN 1–6, tipo histograma e cores explícitas. O utilizador reportou que uma versão compilou, mas não apresentou plots; a versão 0.3.0 ainda não foi confirmada como visualmente funcional.
- Documentação técnica: BMFB-IMPL-001, versão 0.3.0.
- Estado técnico global: EXPERIMENTAL. Não validado, não em produção, não integrado na main.
- SHA-256 canónico da documentação: pendente de cálculo determinístico.
- Não há evidência registada de backtest, teste de OHLC independente ou validação no gráfico 60K.

## 3. Roadmap por fases

### F0 — Governação e requisitos
**Estado: EM_REVISAO**

Critérios:
1. Preservar o histórico Git.
2. Aplicar os cabeçalhos Markdown de GOV-CAB-NORMA-001 v1.0.3.
3. Manter origem, autoridade, estado, versão, dependências, histórico, commits e SHA-256 canónico rastreáveis.
4. Não tratar a Constituição GOV-001 como aprovada: o ficheiro consultado está marcado PROPOSTA PARA REVISÃO.
5. Manter experimentação, validação e produção como estados distintos.

### F1 — FEATURE: lógica de rompimentos
**Estado: IMPLEMENTADA; requer confirmação de regressão**

- Implementar B1–B3 e A1–A3 com desigualdades estritas.
- Comparar com o candle exato N posições atrás, sem combinar extremos de candles.
- Bloquear comparação entre datas diferentes.
- Não alterar a lógica central do BRICKMASTER.

Aceitação: compilar a versão atual do indicador visual e confirmar exemplos conhecidos.

### F2 — DEVELOP: corrigir visualização dos contadores
**Estado: PENDENTE — prioridade atual**

Passos:
1. Importar BMFB-002 v0.3.0 como indicador em painel separado.
2. Compilar e registar a mensagem do compilador.
3. Confirmar que as séries PlotN(1..6) são apresentadas e distinguíveis.
4. Verificar se histogramas são visíveis com valores 0, 1, 2, … e se cada série aumenta conforme as condições.
5. Se continuar sem plot, usar um indicador diagnóstico mínimo com Plot(1) e um valor conhecido, depois isolar a causa em sequência; atualizar o código completo e registar o erro/evidência.
6. Não confundir compilação com funcionamento gráfico.

Critério de saída: contadores visíveis num painel separado e atualizados conforme o evento.

### F3 — VALIDATION: correção funcional e diária
**Estado: BLOQUEADA até F2**

Testes obrigatórios:
1. Casos manuais com Close abaixo/igual/acima de Low[N] e abaixo/igual/acima de High[N].
2. Teste na transição de data: nenhuma comparação B/A pode referenciar barras de outra data.
3. Os seis contadores reiniciam na mudança de Date e contam só as ocorrências da data corrente.
4. Comparar todos os resultados com cálculo independente sobre OHLC exportado.
5. Repetir no tipo de gráfico de ticks usado pelo utilizador, incluindo 60K.
6. Registar ativo, período, quantidade de barras, versão do Profit, código/commit, resultados e capturas de evidência.
7. Recalcular SHA-256 canónico dos documentos atualizados; atualizar os cabeçalhos e validar consistência dos links/IDs.

Critério de saída: todos os testes aprovados com evidências reproduzíveis, sem divergências inexplicadas.

### F4 — REVIEW / APROVAÇÃO
**Estado: NÃO INICIADA**

- Revisão técnica e documental separadas.
- Registar defeitos e limitações não resolvidos.
- Aprovar uma versão exata por commit; não promover por mera compilação.
- Confirmar autoridade aprovadora e decisão rastreável.

### F5 — MAIN / PRODUÇÃO
**Estado: BLOQUEADA**

- Só após F0–F4 cumpridas e aprovação explícita.
- Criar proposta de merge para main; não fazer merge automático.
- Preservar reversibilidade e manter o módulo sem ordens, salvo decisão futura, explícita e separadamente governada.

## 4. Dependências, riscos e limitações

- A interpretação de `Date` depende da sessão e do comportamento do gráfico no Profit; confirmar no ativo e tipo de gráfico usados.
- Os seis plots podem ser invisíveis se apresentados na escala de preços principal; usar painel separado.
- Os valores pequenos dos contadores devem ser verificados em escala própria.
- NTSL compilar não demonstra que o plot está visível ou que o contador está correto.
- Capturas de tela sem dados OHLC exportados não bastam para confirmar contagens numéricas.
- Nenhuma ordem deve ser emitida por este módulo.

## 5. Evidências e checkpoints

- Norma documental aprovada: [GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md).
- Constituição consultada está em estado de proposta para revisão: [GOV-001](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md).
- Indicador visual: [BMFB-001-INDICADOR-VISUAL.ntsl](BMFB-001-INDICADOR-VISUAL.ntsl).
- Contadores: [BMFB-002-CONTADORES.ntsl](BMFB-002-CONTADORES.ntsl).
- Especificação técnica: [BMFB-IMPL-001-README.md](BMFB-IMPL-001-README.md).
- Estudo matemático: [BMFB-001-FECHAMENTOS-MINIMAS-MAXIMAS.md](BMFB-001-FECHAMENTOS-MINIMAS-MAXIMAS.md).

## 6. Histórico de alterações

- 2026-10-17 — criação do roadmap formal com fases, critérios de saída e bloqueios.
