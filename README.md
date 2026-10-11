<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: BRICKMASTER RAIZ — Portal do Projeto
IDENTIFICADOR: BM-ROOT-001
VERSÃO: 1.0.0
ESTADO: DOCUMENTADO — NÃO VALIDADO EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-11
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO: 2026-10-11 | v1.0.0 | Estrutura inicial.
FONTE DA VERDADE: repositório oficial.
-->

# BRICKMASTER RAIZ

Sistema modular de leitura de mercado, estado do gráfico, evidências, decisão, risco e observabilidade.

## Comece por aqui
- [Arquitetura modular](BRICKMASTER_ARQUITETURA/README.md)
- [Governança técnica](BRICKMASTER_ARQUITETURA/GOVERNANCA.md)
- [Roadmap](BRICKMASTER_ARQUITETURA/ROADMAP.md)
- [Catálogo de módulos](BRICKMASTER_ARQUITETURA/MAPA_MODULOS.md)
- [Contrato padrão de módulo](BRICKMASTER_ARQUITETURA/CONTRATO_MODULO.md)
- [Template de módulo](TEMPLATES/README_MODULO.md)

## Princípio operacional
O sistema deve responder onde o operador está no gráfico, qual o regime de mercado, quais evidências existem, o que contradiz a leitura e quais condições a invalidam. Nenhuma leitura substitui os gates de risco.

## Referências do projeto
- Manual NTSL 4.4, 03/08/2026 — referência principal fornecida para validação técnica de NTSL.
- [FVG-ATLAS](https://github.com/carlos-andrade/FVG-ATLAS) — projeto relacionado.
- [B3](https://github.com/carlos-andrade/B3) e [BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL) — fontes auxiliares de dados e pesquisa, sem pressupor disponibilidade em tempo real.

## Estado
Documentação inicial versionada em branch de trabalho. Implementação e validação dos módulos continuam pendentes.
