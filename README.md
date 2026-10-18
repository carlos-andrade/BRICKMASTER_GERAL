<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: README PRINCIPAL — PORTAL DO PROJETO
IDENTIFICADOR: BM-ROOT-001
VERSÃO: 2.0.0
ESTADO: DOCUMENTAÇÃO DE ENTRADA — INVENTÁRIO TÉCNICO PENDENTE
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-19
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-10-11 | v1.0.0 | Estrutura inicial e ligações básicas.
- 2026-10-19 | v2.0.0 | Portal ampliado: missão, arquitetura, módulos, roadmap, governança, validação e referências.
SHA-256: ccd31845296a500e14b1d06eba151ed8fa731c87e35d02ee5c7034793d034d21 (conteúdo UTF-8 com as linhas SHA-256 e COMMIT DE REFERÊNCIA excluídas)
COMMIT DE REFERÊNCIA: 60fb8bea17144468ac0283606e0f734130d8693d (HEAD de base da proposta; a atualização está no commit subsequente)
FONTE DA VERDADE: documentos e código versionados no repositório.
-->

# BRICKMASTER RAIZ

**Sistema modular de leitura do contexto de mercado, destinado a responder onde o operador está no gráfico, quais evidências sustentam a leitura, o que a contradiz e quando a incerteza exige reduzir confiança ou bloquear ações.**

> **Estado geral:** em desenvolvimento. Especificações e entradas no catálogo não comprovam, por si só, implementação, compilação, backtest, validação no Profit ou prontidão para produção.

## 1. Missão operacional

O sistema deve tornar visíveis, de forma explicável e auditável:

- **Localização no gráfico:** instrumento, sessão, tipo de gráfico, posição relativa, estrutura, níveis e distância da referência desde a abertura.
- **Regime de mercado:** tendência, congestão, expansão, retração e volatilidade, de acordo com dados disponíveis.
- **Evidências:** dados observados e derivados, fonte, timestamp, versão e módulo responsável.
- **Contradições e invalidação:** divergências entre fontes, dados atrasados, mudança de regime e condições que invalidam a leitura.
- **Estado operacional:** saúde dos dados e módulos, confiança, vetos de risco e motivos de bloqueio.

O **Giroscópio** consolida o contexto sem esconder divergências nem converter hipóteses em fatos.

## 2. Princípios obrigatórios

1. Preservar históricos, versões, decisões, erros e evidências.
2. Não declarar testes, validação ou resultados sem evidência identificável.
3. Separar dados, inteligência, decisão, risco soberano, execução conciliada e watchdog.
4. Dados ausentes, inválidos, atrasados ou contraditórios reduzem confiança ou bloqueiam ações críticas.
5. Risco soberano pode vetar decisões; nenhum score pode contorná-lo.
6. Não enviar ordens por padrão. Execução requer autorização explícita e gates de risco.
7. Gráficos de ticks, incluindo 60K, são essenciais aos cenários relevantes de projeto e validação.
8. A meta de 1% a partir da abertura do dia é hipótese de pesquisa, não promessa de rentabilidade ou prioridade sobre o risco.
9. Backtests não podem usar informação indisponível no instante da decisão (look-ahead).
10. Resultados precisam indicar fonte, instrumento, sessão, fuso, versão, parâmetros, método e limitações.

## 3. Navegação principal

