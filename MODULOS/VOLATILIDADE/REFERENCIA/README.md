---
projeto: "BRICKMASTER RAIZ"
repositorio: "carlos-andrade/BRICKMASTER_GERAL"
tipo_documento: "README_LABORATORIO_QUANTITATIVO"
fase: "F2 — Implementação de referência isolada"
id_documento: "BM-VOL-REF-README-001"
titulo: "Biblioteca de referência — VOLATILIDADE B3"
status: "EXPERIMENTAL"
versao: "1.0.0"
data_criacao: "2026-10-18"
data_atualizacao: "2026-10-18"
origem: "Implementação de referência isolada para investigação quantitativa"
autoridade_documental: "GOVERNANCA; especificação quantitativa VOLATILIDADE B3"
cadeia_autoridade: "PROMPTS → CARTAS → ESPECIFICAÇÃO QUANTITATIVA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "PR #30; testes unittest; workflow GitHub Actions"
escopo: "Biblioteca isolada de estimadores de volatilidade"
objetivo: "Comparar RV, ATR e estimadores OHLC com dados sintéticos reprodutíveis"
dependencias: "Python 3.12 no CI; runtime apenas com biblioteca padrão"
---

# Biblioteca de referência — VOLATILIDADE B3
### BRICKMASTER RAIZ | Laboratório quantitativo isolado

| Campo | Valor |
|---|---|
| **ID** | BM-VOL-REF-README-001 |
| **Projeto** | BRICKMASTER RAIZ |
| **Repositório** | [carlos-andrade/BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) |
| **Tipo documental** | README_LABORATORIO_QUANTITATIVO |
| **Fase** | F2 — Implementação de referência isolada |
| **Estado** | EXPERIMENTAL |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 18aa89f173b6072afea2c05f578432c850081932876978ec876f4e46fcfcfa50 |
| **Commit de referência (versão anterior)** | [5e5d106a71578fb4fce9c564b039381ab4faec58](https://github.com/carlos-andrade/BRICKMASTER_GERAL/commit/057065d4f742f4a329f5bfbe99188b2ddad0db00) |
| **Data** | 2026-10-18 |
| **Dependências** | Python 3.12 para CI; runtime usa apenas a biblioteca padrão |
| **Integração** | Nenhuma; Giroscópio, Profit/NTSL e execução não são chamados |

## Objetivo

Fornecer implementação de referência independente e reprodutível para comparar variância/volatilidade realizada (RV), ATR e estimadores OHLC antes de qualquer integração. Este laboratório não consome feeds de mercado e não emite ordens.

## Conteúdo

- **volatility_reference.py:** retornos logarítmicos, RV, desvio-padrão amostral, Parkinson, Garman–Klass, Rogers–Satchell, True Range, ATR simples e Wilder, gerador sintético e comparação.
- **test_volatility_reference.py:** testes unittest determinísticos com fixtures conhecidos, série plana, entradas inválidas e série sintética.
- **comparar_estimadores.py:** comparação JSON reproduzível com seed fixa.
- **.github/workflows/volatilidade-reference-tests.yml:** testes e comparação no GitHub Actions em push/PR.

## Executar localmente

A partir da raiz do repositório:

    python -m unittest discover -s MODULOS/VOLATILIDADE/REFERENCIA -p "test_*.py" -v

    cd MODULOS/VOLATILIDADE/REFERENCIA
    python comparar_estimadores.py

A saída é JSON. A seed é 20261018, o gerador produz 500 barras sintéticas e o ATR usa período 14.

## Interpretação e limites

- A série é sintética, inspirada em movimento geométrico Browniano; os extremos intrabar são aproximações aleatórias, não simulação exata de máximos/mínimos GBM.
- RV e estimadores OHLC estão na escala de retornos; ATR está em unidades de preço. **Não comparar valores absolutos como se tivessem a mesma unidade.**
- Parkinson, Garman–Klass e Rogers–Satchell são estimadores distintos, com pressupostos próprios. Dados sintéticos verificam pipeline e propriedades básicas; não validam adequação em WIN/WDO ou outros instrumentos B3.
- Variância negativa de Garman–Klass ou Rogers–Satchell não é truncada silenciosamente; a implementação gera erro explícito.
- O ATR usa True Range da primeira barra como high-low, pois não existe fecho anterior.
- A comparação é diagnóstica, não regra de negociação, calibração de regime ou recomendação de stop.
- Nenhum teste de mercado real, backtest, benchmark ou teste em produção é declarado.

## Contratos e regras de segurança

1. Sem dados externos, dependências de feeds ou efeitos de negociação.
2. Preços finitos e positivos; OHLC inconsistente é rejeitado.
3. Amostra insuficiente, parâmetros inválidos e estimadores indefinidos geram erro explícito.
4. Nenhum threshold de regime está definido.
5. Estado EXPERIMENTAL até testes adicionais com séries de referência, dados autorizados e revisão independente.
6. Não ligar ao Giroscópio até aprovação do contrato, testes de integração e gates de governança.

## Roadmap

- [x] Criar funções de referência e gerador sintético determinístico.
- [x] Criar testes unitários e workflow de CI.
- [ ] Executar e inspecionar os testes via GitHub Actions; guardar evidência do run.
- [ ] Comparar com implementação independente/referências numéricas conhecidas.
- [ ] Definir datasets autorizados e contrato de dados B3.
- [ ] Avaliar separadamente barras temporais, ticks (incluindo 60K) e Renko.
- [ ] Fazer revisão quantitativa e de código antes de qualquer integração.

## Histórico

| Versão | Data | Alteração | Estado |
|---|---|---|---|
| 1.0.0 | 2026-10-18 | Biblioteca isolada, testes sintéticos, comparador e CI | EXPERIMENTAL |

## Integridade documental

O SHA-256 canónico é calculado em UTF-8 com finais de linha LF, excluindo apenas as linhas de metadados SHA-256 (conteúdo canónico) e Commit de referência (versão anterior), conforme a norma GOVERNANCA. Confirmar o valor por leitura após publicação.

## Contexto Histórico

O módulo VOLATILIDADE permanece experimental e isolado. Esta biblioteca foi criada como camada de referência antes de qualquer integração. A implementação não altera módulos existentes nem consome dados reais.

## Estado

EXPERIMENTAL. O workflow específico de testes passou na execução inicial; o validador documental identificou inicialmente falta de Front Matter, agora corrigida nesta alteração. A nova execução do validador ainda precisa confirmar a correção.

## Evidências

- [Pull request #30](https://github.com/carlos-andrade/BRICKMASTER_GERAL/pull/30)
- [Workflow de testes da biblioteca](https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/workflows/volatilidade-reference-tests.yml)
- [Workflow de validação documental](https://github.com/carlos-andrade/BRICKMASTER_GERAL/actions/workflows/validar-cabecalhos-documentais.yml)

## Validação

Testes unitários e comparador sintético passaram na primeira execução do workflow dedicado (run 39174331830). A validação documental falhou inicialmente por ausência de Front Matter; esta correção é submetida para nova execução. Nenhum teste com dados reais B3 foi executado.

## Resultado

Biblioteca isolada, testes determinísticos e comparação JSON publicados na branch feature. A integração com o Giroscópio permanece bloqueada até revisão, validação adicional e aprovação.

## Próxima Ação

Confirmar o novo resultado do workflow documental, rever a implementação quantitativa e comparar os estimadores com fixtures independentes antes de aprovar o PR.
