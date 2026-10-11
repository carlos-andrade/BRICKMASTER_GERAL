# BRICKMASTER RAIZ — Registo de módulos e checkpoints

Data: 2026-10-11  
Estado inicial: DOCUMENTAÇÃO CRIADA; inventário completo dos arquivos ainda não executado.  
Documento associado: ARQUITETURA/BRICKMASTER_RAIZ/ARQUITETURA_MODULAR_BASELINE_2026-10-11.md

## 1. Registo mestre de módulos

Este registo é um índice de trabalho. Os estados abaixo descrevem o que está confirmado neste checkpoint documental, não a existência ou inexistência de código em outros caminhos.

| ID | Módulo | Responsabilidade | Estado do inventário | Próxima ação |
|---|---|---|---|---|
| BM-CORE-001 | GIROSCÓPIO | Contexto central e localização do operador no gráfico | A inventariar | Localizar versões existentes e consolidar definições |
| BM-DATA-001 | Relógio/Sessão/Abertura | Identificar sessão e referência diária | A inventariar | Localizar cálculos existentes; definir testes de transição |
| BM-STRUCT-001 | Estrutura de preço | Swings, deslocamento e rompimento | A inventariar | Mapear código e documentação |
| BM-FVG-001 | FVG Atlas | Identificar FVGs, dimensão e ciclo de vida | Repositório relacionado conhecido; código a inventariar | Comparar com FVG-ATLAS e localizar versões no repositório central |
| BM-LIQ-001 | Liquidez | Níveis, varredura e reação | A inventariar | Localizar especificações existentes e formalizar condições |
| BM-TOUCH-001 | Contador de toques | Contagem e invalidação de contactos com níveis | A inventariar | Recuperar desenho anterior e identificar parâmetros |
| BM-FLOW-001 | Fluxo | Delta, volume financeiro e VWAP/TWAP | A inventariar | Confirmar campos reais, fonte e sincronização |
| BM-MACRO-001 | Calendário económico | Contexto macro e janelas de risco | A inventariar | Inventariar fontes e regras de horário |
| BM-REF-001 | Referências externas | VIX e IBOV como contexto | A inventariar | Definir proveniência, atraso e regra de uso |
| BM-RISK-001 | Gestão de risco | Limites, exposição e interrupção | A inventariar | Identificar regras anteriores e propor contrato testável |
| BM-EXEC-001 | Adaptador NTSL | Implementação e execução controlada | A inventariar | Verificar código e compatibilidade com Manual NTSL 4.4 |
| BM-OBS-001 | Watchdog/Auditoria | Saúde dos dados, logs e alertas | A inventariar | Localizar watchdog e definir heartbeat e falhas |

## 2. Modelo obrigatório de checkpoint

### Identificação
- ID do checkpoint:
- Data/hora e fuso:
- Fase:
- Responsável:
- Branch/commit de referência:

### Escopo
- Pedido:
- Caminhos inspecionados:
- Fontes e versões consultadas:
- Dependências:

### Alterações
- Arquivos criados:
- Arquivos alterados:
- Arquivos removidos (evitar; justificar e aprovar):
- Resumo do diff:
- Motivo da alteração:

### Verificação
- Comandos/testes executados:
- Ambiente:
- Resultado: PASS / FAIL / BLOCKED / NOT_RUN / PROPOSED
- Evidência reproduzível:
- O que não foi testado:
- Riscos/regressões:
- Plano de rollback:

### Fecho
- Decisão:
- Próxima ação única:
- Critério objetivo de conclusão:
- Artefatos anexos:

## 3. Critérios para declarar um módulo integrado

Um módulo só muda para INTEGRATED quando:
1. A interface de entrada/saída está documentada.
2. As dependências e incompatibilidades estão registadas.
3. Os testes unitários passam.
4. Os casos de dados ausentes e de fronteira são tratados.
5. O comportamento em gráficos de ticks, incluindo 60K quando aplicável, foi observado.
6. A comparação histórico/replay/tempo real está documentada, quando suportada.
7. Existe evidência do teste no repositório.
8. A integração pode ser revertida sem apagar o módulo isolado.

A compilação isolada não satisfaz, por si só, estes critérios.

## 4. Política de segurança para desenvolvimento

- Não enviar ordens reais durante desenvolvimento, depuração ou teste inicial.
- Não alterar módulos existentes antes de inventariar as versões e preservar uma referência reversível.
- Não afirmar que uma fórmula/função NTSL existe sem conferir o Manual 4.4 ou validar no editor da plataforma.
- Não inferir que dados de delta, agressão, livro de ofertas, VIX ou TWAP estão disponíveis só porque são desejáveis na estratégia.
- Separar resultados de backtest, replay, simulação e execução real.
- Documentar limitações e condições de bloqueio como parte do comportamento esperado.

## 5. Estado deste checkpoint

- Arquitetura modular de alto nível: DOCUMENTADA.
- Registo mestre de módulos: DOCUMENTADO.
- Inventário integral do repositório: NOT_RUN.
- Código NTSL alterado: NÃO.
- Testes de estratégia executados: NÃO.
- Rentabilidade validada: NÃO.
- Próximo passo: inventariar os arquivos reais e atualizar este registo com caminhos, versões e evidências verificáveis.
