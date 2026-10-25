---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ROADMAP_MESTRE"
fase: "GOVERNANCA"
id_documento: "BM-ROADMAP-001"
titulo: "Roadmap Mestre — BRICKMASTER RAIZ"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; branch feature/pr3-governanca-mainline-reconciliation; main-base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "Roadmap Mestre — BRICKMASTER RAIZ"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "6a81bbc870b413ccffd2f7249ad96c12daea81297d97af92b48263cd872b9619"
commit_referencia: "PENDENTE_APOS_COMMIT"
---

# Roadmap Mestre — BRICKMASTER RAIZ

## Contexto Histórico

O desenvolvimento do BRICKMASTER RAIZ, dos módulos experimentais e dos componentes Profit/NTSL ocorreu ao longo de diferentes conversas e áreas de trabalho. Este roadmap centraliza a sequência de trabalho e os critérios de passagem entre fases. Não substitui especificações existentes, não elimina históricos e não declara que uma funcionalidade está implementada ou validada sem evidência.

## Estado

Roadmap inicial proposto. A fundação documental está recuperada no PR #41 e continua sujeita a validação e revisão.

## Princípios de execução

1. Preservar histórico, decisões, artefactos e falhas.
2. Usar o ciclo `feature/* → develop → validação → main`.
3. Separar EXPERIMENTAL, VALIDADO, PRODUÇÃO, BLOQUEADO e DEPRECADO.
4. Cada módulo deve ter contrato, dependências, testes, evidências, limitações e checkpoint.
5. Dados ausentes, inválidos, atrasados ou contraditórios reduzem confiança ou bloqueiam ações.
6. O Giroscópio consolida o estado contextual; não substitui a validação da fonte.
7. Risco soberano pode vetar a decisão e a execução.
8. Não enviar ordens por padrão; execução exige autorização explícita.
9. O gráfico de referência BRICKMASTER usa 60K trades; a linha branca representa o preço de abertura do mercado.
10. A meta de 1% desde a abertura é hipótese de pesquisa, não promessa nem prioridade sobre o risco.

## Fases do roadmap

| Fase | Objetivo | Entrega verificável | Estado inicial |
|---|---|---|---|
| 00 — Inventário e governança | Consolidar documentos, versões, decisões, módulos e evidências sem apagar históricos | Inventário rastreável, mapa de dependências, decisões e roadmap aprovado | EM ESTRUTURAÇÃO |
| 01 — Giroscópio | Definir o estado canónico e a localização contextual do operador no gráfico | Contrato versionado, estados, qualidade/confiança, bloqueios e fixtures | ESPECIFICAÇÃO PENDENTE |
| 02 — Dados, tempo e persistência | Padronizar instrumento, sessão, timestamp/fuso, validade, lacunas, armazenamento e replay | Contratos de dados, testes de qualidade e persistência reproduzível | VALIDAÇÃO PENDENTE |
| 03 — Módulos analíticos | Desenvolver e testar módulos independentes | Contrato e testes separados para FVG-ATLAS, contador de toques, liquidez, Market DNA, VWAP/TWAP, fluxo, VIX, IBOV e calendário económico | PARCIAL / EXPERIMENTAL |
| 04 — Inteligência e decisão | Combinar evidências sem contar sinais correlacionados como independentes | Regras explicáveis, conflitos, confiança, cenários e invalidação | ESPECIFICAÇÃO PENDENTE |
| 05 — Risco soberano | Aplicar limites e bloqueios independentes da estratégia | Matriz de risco, condições de bloqueio e testes de falha segura | ESPECIFICAÇÃO PENDENTE |
| 06 — Profit/NTSL, execução e Watchdog | Validar a estratégia, reconciliar ordens/posições e detetar falhas | Compilação documentada, testes no Profit, reconciliação e recuperação | NÃO VALIDADO |
| 07 — Replay e validação integrada | Medir comportamento histórico e operacional com custos e limitações | Relatório reproduzível, baseline, métricas, testes de regressão e cenários 60K trades | PENDENTE |
| 08 — Promoção controlada | Integrar somente componentes aprovados | Aprovação explícita, versão/tag, monitorização, rollback e checkpoint de produção | PENDENTE |

