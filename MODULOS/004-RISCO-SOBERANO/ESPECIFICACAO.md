---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "FASE_05_DECISAO_E_RISCO_SOBERANO"
id_documento: "BM-RISK-001-ESPECIFICACAO"
titulo: "Contrato técnico — Risco soberano"
status: "CONTRATO_INICIAL; PARAMETROS_PENDENTES"
versao: "0.1.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "Baseline arquitetural BRICKMASTER RAIZ"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/fase05-risco-soberano"
escopo: "Permissão/bloqueio de decisão e execução segundo limites explícitos"
objetivo: "Impedir que sinais, metas ou falhas de dados ultrapassem limites soberanos de risco"
dependencias: "BM-DATA-001; BM-CORE-001; adaptador de execução conciliada"
---

# Contrato técnico — Risco soberano

## Contexto Histórico

O sistema exige separação entre inteligência, decisão, risco e execução. O risco deve prevalecer sobre a meta experimental de 1% desde a abertura e sobre qualquer módulo que produza um sinal.

## Estado

CONTRATO INICIAL — NÃO IMPLEMENTADO. Os limites de perda, risco por operação, exposição máxima, número de tentativas e parâmetros de conta não foram definidos neste documento; nenhum valor é inventado.

## Contrato

### Entradas
- Identidade do instrumento/contrato e estado de sessão.
- Estado de qualidade/frescura dos dados e contexto do Giroscópio.
- Decisão/sinal proposto e sua explicação.
- Estado reconciliado de posição, ordens pendentes e resultado diário, quando disponível.
- Limites aprovados, versionados e válidos para a conta/instrumento.
- Estado da ligação e do Watchdog.

### Saídas
- `risk_state`: `ALLOW`, `BLOCK` ou `HALT`.
- `reason_codes`: razões auditáveis para a decisão.
- `risk_policy_version`: versão dos limites usados.
- `decision_id` correlacionado com o sinal e a execução.
- Opcionalmente, orçamento de risco calculado somente quando os inputs e parâmetros estiverem definidos e validados.

### Regras soberanas
- Se limites obrigatórios, estado da posição ou resultado diário forem desconhecidos, a saída é `BLOCK` ou `HALT` conforme política aprovada; nunca assumir risco ilimitado.
- Se dados essenciais estiverem ausentes, atrasados ou contraditórios, bloquear.
- Se o limite de perda, exposição ou número de tentativas aprovado for atingido, bloquear novas entradas.
- Divergência entre posição/ordens locais e Profit implica bloqueio até reconciliação.
- A meta de 1% desde a abertura é apenas hipótese de avaliação; atingi-la não obriga a continuar, não atingir não autoriza aumentar risco e nenhum sinal deve ser criado para perseguir a meta.
- O risco não é alterável por módulos de inteligência e não pode ser ultrapassado por configuração de estratégia.
- A saída `ALLOW` não envia ordem; apenas indica que o veto soberano não bloqueou a proposta. A execução necessita de autorização própria.

### Estados
- `ALLOW`: limites configurados, inputs essenciais válidos e nenhuma regra de veto acionada.
- `BLOCK`: proposta não autorizada por uma condição de risco/dados recuperável.
- `HALT`: falha crítica, limite soberano atingido ou estado de execução inconciliável; exige recuperação explícita.

### Dependências
BM-DATA-001, BM-CORE-001, limites de risco aprovados, estado de conta/posição e adaptador de execução conciliada. Até estes contratos existirem, a implementação não pode autorizar execução.

## Evidências

A baseline arquitetural L7 exige risco por operação, limite diário de perda, exposição máxima, limite de tentativas, interrupção e custos/slippage. O roadmap estabelece que o risco pode vetar qualquer sinal.

## Validação

Contrato estático. Sem parâmetros numéricos aprovados, testes, cálculo de sizing, simulação ou execução real. Critério de passagem: todos os vetos testados e impossibilidade de contornar o risco a partir de outros módulos.

## Resultado

Contrato inicial de veto e bloqueio definido; módulo permanece não implementado e não validado.

## Próxima Ação

Recolher e aprovar os limites de risco como política versionada; definir casos de teste e testar primeiro em simulação, com ordens reais desativadas.

## Histórico de versões

- 0.1.0 — 2026-10-11 — primeiro contrato do risco soberano, sem parâmetros inventados.
