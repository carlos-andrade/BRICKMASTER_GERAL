---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE_03_GIROSCOPIO_ESTADO_DO_GRAFICO"
id_documento: "BM-CORE-001-TESTES"
titulo: "Plano de testes — Giroscópio contextual"
status: "PLANEADO; NAO_EXECUTADO"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Contrato BM-CORE-001-ESPECIFICACAO"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase02-03-contracts"
escopo: "Testes determinísticos de localização, qualidade e bloqueios"
objetivo: "Verificar o contrato antes da integração"
dependencias: "ESPECIFICACAO.md; BM-DATA-001; módulos produtores aprovados"
---

# Plano de testes — Giroscópio contextual

## Contexto Histórico

Criado antes da implementação para separar contexto de sinal, decisão, risco e execução.

## Estado

PLANEADO — todos os casos NOT_RUN.

## Evidências

A produzir após implementação: inputs, versões, tipo de gráfico, timestamp, modo de dados, resultado esperado/observado e artefacto.

## Validação

A existência do plano não comprova implementação nem execução de testes.

## Resultado

Critérios mínimos de aceitação definidos para o contrato.

## Próxima Ação

Executar cada caso após implementação isolada; falhas essenciais devem bloquear ou resultar em estado desconhecido.

| ID | Caso | Resultado esperado | Estado |
|---|---|---|---|
| GY-01 | Preço acima/abaixo/na abertura | Localização coerente com referência e tolerância aprovada | NOT_RUN |
| GY-02 | Abertura ausente | `BLOCKED/UNKNOWN`; sem localização inventada | NOT_RUN |
| GY-03 | Dados essenciais obsoletos | `BLOCKED` com motivo | NOT_RUN |
| GY-04 | Fonte não essencial ausente | `DEGRADED` com razão | NOT_RUN |
| GY-05 | Fontes atuais contraditórias | `CONFLICT` e evidências expostas | NOT_RUN |
| GY-06 | Identidade ausente | `BLOCKED` | NOT_RUN |
| GY-07 | Mudança de sessão | Transição determinística | NOT_RUN |
| GY-08 | Mesmo input em replay | Mesmo estado/localização | NOT_RUN |
| GY-09 | Gráfico de 60K ticks | Estado reproduzível | NOT_RUN |
| GY-10 | Módulo FVG/fluxo não validado | Não é usado como entrada essencial | NOT_RUN |
| GY-11 | Conflito entre módulos | Sem score arbitrário; estado `CONFLICT` | NOT_RUN |
| GY-12 | Efeitos colaterais | Nenhuma ordem/posição alterada | NOT_RUN |
| GY-13 | Entrada inválida e recuperação | Bloqueio até dados válidos e recuperação explícita | NOT_RUN |
