"""Casos del hook bloquear-secretos.sh: los que tiene que bloquear y los que tiene que dejar.

Uso, desde plugins/luptecx:  python hooks/probar_bloquear_secretos.py
Cada cambio al hook se prueba con esto antes de subirlo; un caso nuevo va a una de las dos
listas.
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HOOK = str(Path(__file__).with_name("bloquear-secretos.sh"))
# En Windows, el bash de Git (el que usa Claude Code), no el de WSL.
GIT_BASH = r"C:\Program Files\Git\usr\bin\bash.exe"
BASH = os.environ.get("BASH_DEL_HOOK") or (
    GIT_BASH if Path(GIT_BASH).exists() else shutil.which("bash") or "bash"
)

BLOQUEAR = [
    "cat .env",
    "type .env",
    "Get-Content .env",
    'Get-Content ".env"',
    "cat ./app/.env",
    "head -5 .env.production",
    "cp .env.ejemplo .env",
    "grep TOKEN .env",
    "cat credentials.json",
    "python -c \"print(open('credentials.json').read())\"",
    "cat ~/.ssh/id_ed25519",
    "cat server.pem",
    "printenv",
    "env",
    "env | grep TOKEN",
    "Get-ChildItem env:",
    "gci Env:",
    "echo $env:GITHUB_TOKEN",
    "echo $TOKEN_METRICAS",
    "echo ${ANTHROPIC_API_KEY}",
    "gh auth token",
    "gh auth status --show-token",
    "ls && cat .env",
]

DEJAR = [
    "git status",
    'git commit -m "documentacion: no subir el .env"',
    "cat .env.ejemplo",
    "cat credentials.json.ejemplo",
    "cat ~/.ssh/id_ed25519.pub",
    "uv run pytest",
    "env UV_LINK_MODE=copy uv sync",
    "grep -rn TOKEN app/",
    "gh auth status",
    "docker compose up -d",
    "ls -la",
    "uv run python -m app.metricas 2026-10",
    "echo $HOME",
    "cat app/configuracion.py",
]


def corre(comando: str) -> int:
    entrada = json.dumps({"tool_name": "Bash", "tool_input": {"command": comando}})
    resultado = subprocess.run([BASH, HOOK], input=entrada, text=True, capture_output=True)
    return resultado.returncode


def main() -> int:
    fallas = 0
    for comando in BLOQUEAR:
        if corre(comando) != 2:
            fallas += 1
            print("NO BLOQUEÓ:", comando)
    for comando in DEJAR:
        if corre(comando) != 0:
            fallas += 1
            print("BLOQUEÓ DE MÁS:", comando)
    print(f"{len(BLOQUEAR) + len(DEJAR)} casos, {fallas} fallas")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
