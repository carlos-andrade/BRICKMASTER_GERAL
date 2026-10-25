#!/usr/bin/env bash
set -euo pipefail
fail=0
while IFS= read -r -d '' file; do
  if [[ "$(head -n 1 "$file" || true)" != "---" ]]; then
    echo "::error file=$file::Falta Front Matter YAML no início."
    fail=1
    continue
  fi
  for field in projeto repositorio tipo_documento fase id_documento titulo status versao data_criacao data_atualizacao origem autoridade_documental cadeia_autoridade rastreabilidade escopo objetivo dependencias; do
    if ! grep -Eq "^${field}:" "$file"; then
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
if [[ "$fail" -ne 0 ]]; then
  echo "Validação documental FALHOU."
  exit 1
fi
echo "Validação documental PASS."
