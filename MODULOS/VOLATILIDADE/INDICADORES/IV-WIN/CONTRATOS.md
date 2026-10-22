<!--
projeto: BRICKMASTER RAIZ
repositorio: carlos-andrade/BRICKMASTER_GERAL
tipo_documento: CONTRATO_DADOS
fase: feature
id_documento: BM_VOL_IVWIN_CONTRACT_001
titulo: Contrato canonico de dados e saidas IV-WIN
status: EXPERIMENTAL
versao: 1.0.0
data_criacao: 2026-10-20
data_atualizacao: 2026-10-20
origem: requisito universal IV-WIN
autoridade_documental: GOVERNANCA e BRICKMASTER_GERAL
cadeia_autoridade: REQUISITOS -> ESPECIFICACAO -> CONTRATOS -> IMPLEMENTACAO -> VALIDACAO
rastreabilidade: feature/iv-win-universal-options-v1
escopo: entradas, saidas, qualidade e agregacao multi-serie
objetivo: preservar identidade, proveniencia, metodologia e qualidade
dependencias: fontes de opcoes, schema de contratos, timestamps e modelo compativel
sha256_canonico: b2648d1916d6952aa4dbca6893e7c1afb42f9b1e5bb31c5cf909bf6ea1877aca
commit_referencia: ae2bc43a877b540059a40ed4653a8408936dad2c
-->

# IV-WIN — Contrato canónico de dados e saídas

## Contexto Histórico

Documento complementar à especificação IV-WIN. Formaliza interfaces para suportar séries diversas sem presumir feeds, licenças ou testes já existentes.

## Estado

EXPERIMENTAL. Contrato proposto; sem implementação validada.

## Entrada canónica

Cada observação deve conter source_id, instrument_id, underlying_id, asset_class, option_type, strike, expiry, exercise_style, settlement_type, multiplier, currency, price_unit, event_timestamp, receive_timestamp e data_status. bid/ask e last_price são opcionais conforme a fonte; implied_volatility só é aceite como dado de origem se a metodologia e a convenção estiverem documentadas. Para cálculo próprio, registar model_id, model_version, inputs e solver_status.

Preservar o registo RAW e a transformação aplicada. Não substituir valores ausentes por zero. Campos não aplicáveis devem ser identificados explicitamente.

## Saída canónica

Cada resultado deve incluir module_id, as_of_timestamp, source_timestamp, source_id, instrument_id, underlying_id, method_id, method_version, iv_value, iv_unit, quality_state, reason_codes e evidence_ref. Métricas agregadas devem também declarar constituent_ids, regra de seleção, tenor/horizonte, timestamp de corte e versão do agregador.

## Estados e precedência

Estados permitidos: VALIDA, VALIDA_COM_RESTRICOES, INVALIDA, SEM_DADOS, DESATUALIZADA, NAO_COMPARAVEL. Se uma condição crítica falhar, o estado mais restritivo prevalece. Um estado não válido não pode alimentar classificação operacional. O limiar de frescura deve ser configurado por fonte, mercado e finalidade; não existe TTL universal assumido.

## Contrato de agregação

Não misturar diretamente IVs de subjacentes, moedas, convenções, estilos ou horizontes diferentes. Estrutura temporal e skew requerem regras explícitas de tenor/moneyness e dados comparáveis. Toda a agregação deve permitir recuperar os contratos constituintes e os motivos de exclusão.

## Falhas e segurança

Dados atrasados, contraditórios, incompletos ou sem proveniência bloqueiam a saída dependente. O módulo não emite ordens. Integração com o Giroscópio exige contrato adicional, fallback para UNKNOWN e aprovação explícita.

## Evidências

Requisito aprovado em 2026-10-20; especificação IV-WIN no mesmo diretório; repositório oficial BRICKMASTER_GERAL.

## Validação

O documento define um contrato proposto. Não foram executados testes de integração, de dados ou de cálculo. Critérios de schema, timestamps, estados e agregação precisam de testes antes de estabilizar o contrato.

## Resultado

Contrato mínimo para preservar identidade do instrumento, proveniência, metodologia, qualidade e rastreabilidade entre entrada, cálculo e agregação.

## Próxima Ação

Converter o contrato em schema validável, definir enumeradores/unidades e criar fixtures para casos válidos, ausentes, atrasados, contraditórios e não comparáveis.
