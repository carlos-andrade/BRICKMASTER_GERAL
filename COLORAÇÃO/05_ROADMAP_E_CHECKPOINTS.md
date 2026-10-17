# BRICKMASTER RAIZ — Roadmap e Checkpoints de COLORAÇÃO

> **ID:** BM-COL-ROADMAP-001  
> **Versão:** 1.0.1  
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
| C5 | Compilação e testes no Profit | Pendente — requer execução no ambiente Profit | Não há evidência de compilação/execução neste checkpoint |
| C6 | Revisão de regressão e aprovação de integração | Pendente | Depende de C5 |
| C7 | Promoção para VALIDADO/PRODUÇÃO | Pendente | Exige evidências e aprovação formal |

## Checkpoint CP-COL-2026-10-17-01

- Criados contrato, especificação, protótipo NTSL, plano de testes e roadmap.
- O protótipo foi ajustado ao exemplo documental do Manual NTSL 4.4: igualdade = amarelo; fechamento superior = verde; caso restante = vermelho.
- A revisão documental da sintaxe básica não equivale a compilação.
- Nenhuma ordem é enviada pelo protótipo.
- Não foi declarada compilação nem execução no Profit.
- A meta diária de 1% não faz parte desta regra e não constitui promessa de resultado.
- Inventário da pasta confirmado no GitHub; seis ficheiros presentes.

## Pendências externas ao repositório

1. Compilar `03_IMPLEMENTACAO_NTSL_EXPERIMENTAL.src` no Profit.
2. Executar COL-T01 a COL-T08 e guardar evidências, incluindo gráficos de ticks (60K) e Renko.
3. Corrigir o ficheiro completo se qualquer teste falhar e repetir a bateria.
4. Realizar revisão de regressão.
5. Só então decidir se a regra será mantida, revista ou descartada e se pode ser promovida.

## Regra de progresso

Não atribuir percentual global artificial. Documentação e revisão textual estão concluídas; validação no Profit permanece pendente. O módulo continua EXPERIMENTAL.
