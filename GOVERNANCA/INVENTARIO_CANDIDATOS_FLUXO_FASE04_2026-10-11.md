---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "INVENTARIO_DE_CANDIDATOS_DE_FLUXO"
fase: "FASE_04_ESTRUTURA_E_MODULOS_DE_MERCADO"
id_documento: "BM-INV-FLOW-001"
titulo: "Inventário inicial de candidatos de fluxo, VWAP/TWAP e volume"
status: "INVENTARIO_DE_CAMINHOS_CONCLUIDO; VALIDACAO_TECNICA_PENDENTE"
versao: "1.0.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Árvore recursiva de BRICKMASTER_GERAL/develop e leitura focalizada dos ficheiros indicados"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase04-inventario-fluxo"
escopo: "Identificar candidatos existentes para fluxo, delta, volume financeiro e VWAP/TWAP sem os declarar canónicos"
objetivo: "Evitar duplicação de módulos e tornar explícitas as lacunas antes de integração"
dependencias: "Manual NTSL 4.4; ARQUITETURA/BRICKMASTER_RAIZ/REGISTRO_MODULOS_E_CHECKPOINTS.md"
---

# Inventário inicial de candidatos de fluxo, VWAP/TWAP e volume

> **Projeto:** BRICKMASTER RAIZ  
> **Fase:** 04 — Estrutura e módulos de mercado  
> **ID:** BM-INV-FLOW-001  
> **Estado:** INVENTÁRIO DE CAMINHOS CONCLUÍDO; VALIDAÇÃO TÉCNICA PENDENTE  
> **Data:** 2026-10-11

## Contexto Histórico

A baseline arquitetural define L4 como fluxo e confirmação, mas adverte que delta, agressão, volume financeiro, VWAP/TWAP e fontes externas não devem ser presumidos disponíveis sem verificar fonte e suporte real. A árvore de BRICKMASTER contém ficheiros experimentais/legados com nomes relacionados. Este documento apenas cataloga candidatos e hashes; não os promove a módulos oficiais nem altera código.

## Estado

### Candidatos identificados

| Candidato | Caminho | Blob SHA | Evidência de estado | Próxima ação |
|---|---|---|---|---|
| VWAP diária/semanal/mensal | `ROBÔ_TRADE/CARLOS_SETUP_VWAPS.src` | `0583192d32c8fa3eef6c2ccfefa84458a6a5e245` | Fonte curta com `VWAP(1/2/3)`; sintaxe/semântica não validadas nesta tarefa | Conferir funções e período no Manual NTSL 4.4 e no Profit |
| VWAP/TWAP e ativos externos | `ROBÔ_TRADE/CAR_TWAP.src` | `c6963c27aa5c0998f7dd8c792f49835e40f0bce2` | Código experimental; inclui referências a WINFUT e IBOV | Definir se TWAP é por tempo, negócio ou outra janela; verificar feeds, sincronização e funções |
| VWAP/Heikin-Ashi | `ROBÔ_TRADE/HEIKIN_VWAP.src` | `196a3233cdf41d2f8d455fd776e4e9d652ac5eca` | Código experimental combinado, não isolado | Separar responsabilidade de VWAP e Heikin-Ashi antes de qualquer reaproveitamento |
| Delta de preço em Renko | `ROBÔ_TRADE/CAR_DELTAPRICE_RENKOv1.src` | `a725fb1badb6153abd027e0f50709c6b2598ad70` | Cabeçalho restringe uso a Renko 15R/WINFUT; não generalizar para ticks/60K | Definir contrato e limites de compatibilidade de gráfico |
| Delta quadro em Renko | `ROBÔ_TRADE/CAR_DELTAQUADRO_RENKOv1.src` | `829b7b577ed10787b41f78eb494d0d5286ae704c` | Variante legada; não é canónica por nome | Comparar lógica e diferenças contra variantes irmãs |
| Delta em Renko | `ROBÔ_TRADE/CAR_DELTA_RENKOv1.src` | `0e2c941ccc80a6694c9569ee211f338556d73fc9` | Variante legada; não é canónica por nome | Comparar lógica e diferenças contra variantes irmãs |
| Delta preço/range Renko | `ROBÔ_TRADE/CAR_DELTAPRICERANGE_RENKOv1.src` | `9f80d8b7dcc7f2567ede4fb87dced9b5ff99b386` | Variante legada; não é canónica por nome | Comparar lógica e diferenças contra variantes irmãs |
| Volume financeiro acumulado anómalo | `BRICKMASTER_CLAUDE/CÓDIGO NTSL/BRICKMASTER_CumulativeVolume_Standalone.src` | `0bb65120663f0de9f1b7d54ee88d32895d6ab095` | Comentário identifica indicador standalone v2 e Manual NTSL v4.2; não é prova de compatibilidade 4.4 | Rever sintaxe/funções e a definição de volume com Manual 4.4; testar separadamente |

