<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: Contrato Padrão de Módulo
IDENTIFICADOR: BM-STD-001
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

# Contrato padrão de módulo

Cada módulo deve manter no mínimo:
- `README.md` — documentação inicial e estado atual.
- `SPEC.md` — definição técnica, fórmulas, unidades, premissas e critérios de invalidação.
- `TESTES.md` — casos, dados de teste, resultados e evidências.
- `CHANGELOG.md` — histórico incremental.

## Campos obrigatórios
1. Objetivo e não objetivos.
2. Problema operacional que resolve.
3. Entradas, tipo, unidade, origem, timestamp e política de dados ausentes.
4. Saídas, significado, escala e semântica.
5. Algoritmo/fórmulas e pseudocódigo.
6. Dependências e modo degradado.
7. Limitações e riscos de interpretação.
8. Regras anti-look-ahead.
9. Testes positivos, negativos, limites e regressão.
10. Critérios de aceite mensuráveis.
11. Estado de maturidade e próxima ação.
12. Referências e histórico.

## Proibição
Nenhum módulo pode declarar “validado”, “preciso” ou “rentável” sem teste reproduzível documentado.
