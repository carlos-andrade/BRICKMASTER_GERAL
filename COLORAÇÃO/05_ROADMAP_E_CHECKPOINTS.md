# BRICKMASTER RAIZ — Roadmap e Checkpoints de COLORAÇÃO

> **ID:** BM-COL-ROADMAP-001  
> **Versão:** 1.0.2  
> **Data:** 2026-10-17  
> **Estado global:** EXPERIMENTAL — validação operacional pendente

## Roadmap verificável

| Fase | Entregável | Estado | Evidência |
|---|---|---|---|
| C0 | Diretório e README inicial | Concluído | Diretório confirmado pela API do GitHub |
| C1 | Contrato e limites arquiteturais | Concluído documentalmente | `01_ARQUITETURA_E_CONTRATO.md` |
| C2 | Regra visual base especificada | Concluído documentalmente | `02_REGRA_BASE_EXPERIMENTAL.md` |
| C3 | Protótipo NTSL sem ordens | Experimental | `03_IMPLEMENTACAO_NTSL_EXPERIMENTAL.src` |
| C3a | Revisão documental da sintaxe básica | Concluída | Manual NTSL 4.4, seção 5.1, contém exemplo de `Close`, `Close[1]` e `PaintBar` com amarelo/verde/vermelho |
| C4 | Plano de testes e critérios de evidência | Concluído como plano; execução pendente | `04_PLANO_DE_TESTES_E_EVIDENCIAS.md` |
| C4a | Inspeção visual de captura do gráfico 60K | Evidência visual recebida; validação da regra pendente | Captura fornecida pelo utilizador: candle identificado como 26 aparece amarelo; valores de fechamento e compilação não estão visíveis |
| C5 | Compilação e testes no Profit | Pendente — requer execução no ambiente Profit | Não há evidência de compilação/execução neste checkpoint |
| C6 | Revisão de regressão e aprovação de integração | Pendente | Depende de C5 |
| C7 | Promoção para VALIDADO/PRODUÇÃO | Pendente | Exige evidências e aprovação formal |

## Checkpoint CP-COL-2026-10-17-02

- A captura do gráfico de 60.000 ticks fornecida pelo utilizador foi inspecionada visualmente.
- O candle identificado como 26 aparece amarelo na captura. Isto regista apenas a observação visual; não comprova que `Close = Close[1]`, nem identifica de forma independente o código/build efetivamente aplicado ao gráfico.
- A captura não apresenta os valores numéricos dos fechamentos nem a janela/resultado de compilação. A imagem original foi recebida na conversa; não foi arquivada como artefacto binário neste repositório por este checkpoint.
- O protótipo permanece EXPERIMENTAL até a compilação e a bateria de testes serem documentadas.
- Nenhuma ordem é enviada pelo protótipo.
- A meta diária de 1% não faz parte desta regra e não constitui promessa de resultado.
- Inventário da pasta anteriormente confirmado no GitHub; seis ficheiros presentes antes deste checkpoint.

## Pendências externas ao repositório

1. Compilar `03_IMPLEMENTACAO_NTSL_EXPERIMENTAL.src` no Profit e registar versão/build e resultado.
2. Registar os valores de fechamento do candle 26 e do candle anterior para confirmar a condição de igualdade; confirmar que a coloração vista provém da versão testada.
3. Executar COL-T01 a COL-T08 e guardar evidências, incluindo gráficos de ticks (60K) e Renko.
4. Corrigir o ficheiro completo se qualquer teste falhar e repetir a bateria.
5. Realizar revisão de regressão.
6. Só então decidir se a regra será mantida, revista ou descartada e se pode ser promovida.

## Regra de progresso

Não atribuir percentual global artificial. Documentação e revisão textual estão concluídas; foi recebida uma observação visual de candle amarelo, mas a validação no Profit permanece pendente. O módulo continua EXPERIMENTAL.