| Documento | Conteúdo |
|---|---|
| [Arquitetura modular](BRICKMASTER_ARQUITETURA/README.md) | Camadas, responsabilidades e princípios arquiteturais |
| [Roadmap inicial](BRICKMASTER_ARQUITETURA/ROADMAP.md) | Fases de desenvolvimento registradas em `main` |
| [Catálogo de módulos](BRICKMASTER_ARQUITETURA/MAPA_MODULOS.md) | IDs e responsabilidades de 19 domínios modulares |
| [Governança técnica](BRICKMASTER_ARQUITETURA/GOVERNANCA.md) | Práticas de mudança, segurança e promoção |
| [Contrato de módulo](BRICKMASTER_ARQUITETURA/CONTRATO_MODULO.md) | Interface e dependências mínimas |
| [Template de documentação de módulo](TEMPLATES/README_MODULO.md) | Modelo reutilizável |
| [Roadmap Mestre — branch de governança](https://github.com/carlos-andrade/BRICKMASTER_GERAL/blob/feature/governanca-fundacao/GOVERNANCA/ROADMAP_MESTRE.md) | Roadmap ampliado, ainda sujeito a revisão |
| [PR #3 — fundação de governança](https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3) | Proposta de governança aberta, ainda não integrada em `main` na última verificação |
| [FVG-ATLAS](https://github.com/carlos-andrade/FVG-ATLAS) | Repositório relacionado, com desenvolvimento independente antes da integração |

## 4. Arquitetura-alvo

```text
Fontes de dados
  → Proveniência, timestamps, sessão, normalização e qualidade
  → Persistência, histórico e replay
  → Giroscópio / estado canônico do contexto
  → Módulos analíticos independentes
  → Inteligência e decisão explicável
  → Risco soberano (veto independente)
  → Execução conciliada (somente após autorização)
  → Watchdog, auditoria e recuperação

Replay, backtest, métricas e evidências atravessam as camadas.
```

O desenho acima é a arquitetura-alvo, não uma afirmação de que todos os componentes estejam implementados. Módulos analíticos não enviam ordens nem alteram diretamente o estado de produção.

### Giroscópio e incerteza

O Giroscópio consolida localização contextual, regime, confiança, proveniência, validade, divergências e motivos de bloqueio. Não deve corrigir silenciosamente a fonte, eliminar contradições nem substituir a camada de risco.

- Dado ausente ou atrasado: explicitar disponibilidade e atualidade; degradar confiança ou bloquear conforme criticidade.
- Fontes contraditórias: preservar a divergência e identificar as fontes.
- Módulo indisponível: seguir comportamento de degradação definido no contrato.
- Estado de execução desconhecido: não presumir posição zero nem equiparar intenção a execução.
- Recuperação: reconciliar o estado observado antes de retomar qualquer operação autorizada.

## 5. Catálogo resumido de módulos

O [catálogo de módulos](BRICKMASTER_ARQUITETURA/MAPA_MODULOS.md) contém IDs, pastas e papéis definidos na linha de base documental.

| ID | Módulo | Responsabilidade |
|---|---|---|
| BM-001 | Giroscópio / Estado do Mercado | Estado contextual, confiança e divergências |
| BM-002 | Estado do Gráfico | Localização contextual no gráfico |
| BM-003 | Market DNA | Comportamento e regime |
| BM-004 | Estrutura de Mercado | Swings, deslocamento e mudança estrutural |
| BM-005 | FVG Atlas | Detecção, tamanho e acompanhamento de FVGs |
| BM-006 | Liquidez | Varreduras, captura e retorno a zonas |
| BM-007 | Contador de Toques | Contagem e qualidade de reações em zonas |
| BM-008 | VWAP/TWAP Gap | Distâncias e contexto relativo do preço |
| BM-009 | Fluxo e Volume | Volume financeiro, delta e absorção, se houver dados adequados |
| BM-010 | Volatilidade / VIX | Contexto de volatilidade e risco |
| BM-011 | IBOV / Intermercado | Contexto do índice e relações externas |
| BM-012 | Calendário Econômico | Eventos, janelas e bloqueios |
| BM-013 | Alvo +1% da Abertura | Referência analítica desde a abertura |
| BM-014 | Risco e Elegibilidade | Limites e bloqueios independentes |
| BM-015 | Adaptador NTSL/Profit | Compatibilidade e integração com a plataforma |
| BM-016 | Replay e Backtest | Reprodutibilidade e avaliação |
| BM-017 | Watchdog / Observabilidade | Saúde, alertas, falhas e kill switch |
| BM-018 | Dados e Qualidade | Integridade, sincronização e proveniência |
| BM-019 | Marcação a Mercado | P&L, exposição e reconciliação |

**Importante:** a linha de base caracteriza esses domínios como especificações/documentação inicial. O estado real de cada módulo só deve ser definido após inventário de código e evidências.

## 6. Roadmap

| Fase | Prioridade | Entrega verificável |
|---|---|---|
| 00 | Inventário, histórico e governança | Inventário de arquivos, versões, dependências, código, testes e decisões |
| 01 | Giroscópio e estado canônico | Contrato, estados, confiança, divergências, bloqueios e fixtures |
| 02 | Dados, tempo e persistência | Contratos, sessões/fusos, controles de qualidade e replay reproduzível |
| 03 | Módulos analíticos | Especificação e testes isolados por módulo |
| 04 | Inteligência e decisão | Regras explicáveis, conflitos, correlação e invalidação |
| 05 | Risco soberano | Limites, veto independente e testes de falha segura |
| 06 | Profit/NTSL, execução e watchdog | Compatibilidade, reconciliação, recuperação e monitorização |
| 07 | Replay e validação integrada | Testes reproduzíveis com custos, slippage, regressão e cenários tick/60K |
| 08 | Promoção controlada | Revisão, aprovação, versão, monitorização e rollback |

A percentagem global de conclusão **não está calculada**. Só deverá ser calculada depois do inventário técnico e separada em cobertura documental, implementação, testes executados, validação reproduzível e prontidão operacional.

### Critério de passagem

Documentação ou código existente não é suficiente. Exigir critérios de aceitação definidos antes de executar, testes efetivamente realizados, evidências reproduzíveis, limitações e riscos residuais explícitos, dependências verificadas, checkpoint e aprovação conforme a governança.

## 7. Estados de maturidade

- **PROPOSTA:** em discussão ou revisão.
- **EXPERIMENTAL:** pesquisa ou implementação isolada, sem autoridade operacional.
- **IMPLEMENTADO — NÃO VALIDADO:** existe código, faltam evidências suficientes.
- **VALIDADO:** critérios definidos satisfeitos com evidências identificáveis e reproduzíveis no escopo declarado.
- **PRODUÇÃO:** promoção formal aprovada, monitorização, recuperação e rollback.
- **BLOQUEADO:** dependência ou condição de segurança não satisfeita.
- **DEPRECADO:** substituído/descontinuado com histórico preservado.

Compilar não prova desempenho; um backtest isolado não prova robustez; um documento não prova implementação.

## 8. Desenvolvimento, rastreabilidade e integridade

Fluxo previsto: **`feature/* → develop → validação → principal`**.

Cada mudança relevante mantém objetivo, contrato, dependências, critérios de aceitação, testes e resultados observados, evidências, instruções de reprodução, limitações, checkpoint, SHA-256 do artefato e commit de referência. Não eliminar ou mover documentos históricos sem inventário e plano de migração. Não promover à branch principal sem revisão e aprovação explícitas.

## 9. Referências de projeto

- **Manual NTSL 4.4 — 03/08/2026:** referência principal fornecida para analisar sintaxe e funcionalidades NTSL; cada implementação ainda exige verificação de compatibilidade com o manual e a versão real do Profit.
- [FVG-ATLAS](https://github.com/carlos-andrade/FVG-ATLAS): desenvolver e validar separadamente antes da integração.
- [B3](https://github.com/carlos-andrade/B3): repositório relacionado; não presumir atualização, licença ou disponibilidade sem prova.
- [BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL): projeto separado; consumir somente interfaces e dados documentados e autorizados.
- [PR #3 — governança](https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3): proposta aberta na última verificação, não integrada em `main`.

## 10. Segurança e limites de afirmação

O BRICKMASTER não promete retorno financeiro nem garante atingir 1% ao dia. A referência de 1% é hipótese de pesquisa e permanece subordinada à qualidade dos dados e ao risco soberano.

Não declarar estratégia compilada, testada no Profit, lucrativa, operacional ou pronta para capital real sem evidência específica. Esta página é um portal de navegação; evidências detalhadas pertencem aos artefatos e relatórios de cada módulo.

## 11. Estado conhecido na revisão de 2026-10-19

- `main` contém a arquitetura inicial, roadmap inicial e catálogo documental.
- O Roadmap Mestre e a fundação documental de governança estão associados à branch `feature/governanca-fundacao` e ao PR #3.
- O PR #3 estava aberto e não integrado na consulta realizada.
- O inventário completo da árvore histórica e a reconciliação de todos os artefatos permanecem pendentes.
- Nesta atualização documental não foram executados testes NTSL, compilação no Profit, backtests, paper trading ou validação operacional.

## 12. Próximo checkpoint

**ID:** BM-CP-README-0002  
**Objetivo:** ampliar o portal principal, ligando arquitetura, módulos, roadmap, governança e critérios de evidência sem apagar histórico.  
**Critério de encerramento:** conteúdo versionado, hash calculado a partir dos bytes finais, commit identificado, links e diff revisados.  
**Próxima ação técnica:** concluir o inventário da fase 00 e reconciliar os estados de cada módulo contra código e evidências reais.

---

**Integridade documental:** o SHA-256 precisa ser calculado sobre a versão final gravada. O commit de referência só pode ser registado após a criação desse commit.
