<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Governança Técnica
IDENTIFICADOR: BM-GOV-001
VERSÃO: 1.0.0
ESTADO: PROPOSTA INICIAL — NÃO VALIDADA EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-11
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-10-11 | v1.0.0 | Estrutura inicial modular e regras de governança.
FONTE DA VERDADE: documentação e código versionados neste repositório.
-->

# Governança técnica

## Estados padronizados
- **RASCUNHO:** proposta ainda incompleta.
- **DOCUMENTADO:** especificação inicial escrita.
- **EM_DESENVOLVIMENTO:** implementação em curso.
- **EM_TESTE:** execução de testes reproduzíveis.
- **VALIDADO_EM_SIMULACAO:** critérios passaram em dados/replay definidos.
- **APROVADO_PARA_PAPER:** autorização limitada a simulação em tempo real.
- **APROVADO_PARA_PRODUCAO:** somente após revisão explícita de risco e operação.
- **BLOQUEADO:** falha ou dependência crítica pendente.
- **DEPRECADO:** mantido apenas para rastreabilidade.

## Regra para qualquer mudança
Toda mudança relevante deve declarar: problema, hipótese, escopo, arquivos, dependências, risco de regressão, testes executados, resultado observado, limitações e próximo checkpoint.

## Cabeçalho obrigatório
Cada documento novo deve conter: projeto, documento, identificador, versão, estado, datas de criação/revisão, responsável, repositório, histórico de alterações e fontes da verdade. Quando o modelo oficial de cabeçalho for recuperado, alinhar este cabeçalho sem apagar o histórico.

## Fonte técnica NTSL
Manual NTSL 4.4 de 03/08/2026 é a referência prioritária fornecida para sintaxe e recursos. Versões anteriores são referências históricas. Não afirmar suporte a uma função sem evidência documental ou teste no Profit.

## Portões de qualidade
1. Especificação revisada.
2. Entradas/saídas e unidades definidas.
3. Testes unitários e casos-limite.
4. Teste temporal sem look-ahead.
5. Backtest com custos, slippage e regras de sessão.
6. Comparação fora da amostra.
7. Teste de robustez por regime.
8. Revisão de risco e logs.
9. Checkpoint com evidência reproduzível.