## Lacunas identificadas na árvore consultada

Não foram encontrados caminhos de ficheiros com nomes identificáveis para módulos autónomos de:

- Giroscópio.
- Liquidez/sweep.
- Contador de toques.
- Market DNA.
- Watchdog.
- Adaptador de risco soberano/execução conciliada.

Esta conclusão limita-se aos caminhos e nomes pesquisados na árvore atual. Não prova inexistência em conteúdos internos, conversas anteriores, outros repositórios ou ficheiros com nomes não relacionados.

VIX e IBOV aparecem como referências em arquitetura/código, mas não foi validado neste inventário um adaptador fiável com timestamp, atraso, proveniência e política de bloqueio.

## Evidências

- Árvore recursiva de `BRICKMASTER_GERAL/develop`: SHA `4123a35207398e9420b4deba8c2ef19dc5cb0ae8`, `truncated=false`, 215 blobs no momento da consulta.
- Os caminhos e hashes da tabela foram lidos da árvore GitHub; os seis primeiros códigos foram inspecionados de forma focalizada quanto ao cabeçalho e ao início do conteúdo.
- A fonte CumulativeVolume declara no comentário inicial Manual NTSL v4.2, não v4.4.
- A baseline arquitetural existente exige confirmar suporte real para delta/agressão/book/VWAP/TWAP e declarar compatibilidade por tipo de gráfico.

## Validação

**Concluído:** inventário inicial dos candidatos de código e registo dos hashes.

**Pendente:** revisão linha a linha, análise de dependências/funções, compilação NTSL 4.4, execução no Profit, validação em gráficos de ticks (incluindo 60K), dados de replay e testes estatísticos.

Os nomes dos ficheiros não estabelecem prioridade, qualidade, validade ou versão canónica. Não foram enviados sinais ou ordens.

## Resultado

Os candidatos de fluxo/VWAP/TWAP/volume foram identificados sem alterar código. O estado correto é **legado/experimental a avaliar**, não “validado” ou “pronto para integração”. As lacunas de módulos centrais ficam registadas para recuperação de históricos ou especificação controlada.

## Próxima Ação

1. Comparar as variantes de delta para descobrir diferenças reais antes de escolher uma referência.
2. Conferir cada função com o Manual NTSL 4.4 e documentar a evidência da consulta.
3. Definir contratos independentes para VWAP, TWAP, delta e volume financeiro; não combinar os módulos prematuramente.
4. Recuperar ou especificar os módulos ausentes (Giroscópio, liquidez, contador de toques, Market DNA, risco e Watchdog).
5. Executar testes isolados no Profit apenas com critérios, dados e evidências registados.

## Histórico de versões

- 1.0.0 — 2026-10-11 — primeiro inventário de candidatos de fluxo e indicadores associados.

<!-- RECONCILIACAO_SHA256: d6f78573a55fb19264881286633e872555c2fd3cb6e3d8885d703e626f9fc637
COMMIT_DE_REFERENCIA: c0740f9fd4d1485b3c3a1b8568053b8cd077e688
-->
