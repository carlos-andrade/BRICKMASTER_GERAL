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
| **SHA-256 (conteúdo canónico)** | 602357591d77656e9bc7582225b3f5273eab1464928de26c0d6835714104ca06 |
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
