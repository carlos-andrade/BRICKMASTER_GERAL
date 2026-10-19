---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "REVISAO_ESTATICA_NTSL"
fase: "FASE_06_NTSL_PROFIT_EXECUCAO_CONCILIADA_WATCHDOG"
id_documento: "BM-AUDIT-CUMULATIVE-VOLUME-001"
titulo: "Revisão estática — Cumulative Volume Anómalo versus Manual NTSL 4.4"
status: "REVISAO_ESTATICA_COM_ACHADOS; COMPILACAO_E_PROFIT_PENDENTES"
versao: "1.0.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "BRICKMASTER_CumulativeVolume_Standalone.src e Manual NTSL 4.4 (03/08/2026)"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase06-auditoria-volume-estatica"
escopo: "Revisão estática focalizada do candidato CumulativeVolume; sem alteração do código"
objetivo: "Identificar compatibilidade documentada, riscos de sessão e testes necessários antes de reaproveitamento"
dependencias: "Manual NTSL 4.4; BRICKMASTER_CumulativeVolume_Standalone.src"
---

# Revisão estática — Cumulative Volume Anómalo versus Manual NTSL 4.4

> **Projeto:** BRICKMASTER RAIZ  
> **Fase:** 06 — NTSL/Profit, execução conciliada e Watchdog  
> **ID:** BM-AUDIT-CUMULATIVE-VOLUME-001  
> **Estado:** REVISÃO ESTÁTICA COM ACHADOS; COMPILAÇÃO E PROFIT PENDENTES  
> **Data:** 2026-10-11

## Contexto Histórico

O inventário de fase 04 encontrou o ficheiro `BRICKMASTER_CLAUDE/CÓDIGO NTSL/BRICKMASTER_CumulativeVolume_Standalone.src`, blob SHA `0bb65120663f0de9f1b7d54ee88d32895d6ab095`. O cabeçalho do código declara como referência Manual NTSL v4.2 (20/01/2026). Foi feita uma comparação estática focalizada com o Manual NTSL 4.4 fornecido no projeto, datado de 03/08/2026. O código original não foi modificado.

## Estado

### Pontos confirmados no Manual NTSL 4.4

1. **Série `Volume`:** a secção 4.2, “Séries de dados”, define `Volume` como o volume financeiro de cada candle (página impressa 4). Portanto, o uso de `Volume` é coerente com a intenção declarada de acumular volume financeiro; não se deve substituí-lo automaticamente por `Quantity`.
2. **Data do candle:** a secção 16.15, “Função Date”, define `Date()` como a data do candle analisado, tipo Integer (página impressa 118).
3. **Hora do candle:** a secção 16.55, “Função Time”, define `Time()` como a hora de abertura do candle atual, tipo Integer (página impressa 166).
4. **Função alternativa de volume financeiro:** a secção 20.53 documenta `FinancialVol(VolumeProjetado, SoAgressores)` (página impressa 306), com opções para volume projetado e leilão/trades diretos. O parâmetro `SoAgressores` depende do plugin Tape Reading segundo o manual; não é um substituto semântica e operacionalmente idêntico a `Volume`.
5. **Arrays:** a secção 4.3 documenta arrays estáticos com indexação, incluindo exemplo `Array[1..10] Of Integer` (página impressa 5).

Estes pontos confirmam documentação de referência, não a compilação do código completo.

## Evidências

- Código candidato: `BRICKMASTER_CLAUDE/CÓDIGO NTSL/BRICKMASTER_CumulativeVolume_Standalone.src`, SHA `0bb65120663f0de9f1b7d54ee88d32895d6ab095`.
- Manual fornecido: `Manual NTSL_VERSÃO 4.4 - 03-08-2026.pdf`, versão 4.4, data de capa 03/08/2026.
- Secção 4.2 — Séries de dados, página impressa 4: `Volume` é volume financeiro por candle.
- Secção 4.3 — Arrays, página impressa 5.
- Secção 16.15 — Date, página impressa 118.
- Secção 16.55 — Time, página impressa 166.
- Secção 20.53 — FinancialVol, página impressa 306.

## Validação

### Achados estáticos

**A-01 — Limites de sessão não são aplicados explicitamente (prioridade alta).**  
Os inputs de fim de janela vão de 10:00 a 17:30, mas a seleção começa com `if Time < JanelaFim1 then JanelaAtual := 1`. Assim, qualquer candle anterior às 09:00 também entra na janela 1. Depois da última transição, o ramo final atribui a janela 8 a todo horário igual ou superior a 16:00, incluindo horários posteriores a 17:30. Isto não corresponde estritamente ao comentário “janelas horárias cobrindo 09:00–17:30”. A correção deve introduzir um estado explícito FORA_DA_SESSAO ou um bloqueio por hora inicial/final configurável, com o horário oficial do instrumento confirmado antes de o fixar.

