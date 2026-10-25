<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: BRICKMASTER RAIZ — Portal do Projeto
IDENTIFICADOR: BM-ROOT-001
VERSÃO: 1.1.0
ESTADO: DOCUMENTADO — NÃO VALIDADO EM PRODUÇÃO
CRIADO EM: 2026-10-11
ÚLTIMA REVISÃO: 2026-10-25
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO: 2026-10-11 | v1.0.0 | Estrutura inicial.
FONTE DA VERDADE: repositório oficial.

SHA-256 CANÓNICO: d113a606432b4f9c99b41e7ce1354ceae826bedc46192f9285c4dc9b5736a135 (SHA-256 do corpo Markdown UTF-8/LF após o comentário)
COMMIT DE REFERÊNCIA: 3db0c88f27fec4c6ea2418749de09ebba8130fe7-->

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

## Governança central

- [Índice de governança](GOVERNANCA/README.md)
- [Carta de governança](GOVERNANCA/CARTA_GOVERNANCA.md)
- [Roadmap Mestre](GOVERNANCA/ROADMAP_MESTRE.md)
- [Inventário documental](GOVERNANCA/INVENTARIO_DOCUMENTAL.md)
- [Registo de módulos e checkpoints](ARQUITETURA/BRICKMASTER_RAIZ/REGISTRO_MODULOS_E_CHECKPOINTS.md)

A proposta de governança está em revisão. A presença destes documentos não representa aprovação para produção nem prova de testes de trading.
