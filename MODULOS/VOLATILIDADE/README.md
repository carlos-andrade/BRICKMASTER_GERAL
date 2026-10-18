# Módulo VOLATILIDADE — BRICKMASTER RAIZ

**Estado:** Estrutura inicial criada — experimental, não validada para produção.  
**Local:** `MODULOS/VOLATILIDADE/`

## Objetivo

Centralizar a especificação e a evolução dos componentes de volatilidade do BRICKMASTER RAIZ, fornecendo contexto ao Giroscópio sem gerar ordens de negociação.

## Escopo inicial

- Medição da volatilidade observada e de sua variação.
- Classificação do regime de mercado, com limiares documentados e sujeitos a calibração.
- Integração futura com o Giroscópio, Estado Gráfico, Fluxo/Volume, VWAP/TWAP, Intermercado e Risco.
- Tratamento explícito de dados ausentes, atrasados, inválidos ou contraditórios.
- Registo de evidências, testes, limitações e decisões de versão.

## Contrato preliminar

### Entradas
Dados de mercado identificados por ativo, fonte, horário do evento, horário de receção, unidade e estado de qualidade. Métricas e séries externas, incluindo VIX, só podem ser usadas quando a fonte, a sincronização e a disponibilidade estiverem verificadas.

### Saídas
Um contexto de volatilidade com, no mínimo:

- regime: `DESCONHECIDO`, `BAIXO`, `NORMAL`, `ELEVADO` ou `EXTREMO`;
- métricas e respetivas unidades;
- instante e fonte dos dados;
- qualidade, atualidade e confiança;
- motivo de bloqueio, quando aplicável.

Os limiares numéricos ainda não estão definidos nem validados. Não devem ser presumidos como parâmetros de produção.

## Regras de segurança

1. Este módulo é informativo e não envia ordens.
2. Dados inválidos, atrasados ou incompatíveis reduzem a confiança; quando comprometem a interpretação, o estado passa a `DESCONHECIDO` e a integração deve bloquear decisões dependentes.
3. O VIX não é substituto automático da volatilidade realizada do ativo negociado; qualquer uso exige definição de fonte, sincronização e finalidade.
4. Nenhum alvo diário, incluindo a hipótese de 1% desde a abertura, prevalece sobre os limites soberanos de risco.
5. Nenhum componente será marcado como validado sem testes reproduzíveis e evidências registadas.

## Estrutura prevista

- `README.md` — contrato e estado do módulo.
- `ESPECIFICACAO.md` — metodologia, fórmulas e regras de classificação.
- `CONTRATOS.md` — interfaces, dependências e semântica dos campos.
- `TESTES.md` — cenários, critérios de aceitação e evidências.
- `CHECKPOINTS.md` — histórico de alterações, validações e pendências.

Os ficheiros acima, exceto este README, serão adicionados conforme a especificação evoluir.

## Dependências previstas

- Giroscópio: consolidação do contexto e confiança.
- Estado Gráfico: tipo e granularidade do gráfico, incluindo gráficos de ticks.
- Dados/Qualidade: proveniência, sincronização e validação de integridade.
- Risco: autoridade final sobre bloqueio de operações.

As interfaces efetivas permanecem pendentes de verificação nos módulos correspondentes.

## Roadmap

1. **F0 — Estrutura:** concluída com a criação deste README.
2. **F1 — Levantamento:** inspecionar módulos existentes e evitar duplicação com `10_VOLATILIDADE_VIX`.
3. **F2 — Especificação:** definir métricas, unidades, janelas, regimes e comportamento para dados inválidos.
4. **F3 — Testes isolados:** criar casos sintéticos e reproduzíveis.
5. **F4 — Integração:** propor contrato para o Giroscópio; manter sem execução de ordens.
6. **F5 — Validação:** recolher evidências em replay/backtest antes de qualquer classificação de produção.

## Checkpoint inicial

- Criado por solicitação para estabelecer `MODULOS/VOLATILIDADE/`.
- Nenhuma lógica de cálculo foi implementada ou testada neste checkpoint.
- A pasta existente `MODULOS/10_VOLATILIDADE_VIX/` foi identificada na árvore atual; deve ser inspecionada antes de decidir reutilização, coexistência ou migração.
- Não houve alteração dos ficheiros existentes.
