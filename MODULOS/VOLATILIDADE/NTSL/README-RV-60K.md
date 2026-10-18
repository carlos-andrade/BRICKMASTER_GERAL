---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "INDICADOR_NTSL_EXPERIMENTAL"
fase: "F3 — Construção isolada"
id_documento: "BM-VOL-RV-60K-README-001"
titulo: "RV-60K — Volatilidade Realizada Intradiária"
estado: "EXPERIMENTAL"
versao: "1.0.0"
data_atualizacao: "2026-10-19"
---

# RV-60K — Volatilidade Realizada Intradiária

| Campo | Valor |
|---|---|
| ID | BM-VOL-RV-60K-README-001 |
| Estado | EXPERIMENTAL — não validado no Profit |
| Versão | 1.0.0 |
| SHA-256 (conteúdo canónico) | ff48f5b70d3485a2b511315b2d46d5a805154d6addb3d3ef7397f45525085da6 |
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

- Requer verificação da sintaxe/compilação na versão instalada do Profit; a presença das funções no Manual NTSL 4.4 não comprova a compilação deste arquivo.
- A lógica de reset por `Date` é provisória. É necessário confirmar o calendário e a sessão de negociação de WIN/WDO, especialmente barras associadas à sessão noturna, antes de declarar reset operacional correto.
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
7. Confirmar que a mudança de data reinicia a série e avaliar explicitamente a sessão noturna.
8. Guardar capturas, versão do Profit, ativo, configuração do gráfico, data/hora e resultado da compilação como evidência.
9. Só após os testes anteriores, comparar com cálculo independente em Python e avaliar a integração.

## Critérios de aceitação

- Compila no Profit sem erros.
- Aplica-se a WIN e WDO sem dependência de ordens.
- Resultados coincidem com cálculo manual independente dentro da tolerância definida.
- Reset de sessão é especificado e comprovado, incluindo sessão noturna.
- Evidências anexadas e revisão concluída antes de promover de EXPERIMENTAL.

## Estado de validação

**Ainda não validado na plataforma.** A revisão documental confirmou que o Manual NTSL 4.4 documenta `Log(Valor)` como logaritmo natural, `Sqrt(Valor)` como raiz quadrada, `Date()` como data da barra e `Plot(Valor)` como função de plotagem. Isto apoia a escolha das funções, mas não comprova compilação nem comportamento do indicador completo.

## Histórico

| Versão | Data | Alteração | Estado |
|---|---|---|---|
| 1.0.0 | 2026-10-19 | Primeiro protótipo RV acumulada por data para gráfico de 60K trades | EXPERIMENTAL |

## Integridade documental

O SHA-256 canónico é calculado em UTF-8 com finais de linha LF, excluindo as linhas `SHA-256 (conteúdo canónico)` e `Commit de referência`, conforme a regra documental adotada. O commit indicado é referência de rastreabilidade, não uma declaração de aprovação.
