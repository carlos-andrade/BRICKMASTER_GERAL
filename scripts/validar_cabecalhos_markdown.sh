#!/usr/bin/env bash
set -euo pipefail

# BRICKMASTER RAIZ — canonical Markdown validator.
# Validate the canonical YAML header contract where present.
# For inherited legacy documents, report their leading format and require
# controlled migration in a separate inventory; do not silently call them valid.
# This script is deliberately structural and does not validate SHA-256 fields.

fail=0
checked=0
yaml=0
html_legacy=0
other_legacy=0

while IFS= read -r -d '' file; do
  checked=$((checked + 1))
  first_line="$(head -n 1 "$file" || true)"

  if [[ "$first_line" != "---" ]]; then
    if [[ "$first_line" == "<!--" ]]; then
      html_legacy=$((html_legacy + 1))
      echo "::notice file=$file::Cabeçalho legado em comentário HTML; migração controlada pendente."
    else
      other_legacy=$((other_legacy + 1))
      echo "::notice file=$file::Cabeçalho legado sem Front Matter YAML; migração controlada pendente."
    fi
    continue
  fi

  yaml=$((yaml + 1))
  for field in projeto repositorio tipo_documento fase id_documento titulo status versao data_criacao data_atualizacao origem autoridade_documental cadeia_autoridade rastreabilidade escopo objetivo dependencias; do
    if ! grep -Eq "^$field:" "$file"; then
      echo "::error file=$file::Campo obrigatório ausente: $field"
      fail=1
    fi
  done

  for section in "Contexto Histórico" "Estado" "Evidências" "Validação" "Resultado" "Próxima Ação"; do
    if ! grep -Fq "## $section" "$file"; then
      echo "::error file=$file::Secção obrigatória ausente: $section"
      fail=1
    fi
  done
done < <(git ls-files -z '*.md')

echo "Ficheiros Markdown rastreados: $checked"
echo "Documentos com Front Matter YAML verificados: $yaml"
echo "Cabeçalhos HTML legados: $html_legacy"
echo "Outros formatos legados: $other_legacy"

if [[ "$fail" -ne 0 ]]; then
  echo "Validação estrutural FALHOU."
  exit 1
fi

echo "Validação estrutural dos cabeçalhos YAML presentes PASS; documentos legados continuam pendentes de migração."
