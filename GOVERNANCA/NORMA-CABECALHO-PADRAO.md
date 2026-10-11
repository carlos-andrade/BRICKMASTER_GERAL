---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "NORMA_DE_GOVERNANCA_DOCUMENTAL"
fase: "GOVERNANCA"
id_documento: "BM-GOV-CABECALHO-PADRAO-001"
titulo: "Norma obrigatória de cabeçalho documental — BRICKMASTER RAIZ"
status: "IMPLEMENTADO"
versao: "1.0.0"
data_criacao: "2026-10-11"
data_atualizacao: "2026-10-11"
origem: "MODELO-PADRAO-CABECALHO.md do repositório Curioso-da-Internet-IA"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "feat/cabecalho-padrao-documental"
escopo: "Documentos de BRICKMASTER_GERAL e todas as subpastas"
objetivo: "Impor identificação, contexto histórico, evidências, validação, resultado e próxima ação"
dependencias: "CABEÇALHO/MODELO-PADRAO-CABECALHO.md como referência externa"
---

# Norma obrigatória de cabeçalho documental — BRICKMASTER RAIZ

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Tipo:** NORMA DE GOVERNANÇA DOCUMENTAL  
> **Fase:** GOVERNANÇA  
> **ID:** BM-GOV-CABECALHO-PADRAO-001  
> **Status:** IMPLEMENTADO  
> **Versão:** 1.0.0  
> **Criação:** 2026-10-11  
> **Atualização:** 2026-10-11  
> **Origem:** MODELO-PADRAO-CABECALHO.md — Curioso-da-Internet-IA  
> **Autoridade:** GOVERNANÇA  
> **Rastreabilidade:** feat/cabecalho-padrao-documental

## Contexto Histórico

Foi determinada a adoção obrigatória do modelo canónico de cabeçalho definido em [Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md](https://github.com/carlos-andrade/Curioso-da-Internet-IA/blob/main/CABE%C3%87ALHO/MODELO-PADRAO-CABECALHO.md) em todo o repositório BRICKMASTER_GERAL, incluindo todas as subpastas. A padronização não pode apagar ou reescrever a história técnica dos artefatos.

## Regra obrigatória

1. Todo novo documento Markdown (`.md`) deve começar com Front Matter YAML e cabeçalho visível segundo o modelo canónico.
2. Todos os documentos Markdown existentes devem ser migrados sem eliminar conteúdo técnico, histórico, decisões, limitações ou evidências.
3. Os campos YAML devem manter nomes estáveis: `projeto`, `repositorio`, `tipo_documento`, `fase`, `id_documento`, `titulo`, `status`, `versao`, `data_criacao`, `data_atualizacao`, `origem`, `autoridade_documental`, `cadeia_autoridade`, `rastreabilidade`, `escopo`, `objetivo`, `dependencias`.
4. Datas desconhecidas recebem `N/A`; nunca inventar datas, testes, aprovações ou referências.
5. `id_documento` deve ser único no repositório.
6. Todo documento deve conter as secções `Contexto Histórico`, `Estado`, `Evidências`, `Validação`, `Resultado` e `Próxima Ação`.
7. O cabeçalho identifica o documento; não substitui o seu conteúdo.
8. Alterações relevantes atualizam versão, data e rastreabilidade. O histórico Git deve ser preservado.
9. Estados e níveis de confiança devem refletir evidência real. `VALIDADO` nunca significa apenas que o cabeçalho foi verificado.
10. Documentos HTML, TXT ou outros formatos legíveis devem receber uma variante equivalente do cabeçalho que não danifique a sintaxe, o renderizador ou a execução. Em HTML, inserir comentário e bloco visível em posição compatível com o documento; em código NTSL, não inserir YAML Markdown: usar comentários NTSL apenas quando isso for sintaticamente seguro.
11. Não alterar binários, imagens, PDFs ou artefactos executáveis de forma indiscriminada. Para formatos que não suportam cabeçalho interno, criar um documento sidecar de metadados e rastreabilidade.
12. Os documentos normativos e de arquitetura devem manter a cadeia de autoridade **PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO**.

## Estado

A norma fica estabelecida nesta branch de trabalho. A migração de todos os formatos do repositório deve ser controlada por inventário e validação, sem declarar cobertura completa antes da verificação.

## Evidências

- Modelo canónico externo consultado.
- Inventário recursivo de `main`: 209 ficheiros no snapshot consultado, incluindo 10 Markdown, 69 HTML, 92 SRC, 34 TXT, 2 DOCX, 1 PDF e 1 PNG.
- Os 10 documentos Markdown listados no inventário foram alvo da migração nesta branch; a validação final ainda é necessária.

## Validação

A existência desta norma não prova que todos os ficheiros de todos os formatos já foram migrados. A verificação de cobertura deve conferir cada artefacto e o histórico Git.

## Resultado

Norma documental central criada para governar documentos existentes e futuros, com exigência explícita de preservar o conteúdo original e não inventar evidências.

## Próxima Ação

Concluir o inventário por formato, migrar os documentos legíveis ainda sem cabeçalho, implementar validação automática para Markdown e rever o resultado antes de integrar em `main`.
