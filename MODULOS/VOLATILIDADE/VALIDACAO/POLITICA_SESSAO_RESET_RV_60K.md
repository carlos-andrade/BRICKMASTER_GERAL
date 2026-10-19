---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "ESPECIFICACAO_FUNCIONAL"
id_documento: "BM-VOL-RV-60K-SESSAO-001"
titulo: "Política de sessão e reset do RV-60K"
estado: "PROPOSTA PARA REVISÃO"
versao: "1.0.0"
data_atualizacao: "2026-10-19"
---

# Política de sessão e reset do RV-60K

## 1. Objetivo

Distinguir a data civil associada à barra da sessão operacional de negociação para o indicador de volatilidade realizada RV-60K, executado separadamente nos gráficos de 60K trades de WIN e WDO.

## 2. Decisão proposta

- A data civil é metadado de auditoria e agrupamento cronológico; não é, por si só, a identidade da sessão.
- A sessão operacional é determinada por calendário versionado por instrumento, com vigência, fuso, início/fim, exceções e referência oficial.
- O reset da RV ocorre na primeira barra válida identificada como pertencente a uma nova sessão operacional.
- Barras que atravessem a meia-noite civil não provocam reset automaticamente se pertencerem à mesma sessão operacional.
- Uma nova data civil não cria automaticamente uma nova sessão operacional.
- Se o módulo não conseguir determinar a sessão de forma inequívoca, deve sinalizar CONTEXTO_SESSAO_DESCONHECIDO. A RV pode continuar apenas em modo diagnóstico claramente marcado; qualquer consumidor que dependa do reset correto deve bloquear decisões dependentes desse estado.
- Não inferir a sessão a partir do número da barra, do nome do ficheiro ou apenas de `Date`.

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

## 5. Comportamento atual e migração

O código NTSL atual usa `Date <> Date[1]`. Isto implementa reset por mudança da data civil, não por sessão operacional. Não alterar silenciosamente a semântica do código.

Migração proposta:
1. manter a versão atual como referência histórica;
2. confirmar que o timestamp exportado do Profit tem precisão e fuso adequados;
3. construir e revisar calendário histórico por instrumento;
4. classificar transições: mesma sessão/data diferente; sessão nova/data igual; sessão nova/data diferente; lacuna de dados; timestamp inválido/ambíguo;
5. definir o identificador de sessão fora do indicador NTSL se a linguagem/plataforma não disponibilizar dados suficientes;
6. só então decidir se o reset será implementado no indicador ou fornecido por um módulo de contexto;
7. comparar resultados antes/depois e preservar ambos os artefactos.

## 6. Matriz mínima de validação

| Caso | Resultado esperado |
|---|---|
| Barras consecutivas na mesma sessão e mesma data civil | Não reiniciar |
| Sessão cruza a meia-noite civil | Não reiniciar apenas pela mudança de data |
| Nova sessão no mesmo dia civil | Reiniciar se o calendário marcar nova sessão |
| Feriado ou dia sem negociação | Não inventar sessão nem barras |
| Horário especial publicado pela B3 | Aplicar calendário com vigência correspondente |
| Timestamp ausente, ambíguo ou contraditório | Sessão desconhecida; bloquear consumidores dependentes |
| Lacuna de barras sem evidência de nova sessão | Não presumir que a lacuna equivale a nova sessão |
| WIN versus WDO | Aplicar calendário específico de cada instrumento |

## 7. Evidência existente e limites

Os ficheiros OHLC/RV e as capturas anteriormente analisados foram extraídos do Profit, conforme confirmado pelo utilizador. A auditoria independente encontrou:
- WIN: 10.858 registos pareados; 124 datas; todas as diferenças absolutas dentro de 0,01.
- WDO: 10.000 registos pareados; 818 datas; todas as diferenças absolutas dentro de 0,01.
- Em ambos os conjuntos, a primeira barra observada de cada data tem RV zero e não foram detetadas quedas intradiárias.

Estes resultados apoiam a consistência numérica da série e o comportamento observado do reset por data civil. **Não demonstram, por si só, que data civil equivale a sessão oficial em todos os casos**, nem provam cobertura de todos os calendários especiais. A proveniência Profit não está em causa.

## 8. Critérios de aceitação

- [ ] Fonte oficial e versão do calendário registadas para WIN e WDO.
- [ ] Fuso e precisão temporal das exportações confirmados.
- [ ] Transições da matriz mínima classificadas com evidência.
- [ ] Sessões noturnas e exceções tratadas segundo calendário vigente.
- [ ] Comparação antes/depois documentada, sem apagar histórico.
- [ ] SHA-256 e commit de referência incluídos.
- [ ] Revisão aprovada antes de promover de PROPOSTA para VALIDADO.

## 9. Fontes externas de referência

- B3 — horários de negociação de derivativos referenciados em índices: https://www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/horario-de-negociacao/derivativos/indices/
- B3 — câmbio e dólar pronto: https://www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/horario-de-negociacao/derivativos/cambio-e-dolar-pronto/
- B3 — alteração de horários publicada em 06/03/2026: https://www.b3.com.br/pt_br/noticias/operacoes-8AA8D0CD9C709633019CC38376552862.htm

Estas páginas são referências de consulta, não um calendário histórico completo arquivado. A regra final deve ser validada contra o calendário oficial aplicável a cada data.

## 10. Integridade documental

- SHA-256 canónico (excluindo os campos SHA-256, commit e estado desta secção): 347c75eb6763ab70c3213bd21e0600bc0569ba4ca0ab3773f07d6cacd22714b9
- Commit de referência: `df99fb3388a911279b8972e51ed6527489312a7d` (commit que criou este documento).
- Estado: proposta documental; não modifica o código NTSL nem promove o módulo a produção.
