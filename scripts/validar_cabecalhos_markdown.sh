#!/usr/bin/env bash
set -euo pipefail

# BRICKMASTER RAIZ — canonical Markdown validator.
# Legacy Markdown with an HTML comment header is tolerated only as legacy format;
# recovered governance docs with YAML front matter must meet the full contract.
# This validation checks structure only, not SHA-256 values or semantic approval.

fail=0
checked=0
legacy=0

while IFS= read -r -d '' file; do
  checked=$((checked + 1))
  first_line="$(head -n 1 "$file" || true)"

  if [[ "$first_line" != "---" ]]; then
    if [[ "$first_line" == "<!--" ]]; then
      legacy=$((legacy + 1))
      echo "::notice file=$file::Formato legado de cabeçalho HTML preservado; migração controlada pendente."
      continue
    fi
    echo "::error file=$file::Cabeçalho não reconhecido: esperado Front Matter YAML (---) ou comentário HTML legado (<!--)."
    fail=1
    continue
  fi

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
echo "Cabeçalhos HTML legados tolerados sem migração: $legacy"

if [[ "$fail" -ne 0 ]]; then
  echo "Validação documental FALHOU."
  exit 1
fi

echo "Validação estrutural dos cabeçalhos Markdown PASS (não certifica hashes nem conteúdo semântico)."
