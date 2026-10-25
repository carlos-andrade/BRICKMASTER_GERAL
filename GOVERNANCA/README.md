---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "README_GOVERNANCA"
fase: "GOVERNANCA"
id_documento: "BM-GOV-README-001"
titulo: "BRICKMASTER RAIZ — Governança"
status: "PROPOSTA_PARA_REVISAO"
versao: "1.0.1"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-25"
origem: "Recuperação documental do PR #3 fechado sem merge"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #41; branch feature/pr3-governanca-mainline-reconciliation; main-base 3db0c88f27fec4c6ea2418749de09ebba8130fe7"
escopo: "Governança documental do BRICKMASTER RAIZ"
objetivo: "BRICKMASTER RAIZ — Governança"
dependencias: "main e documentos canónicos preexistentes; ver corpo documental"
sha256_canonico: "7de9912abed3cb05900b34a12c5722203b54614d6036fff8a9631a306494a699"
commit_referencia: "PENDENTE_APOS_COMMIT"
---

# BRICKMASTER RAIZ — Governança

- Estado: estrutura documental em revisão; a existência dos documentos não significa aprovação.
- Repositório: https://github.com/carlos-andrade/BRICKMASTER_GERAL
- Pasta canónica: `GOVERNANCA/`.
- Integridade: preservar históricos; não declarar testes, aprovações ou validações sem evidências verificáveis.

## Finalidade

Esta pasta centraliza os documentos de governança do BRICKMASTER RAIZ: autoridade decisória, ciclo de desenvolvimento, gestão de mudanças, contratos, riscos, evidências, checkpoints, decisões e auditoria.

## Mapa documental

- [Carta de Governança](CARTA_GOVERNANCA.md) — princípios, autoridade e limites.
- [Ciclo de Desenvolvimento](CICLO_DE_DESENVOLVIMENTO.md) — fluxo feature → develop → validação → main.
- [Padrão de Módulos](PADRAO_DE_MODULOS_E_CONTRATOS.md) — contratos, dependências, estados e testes.
- [Risco e Segurança](RISCO_E_SEGURANCA.md) — risco soberano, dados inválidos e bloqueios.
- [Checkpoints e Evidências](CHECKPOINTS_E_EVIDENCIAS.md) — checkpoints reproduzíveis e trilha de evidências.
- [Registo de Decisões](REGISTRO_DE_DECISOES.md) — decisões arquiteturais.
- [Registo Mestre](REGISTRO_MODULOS_E_CHECKPOINTS.md) — registo de módulos já mantido em main.
- [Norma de Cabeçalho](NORMA-CABECALHO-PADRAO.md) — norma documental preexistente.
- [Inventário Documental](INVENTARIO_DOCUMENTAL.md) — estado do inventário e recuperação PR #3.
- [Modelo de Checkpoint](MODELO_CHECKPOINT.md) — modelo reutilizável.
- [Modelo de Decisão](MODELO_DECISAO.md) — modelo reutilizável.
- [Histórico](HISTORICO.md) — histórico de alterações.
- [Roadmap Mestre](ROADMAP_MESTRE.md) — fases e critérios de promoção.

## Estados controlados

- **EXPERIMENTAL:** hipótese, protótipo ou implementação sem evidência suficiente.
- **VALIDADO:** passou pelos testes documentados e reproduzíveis dentro de escopo definido.
- **PRODUÇÃO:** aprovado para uso operacional, com monitorização, recuperação e rollback.
- **BLOQUEADO:** dependência, qualidade dos dados, divergência ou risco impede avanço seguro.
- **DEPRECADO:** substituído formalmente; preservar referência histórica e motivo.

Não promover um componente apenas porque compila ou porque passou por um teste isolado.

## Regra para documentos existentes

Não apagar documentos para limpar a estrutura. Toda migração deve registar caminho anterior, caminho novo, motivo, data e commit. Conteúdo técnico que não seja documento de governança permanece na pasta funcional de origem e é referenciado aqui quando necessário.

## Início de sessão

1. Ler esta página e a Carta de Governança.
2. Ler o checkpoint mais recente e o registo de decisões.
3. Confirmar branch, commit-base e estado do repositório.
4. Identificar evidências, testes pendentes, riscos e bloqueios.
5. Executar o próximo passo seguro e verificável.
6. Atualizar checkpoint, histórico e decisão quando aplicável.

## Limite operacional

A meta de 1% desde a abertura do dia é hipótese de pesquisa, não promessa de rentabilidade. A governança de risco prevalece sobre metas de resultado. Nenhuma ordem de mercado deve ser enviada por padrão.

## Contexto Histórico

Documento recuperado da proposta histórica PR #3, fechada sem merge, e reconciliado numa branch derivada do main corrente.

## Estado

PROPOSTA PARA REVISÃO. Não equivale a aprovação da governança, implementação operacional ou produção.

## Evidências

- PR #3 fechado sem merge: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/3
- PR de recuperação: https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/41
- Main-base: 3db0c88f27fec4c6ea2418749de09ebba8130fe7

## Validação

Estrutura documental sujeita ao workflow do repositório. O SHA-256 canónico será calculado sobre o corpo normalizado UTF-8/LF, excluindo apenas este bloco de metadados; o commit de referência será atualizado após a gravação final. Não foram executados testes NTSL, Profit, backtest nem validação operacional.

## Resultado

Conteúdo preservado e adaptado para revisão sobre o main corrente, sem substituir os artefactos de governança preexistentes.

## Próxima Ação

Executar a validação documental, auditar o SHA-256 final, conferir links e referências cruzadas e rever o PR antes de qualquer integração.
