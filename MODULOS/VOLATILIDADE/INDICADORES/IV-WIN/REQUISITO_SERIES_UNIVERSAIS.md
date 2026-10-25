<!--
projeto: BRICKMASTER RAIZ
repositorio: carlos-andrade/BRICKMASTER_GERAL
tipo_documento: REQUISITO_TECNICO
fase: develop
id_documento: BM_VOL_IVWIN_UNIVERSAL_001
titulo: Requisito de cobertura universal de series de opcoes IV-WIN
status: EXPERIMENTAL
versao: 1.0.0
data_criacao: 2026-10-20
data_atualizacao: 2026-10-24
origem: requisito aprovado pelo utilizador e especificacao IV-WIN existente
autoridade_documental: GOVERNANCA e BRICKMASTER_GERAL
cadeia_autoridade: REQUISITOS -> ESPECIFICACAO -> CONTRATOS -> IMPLEMENTACAO -> VALIDACAO
rastreabilidade: PR #38 integrado em develop; commit 6ec1e2e19944f24422adeef06d1bff0fa9e0dc1c
escopo: cobertura multi-serie de opcoes no IV-WIN
objetivo: formalizar suporte agnostico a series, preservando modelo e qualidade por contrato
dependencias: fontes autorizadas, identificadores e termos contratuais, dados sincronizados e modelo compatível
sha256_canonico: bc0a755cf7cb1931254501f851137f1cc6fb591f6338ecc6f0b96d0a44087027
commit_referencia: 6ec1e2e19944f24422adeef06d1bff0fa9e0dc1c
-->

# IV-WIN — Requisito de cobertura universal de séries de opções

## Contexto Histórico

A especificação IV-WIN existente propõe investigar volatilidade implícita como contexto para o Mini Índice WIN. O requisito aprovado amplia a arquitetura: o motor não pode ficar limitado a opções sobre o Ibovespa, BOVA11 ou um único vencimento. Este documento complementa a especificação existente, sem a substituir nem declarar implementação concluída.

## Estado

**EXPERIMENTAL — requisito documental integrado em develop.** Feed, cálculo, licenças, testes empíricos e integração operacional não estão comprovados por este documento.

## Requisito obrigatório

O IV-WIN deve aceitar qualquer série de opções que seja identificável por uma fonte autorizada e para a qual existam dados suficientes, termos contratuais conhecidos e um modelo de avaliação compatível. O núcleo não deve depender de uma lista fixa de símbolos, subjacentes, strikes ou vencimentos.

A cobertura pode incluir calls e puts sobre índices, ações, ETFs e futuros, quando efetivamente suportados pela fonte e pelo modelo. “Qualquer série” é um requisito de extensibilidade; não significa acesso automático a todos os mercados nem que toda a série permita uma IV fiável.

## Contrato mínimo de identificação

Cada contrato deve preservar:
- ID nativo e fonte;
- subjacente e classe do instrumento;
- call/put;
- strike, vencimento e calendário aplicável;
- estilo de exercício e forma de liquidação;
- multiplicador, moeda e unidade de preço;
- timestamps de evento e receção;
- bid/ask e negócio mais recente, quando disponíveis;
- modelo, parâmetros e convenções usados para obter IV.

Os campos não aplicáveis devem ser explicitamente marcados como não aplicáveis; não se devem preencher por suposição.

## Seleção de modelo

O motor deve selecionar um método compatível com o tipo de contrato. Não aplicar indiscriminadamente um modelo de opções sobre ações a opções sobre futuros. Se a metodologia, os parâmetros ou a convenção não estiverem definidos, a observação fica SEM_DADOS ou INVALIDA, com motivo registado.

## Estados de qualidade

- VALIDA: dados e cálculo cumprem critérios configurados.
- VALIDA_COM_RESTRICOES: calculável, mas com limitação explícita e uso restrito.
- INVALIDA: contrato, cotação ou cálculo inconsistente.
- SEM_DADOS: falta informação essencial.
- DESATUALIZADA: idade da observação excede o limite configurado para o uso.
- NAO_COMPARAVEL: IV individual válida, mas inadequada para a agregação/comparação pretendida.

Frescura, tolerâncias e convergência devem ser parâmetros versionados por fonte e classe de instrumento. Ausência nunca é convertida em zero.

## Métricas candidatas

Nível e variação da IV, estrutura temporal, skew/smile e prémio de volatilidade face a RV com horizonte comparável. São métricas de investigação, não sinais direcionais nem capacidades validadas.

Agregações só podem combinar observações com subjacente, convenções, timestamps e horizontes comparáveis. A IV individual de um contrato deve permanecer disponível para auditoria, mesmo quando não elegível para agregação.

## Segurança e limites

- Dados críticos ausentes, atrasados ou contraditórios bloqueiam a saída dependente.
- O módulo calcula e qualifica dados; não envia ordens.
- A integração com o Giroscópio depende de contrato separado e validação.
- RV-60K permanece indicador distinto e inalterado.
- O gráfico-alvo BRICKMASTER é 60K trades; a barra de 60K trades não tem duração temporal fixa.
- A linha branca dos gráficos representa o preço de abertura do mercado.
- A meta de 1% desde a abertura é hipótese, nunca promessa nem prioridade sobre risco.

## Testes e critérios de aceitação

Antes de considerar a cobertura implementada, demonstrar com testes reproduzíveis:
1. normalização de classes de instrumento e IDs de fontes diferentes;
2. processamento de calls/puts, múltiplos strikes e vencimentos;
3. tratamento de dados ausentes, atrasados, duplicados e contraditórios;
4. rejeição de contratos e parâmetros incompatíveis com o modelo;
5. deteção de falha de convergência ou ausência de solução;
6. consistência de unidades, calendários e convenções;
7. agregação apenas de observações comparáveis;
8. sincronização com WIN sem look-ahead;
9. rastreabilidade completa dos resultados até aos dados e parâmetros originais.

## Evidências

- Requisito aprovado no diálogo do projeto em 2026-10-20.
- Especificação IV-WIN: ESPECIFICACAO.md.
- README IV-WIN: README.md.
- Repositório oficial: https://github.com/carlos-andrade/BRICKMASTER_GERAL.

## Validação

A revisão formaliza o requisito de cobertura universal e os estados de qualidade. Não foram executados testes de dados, cálculo, replay, backtest ou integração. O SHA-256 canónico refere-se ao corpo deste documento em UTF-8/LF, excluindo o bloco de metadados.

## Resultado

Requisito definido para um motor agnóstico a séries, condicionado por suporte da fonte, termos contratuais, qualidade dos dados e modelo matemático compatível.

## Próxima Ação

Ligar este requisito à especificação principal, definir o esquema canónico de dados, inventariar fontes e licenças, selecionar modelos por classe de contrato e criar testes isolados antes de implementar qualquer integração.
