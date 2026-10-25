# Inventário Documental e Plano de Migração

- Estado: INVENTÁRIO INICIAL EXECUTADO; classificação semântica final ainda requer revisão.
- Data: 2026-10-11
- Base examinada: árvore Git recursiva da branch `feature/governanca-fundacao`, derivada de `main`.
- Método: caminhos e metadados Git; conteúdo integral não foi revisto para todos os 212 arquivos.

## Critério de classificação

1. Governança: regras, autoridade, risco, decisões, checkpoints, contratos transversais e padrões documentais.
2. Arquitetura: desenho técnico e organização de camadas; permanece na pasta de arquitetura salvo quando o documento é um registo operacional de governança.
3. Módulo: especificações e testes próprios; permanecem junto ao módulo.
4. Evidência/referência: permanece na localização funcional original, com referência na governança quando necessário.

## Migrações nesta alteração

| ID | Origem | Destino | Motivo | Estado |
|---|---|---|---|---|
| MIG-0001 | `GOVERNANÇA/CARTA_GOVERNANCA.md` | `GOVERNANCA/CARTA_GOVERNANCA.md` | Padronizar o destino para a pasta canónica já existente em main | PROPOSTO NA BRANCH |
| MIG-0002 | `GOVERNANÇA/CHECKPOINTS_E_EVIDENCIAS.md` | `GOVERNANCA/CHECKPOINTS_E_EVIDENCIAS.md` | Centralizar regras de evidência | PROPOSTO NA BRANCH |
| MIG-0003 | `GOVERNANÇA/CICLO_DE_DESENVOLVIMENTO.md` | `GOVERNANCA/CICLO_DE_DESENVOLVIMENTO.md` | Centralizar ciclo de desenvolvimento | PROPOSTO NA BRANCH |
| MIG-0004 | `GOVERNANÇA/HISTORICO.md` | `GOVERNANCA/HISTORICO.md` | Centralizar histórico da governança | PROPOSTO NA BRANCH |
| MIG-0005 | `GOVERNANÇA/INVENTARIO_DOCUMENTAL.md` | `GOVERNANCA/INVENTARIO_DOCUMENTAL.md` | Centralizar inventário | PROPOSTO NA BRANCH |
| MIG-0006 | `GOVERNANÇA/MODELO_CHECKPOINT.md` | `GOVERNANCA/MODELO_CHECKPOINT.md` | Centralizar modelo de checkpoint | PROPOSTO NA BRANCH |
| MIG-0007 | `GOVERNANÇA/MODELO_DECISAO.md` | `GOVERNANCA/MODELO_DECISAO.md` | Centralizar modelo de decisão | PROPOSTO NA BRANCH |
| MIG-0008 | `GOVERNANÇA/PADRAO_DE_MODULOS_E_CONTRATOS.md` | `GOVERNANCA/PADRAO_DE_MODULOS_E_CONTRATOS.md` | Centralizar contratos transversais | PROPOSTO NA BRANCH |
| MIG-0009 | `GOVERNANÇA/README.md` | `GOVERNANCA/README.md` | Índice central no caminho solicitado | PROPOSTO NA BRANCH |
| MIG-0010 | `GOVERNANÇA/REGISTRO_DE_DECISOES.md` | `GOVERNANCA/REGISTRO_DE_DECISOES.md` | Centralizar decisões | PROPOSTO NA BRANCH |
| MIG-0011 | `GOVERNANÇA/RISCO_E_SEGURANCA.md` | `GOVERNANCA/RISCO_E_SEGURANCA.md` | Centralizar política de risco | PROPOSTO NA BRANCH |
| MIG-0012 | `ARQUITETURA/BRICKMASTER_RAIZ/REGISTRO_MODULOS_E_CHECKPOINTS.md` | `GOVERNANCA/REGISTRO_MODULOS_E_CHECKPOINTS.md` | O conteúdo é registo transversal de governança e checkpoints | PROPOSTO NA BRANCH |

O arquivo `GOVERNANCA/NORMA-CABECALHO-PADRAO.md` já existia no destino e é preservado.

## Documentos que permanecem fora da pasta

- `ARQUITETURA/BRICKMASTER_RAIZ/ARQUITETURA_MODULAR_BASELINE_2026-10-11.md`: documento de arquitetura técnica; referenciado pela governança, mas não movido automaticamente.
- Especificações, changelogs, evidências e testes específicos de módulos: permanecem junto aos respetivos módulos.
- `.github/workflows/validar-cabecalhos-documentais.yml`: automação executável, não documento de política; permanece em `.github/workflows/`.

## Verificações

- Árvore recursiva consultada: 212 arquivos no commit da base consultada.
- Caminhos identificados por nome: norma de cabeçalho e registo de módulos/checkpoints, além dos documentos criados nesta iniciativa.
- A classificação semântica de todos os arquivos não está concluída, porque nem todos os conteúdos foram lidos integralmente.
- Não foram executados testes de código ou validações automáticas nesta etapa.
- A migração só será efetiva em `main` após revisão e merge do PR.

## Próximo passo

Rever os documentos de governança e verificar referências cruzadas e links após a migração de caminhos. Não declarar a migração concluída em `main` antes do merge.
