# Especificação técnica — Módulo 001

## Contrato funcional

**Entrada:** preço de referência da abertura da sessão, instrumento, tick size e identificação da sessão.  
**Processamento:** congelar a referência da sessão e calcular oito níveis percentuais.  
**Saída:** linha-base e oito linhas horizontais plotadas no gráfico.  
**Efeitos colaterais proibidos:** envio de ordens, alteração de posição ou dependência obrigatória de outros módulos.

## Modelo matemático

Seja (P₀) o preço de abertura válido para a sessão e (r) um dos valores {-3,-2,-1,-0,5,0,5,1,2,3}. Então:

`L(r) = P₀ × (1 + r/100)`

A linha-base é `L(0) = P₀`. A lista inclui oito níveis externos à linha-base. Os valores calculados antes do arredondamento devem ser preservados para validação; os valores efetivamente plotados devem seguir a regra de tick size aprovada.

## Ciclo de vida da referência

1. Detetar a sessão de mercado relevante.
2. Obter o preço que corresponde à definição aprovada de abertura.
3. Guardar esse valor como referência imutável durante a sessão.
4. Calcular e plotar a linha-base e os oito níveis.
5. Não recalcular a referência em cada tick.
6. Na próxima sessão válida, reinicializar apenas quando a nova abertura puder ser identificada sem ambiguidade.

Se a plataforma não disponibilizar a abertura pretendida no contexto de execução escolhido, a implementação deve falhar de forma explícita ou aguardar uma condição válida; não deve substituir a abertura por um preço arbitrário.

## Compatibilidade

O projeto utiliza gráficos atemporais/de ticks em partes da arquitetura BRICKMASTER. Por isso, a identificação de sessão não pode depender exclusivamente de uma suposição de que cada barra representa um intervalo fixo de tempo. A implementação deve ser validada contra a documentação NTSL versão 4.4 e contra o comportamento real do Profit.

## Decisões que exigem confirmação/teste

- Instrumento prioritário de validação.
- Fonte exata do preço de abertura.
- Horário oficial aplicável ao instrumento e tratamento de leilões.
- Método de deteção de nova sessão no NTSL.
- Regra de arredondamento dos níveis ao tick size.
- Extensão visual das linhas e comportamento em carregamento/reprocessamento histórico.

## Não objetivos

- Gerar sinais operacionais.
- Calcular alvos com base em volatilidade.
- Ajustar níveis dinamicamente.
- Integrar VWAP, TWAP, FVG, fluxo, delta ou outros módulos.
- Executar ordens.
