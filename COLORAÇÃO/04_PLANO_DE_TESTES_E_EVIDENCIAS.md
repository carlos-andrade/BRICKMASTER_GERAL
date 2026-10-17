# BRICKMASTER RAIZ — Plano de Testes e Evidências de COLORAÇÃO

> **ID:** BM-COL-TEST-001  
> **Estado:** PENDENTE DE EXECUÇÃO NO PROFIT  
> **Versão:** 1.0.1  
> **Data:** 2026-10-17

## 1. Objetivo

Estabelecer verificações reproduzíveis para o protótipo BM-COL-RULE-001. Nenhum teste é considerado executado até existir evidência verificável.

## 2. Pré-condições a registar

- Versão/build do Profit.
- Ativo e vencimento, quando aplicável.
- Tipo de gráfico (incluindo gráfico de ticks/Renko, se usado).
- Configuração do gráfico e quantidade de histórico carregado.
- Data/hora do teste e fuso horário.
- Commit/hash do ficheiro testado.
- Capturas do código, compilação e gráfico resultante.

## 3. Casos de teste

| ID | Cenário | Resultado esperado | Estado |
|---|---|---|---|
| COL-T01 | Close > Close[1] | Barra verde (`clGreen`) | Pendente |
| COL-T02 | Close < Close[1] | Barra vermelha (`clRed`) | Pendente |
| COL-T03 | Close = Close[1] | Barra amarela (`clYellow`) | Pendente |
| COL-T04 | Histórico inicial insuficiente | Verificar comportamento sem classificação enganadora | Pendente |
| COL-T05 | Gráfico de ticks, incluindo 60K | Comportamento consistente com os fechamentos disponibilizados pelo Profit | Pendente |
| COL-T06 | Gráfico Renko | Comportamento consistente com os fechamentos das barras Renko | Pendente |
| COL-T07 | Revisão de efeitos colaterais | Nenhuma ordem, posição ou stop é alterado | Pendente |
| COL-T08 | Regressão após alteração | Casos anteriores continuam a passar | Pendente |

## 4. Critério de aprovação

Todos os casos aplicáveis devem ser executados e acompanhados de evidência. Se a sintaxe falhar, corrigir o ficheiro completo, registar o motivo e repetir a bateria. Não promover para VALIDADO com base apenas em revisão textual.

## 5. Evidência e limitações atuais

O Manual NTSL 4.4 contém exemplo explícito de `PaintBar` com `clYellow`, `clGreen` e `clRed` e comparação de `Close` com `Close[1]`. O protótipo segue esse padrão documental. Ainda não existe evidência anexada de compilação ou execução no Profit; portanto, o código permanece EXPERIMENTAL.
