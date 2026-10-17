# COLORAÇÃO — BRICKMASTER RAIZ

## Objetivo
Diretório dedicado às regras de coloração visual do gráfico e à documentação dos critérios usados para classificar estados do mercado no ecossistema BRICKMASTER.

## Conteúdo
- `01_ARQUITETURA_E_CONTRATO.md` — responsabilidades, entradas/saídas e invariantes.
- `02_REGRA_BASE_EXPERIMENTAL.md` — regra visual de referência.
- `03_IMPLEMENTACAO_NTSL_EXPERIMENTAL.src` — protótipo sem ordens.
- `04_PLANO_DE_TESTES_E_EVIDENCIAS.md` — casos de teste e evidências exigidas.
- `05_ROADMAP_E_CHECKPOINTS.md` — estados, pendências e checkpoint.

## Governança
- Preservar históricos e versões existentes; não sobrescrever artefactos sem auditoria.
- Separar conteúdo experimental, validado e de produção.
- Documentar objetivo, entradas, saídas, dependências, limitações e testes de cada regra.
- Não declarar validação de código NTSL sem evidência de compilação ou execução no Profit.
- A coloração é informativa; não deve enviar ordens nem substituir os controlos de risco soberano.
- Manual NTSL 4.4 (03-08-2026) é a referência documental prioritária.

## Estado atual
**EXPERIMENTAL.** A sintaxe básica foi conferida contra o exemplo do Manual 4.4; a compilação e os testes no Profit ainda não foram comprovados.
