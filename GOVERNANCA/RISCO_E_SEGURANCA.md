---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "NORMA_RISCO"
fase: "GOVERNANCA"
id_documento: "BM-GOV-RISCO-001"
titulo: "Risco Soberano, Segurança e Falha Segura"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; branch feature/pr3-governanca-mainline-reconciliation; main-base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "Risco Soberano, Segurança e Falha Segura"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "032e8ed2d0a17c4615099953bd57b0e92000d4aaf4ab8273a766e362c3c8b8fd"
commit_referencia: "PENDENTE_APOS_COMMIT"
---

# Risco Soberano, Segurança e Falha Segura

Estado: PROPOSTA PARA REVISÃO. Data: 2026-10-25.

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
Registar fonte, instrumento, timestamp da fonte e receção, fuso, unidade, método, atraso/qualidade, sequência/lacunas e transformação aplicada. Não misturar fontes, unidades ou contratos sem transformação declarada.

## Execução conciliada
Antes de envio autorizado: confirmar instrumento/lado/quantidade/limites; verificar conexão e validade dos dados; consultar posição e ordens; evitar duplicidade; aplicar limites soberanos; exigir autorização explícita; registar intenção e resposta; reconciliar ordens, negócios e posição; bloquear e alertar diante de discrepância. Este documento não autoriza envio automático de ordens.

## Watchdog e recuperação
Monitorar heartbeat, idade dos dados, erros, conexão, divergências, latência e estado de ordens/posição. Alertas devem conter ID, severidade, horário, componente, condição, impacto e ação recomendada. Após falha, entrar em recuperação, reconstruir e reconciliar estado, revalidar dados e liberar operação somente após critérios documentados.

## Meta de 1%
A meta de 1% desde a abertura é hipótese de pesquisa, não garantia. Avaliar drawdown, distribuição de resultados, custos, slippage, sensibilidade e períodos fora da amostra.

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
