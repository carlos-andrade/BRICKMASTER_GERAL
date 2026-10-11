# Padrão de Módulos e Contratos

Estado: PROPOSTA PARA REVISÃO. Data: 2026-10-11.

## Estrutura mínima
Cada módulo deve manter especificação, implementação, contrato, testes, fixtures, limitações, checkpoint e histórico, conforme a tecnologia.

## Campos do contrato
- Identidade: nome, ID estável, versão e responsável.
- Objetivo: problema resolvido e resultado esperado.
- Estado: EXPERIMENTAL, VALIDADO, PRODUÇÃO, BLOQUEADO ou DEPRECADO.
- Entradas: campos, tipos, unidades, fonte, timestamp e validade.
- Saídas: campos, tipos, unidades, semântica e garantias.
- Dependências: módulos/serviços, versões e disponibilidade exigida.
- Pré e pós-condições.
- Erros: códigos, causas, severidade e recuperação.
- Falha segura para dados/dependências não confiáveis.
- Observabilidade: logs, métricas, eventos e correlação.
- Testes: casos, ambiente, resultado e artefatos.
- Compatibilidade, migração, segurança, rollback e limitações.

## Giroscópio
O Giroscópio consolida contexto operacional; não é fonte mágica de verdade. Deve publicar instrumento, sessão, tipo de gráfico, posição contextual, estado/confiança das fontes, idade/validade dos dados, divergências, elegibilidade, motivo de bloqueio, versão da regra e timestamp de cálculo. Fórmulas e semântica devem ser especificadas e testadas antes de validação.

## Dependências
Declarar dependências diretas e indiretas, evitar ciclos não aprovados, definir comportamento de indisponibilidade e executar testes de contrato após atualizações. Nenhum módulo pode contornar o veto do Risco Soberano.

## Testes mínimos
Caminho normal; limites; campos ausentes/inválidos; atraso e fora de ordem; duplicidade; contradição entre fontes; dependência indisponível; reinício/recuperação; compatibilidade; regressão.

Módulo experimental só pode ser acoplado em sandbox/observação, sem autoridade para emitir ordens ou alterar estado de produção.