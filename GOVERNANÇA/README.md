# BRICKMASTER RAIZ — Governança

> Estado: fundação documental proposta; requer revisão e validação do responsável pelo projeto.
> Repositório: https://github.com/carlos-andrade/BRICKMASTER_GERAL
> Integridade: preservar históricos; não declarar testes, aprovações ou validações sem evidências verificáveis.

## Finalidade

Esta pasta é a fonte central dos documentos de governança do BRICKMASTER RAIZ: autoridade decisória, ciclo de desenvolvimento, gestão de mudanças, arquitetura, riscos, evidências, checkpoints e auditoria.

## Mapa documental

- [CARTA_GOVERNANCA.md](CARTA_GOVERNANCA.md) — princípios, autoridade e limites.
- [CICLO_DE_DESENVOLVIMENTO.md](CICLO_DE_DESENVOLVIMENTO.md) — fluxo feature → develop → validação → principal.
- [PADRAO_DE_MODULOS_E_CONTRATOS.md](PADRAO_DE_MODULOS_E_CONTRATOS.md) — contratos, dependências, estados e testes.
- [RISCO_E_SEGURANCA.md](RISCO_E_SEGURANCA.md) — risco soberano, dados inválidos e bloqueios.
- [CHECKPOINTS_E_EVIDENCIAS.md](CHECKPOINTS_E_EVIDENCIAS.md) — checkpoints reproduzíveis e trilha de evidências.
- [REGISTRO_DE_DECISOES.md](REGISTRO_DE_DECISOES.md) — decisões arquiteturais.
- [INVENTARIO_DOCUMENTAL.md](INVENTARIO_DOCUMENTAL.md) — inventário e migração de documentos existentes.
- [MODELO_CHECKPOINT.md](MODELO_CHECKPOINT.md) — modelo reutilizável de checkpoint.
- [MODELO_DECISAO.md](MODELO_DECISAO.md) — modelo reutilizável de decisão.
- [HISTORICO.md](HISTORICO.md) — histórico de alterações.

## Estados

- **EXPERIMENTAL:** hipótese, protótipo ou implementação sem evidência suficiente.
- **VALIDADO:** passou pelos testes documentados e reproduzíveis dentro de um escopo definido.
- **PRODUÇÃO:** aprovado para uso operacional, com monitoramento, recuperação e rollback.
- **BLOQUEADO:** dependência, qualidade dos dados, divergência ou risco impede avanço seguro.
- **DEPRECADO:** substituído formalmente; preservar referência histórica e motivo.

Não promover um componente apenas porque compila ou porque passou por um teste isolado.

## Regra para documentos existentes

Não apagar documentos para limpar a estrutura. Toda migração deve registrar caminho anterior, caminho novo, motivo, data e commit. Quando localização ou conteúdo não puderem ser confirmados, marcar como PENDENTE DE INVENTÁRIO.

## Início de sessão

1. Ler esta página e a Carta de Governança.
2. Ler o checkpoint mais recente e o registro de decisões.
3. Confirmar branch, commit-base e estado do repositório.
4. Identificar evidências, testes pendentes, riscos e bloqueios.
5. Executar o próximo passo seguro e verificável.
6. Atualizar checkpoint, histórico e decisão quando aplicável.

## Limite operacional

A meta de 1% desde a abertura do dia é hipótese de pesquisa, não promessa de rentabilidade. A governança de risco prevalece sobre metas de resultado. Nenhuma ordem de mercado deve ser enviada por padrão.
