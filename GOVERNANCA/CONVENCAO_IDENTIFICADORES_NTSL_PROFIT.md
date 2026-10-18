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

## Integridade documental

O SHA-256 canónico é calculado em UTF-8 com finais de linha LF, excluindo as linhas `SHA-256 (conteúdo canónico)` e `Commit de referência`.
