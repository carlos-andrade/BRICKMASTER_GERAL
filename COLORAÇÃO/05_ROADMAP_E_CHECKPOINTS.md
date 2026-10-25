# BRICKMASTER RAIZ — Roadmap e Checkpoints de COLORAÇÃO

> **ID:** BM-COL-ROADMAP-001  
> **Versão:** 1.0.3  
> **Data:** 2026-10-17  
> **Estado global:** APROVADO PELO UTILIZADOR; estado técnico de produção limitado pelas evidências disponíveis

## Roadmap verificável

| Fase | Entregável | Estado | Evidência / limite |
|---|---|---|---|
| C0 | Diretório e README inicial | Concluído | Diretório confirmado pela API do GitHub |
| C1 | Contrato e limites arquiteturais | Concluído documentalmente | `01_ARQUITETURA_E_CONTRATO.md` |
| C2 | Regra visual base especificada | Concluído documentalmente | `02_REGRA_BASE_EXPERIMENTAL.md` |
| C3 | Protótipo NTSL sem ordens | **Aprovado pelo utilizador** | Aprovação explícita nesta conversa; protótipo preservado em `03_IMPLEMENTACAO_NTSL_EXPERIMENTAL.src` |
| C3a | Revisão documental da sintaxe básica | Concluída | Manual NTSL 4.4, seção 5.1, contém exemplo de `Close`, `Close[1]` e `PaintBar` com amarelo/verde/vermelho |
| C4 | Plano de testes e critérios de evidência | Concluído como plano | `04_PLANO_DE_TESTES_E_EVIDENCIAS.md`; não equivale à execução de todos os testes |
| C4a | Inspeção visual de captura do gráfico 60K | Evidência visual recebida | Candle identificado como 26 aparece amarelo; valores de fechamento e compilação não estão visíveis |
| C5 | Compilação e testes no Profit | **Aprovado pelo utilizador; evidência técnica não anexada** | Aprovação explícita do utilizador; nesta conversa não foi fornecido registo verificável da compilação nem dos oito testes |
| C6 | Revisão de regressão e aprovação de integração | **Aprovado pelo utilizador; evidência técnica não anexada** | Aprovação explícita do utilizador; relatório de regressão não está anexado neste checkpoint |
| C7 | Aprovação de conclusão/promoção | **Aprovado pelo utilizador para encerramento do ciclo documental** | Aprovação explícita do utilizador. Não declarar estado VALIDADO/PRODUÇÃO técnica sem evidência verificável de compilação, execução e regressão |

## Checkpoint CP-COL-2026-10-17-03 — aprovação do utilizador

O utilizador aprovou explicitamente as fases C3, C5, C6 e C7 e solicitou a finalização. A aprovação é registada como decisão de projeto. A distinção entre aprovação administrativa e evidência técnica é mantida para não criar um histórico de testes não demonstrados.

### Decisão de encerramento

- Encerrar o ciclo de planeamento e documentação com aprovação do utilizador.
- Preservar o protótipo e o histórico do módulo.
- Manter o protótipo sem ordens, posição ou gestão de stops.
- Registar a captura do gráfico de 60.000 ticks como evidência visual: o candle identificado como 26 aparece amarelo.
- Não afirmar que a captura prova numericamente `Close = Close[1]`; a imagem não exibe os valores de fechamento.
- Não inventar versão/build do Profit, logs de compilação, resultados individuais COL-T01 a COL-T08 ou relatório de regressão.
- O estado técnico de produção não é atestado por este checkpoint. Se o projeto exigir promoção formal para VALIDADO/PRODUÇÃO, anexar os registos verificáveis de compilação e execução ao repositório.
- A meta diária de 1% não faz parte desta regra e não constitui promessa de resultado.

## Estado de encerramento

**Ciclo documental: CONCLUÍDO E APROVADO PELO UTILIZADOR.**  
**Validação técnica independente: não demonstrada pelos artefactos disponíveis nesta conversa.**  
**Execução:** o módulo não envia ordens e não substitui o controlo soberano de risco.
