---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_FUNCIONAL"
id_documento: "BM-VOL-RV-60K-SESSAO-001"
titulo: "Política de sessão e reset do RV-60K"
estado: "REGRA CONFIRMADA PELA DOCUMENTAÇÃO PROFIT FORNECIDA"
versao: "1.0.1"
data_atualizacao: "2026-10-19"
---

# Política de sessão e reset do RV-60K

## 1. Objetivo

Formalizar a regra de reinício do RV-60K com base na documentação e nas evidências extraídas do Profit e fornecidas pelo utilizador para os gráficos de 60K trades de WIN e WDO.

## 2. Regra confirmada

**A data civil associada à sessão operacional de negociação controla o reinício do RV-60K.** Esta regra foi confirmada pelo utilizador com base na documentação e nas evidências do Profit enviadas para análise. Não se deve reabrir esta conclusão como se faltasse recolher evidência.

- O código atual usa `Date <> Date[1]` para reiniciar a acumulação quando muda a data civil da barra.
- A auditoria das exportações Profit observou a primeira barra de cada data com RV igual a zero e nenhuma queda intradiária nos conjuntos analisados.
- A data civil não é um campo descartável: faz parte da regra funcional de reset já demonstrada pela documentação fornecida.
- A documentação oficial de horários pode servir para contextualizar sessões especiais e vigências, mas não deve ser usada para contrariar a regra comprovada no material Profit enviado.
- Não alterar a regra nem pedir nova exportação apenas para repetir a evidência já fornecida.

## 3. Contrato de dados

Cada barra usada na decisão de sessão deve disponibilizar:
- instrumento/contrato identificado (WIN ou WDO);
- timestamp da barra, com fuso e sem ambiguidade;
- data civil preservada como campo independente;
- identificador da sessão operacional ou informação suficiente para derivá-lo com calendário validado;
- versão do calendário aplicada;
- estado de qualidade temporal.

Se a exportação não preservar a hora com precisão suficiente, a atribuição de sessão fica pendente; não deve ser fabricada.

## 4. Calendário versionado

Cada regra de calendário deve conter:
- instrumento e mercado;
- fonte oficial e URL;
- data de consulta e data de vigência;
- fuso horário;
- horários de abertura/encerramento;
- feriados, sessões especiais e alterações extraordinárias;
- hash SHA-256 do artefacto de calendário arquivado;
- estado: EXPERIMENTAL, VALIDADO ou OBSOLETO.

Não fixar horários de sessão no código como constantes universais. Horários publicados pela B3 podem mudar conforme instrumento e calendário. O calendário utilizado numa auditoria histórica deve ser o vigente na data analisada.

## 5. Comportamento atual e próximo passo

O código NTSL atual usa `Date <> Date[1]`, o que corresponde à regra de reinício por data civil confirmada na documentação Profit fornecida. **Não é necessária uma migração para substituir a data civil por outro identificador de sessão.**

Próximos passos:
1. preservar o código e as exportações já auditadas;
2. alinhar o estado e a descrição do README com a evidência Profit e a regra de reset confirmada;
3. manter o teste de transição de data como critério de regressão;
4. registar exceções futuras apenas se a documentação Profit ou evidência concreta mostrar um comportamento diferente;
5. preservar histórico, SHA-256 e commits de referência.

## 6. Matriz de regressão da regra confirmada

| Caso | Resultado esperado |
|---|---|
| Barras consecutivas na mesma sessão e mesma data civil | Não reiniciar |
| Mudança de data civil da barra conforme a regra documentada | Reiniciar a acumulação |
| Barras consecutivas na mesma data civil | Não reiniciar apenas por continuidade das barras |
| Feriado ou dia sem negociação | Não inventar sessão nem barras |
| Horário especial publicado pela B3 | Aplicar calendário com vigência correspondente |
| Timestamp ausente, ambíguo ou contraditório | Sessão desconhecida; bloquear consumidores dependentes |
| Lacuna de barras sem evidência de nova sessão | Não presumir que a lacuna equivale a nova sessão |
| WIN versus WDO | Aplicar calendário específico de cada instrumento |

## 7. Evidência Profit e resultado da auditoria

Os ficheiros OHLC/RV e as capturas analisados foram extraídos do Profit, conforme confirmado pelo utilizador. A documentação enviada estabelece a regra de reset por data civil da sessão operacional. A auditoria independente encontrou:
- WIN: 10.858 registos pareados; 124 datas; todas as diferenças absolutas dentro de 0,01.
- WDO: 10.000 registos pareados; 818 datas; todas as diferenças absolutas dentro de 0,01.
- Em ambos os conjuntos, a primeira barra observada de cada data tem RV zero e não foram detetadas quedas intradiárias.

Estes resultados apoiam a consistência numérica das séries exportadas e corroboram o comportamento observado do reset por data civil. A proveniência Profit e a regra funcional indicada pelo utilizador ficam registadas como confirmadas. Não declarar testes de exceções que não constem das evidências fornecidas.

## 8. Critérios de aceitação

- [x] Regra de reset por data civil registada a partir da documentação Profit fornecida.
- [x] Coerência numérica auditada para as exportações de WIN e WDO dentro da tolerância 0,01.
- [x] Código atual preservado como referência histórica.
- [ ] README e estado do módulo alinhados com a evidência.
- [ ] Revisão do PR e decisão formal de promoção de fase.

## 9. Fontes externas de referência

- B3 — horários de negociação de derivativos referenciados em índices: https://www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/horario-de-negociacao/derivativos/indices/
- B3 — câmbio e dólar pronto: https://www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/horario-de-negociacao/derivativos/cambio-e-dolar-pronto/
- B3 — alteração de horários publicada em 06/03/2026: https://www.b3.com.br/pt_br/noticias/operacoes-8AA8D0CD9C709633019CC38376552862.htm

Estas páginas são referências auxiliares para alterações de horários. Não substituem nem anulam a regra de reset confirmada pela documentação Profit fornecida para este módulo.

## 10. Integridade documental

- SHA-256 canónico do conteúdo, excluindo esta secção: 8aad80db0651305b42f9671091c7f4be5add43635398f8f2a51278d0f016cca6
- Commit de referência: `33fd71220dd516dd0deb261e055f9685290e8d2d` (commit anterior desta especificação).
- Estado: regra funcional confirmada; atualização documental, sem alteração do código NTSL nem promoção automática a produção.
