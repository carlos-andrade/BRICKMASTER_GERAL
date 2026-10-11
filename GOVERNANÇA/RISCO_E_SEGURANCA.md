# Risco Soberano, Segurança e Falha Segura

Estado: PROPOSTA PARA REVISÃO. Data: 2026-10-11.

## Princípio
A camada de risco soberano pode vetar qualquer decisão ou execução. Meta diária, conveniência e confiança de outro módulo não podem sobrepor esse veto.

## Condições de bloqueio/degradação
- Dado essencial ausente, inválido, atrasado ou fora da validade.
- Divergência material entre fontes não reconciliada.
- Instrumento, símbolo, sessão, timestamp ou fuso ambíguos.
- Estado de posição/ordem não conciliado.
- Dependência crítica indisponível.
- Limites de exposição/perda violados ou desconhecidos.
- Watchdog sem heartbeat dentro do limite configurado.
- Módulo ou configuração incompatível com a versão aprovada.
- Evento sem política operacional documentada.

Os limites numéricos devem ser definidos pelo responsável e validados; não inventar valores.

## Estados sugeridos
- OK: entradas essenciais válidas e conciliadas.
- DEGRADADO: capacidade parcial; confiança reduzida e ações limitadas.
- BLOQUEADO: não elegível para decisão/execução.
- EM_RECUPERACAO: recuperação em curso; exige nova conciliação.
- DESCONHECIDO: estado indeterminável; bloquear execução.

## Proveniência de dados
Registrar fonte, instrumento, timestamp da fonte e recepção, fuso, unidade, método, atraso/qualidade, sequência/lacunas e transformação aplicada. Não misturar fontes, unidades ou contratos sem transformação declarada.

## Execução conciliada
Antes de envio autorizado: confirmar instrumento/lado/quantidade/limites; verificar conexão e validade dos dados; consultar posição e ordens; evitar duplicidade; aplicar limites soberanos; exigir autorização explícita; registrar intenção e resposta; reconciliar ordens, negócios e posição; bloquear e alertar diante de discrepância. Este documento não autoriza envio automático de ordens.

## Watchdog e recuperação
Monitorar heartbeat, idade dos dados, erros, conexão, divergências, latência e estado de ordens/posição. Alertas devem conter ID, severidade, horário, componente, condição, impacto e ação recomendada. Após falha, entrar em recuperação, reconstruir e reconciliar estado, revalidar dados e liberar operação somente após critérios documentados.

## Meta de 1%
A meta de 1% desde a abertura é hipótese de pesquisa, não garantia. Avaliar drawdown, distribuição de resultados, custos, slippage, sensibilidade e períodos fora da amostra.