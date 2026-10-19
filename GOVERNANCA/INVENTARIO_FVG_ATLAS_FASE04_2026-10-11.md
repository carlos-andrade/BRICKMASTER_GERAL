---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "INVENTARIO_DE_MODULO_EXTERNO"
fase: "FASE_04_ESTRUTURA_E_MODULOS_DE_MERCADO"
id_documento: "BM-INV-FVG-ATLAS-001"
titulo: "Inventário técnico inicial — FVG-ATLAS"
status: "INVENTARIADO; INTEGRACAO_BRICKMASTER_PENDENTE"
versao: "1.0.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Repositório privado carlos-andrade/FVG-ATLAS, branch main"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase04-inventario-fvg"
escopo: "Inventário inicial de ficheiros, versão de referência, evidências e pendências do FVG-ATLAS"
objetivo: "Integrar o conhecimento do FVG-ATLAS no catálogo BRICKMASTER sem copiar código nem apagar históricos"
dependencias: "carlos-andrade/FVG-ATLAS; Manual NTSL 4.4; BRICKMASTER_GERAL"
---

# Inventário técnico inicial — FVG-ATLAS

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório central:** carlos-andrade/BRICKMASTER_GERAL  
> **Fonte externa:** carlos-andrade/FVG-ATLAS  
> **Tipo:** INVENTÁRIO DE MÓDULO EXTERNO  
> **Fase:** 04 — Estrutura e módulos de mercado  
> **ID:** BM-INV-FVG-ATLAS-001  
> **Estado:** INVENTARIADO; INTEGRAÇÃO BRICKMASTER PENDENTE  
> **Versão do documento:** 1.0.0  
> **Data:** 2026-10-11

## Contexto Histórico

O registo mestre BRICKMASTER já identificava o FVG-ATLAS como repositório relacionado, mas deixava o código por inventariar. Foi consultada a árvore recursiva de `main` do repositório privado `carlos-andrade/FVG-ATLAS`. Este documento referencia a fonte sem copiar ficheiros, alterar o repositório externo ou substituir o histórico de versões.

## Estado

**Inventário estrutural da fonte externa:** concluído para o snapshot indicado.

- Repositório: https://github.com/carlos-andrade/FVG-ATLAS
- Branch: `main`
- SHA da árvore: `379115a60f70d8835f1fa71278dd344e6a253bd0`
- Árvore truncada: `false`
- Total: 249 ficheiros/blobs.
- Extensões: 101 `.src`, 147 `.md`, 1 `.pdf`.
- Fonte de código de referência indicada pelo roadmap externo: `FVG_ATLAS_V2.1.33_REGRESSAO_INTEGRADA_LATCH_HISTORICO.src`.
- Blob SHA do código: `1294ff5054754060ac52dd87b368c6e474e6179d`.
- Resultado associado: `testes/FVG_ATLAS_V2.1.33_RESULTADO_REGRESSAO_INTEGRADA_APROVADO_2026-09-23.md`, SHA `e0ff480371b940b249ea2f769995b6bf05caae93`.
- Roadmap externo: `docs/FVG_ATLAS_ROADMAP_ATUALIZADO_2026-09-23.md`, SHA `581342614f732d7bd440d8282fe3adddba9e8830`.

### Contrato de comportamento descrito pela fonte

A versão 2.1.33 documenta um ciclo de vida de FVG:

`FORMATION → STATE/HITS → RETEST → REACTION → INVALIDATION → RECYCLE`

Regras explicitadas no código/relatórios consultados:

- Formação BULL: `Low > High[2]`.
- Formação BEAR: `High < Low[2]`.
- STATE progressivo: `0 → 25 → 50 → 75 → 100`, baseado em MAX penetration sem regressão.
- CURRENT, MAX e STATE são conceitos distintos; `GAP = MAX - CURRENT`.
- A barra de formação não deve contar como RETEST nem INVALIDATION.
- Igualdade na borda não invalida, segundo o protocolo de regressão.
- RECYCLE deve libertar o slot invalidado, preservar o histórico e reutilizar o mesmo slot.
- A evidência descrita reporta capacidade de 20 FVGs.

