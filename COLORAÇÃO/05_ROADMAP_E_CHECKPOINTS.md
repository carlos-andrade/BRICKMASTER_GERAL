# BRICKMASTER RAIZ — Roadmap e Checkpoints de COLORAÇÃO

> **ID:** BM-COL-ROADMAP-001  
> **Versão:** 1.0.0  
> **Data:** 2026-10-17  
> **Estado global:** EM DESENVOLVIMENTO

## Roadmap verificável

| Fase | Entregável | Estado | Evidência |
|---|---|---|---|
| C0 | Diretório e README inicial | Concluído | Commit anterior de criação da pasta |
| C1 | Contrato e limites arquiteturais | Concluído | `01_ARQUITETURA_E_CONTRATO.md` |
| C2 | Regra visual base especificada | Concluído | `02_REGRA_BASE_EXPERIMENTAL.md` |
| C3 | Protótipo NTSL sem ordens | Experimental | `03_IMPLEMENTACAO_NTSL_EXPERIMENTAL.src`; compilação não comprovada |
| C4 | Plano de testes | Concluído como plano; execução pendente | `04_PLANO_DE_TESTES_E_EVIDENCIAS.md` |
| C5 | Compilação e testes no Profit | Bloqueado por necessidade de execução no ambiente Profit | Evidências ainda não fornecidas |
| C6 | Revisão de regressão e aprovação de integração | Pendente | Depende de C5 |
| C7 | Promoção para VALIDADO/PRODUÇÃO | Pendente | Exige evidências e aprovação |

## Checkpoint CP-COL-2026-10-17-01

- Criados contrato, especificação, protótipo e plano de testes.
- A regra de referência apenas compara o fechamento atual com o anterior.
- Nenhuma ordem é enviada pelo protótipo.
- Não foi declarada compilação nem execução no Profit.
- A meta diária de 1% não faz parte desta regra e não constitui promessa de resultado.

## Pendências que exigem ambiente externo

1. Confirmar a sintaxe do protótipo no Manual 4.4/editor NTSL e compilar no Profit.
2. Executar COL-T01 a COL-T08 e guardar evidências.
3. Corrigir integralmente o ficheiro caso qualquer caso falhe.
4. Realizar revisão de regressão.
5. Só então decidir se a regra será mantida, revista ou descartada.

## Regra de progresso

Percentuais de conclusão só podem ser atribuídos com base em critérios verificáveis. Documentação concluída não equivale a código validado. O módulo permanece EXPERIMENTAL até ao fecho das pendências acima.
