---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "INDICE_DE_MODULOS"
fase: "ARQUITETURA_MODULAR"
id_documento: "BM-DOC-MODULOS-README"
titulo: "BRICKMASTER RAIZ — Arquitetura modular"
status: "EM_DESENVOLVIMENTO"
versao: "1.0.0"
data_criacao: "N/A"
data_atualizacao: "2026-10-19"
sha256_canonico: "PENDENTE DE RECÁLCULO INDEPENDENTE"
commit_referencia: "d1f91fdcae5d92ac56449b570022011ae7857e6b"
origem: "Conteúdo preexistente; histórico Git"
autoridade_documental: "GOVERNANCA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR feat/cabecalho-padrao-documental"
escopo: "Índice e regras estruturais dos módulos"
objetivo: "Padronizar a documentação modular e os seus ciclos de validação"
dependencias: "Documentos de cada módulo"
---

# BRICKMASTER RAIZ — Arquitetura modular

> **Projeto:** BRICKMASTER RAIZ  
> **Repositório:** carlos-andrade/BRICKMASTER_GERAL  
> **Tipo:** ÍNDICE DE MÓDULOS  
> **Fase:** ARQUITETURA MODULAR  
> **ID:** BM-DOC-MODULOS-README  
> **Status:** EM_DESENVOLVIMENTO  
> **Versão:** 1.0.0  
> **Criação:** N/A  
> **Atualização:** 2026-10-11  
> **Origem:** Conteúdo preexistente; histórico Git  
> **Autoridade:** GOVERNANÇA  
> **Rastreabilidade:** PR feat/cabecalho-padrao-documental

## Contexto Histórico

Índice preexistente que define a estrutura e o ciclo de vida dos módulos BRICKMASTER.

## Regra estrutural

Cada módulo do BRICKMASTER deve existir na sua própria pasta dentro de `MODULOS/`. O desenvolvimento, os testes, os registos de evidência e a aprovação são feitos individualmente. A integração só pode ocorrer depois de o módulo passar pelos critérios de aceitação e receber aprovação explícita.

## Módulo fundador

**MÓDULO 001 — LINHA DE ABERTURA E PROJEÇÕES PERCENTUAIS**

É o primeiro módulo do sistema e a referência estrutural inicial para os módulos posteriores. No início de cada sessão de mercado, identifica o preço de referência da abertura, plota uma linha-base e calcula/representa os níveis percentuais simétricos:

- +0,5% e −0,5%
- +1% e −1%
- +2% e −2%
- +3% e −3%

Fórmula conceptual, tomando (P_0) como o preço de abertura definido para a sessão:

`Nível(p) = P₀ × (1 + p/100)`

Para níveis inferiores, `p` é negativo. A definição operacional exata de “abertura” — preço do primeiro negócio, abertura oficial do ativo ou outra referência disponibilizada pela plataforma — deve ser documentada e validada no ativo e no gráfico escolhidos antes da implementação final.

## Estrutura por módulo

Cada pasta de módulo deve conter, conforme aplicável:

1. `README.md` — objetivo, âmbito, regras e estado.
2. `ESPECIFICACAO.md` — comportamento esperado e decisões técnicas.
3. `tests/` — casos de teste e dados de teste.
4. `evidencias/` — resultados, capturas e registos de execução.
5. `CHANGELOG.md` — alterações por versão.
6. Código isolado — sem dependência da integração final durante a fase de teste.

## Ciclo obrigatório

1. Especificar.
2. Implementar isoladamente.
3. Validar sintaxe e limitações da plataforma.
4. Executar testes funcionais e de fronteira.
5. Registar evidências reproduzíveis.
6. Corrigir falhas e repetir os testes.
7. Aprovar o módulo.
8. Só então preparar a integração com os restantes módulos.

**Não integrar módulos que não tenham evidências de teste e critérios de aceitação satisfeitos.** A aprovação num backtest não equivale, por si só, a validação em tempo real ou garantia de rentabilidade.

## Estado

EM_DESENVOLVIMENTO — regras modulares documentadas. `MODULOS/10_VOLATILIDADE_VIX/` foi removida de `main` pelo PR #33 (commit `d1f91fdcae5d92ac56449b570022011ae7857e6b`). O módulo canónico de volatilidade é `MODULOS/VOLATILIDADE/`.

## Evidências

O conteúdo original deste índice e os documentos vinculados no repositório.

## Validação

O cabeçalho foi padronizado; não foram executados testes de trading por esta alteração.

## Resultado

Índice com identificação e rastreabilidade.

## Próxima Ação

Aplicar a mesma governança aos restantes documentos e validar a cobertura documental.
