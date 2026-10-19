---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "INDICADOR_NTSL_EXPERIMENTAL"
fase: "F3 — Construção isolada"
id_documento: "BM-VOL-RV-60K-README-001"
titulo: "RV-60K — Volatilidade Realizada Intradiária"
estado: "VALIDAÇÃO FUNCIONAL COM EVIDÊNCIAS PROFIT — REVISÃO DO PR PENDENTE"
versao: "1.0.1"
data_atualizacao: "2026-10-19"
---

# RV-60K — Volatilidade Realizada Intradiária

| Campo | Valor |
|---|---|
| ID | BM-VOL-RV-60K-README-001 |
| Estado | Validação funcional com evidências Profit; revisão global do PR pendente |
| Versão | 1.0.0 |
| SHA-256 (conteúdo canónico) | 4e5d2a42e4de94d1667d9e856d687196d9cc87c132d9c21114d0122fbe2e5b0c |
| Commit de referência | 4224a4a848a6ae7fe3da8e864c1f0876a66ba04a |
| Código | [RV_60K_V1.0.src](RV_60K_V1.0.src) |
| Referência NTSL | Manual NTSL 4.4, funções `Log`, `Sqrt`, `Date` e `Plot` |

## Objetivo

Criar o primeiro indicador visual isolado de volatilidade realizada para aplicação separada nos gráficos do Mini Índice (WIN) e Mini Dólar (WDO). O gráfico-alvo do BRICKMASTER é **60K trades**; isto não é gráfico de ticks nem Renko.

## Fórmula

Para os fechamentos C_i, o retorno logarítmico por barra é:

`r_i = ln(C_i / C_(i-1))`

A volatilidade realizada acumulada é:

`RV_t = 100 × sqrt(sum(r_i²))`

O fator 100 expressa o resultado numa escala percentual. Não é previsão, probabilidade, alvo de preço nem garantia de resultado. Como a amostragem de 60K trades tem duração variável, a medida é acumulada por barra e **não deve ser interpretada como volatilidade anualizada ou por unidade de tempo**.

## Contrato

- **Entrada:** `Close` do ativo exibido no gráfico e data associada à barra.
- **Saída:** uma série numérica plotada, correspondente à RV acumulada desde a reinicialização da data.
- **Ativos:** executar o mesmo indicador separadamente em WIN e WDO; não mistura séries nem compara escalas entre ativos automaticamente.
- **Gráfico:** concebido para 60K trades.
- **Reset inicial:** quando `Date` difere de `Date[1]`; no primeiro candle de nova data a acumulação reinicia e o retorno entre datas é excluído.
- **Segurança:** sem ordens, sem automação, sem leitura de VIX, sem limiares de regime e sem ligação ao Giroscópio.
- **Dados inválidos:** se um dos dois fechamentos for não positivo, o código mantém a acumulação anterior e não acrescenta retorno.

## Dependências e limitações

- A compilação no Profit foi confirmada por evidência visual fornecida pelo utilizador.
- As exportações OHLC e RV de WIN e WDO e as capturas de apoio foram extraídas do Profit, conforme confirmação expressa do utilizador.
- A regra funcional de reset pela data civil da sessão operacional foi confirmada com a documentação Profit fornecida; não reabrir esta conclusão como falta de evidência.
- O indicador depende de fechamentos de barras. Em 60K trades, cada barra agrega 60.000 negócios e o intervalo temporal entre barras é variável.
- Não contém suavização, classificação de regime, limiares, previsão, stop, gestão de risco nem execução.
- O resultado é uma estatística acumulada dependente da granularidade e do caminho de preços; não comparar diretamente valores de WIN e WDO como se tivessem a mesma distribuição.
- Nenhum teste de compilação, replay, backtest ou mercado real foi executado nesta versão.

## Plano de validação

1. Importar o `.src` no Editor de Estratégias/Indicadores do Profit e compilar.
2. Aplicar num gráfico de 60K trades de WIN e verificar se o indicador aparece sem erros.
3. Repetir em WDO, sem alterar o código.
4. Conferir manualmente uma pequena sequência de fechamentos, calculando `ln(C_i/C_(i-1))`, soma dos quadrados e raiz quadrada vezes 100.
5. Verificar série plana: RV deve permanecer em zero.
6. Verificar queda e alta: o incremento de RV depende do quadrado do retorno, não da direção.
7. Regra de reset pela data civil confirmada na documentação Profit enviada.
8. Evidências visuais e exportações Profit já fornecidas e preservadas no contexto de validação.
9. Comparação independente das séries exportadas executada; resultados e tolerâncias registados no relatório de validação funcional.

## Critérios de aceitação

- Compilação no Profit evidenciada pelo utilizador.
- Aplicação separada em WIN e WDO nos gráficos de 60K trades evidenciada.
- Comparação independente: 10.858/10.858 registos WIN e 10.000/10.000 WDO dentro da tolerância absoluta de 0,01.
- Reset pela data civil confirmado pela documentação Profit fornecida.
- Relatório e manifesto SHA-256 integrados na branch feature; revisão global do PR continua pendente.

## Estado de validação

**Validação funcional documentada com evidências do Profit; revisão global do PR pendente.** O utilizador forneceu evidência de compilação e exportações reais de WIN e WDO. A auditoria independente das exportações ficou dentro da tolerância absoluta de 0,01 em todos os registos analisados. A regra de reset por data civil foi confirmada com a documentação Profit fornecida. Isto não equivale a aprovação para produção, backtest estatístico de estratégia ou autorização para execução de ordens.

## Histórico

| Versão | Data | Alteração | Estado |
|---|---|---|---|
| 1.0.0 | 2026-10-19 | Primeiro protótipo RV acumulada por data para gráfico de 60K trades | EXPERIMENTAL |
| 1.0.1 | 2026-10-19 | Estado de validação atualizado com compilação, exportações Profit e auditoria independente já fornecidas | REVISÃO DO PR PENDENTE |

## Integridade documental

- SHA-256 canónico do conteúdo, excluindo esta secção: 0d8e6d3ae51a5a0f711d866e178ce84ba8d0d7b0b829150e463ff8b01d1decb1
- Commit de referência do código original: `2b04df92c2785e4adacf921f7379d9b0ed49da56`
- Commit desta atualização documental: a registar após o commit ser criado.
- Relatório de validação: [RELATORIO_VALIDACAO_FUNCIONAL_RV_60K.md](../VALIDACAO/RELATORIO_VALIDACAO_FUNCIONAL_RV_60K.md)
- Política de reset: [POLITICA_SESSAO_RESET_RV_60K.md](../VALIDACAO/POLITICA_SESSAO_RESET_RV_60K.md)