Estas regras são transcritas como conteúdo documental da fonte externa; a integração e a compatibilidade no BRICKMASTER ainda não foram verificadas.

### Estado do roadmap externo

O roadmap de 2026-09-23 classifica V2.1.33 como aprovada na regressão integrada do ciclo de vida, com evidência documentada para FORMATION, STATE, RETEST, REACTION, INVALIDATION e RECYCLE. O próprio roadmap declara pendências posteriores: congelar a especificação oficial, formalizar a máquina de estados, desenvolver o FVG Engine científico, fechar MFE/MAE/FILL, consolidar base de dados/histórico, observabilidade, testes de stress e validação estatística.

## Evidências

1. Árvore GitHub recursiva de `main`, SHA `379115a60f70d8835f1fa71278dd344e6a253bd0`, sem truncamento.
2. Código de referência V2.1.33, blob SHA `1294ff5054754060ac52dd87b368c6e474e6179d`.
3. Resultado de regressão integrada V2.1.33, blob SHA `e0ff480371b940b249ea2f769995b6bf05caae93`.
4. Roadmap atualizado do FVG-ATLAS, blob SHA `581342614f732d7bd440d8282fe3adddba9e8830`.
5. O relatório de resultado identifica o resultado numérico como corrigido/informado pelo utilizador e conclui que o ciclo completo foi aprovado. Esta é evidência documental do projeto FVG-ATLAS, não um teste executado nesta sessão nem uma validação independente do BRICKMASTER.

## Validação

**Validado nesta tarefa:** existência dos artefactos e hashes na árvore GitHub; contagem/extensões; leitura dos cabeçalhos do código, roadmap e relatório de resultado; identificação das pendências declaradas pelo projeto externo.

**Não validado nesta tarefa:** compilação do código no Profit, compatibilidade efetiva com Manual NTSL 4.4, comportamento em gráfico de 60K ticks, replay, execução em tempo real, desempenho estatístico ou integração com o Giroscópio/risco soberano.

O volume de versões históricas não autoriza escolher ou apagar ficheiros automaticamente. V2.1.33 é a referência indicada pelo roadmap externo para a regressão integrada, mas não é, por esse motivo isolado, uma release de produção BRICKMASTER.

## Resultado

FVG-ATLAS passa de “repositório relacionado conhecido; código a inventariar” para **“inventário estrutural concluído; referência V2.1.33 identificada; integração BRICKMASTER pendente”**. O módulo não está aprovado para decisão ou execução de trading no BRICKMASTER.

## Próxima Ação

1. Congelar a especificação do ciclo de vida externo sem alterar regras de mercado aprovadas.
2. Mapear entradas, saídas, variáveis persistentes, limites de arrays/slots e efeitos de diagnóstico da V2.1.33.
3. Comparar as funções utilizadas com o Manual NTSL 4.4 antes de declarar compatibilidade.
4. Definir contrato BRICKMASTER para ID estável do FVG, direção, Top/Bottom, tamanho, idade, estado, mitigação, retest, reaction, invalidation e recycle.
5. Criar testes de contrato isolados, incluindo dados ausentes, formação/reteste na mesma barra, igualdade de borda, 20/20 slots e preservação histórica.
6. Só depois decidir o adaptador de integração; manter execução financeira desativada.

## Histórico de versões

- 1.0.0 — 2026-10-11 — primeiro inventário estrutural e técnico baseado nos artefactos consultados no FVG-ATLAS.

<!-- RECONCILIACAO_SHA256: fcdfc8a9a5f996fc1af0e7f7f50f68d8b86b15bf335ca643c216f03e0cbd4b1b
COMMIT_DE_REFERENCIA: c0740f9fd4d1485b3c3a1b8568053b8cd077e688
-->
