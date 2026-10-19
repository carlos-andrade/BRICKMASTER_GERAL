---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "MODULO_001"
id_documento: "BM-DOC-MODULO-001-ESPECIFICACAO"
titulo: "Especificação técnica — Módulo 001"
status: "PLANEJADO"
versao: "1.0.3"
data_criacao: "N/A"
data_atualizacao: "2026-10-19"
sha256_canonico: "f19a30d42dc9cf57f7e2f2d57efcd29839e8c7366ca1f1117bf326f2d7336227"
commit_referencia: "c0740f9fd4d1485b3c3a1b8568053b8cd077e688"
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
> **Versão:** 1.0.3  
> **Criação:** N/A  
> **Atualização:** 2026-10-19  
> **Origem:** Conteúdo preexistente; histórico Git  
> **Autoridade:** LAYOUT  
> **Rastreabilidade:** PR feat/cabecalho-padrao-documental

## Contexto Histórico

Especificação preexistente do Módulo 001. Na revisão 1.0.1, a lista matemática de percentagens foi substituída por uma tabela explícita para eliminar a ambiguidade entre vírgula decimal e separador de elementos. A correção esclarece a notação pretendida; não altera o conjunto de níveis documentado nem comprova implementação.

## Contrato funcional

**Entrada:** preço oficial de abertura confirmado pelo Módulo 002, instrumento/contrato, tick size, identificação da sessão, fonte aprovada e timestamp. A política aprovada em 2026-10-12 é a opção B: preço oficial fornecido pela plataforma ou por fonte oficial validada.  
**Processamento:** congelar a referência da sessão e calcular oito níveis percentuais.  
**Saída:** linha-base e oito linhas horizontais plotadas no gráfico.  
**Efeitos colaterais proibidos:** envio de ordens, alteração de posição ou dependência obrigatória de outros módulos.

## Modelo matemático

Seja P₀ o preço de abertura válido para a sessão. Os oito níveis externos à linha-base correspondem às percentagens abaixo, interpretando a vírgula como separador decimal em português:

| Nível | Percentagem | Fórmula |
|---|---:|---|
| Superior 1 | +0,5% | `P₀ × 1,005` |
| Superior 2 | +1% | `P₀ × 1,01` |
| Superior 3 | +2% | `P₀ × 1,02` |
| Superior 4 | +3% | `P₀ × 1,03` |
| Linha-base | 0% | `P₀` |
| Inferior 1 | −0,5% | `P₀ × 0,995` |
| Inferior 2 | −1% | `P₀ × 0,99` |
| Inferior 3 | −2% | `P₀ × 0,98` |
| Inferior 4 | −3% | `P₀ × 0,97` |

Os valores calculados antes do arredondamento devem ser preservados para validação; os valores efetivamente plotados devem seguir a regra de tick size aprovada.

## Ciclo de vida da referência

1. Detetar a sessão de mercado relevante.
2. Obter o preço que corresponde à definição aprovada de abertura.
3. Guardar esse valor como referência imutável durante a sessão.
4. Calcular e plotar a linha-base e os oito níveis.
5. Não recalcular a referência em cada tick.
6. Na próxima sessão válida, reinicializar apenas quando a nova abertura puder ser identificada sem ambiguidade.

Se a plataforma não disponibilizar o campo oficial no contexto escolhido, a implementação deve aguardar ou falhar explicitamente. Não deve substituir a abertura por preço atual, primeiro negócio observado ou primeiro candle visível. Fontes secundárias só podem ser usadas se previamente validadas e configuradas. O módulo não deve calcular níveis quando a referência não estiver CONFIRMED.

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

Confirmar decisões em aberto (fonte exata da abertura, reinicialização de sessão e arredondamento ao tick size) e preparar testes isolados antes de qualquer integração.

## Histórico de versões

- 1.0.0 — 2026-10-11 — especificação inicial.
- 1.0.1 — 2026-10-11 — desambiguação da notação das percentagens por tabela; sem alteração da lógica pretendida.


## Decisão de dependência — 2026-10-12

A política B para o preço oficial de abertura foi aprovada pelo utilizador. O Módulo 001 depende de uma referência `CONFIRMED` emitida pelo Módulo 002. A decisão não comprova que o campo exista no Profit/NTSL nem valida qualquer fornecedor; essa verificação permanece pendente.

- 1.0.2 — 2026-10-12 — dependência explícita do preço oficial de abertura do Módulo 002.


- 1.0.3 — 2026-10-19 — reconciliação documental de `develop` para `main`; preservadas as decisões e os bloqueios anteriores. Não implica validação funcional.
