# COLORAÇÃO — BRICKMASTER RAIZ

## Objetivo
Diretório dedicado às regras de coloração visual do gráfico e à documentação dos critérios usados para classificar estados do mercado no ecossistema BRICKMASTER.

## Conteúdo
- `01_ARQUITETURA_E_CONTRATO.md` — responsabilidades, entradas/saídas e invariantes.
- `02_REGRA_BASE_EXPERIMENTAL.md` — regra visual de referência.
- `03_IMPLEMENTACAO_NTSL_EXPERIMENTAL.src` — protótipo sem ordens.
- `04_PLANO_DE_TESTES_E_EVIDENCIAS.md` — casos de teste e evidências exigidas.
- `05_ROADMAP_E_CHECKPOINTS.md` — estados, pendências e checkpoint de aprovação.

## Governança
- Preservar históricos e versões existentes; não sobrescrever artefactos sem auditoria.
- Separar conteúdo experimental, validado e de produção.
- Documentar objetivo, entradas, saídas, dependências, limitações e testes de cada regra.
- Não declarar validação técnica de código NTSL sem evidência verificável de compilação ou execução no Profit.
- A coloração é informativa; não deve enviar ordens nem substituir os controlos de risco soberano.
- Manual NTSL 4.4 (03-08-2026) é a referência documental prioritária.

## Estado de encerramento
**Ciclo documental: CONCLUÍDO E APROVADO PELO UTILIZADOR em 2026-10-17.**

O utilizador aprovou explicitamente C3, C5, C6 e C7. Esta decisão está registada no roadmap. A captura recebida mostra o candle identificado como 26 amarelo num gráfico de 60.000 ticks; não apresenta os valores numéricos de fechamento, a versão/build do Profit ou o log de compilação. Por rigor de auditoria, a aprovação do utilizador não é apresentada como prova técnica independente de compilação, bateria completa de testes ou regressão.

O protótipo permanece sem envio de ordens e sem gestão de posições/stops. A promoção técnica para VALIDADO/PRODUÇÃO só pode ser afirmada quando os artefactos de compilação, execução e regressão estiverem disponíveis e vinculados ao código testado.
