# BRICKMASTER RAIZ — Arquitetura modular

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

## Índice

- [Módulo 001 — Linha de abertura e projeções percentuais](./001-LINHA-ABERTURA-PROJECOES-PERCENTUAIS/README.md)
