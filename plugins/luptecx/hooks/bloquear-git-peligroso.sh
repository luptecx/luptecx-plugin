#!/usr/bin/env bash
# Antes de que Claude corra un comando (Bash o PowerShell), lo bloquea si es un comando de
# git que borra trabajo o se salta los candados. Adaptado de git-guardrails-claude-code
# (Matt Pocock, MIT): allí se bloquea todo `git push`; en LUPTECX se sube directo a `main`,
# así que solo se bloquea forzarlo.
#
# Recibe el JSON del hook por la entrada estándar. Sale con 2 (y el motivo en stderr, que
# Claude lee) para bloquear, y con 0 para dejar pasar.

entrada=$(cat)

# El comando, sin depender de jq: el valor de "command" con sus escapes de JSON.
comando=$(printf '%s' "$entrada" | grep -oE '"command"[[:space:]]*:[[:space:]]*"([^"\\]|\\.)*"' | head -n 1)
comando=${comando#*:}
# Sin el texto entre comillas: un mensaje de commit que nombra --no-verify no es usarlo.
comando=$(printf '%s' "$comando" | sed -E "s/\\\\\"([^\\\\]|\\\\[^\"])*\\\\\"/ /g; s/'[^']*'/ /g")

bloquear() {
  echo "BLOQUEADO por el plugin luptecx: $1. En LUPTECX no se hace (ver luptecx:luptecx-codigo). Si de verdad hace falta, lo corre el usuario a mano después de entender qué se pierde." >&2
  exit 2
}

# Cada parte del comando por separado: ; && || | y saltos de línea (\n escapado en el JSON).
partes=$(printf '%s' "$comando" | sed -E 's/\\n|&&|\|\||;|\|/\n/g')

while IFS= read -r parte; do
  printf '%s' "$parte" | grep -qE '(^|[[:space:]"])git([[:space:]]|$)' || continue

  if printf '%s' "$parte" | grep -qE '[[:space:]]push([[:space:]]|$)'; then
    printf '%s' "$parte" | grep -qE '[[:space:]](-f|--force|--force-with-lease(=[^[:space:]]*)?|--force-if-includes)([[:space:]"]|$)' \
      && bloquear "git push forzado reescribe la historia de main para los dos socios"
    printf '%s' "$parte" | grep -qE '[[:space:]]\+[^[:space:]]+' \
      && bloquear "git push con +rama también es un push forzado"
  fi
  printf '%s' "$parte" | grep -qE '[[:space:]]--no-verify([[:space:]"]|$)' \
    && bloquear "--no-verify se salta los candados; se arregla la causa"
  printf '%s' "$parte" | grep -qE '[[:space:]]commit([[:space:]].*)?[[:space:]]-n([[:space:]"]|$)' \
    && bloquear "git commit -n es --no-verify: se salta los candados"
  printf '%s' "$parte" | grep -qE '[[:space:]]reset([[:space:]].*)?[[:space:]]--hard([[:space:]"]|$)' \
    && bloquear "git reset --hard borra los cambios sin guardar"
  printf '%s' "$parte" | grep -qE '[[:space:]]clean([[:space:]].*)?[[:space:]]-[a-zA-Z]*f' \
    && bloquear "git clean -f borra archivos que git no conoce, sin papelera"
  printf '%s' "$parte" | grep -qE '[[:space:]]branch([[:space:]].*)?[[:space:]](-D|--delete[[:space:]]+--force|--force[[:space:]]+--delete)([[:space:]"]|$)' \
    && bloquear "git branch -D borra una rama aunque no esté integrada"
  printf '%s' "$parte" | grep -qE '[[:space:]]checkout([[:space:]]+--)?[[:space:]]+\.([[:space:]"]|$)' \
    && bloquear "git checkout . descarta todos los cambios sin guardar"
  if printf '%s' "$parte" | grep -qE '[[:space:]]restore([[:space:]].*)?[[:space:]]\.([[:space:]"]|$)'; then
    # Sacar del índice (--staged sin --worktree) no borra nada.
    if ! printf '%s' "$parte" | grep -qE -- '--staged' || printf '%s' "$parte" | grep -qE -- '--worktree'; then
      bloquear "git restore . descarta todos los cambios sin guardar"
    fi
  fi
done <<< "$partes"

exit 0
