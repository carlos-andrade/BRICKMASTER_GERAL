---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "NORMA_TECNICA_NTSL_PROFIT"
fase: "Governança de código"
id_documento: "BM-NTSL-CONV-ID-001"
titulo: "Convenção de identificadores para código NTSL no Profit"
estado: "REGRA_OPERACIONAL"
versao: "1.0.0"
data_atualizacao: "2026-10-19"
status: "EM REVISAO DOCUMENTAL"
data_criacao: "2026-10-19"
origem: "Documentação Profit fornecida pelo utilizador e repositório BRICKMASTER_GERAL"
autoridade_documental: "Manual NTSL 4.4, documentação Profit fornecida e governação do repositório"
cadeia_autoridade: "Documentação de referência > evidência Profit > auditoria independente > documentação do módulo"
rastreabilidade: "PR #32; commits e SHA-256 registados neste documento"
escopo: "Módulo RV-60K e governação documental associada"
objetivo: "Preservar contexto, estado, evidências, validação e próxima ação"
dependencias: "Profit/NTSL 4.4; exportações WIN/WDO; scripts de validação documental"
---

# Convenção de identificadores para código NTSL no Profit

| Campo | Valor |
|---|---|
| ID documental | BM-NTSL-CONV-ID-001 |
| Estado | REGRA OPERACIONAL — requisito geral para novos códigos |
| Versão | 1.0.0 |
| SHA-256 (conteúdo canónico) | 1e82b1da5bb3210d787038130bd3b6bb836b9d84179d909f20bf683b702c4ae5 |
| Commit de referência | 8dbd16976e64a820618d25370c26fed6541104d9 |

## Regra obrigatória

Todo identificador destinado a ser usado como nome de indicador, estratégia ou artefacto compilável no Profit deve usar a convenção compatível confirmada pelo utilizador:

- Usar o prefixo literal `ID:` quando o identificador for declarado no cabeçalho/comentário do código.
- Usar letras, números e underscore (`_`) para separar os componentes do identificador.
- Não usar hífen (`-`) no identificador do Profit.
- Manter nomes curtos, estáveis e rastreáveis; a versão pode ser indicada como sufixo `V1`, `V1_0` ou convenção equivalente aprovada no módulo.

### Exemplo obrigatório

**Correto:**

```text
ID: BM_VOL_RV_60K_001
```

**Incorreto:**

```text
ID: BM-VOL-RV-60K-001
```

## Âmbito

Esta regra aplica-se a todo o código NTSL preparado para compilar ou importar no Profit, incluindo indicadores, estratégias, módulos auxiliares e futuras revisões do BRICKMASTER RAIZ. Não é apenas uma regra do indicador RV-60K.

Os identificadores documentais de Markdown e os nomes de ficheiros podem seguir convenções próprias, desde que não sejam confundidos com o nome/identificador exigido pelo Profit.

## Checklist antes de entregar código

1. Confirmar que o identificador começa com `ID:` quando declarado no cabeçalho.
2. Confirmar que o identificador usa underscore como separador e não contém hífens.
3. Procurar no código e remover identificadores incompatíveis antes de entregar.
4. Preservar o identificador consistente entre código, documentação de compilação e registo de testes.
5. Se o Profit rejeitar o nome, registar o texto exato do erro e corrigir antes de declarar compilação bem-sucedida.

## Regra de evidência

A convenção underscore é uma regra operacional confirmada pelo utilizador a partir do comportamento observado no Profit. A sua adoção não significa que o indicador tenha sido compilado ou testado. A compilação efetiva deve ser registada separadamente, com versão/edição do Profit e evidência observável.

## Histórico

| Versão | Data | Alteração | Estado |
|---|---|---|---|
| 1.0.0 | 2026-10-19 | Formalizada regra geral: IDs para Profit usam underscore, sem hífens | REGRA OPERACIONAL |

## Contexto Histórico

Este documento pertence ao trabalho RV-60K desenvolvido na branch feature e preserva o histórico do protótipo, das evidências fornecidas e das decisões registadas. O gráfico-alvo do sistema é 60K trades.

## Estado

O módulo permanece experimental e isolado. A validação numérica documentada não equivale a aprovação para produção; a validação documental do PR #32 tem de passar antes da integração.

## Evidências

As exportações OHLC/RV e capturas referidas neste conjunto foram extraídas do Profit, conforme confirmação do utilizador. Os resultados quantitativos aplicáveis constam do relatório de validação funcional.

## Validação

A validação distingue consistência numérica das exportações, compilação evidenciada no Profit e validação automática documental. Não declarar testes além dos que têm evidência registada.

## Resultado

O conteúdo técnico e o histórico são preservados. A correção documental não altera a lógica NTSL nem amplia o escopo funcional.

## Próxima Ação

Executar novamente o workflow de validação de cabeçalhos no PR #32. Só após resultado PASS e revisão do diff poderá avançar a integração em develop.

## Integridade documental

- SHA-256 canónico do conteúdo anterior a esta secção: `4b4f2e8f8e70844e39151612134e686abfa8f7a949220657b20ffe10261f53f0`

O SHA-256 canónico é calculado em UTF-8 com finais de linha LF, excluindo as linhas `SHA-256 (conteúdo canónico)` e `Commit de referência`.

<!-- RECONCILIACAO_SHA256: fe725ca916a05d0ee95b9ab213f980d5b90b9abb7173ed467cd0c679fb65f38b
COMMIT_DE_REFERENCIA: c0740f9fd4d1485b3c3a1b8568053b8cd077e688
-->
