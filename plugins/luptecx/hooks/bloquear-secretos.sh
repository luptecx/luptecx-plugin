#!/usr/bin/env bash
# Antes de que Claude corra un comando (Bash o PowerShell), lo bloquea si lee o imprime un
# secreto: archivos .env, credenciales, llaves privadas, variables de entorno con tokens o
# el token de gh. Complementa las reglas `deny` de lectura de .claude/settings.json, que
# cubren las herramientas de archivos de Claude pero no cualquier comando, y el aislamiento
# (sandbox) de Claude Code, que en Windows nativo no funciona.
#
# Recibe el JSON del hook por la entrada estándar. Sale con 2 (y el motivo en stderr, que
# Claude lee) para bloquear, y con 0 para dejar pasar.

entrada=$(cat)

# El comando, sin depender de jq: el valor de "command" con sus escapes de JSON.
comando=$(printf '%s' "$entrada" | grep -oE '"command"[[:space:]]*:[[:space:]]*"([^"\\]|\\.)*"' | head -n 1)
comando=${comando#*:}
# Sin las comillas del valor de JSON, para que el comando empiece donde empieza.
comando=$(printf '%s' "$comando" | sed -E 's/^[[:space:]]*"//; s/"$//')

bloquear() {
  echo "BLOQUEADO por el plugin luptecx: $1. Los secretos no pasan por Claude (ver luptecx:revisar-seguridad): si hace falta, lo hace el usuario en su terminal." >&2
  exit 2
}

# Fin de un nombre de archivo: espacio, comillas (escapadas o no), redirección, separador.
fin='([[:space:]"'"'"'\\>;|)]|$)'

# Cada parte del comando por separado: ; && || | y saltos de línea (\n escapado en el JSON).
partes=$(printf '%s' "$comando" | sed -E 's/\\n|&&|\|\||;|\|/\n/g')

while IFS= read -r parte; do
  # Un mensaje de commit puede nombrar un archivo .env sin leerlo.
  printf '%s' "$parte" | grep -qE '(^|[[:space:]"])git[[:space:]]+commit([[:space:]]|$)' && continue

  printf '%s' "$parte" | grep -qE '(^|[[:space:]/"'"'"'=<])\.env(\.local|\.production)?'"$fin" \
    && bloquear "el comando usa un archivo .env, que tiene los secretos del proyecto"
  printf '%s' "$parte" | grep -qE 'credentials[^[:space:]/"'"'"']*\.json'"$fin" \
    && bloquear "el comando usa un archivo de credenciales"
  printf '%s' "$parte" | grep -qE '\.(pem|key)'"$fin" \
    && bloquear "el comando usa una llave privada"
  printf '%s' "$parte" | grep -qE 'id_(rsa|ed25519|ecdsa)'"$fin" \
    && bloquear "el comando usa una llave SSH privada"

  printf '%s' "$parte" | grep -qE '(^|[[:space:]])printenv([[:space:]]|$)' \
    && bloquear "printenv muestra todas las variables de entorno, con sus secretos"
  printf '%s' "$parte" | grep -qE '^[[:space:]]*env[[:space:]]*$' \
    && bloquear "env sin argumentos muestra todas las variables de entorno"
  printf '%s' "$parte" | grep -qiE '(get-childitem|gci|ls|dir)[[:space:]]+env:' \
    && bloquear "listar env: muestra todas las variables de entorno"
  printf '%s' "$parte" | grep -qiE '\$(env:|\{)?[a-z0-9_]*(token|secret|password|passwd|api_?key)' \
    && bloquear "el comando lee una variable de entorno con un secreto"
  printf '%s' "$parte" | grep -qE '(^|[[:space:]"])gh[[:space:]]+auth[[:space:]]+token([[:space:]]|$)' \
    && bloquear "gh auth token imprime el token de GitHub"
  printf '%s' "$parte" | grep -qE '(^|[[:space:]"])gh[[:space:]]+auth[[:space:]]+status.*[[:space:]](-t|--show-token)([[:space:]"]|$)' \
    && bloquear "gh auth status --show-token imprime el token de GitHub"
done <<< "$partes"

exit 0
