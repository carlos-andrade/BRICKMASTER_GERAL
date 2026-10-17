# BRICKMASTER RAIZ — Arquitetura e Contrato do Módulo COLORAÇÃO

> **ID:** BM-COL-ARCH-001  
> **Estado:** EXPERIMENTAL — especificação inicial  
> **Versão:** 1.0.0  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Branch de referência:** main  
> **Data:** 2026-10-17  
> **Responsável funcional:** Arquitetura BRICKMASTER RAIZ

## 1. Objetivo

Padronizar a representação visual do estado local do preço sem transformar a coloração em sinal autónomo de entrada, autorização de ordem ou substituto do GIROSCÓPIO e do módulo de risco.

## 2. Princípios obrigatórios

1. A coloração é uma camada de apresentação/diagnóstico.
2. Não envia ordens, não altera posições e não modifica stops.
3. Dados ausentes, contraditórios ou insuficientes devem resultar em estado neutro, nunca em falsa certeza.
4. A regra deve ser determinística e reproduzível com os mesmos dados de entrada.
5. Código NTSL só passa a VALIDADO após compilação e testes documentados no Profit; publicação no GitHub, por si só, não prova compilação.
6. O Manual NTSL 4.4 (03-08-2026) é a referência documental prioritária; divergências devem ser registadas.
7. Preservar versões anteriores e evidências. Não substituir artefactos históricos sem inventário e reversão.

## 3. Limites de responsabilidade

- **Dados:** fornece séries de preço do gráfico ativo.
- **Regra de coloração:** classifica apenas a condição visual definida no artefacto correspondente.
- **GIROSCÓPIO:** mantém o contexto global e a confiança; não é substituído por cores.
- **Confluência/decisão:** avalia hipóteses com outros módulos.
- **Risco soberano:** autoriza ou bloqueia qualquer intenção operacional.
- **Execução conciliada:** permanece fora do escopo deste módulo.

## 4. Contrato

### Entradas
- Série de preço suportada pela regra específica.
- Histórico suficiente para avaliar a condição.
- Estado de cálculo disponibilizado pelo Profit/NTSL.

### Saídas
- Uma cor visual por barra, ou estado neutro quando não existir classificação válida.
- Sem efeitos colaterais operacionais.

### Invariantes
- Nenhuma ordem é emitida.
- Nenhuma cor é apresentada como garantia de direção futura.
- Ausência de dados não equivale a condição falsa confirmada; deve ser documentada e, quando possível, exibida como neutra.
- A regra não depende de dados futuros nem de informação indisponível no instante avaliado.

## 5. Estados de maturidade

- **EXPERIMENTAL:** especificação ou código ainda sem validação integral.
- **VALIDADO:** compilação e casos de teste documentados com evidências reproduzíveis.
- **PRODUÇÃO:** integração aprovada, controlo de regressão e monitorização operacional definidos.

## 6. Dependências

- Profit/NTSL e Manual NTSL 4.4.
- Ambiente de teste com ativo, período, tipo de gráfico e histórico registados.
- Revisão de governança antes de integração no BRICKMASTER.

## 7. Critérios de aceitação

- [ ] Código compila na versão Profit identificada.
- [ ] Cores e condições correspondem à especificação.
- [ ] Não há ordens nem efeitos colaterais operacionais.
- [ ] Dados insuficientes não geram classificação enganadora.
- [ ] Testes em alta, baixa, lateralização e histórico insuficiente.
- [ ] Evidências, versão do Profit, ativo e configuração do gráfico registados.
- [ ] Revisão de regressão concluída antes de qualquer integração.

## 8. Riscos e limitações

A cor é uma codificação visual, não uma previsão. Uma regra baseada apenas no preço não confirma fluxo, liquidez, volume financeiro, FVG, VWAP/TWAP ou contexto macroeconómico. Esses elementos, quando necessários, devem permanecer em módulos independentes e fornecer evidências ao GIROSCÓPIO.

## 9. Histórico

- 1.0.0 — criada especificação inicial e limites de responsabilidade.