Os estados acima são uma linha de base de planejamento e devem ser atualizados quando houver evidências novas. Não equivalem a resultados de testes.

## Dependências arquiteturais

```text
Fontes de dados
  → Qualidade, tempo e persistência
  → Giroscópio / estado canónico
  → Módulos analíticos independentes
  → Inteligência e decisão
  → Risco soberano
  → Execução conciliada
  → Watchdog, auditoria e recuperação

Replay/backtest e evidências atravessam todas as camadas.
Interface do operador expõe contexto, estado, confiança, fonte e motivo de bloqueio.
```

## Contrato mínimo obrigatório por módulo

1. Identidade estável, versão e estado de maturidade.
2. Objetivo e não objetivos.
3. Entradas, tipos, unidades, fontes, timestamps e validade.
4. Saídas, semântica, unidades e garantias.
5. Dependências diretas/indiretas e comportamento quando indisponíveis.
6. Regras, parâmetros, pré-condições e pós-condições.
7. Erros, limites, dados ausentes, atrasados, duplicados e contraditórios.
8. Testes unitários, contrato, integração, regressão e falha segura.
9. Fixtures, logs, artefactos e método de reprodução.
10. Limitações, riscos residuais, compatibilidade e rollback.
11. Checkpoint e próximo passo com critério objetivo.

## Critérios para avançar de fase

Uma fase só pode ser marcada como concluída quando os entregáveis estiverem versionados; os critérios forem definidos antes da execução; os testes aplicáveis forem executados; as evidências forem identificáveis e reproduzíveis; as limitações e os riscos estiverem explícitos; as dependências forem verificadas; e o checkpoint registar decisão e próximo passo.

Sem evidência suficiente, o estado é PENDING ou BLOCKED — nunca PASS por omissão.

## Barra de conclusão

A percentagem global ainda não está calculada. Não atribuir percentagens por impressão, número de documentos ou quantidade de ideias. Após inventário por entregável, calcular separadamente cobertura documental, implementação, testes executados, validação reproduzível e prontidão operacional.

## Evidências

- Repositório central: https://github.com/carlos-andrade/BRICKMASTER_GERAL
- PR original #3, encerrado sem merge: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR de recuperação #41: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Manual NTSL 4.4 fornecido no projeto; cada implementação ainda exige verificação de compatibilidade.

## Resultado

Roadmap consolidado como proposta de organização. A criação do documento não demonstra que as fases ou módulos foram concluídos.

## Próxima Ação

Validar estrutura documental, referências e SHA-256 canónicos; depois concluir a revisão do PR de recuperação antes da integração.

## Contexto Histórico

Documento recuperado da proposta histórica PR #3, fechada sem merge, e reconciliado numa branch derivada do main corrente.

## Estado

PROPOSTA PARA REVISÃO. Não equivale a aprovação da governança, implementação operacional ou produção.

## Evidências

- PR #3 fechado sem merge: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR de recuperação: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Main-base: 3db0c88f27fec4c6ea2418749de09ebba8130fe7

## Validação

Estrutura documental sujeita ao workflow do repositório. O SHA-256 canónico será calculado sobre o corpo normalizado UTF-8/LF, excluindo apenas este bloco de metadados; o commit de referência será atualizado após a gravação final. Não foram executados testes NTSL, Profit, backtest nem validação operacional.

## Resultado

Conteúdo preservado e adaptado para revisão sobre o main corrente, sem substituir os artefactos de governança preexistentes.

## Próxima Ação

Executar a validação documental, auditar o SHA-256 final, conferir links e referências cruzadas e rever o PR antes de qualquer integração.
