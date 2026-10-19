---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "DOCUMENTACAO_TECNICA"
fase: "F3 — Construção isolada"
id_documento: "BM-RV60K-DOC-002"
titulo: "RELATORIO VALIDACAO FUNCIONAL RV 60K"
status: "EM REVISAO DOCUMENTAL"
versao: "1.0.2"
data_criacao: "2026-10-19"
data_atualizacao: "2026-10-19"
origem: "Documentação Profit fornecida pelo utilizador e repositório BRICKMASTER_GERAL"
autoridade_documental: "Manual NTSL 4.4, documentação Profit fornecida e governação do repositório"
cadeia_autoridade: "Documentação de referência > evidência Profit > auditoria independente > documentação do módulo"
rastreabilidade: "PR #32; commits e SHA-256 registados neste documento"
escopo: "Módulo RV-60K e governação documental associada"
objetivo: "Preservar contexto, estado, evidências, validação e próxima ação"
dependencias: "Profit/NTSL 4.4; exportações WIN/WDO; scripts de validação documental"
---

# BRICKMASTER RAIZ — Validação funcional RV-60K

## Estado

**Proveniência confirmada:** as séries OHLC, os valores do indicador RV-60K e as capturas analisadas foram extraídos pelo utilizador diretamente do Profit. Não são dados sintéticos nem valores inventados. Esta auditoria recalcula independentemente os valores a partir das exportações reais fornecidas; não substitui nem invalida a evidência visual original do Profit.

## Método

- Ordenação cronológica reconstruída a partir da exportação descendente; desempate por ordem original invertida.
- Emparelhamento por timestamp e ocorrência do timestamp.
- Fórmula de referência: `RV = 100 * sqrt(sum(ln(Close_t / Close_(t-1))^2))`.
- Reinício de referência na mudança de data civil, em concordância com a implementação NTSL atual (`Date <> Date[1]`) e com os registos exportados observados.
- Extração de três registos anteriores e quatro posteriores a cada transição de data para inspeção.
- Os ficheiros de origem foram fornecidos como exportações do Profit; a auditoria não os classifica como sintéticos.

## Resumo por instrumento

| Instrumento | Linhas OHLC | Linhas RV | Pareados | Sem par | Datas | Timestamps duplicados | Erro absoluto máximo | Erro absoluto médio | Erro <= 0,005 | Percentagem <= 0,005 | Erro <= 0,01 | Percentagem <= 0,01 | Quedas intradiárias | Primeira barra zero | Primeira barra não zero | Timestamps alinhados |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| WIN | 10858 | 10858 | 10858 | 0 | 124 | 26 | 0,00500004 | 0,00248485 | 10857 | 99,9908% | 10858 | 100% | 0 | 124 | 0 | Sim |
| WDO | 10000 | 10000 | 10000 | 0 | 818 | 0 | 0,00516232 | 0,00231250 | 9943 | 99,43% | 10000 | 100% | 0 | 818 | 0 | Sim |

## Critérios

- `Erro <= 0,01`: compatibilidade numérica com tolerância definida para a auditoria.
- `Quedas intradiárias`: diminuições no valor exportado dentro da mesma data após ordenação cronológica.
- `Primeira barra zero`: verificação da regra por data, não prova que data civil corresponda sempre à sessão de negociação.
- `Sem pareamento`: registos que não encontraram correspondência no outro ficheiro.

## Estado da validação e limites do que foi demonstrado

1. **Proveniência:** confirmada pelo utilizador: ficheiros e capturas foram extraídos do Profit. Os ficheiros de origem são evidência real do gráfico/plataforma, não dados inventados.
2. **Consistência numérica:** o recálculo independente a partir dos OHLC exportados ficou dentro da tolerância de 0,01 em 100% dos registos de WIN e WDO. Isso sustenta a consistência numérica das exportações, sem afirmar identidade bit a bit.
3. **Reinício diário:** os dados apresentam a primeira barra de cada data com RV igual a zero e nenhuma queda intradiária detetada. O código implementa reinício quando `Date <> Date[1]`.
4. **Limite semântico:** a regra comprovada no código é mudança de data civil. Não se deve chamar-lhe automaticamente “sessão oficial de negociação” para todos os casos de horários especiais ou sessões que cruzem a meia-noite. Este é um ponto de especificação, não uma contestação da origem Profit dos dados.
5. **Estado do artefacto:** não houve alteração do código NTSL. Este relatório é uma atualização documental da auditoria; a integração no GitHub deste documento só fica confirmada após o commit ser devolvido pelo GitHub.

## SHA-256 das fontes

- `MINI_ÍNDICE_6K_TRADES_16-10-2026.xlsx` — `13f1817ae9beb49dab28ab2d8ba13583361550cce070888ff72e332ebedebcc7`
- `BM_VOL_RV_60K.xlsx` — `464010e13c001637a8083eee2f43ffd384de0b86eb91215b800c604b9a45eea7`
- `MINI_DOLAR_6K_TRADES_16-10-2026.xlsx` — `8affcbd770a128637da79ffe05e786237e3adcaec3ae8d34e5dc105a9904cef0`
- `BM_VOL_RV_60K_DOLAR.xlsx` — `60d2722a800af17db3cf6d2f82d56e9f7c1e9dc2f16f10e621e7fb42c40c31e3`

## Referência de código

- Commit do protótipo na branch feature: `2b04df92c2785e4adacf921f7379d9b0ed49da56`
- PR #32: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/32
- Estado do código: experimental; sem promoção a produção.

## Contexto Histórico

Este documento pertence ao trabalho RV-60K desenvolvido na branch feature e preserva o histórico do protótipo, das evidências fornecidas e das decisões registadas. O gráfico-alvo do sistema é 60K trades.

## Evidências

As exportações OHLC/RV e capturas referidas neste conjunto foram extraídas do Profit, conforme confirmação do utilizador. Os resultados quantitativos aplicáveis constam do relatório de validação funcional.

## Validação

A validação distingue consistência numérica das exportações, compilação evidenciada no Profit e validação automática documental. Não declarar testes além dos que têm evidência registada.

## Resultado

O conteúdo técnico e o histórico são preservados. A correção documental não altera a lógica NTSL nem amplia o escopo funcional.

## Próxima Ação

Executar novamente o workflow de validação de cabeçalhos no PR #32. Só após resultado PASS e revisão do diff poderá avançar a integração em develop.

## Integridade documental

- SHA-256 canónico do conteúdo (excluindo esta secção de integridade): `c97d2211972f4f4b467eeddc511f71dc46646f9db345ebc4a593e80fa55bf01b`
- Commit de referência do protótipo/código: `2b04df92c2785e4adacf921f7379d9b0ed49da56`
- PR de referência: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/32
- Estado de integração: commit documental gravado na branch feature; não representa promoção a `develop` ou `main`.
