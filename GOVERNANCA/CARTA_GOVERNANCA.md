---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "CARTA_GOVERNANCA"
fase: "FASE 00 — GOVERNANÇA"
id_documento: "BM-GOV-CHARTER-001"
titulo: "Carta de Governança BRICKMASTER RAIZ"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "PR #3; conteúdo anterior preservado e normalizado"
autoridade_documental: "GOVERNANCA e responsável pelo projeto"
cadeia_autoridade: "PROMPT -> CARTA -> LAYOUT UNICO -> CODIGO"
rastreabilidade: "PR #3; branch feature/pr3-governanca-mainline-reconciliation"
escopo: "Carta de Governança BRICKMASTER RAIZ"
objetivo: "Documentar governança sem declarar aprovação ou testes não executados"
dependencias: "GOVERNANCA/NORMA-CABECALHO-PADRAO.md; main base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
sha256_canonico: "6b800e74aa38b06126f96b49f3977b0d23d685ac7a223b031c31a84fab45fb39"
commit_referencia: "3db0c88f27fec4c6ea2418749de09ebba8130fe7"
---
# Carta de Governança — BRICKMASTER RAIZ

- Versão: 1.0.0
- Estado: PROPOSTA PARA REVISÃO
- Data: 2026-10-11
- Escopo: BRICKMASTER_GERAL e módulos integrados
- Autoridade de aprovação: responsável pelo projeto

## 1. Missão

Desenvolver um sistema modular de leitura de contexto de mercado que ajude o operador a saber onde está no gráfico, qual regime está ativo, quais dados sustentam a leitura e quando a incerteza exige reduzir confiança ou bloquear uma ação.

## 2. Princípios obrigatórios

1. Preservar históricos, decisões e evidências; nunca apagar falhas para melhorar artificialmente o histórico.
2. Não declarar teste, validação, publicação ou resultado sem evidência identificável.
3. Separar dados, inteligência, decisão, risco soberano, execução conciliada e watchdog.
4. Dados ausentes, atrasados, inválidos ou contraditórios reduzem confiança ou bloqueiam ações; nunca são silenciosamente tratados como válidos.
5. Cada módulo declara contrato, dependências, estados, limites, testes e limitações.
6. A camada de risco pode vetar decisões estratégicas e execução.
7. Decisões relevantes devem ser reconstruíveis a partir de versões, parâmetros, dados e evidências.
8. Distinguir EXPERIMENTAL, VALIDADO e PRODUÇÃO.
9. Usar branches e revisão; evitar alterações diretas na branch principal.
10. Registrar erros, atrasos, bloqueios, divergências e decisões.
11. Sinais e análises não autorizam envio de ordens por padrão.
12. A meta de 1% desde a abertura é hipótese, não promessa nem justificativa para elevar risco.

## 3. Responsabilidades

- Responsável pelo projeto: aprovar objetivos, política de risco, mudanças arquiteturais e promoção para produção.
- Arquitetura: definir limites entre camadas, contratos e compatibilidade.
- Responsável pelo módulo: manter especificação, implementação, testes, limitações e checkpoint.
- Validador: revisar evidências e reproduzir testes.
- Risco soberano: vetar ações incompatíveis com limites, qualidade dos dados ou estado operacional.
- Watchdog: detectar ausência de dados, atraso, falhas, divergências e estados travados.
- Execução conciliada: comparar intenção, ordens, confirmações e posição efetiva.

Papéis podem ser acumulados por uma pessoa, mas as responsabilidades continuam distintas.

## 4. Arquitetura governada

- Dados: aquisição, proveniência, timestamp, qualidade, normalização e validade.
- Inteligência: interpretação do mercado e hipóteses contextuais.
- Decisão: combina contexto, confiança e regras de elegibilidade; não ultrapassa o veto de risco.
- Risco soberano: limites de exposição/perda, sessão, dados e condições de bloqueio.
- Execução conciliada: somente após autorização explícita; reconcilia estado pretendido e real.
- Watchdog: monitora saúde ponta a ponta.
- Giroscópio: consolida contexto, localização no gráfico, confiança, divergências e motivos de bloqueio.
- Interface: apresenta instrumento, sessão, tipo de gráfico, estrutura, níveis, qualidade dos dados e estado operacional.

Gráficos baseados em ticks, incluindo 60K ticks, são cenários essenciais de arquitetura e validação.

## 5. Confiança e falha segura

A confiança considera atualidade e integridade dos dados, coerência entre fontes, dependências, clareza da estrutura, consistência dos módulos e risco vigente. A fórmula precisa ser especificada e testada antes de ser considerada validada. Se dados essenciais faltarem ou forem contraditórios, usar estado BLOQUEADO ou equivalente documentado.

## 6. Desenvolvimento

Fluxo normal: feature/* → develop → validação → principal. Promoção exige critérios de aceitação, testes reproduzíveis, evidências, aprovação explícita e rollback. Correções emergenciais exigem justificativa e revisão posterior.

## 7. Critérios mínimos de produção

Contrato versionado; testes unitários e de integração; testes de falha e dados inválidos; limites e comportamento seguro; logs e métricas; recuperação e rollback; compatibilidade verificada; evidência de validação e aprovação. Compilação isolada ou screenshot não bastam.

## 8. Integridade de mercado

Distinguir dado observado, dado derivado, hipótese e sinal. Não fabricar preços, fluxo, volume, delta, VWAP/TWAP, VIX ou eventos de calendário. Registrar fonte, timestamp, fuso, instrumento, unidade e método. Não enviar ordens por padrão.

## 9. Estado desta carta

Esta carta permanece PROPOSTA PARA REVISÃO até aprovação explícita. A existência do documento no repositório não prova sua aprovação.


## Contexto Histórico

Documento histórico de governança preservado e reconciliado a partir da proposta PR #3.


## Estado

PROPOSTA PARA REVISÃO; não representa aprovação ou produção.


## Evidências

- PR #3 e histórico Git do repositório BRICKMASTER_GERAL.


## Validação

Apenas revisão documental; não foram executados testes de trading, compilação NTSL ou validação no Profit por esta alteração.


## Resultado

Conteúdo preservado para revisão; estado não promovido.


## Próxima Ação

Verificar referências, conteúdo e critérios de aceitação antes de aprovação.
