#!/usr/bin/env bash
set -euo pipefail

# Valida estritamente documentos que adotam o padrão YAML Front Matter.
# Documentos históricos com cabeçalho HTML legado são preservados e reportados,
# mas não são reescritos automaticamente por este validador.
fail=0
checked=0
legacy=0

while IFS= read -r -d '' file; do
  first_line="$(head -n 1 "$file" || true)"

  if [[ "$first_line" != "---" ]]; then
    if head -n 5 "$file" | grep -q '<!--'; then
      echo "::notice file=$file::Cabeçalho HTML legado preservado; fora da validação YAML estrita."
      legacy=$((legacy + 1))
    else
      echo "::notice file=$file::Documento histórico sem Front Matter; preservado e não validado por este gate."
      legacy=$((legacy + 1))
    fi
    continue
  fi

  checked=$((checked + 1))
  for field in projeto repositorio tipo_documento fase id_documento titulo status versao data_criacao data_atualizacao origem autoridade_documental cadeia_autoridade rastreabilidade escopo objetivo dependencias; do
    if ! grep -Eq "^\${field}:" "$file"; then
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
  echo "Validação documental FALHOU: $checked documentos YAML verificados; $legacy documentos legados preservados."
  exit 1
fi

echo "Validação documental PASS: $checked documentos YAML verificados; $legacy documentos legados preservados e explicitamente fora do gate YAML."