**A-02 — A hora usada é a abertura do candle, não a hora exata de cada negócio (prioridade alta para gráficos de ticks).**  
O Manual define `Time()` como hora de abertura do candle. Num gráfico de ticks, um candle pode atravessar uma fronteira horária; o volume financeiro desse candle pode então ser atribuído integralmente à janela determinada pelo horário de abertura. O efeito deve ser medido em replay, especialmente em gráficos de ticks e 60K, antes de declarar comparabilidade exata entre janelas.

**A-03 — “Welford” é uma descrição imprecisa do cálculo implementado (prioridade média).**  
O código atualiza a média com `MediaAntiga + (NovoValor - MediaAntiga) / (N + 1)`. Esta é uma atualização incremental da média. O código apresentado não mantém o acumulador de variância (`M2`) normalmente associado ao algoritmo completo de Welford. A documentação deve chamar-lhe “média incremental” ou implementar e testar explicitamente variância se esta for necessária; não se deve inventar desvio-padrão/anomalia estatística que o código não calcula.

**A-04 — Persistência histórica limitada (limitação já reconhecida pelo código).**  
O comentário inicial declara que os arrays são reiniciados quando o indicador é recarregado ou o Profit reiniciado. A confiança no alerta depende, portanto, de como o histórico é recalculado/carregado e de quantos pregões efetivamente contribuem para cada janela. O contador de dias e os estados de cada janela precisam de teste de inicialização, recarga e dados incompletos.

### Matriz mínima de testes antes de alterar o código

| ID | Cenário | Resultado a verificar | Estado |
|---|---|---|---|
| CV-01 | Primeiro candle antes da hora de início configurada | Não é contabilizado em janela de sessão | NOT_RUN |
| CV-02 | Candle no limite exato de cada janela | A regra inclusiva/exclusiva é determinística | NOT_RUN |
| CV-03 | Candle depois da hora final configurada | Volume não aumenta a janela 8 fora da sessão | NOT_RUN |
| CV-04 | Candle de ticks atravessa uma fronteira de janela | Efeito de atribuição por hora de abertura medido e documentado | NOT_RUN |
| CV-05 | Gráfico de 60K ticks versus outro tipo de gráfico | Diferenças de fronteira e total diário comparadas | NOT_RUN |
| CV-06 | Dados ausentes ou sessão interrompida | Alerta fica desconhecido/bloqueado, sem média falsa | NOT_RUN |
| CV-07 | Reiniciar indicador/Profit e recarregar histórico | Dias contribuintes e médias reproduzíveis | NOT_RUN |
| CV-08 | Média incremental após N pregões | Resultado coincide com cálculo independente | NOT_RUN |
| CV-09 | NTSL 4.4 | Código compila no editor da versão alvo | NOT_RUN |
| CV-10 | Efeitos colaterais | Indicador não envia ordens nem altera posições | NOT_RUN |

**Testes executados nesta revisão:** nenhum teste no Profit, replay ou backtest. A revisão é estática e baseada no código e no manual.

## Resultado

A referência NTSL 4.4 confirma que `Volume` é volume financeiro por candle e documenta `Date`, `Time` e arrays utilizados pelo candidato. Foram identificados riscos de limites de sessão e atribuição temporal em gráficos de ticks, além de uma descrição imprecisa do algoritmo de média. O candidato permanece **experimental e não aprovado para integração**.

## Próxima Ação

1. Recuperar/confirmar o horário operacional correto do ativo e formalizar os limites de sessão e janelas.
2. Criar uma variante isolada corrigida, sem substituir o ficheiro histórico.
3. Definir explicitamente a política para candles que atravessam fronteiras temporais em gráficos de ticks.
4. Executar CV-01 a CV-10 no Profit com capturas/logs e configuração reproduzível.
5. Só após aprovação, decidir se o módulo entra no catálogo operacional e se alimenta o Giroscópio; não permitir que o indicador autorize operações.

## Histórico de versões

- 1.0.0 — 2026-10-11 — primeira revisão estática focalizada do candidato com referência ao Manual NTSL 4.4.

<!-- RECONCILIACAO_SHA256: 23a97e3bf93286f87026a50b1b266212a7cd625e28b837e816a399521a03191e
COMMIT_DE_REFERENCIA: c0740f9fd4d1485b3c3a1b8568053b8cd077e688
-->
