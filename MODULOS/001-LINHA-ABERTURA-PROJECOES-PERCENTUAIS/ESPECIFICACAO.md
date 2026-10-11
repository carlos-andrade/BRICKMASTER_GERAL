---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "MODULO_001"
id_documento: "BM-DOC-MODULO-001-ESPECIFICACAO"
titulo: "Especificação técnica — Módulo 001"
status: "PLANEJADO"
versao: "1.0.0"
data_criacao: "N/A"
data_atualizacao: "2026-10-11"
origem: "Conteúdo preexistente; histórico Git"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR feat/cabecalho-padrao-documental"
escopo: "Especificação técnica do Módulo 001"
objetivo: "Definir contrato funcional e condições de implementação sem presumir validação"
dependencias: "Manual NTSL 4.4; confirmação dos parâmetros operacionais"
---

# Especificação técnica — Módulo 001

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Tipo:** ESPECIFICAÇÃO TÉCNICA  
> **Fase:** MÓDULO 001  
> **ID:** BM-DOC-MODULO-001-ESPECIFICACAO  
> **Status:** PLANEJADO  
> **Versão:** 1.0.0  
> **Criação:** N/A  
> **Atualização:** 2026-10-11  
> **Origem:** Conteúdo preexistente; histórico Git  
> **Autoridade:** LAYOUT  
> **Rastreabilidade:** PR feat/cabecalho-padrao-documental

## Contexto Histórico

Especificação preexistente do Módulo 001; o cabeçalho foi acrescentado sem alterar os contratos e as condições técnicas abaixo.

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

## Estado

PLANEJADO — a especificação não comprova implementação.

## Evidências

Conteúdo documental preexistente e referências nele indicadas. Não foram acrescentados resultados de execução.

## Validação

A padronização do cabeçalho não equivale a validação NTSL ou teste no Profit.

## Resultado

Documento identificável e rastreável, preservando a especificação técnica.

## Próxima Ação

Confirmar decisões em aberto e preparar testes isolados antes de qualquer integração.
