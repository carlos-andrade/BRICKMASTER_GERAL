---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE_05_DECISAO_E_RISCO_SOBERANO"
id_documento: "BM-RISK-001-TESTES"
titulo: "Plano de testes — Risco soberano"
status: "PLANEADO; NAO_EXECUTADO"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Contrato BM-RISK-001-ESPECIFICACAO"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase05-risco-soberano"
escopo: "Testes de veto, limites, falhas e reconciliação"
objetivo: "Verificar que o risco soberano prevalece sobre sinais e metas"
dependencias: "ESPECIFICACAO.md; limites aprovados; dados/execução simulados"
---

# Plano de testes — Risco soberano

## Contexto Histórico

Plano criado antes da implementação; os parâmetros numéricos permanecem por aprovar.

## Estado

PLANEADO — todos os casos NOT_RUN.

## Evidências

Registar política/versão, inputs, sinal proposto, posição/ordens, estado esperado/observado e artefacto.

## Validação

Plano documental; não comprova execução.

## Resultado

Casos de veto definidos sem inventar limites de risco.

## Próxima Ação

Executar em ambiente simulado depois de aprovar a política versionada.

| ID | Caso | Resultado esperado | Estado |
|---|---|---|---|
| RK-01 | Limites obrigatórios ausentes | `BLOCK` | NOT_RUN |
| RK-02 | Limite diário de perda atingido | `HALT/BLOCK` conforme política | NOT_RUN |
| RK-03 | Exposição máxima excedida | `BLOCK` | NOT_RUN |
| RK-04 | Número máximo de tentativas atingido | `BLOCK` | NOT_RUN |
| RK-05 | Dados essenciais obsoletos | `BLOCK` | NOT_RUN |
| RK-06 | Posição/ordens divergentes do Profit | `HALT` até reconciliação | NOT_RUN |
| RK-07 | Meta de 1% atingida | Não força novas operações | NOT_RUN |
| RK-08 | Meta de 1% não atingida | Não aumenta risco automaticamente | NOT_RUN |
| RK-09 | Módulo de inteligência tenta contornar veto | Risco prevalece | NOT_RUN |
| RK-10 | Reinício com estado de conta desconhecido | `HALT/BLOCK` | NOT_RUN |
| RK-11 | Recuperação após falha | Requer dados válidos e reconciliação | NOT_RUN |
| RK-12 | Efeitos colaterais | Nenhuma ordem real enviada nos testes iniciais | NOT_RUN |
