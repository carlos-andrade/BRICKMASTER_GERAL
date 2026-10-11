#!/usr/bin/env bash
set -euo pipefail

fail=0
while IFS= read -r -d '' file; do
  first_line="$(head -n 1 "$file" || true)"
  if [[ "$first_line" != "---" ]]; then
    echo "::error file=$file::Falta Front Matter YAML no início do documento."
    fail=1
    continue
  fi
  for field in projeto repositorio tipo_documento fase id_documento titulo status versao data_criacao data_atualizacao origem autoridade_documental cadeia_autoridade rastreabilidade escopo objetivo dependencias; do
    if ! grep -Eq "^\${field}:" "$file"; then
      echo "::error file=$file::Campo obrigatório ausente no Front Matter: $field"
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
  echo "Validação documental FALHOU. Corrigir os documentos antes de integrar."
  exit 1
fi

echo "Validação documental PASS: todos os Markdown rastreados contêm os campos e secções obrigatórios."
