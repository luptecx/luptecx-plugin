r"""Aplica los ajustes de seguridad de LUPTECX a Claude Code en este PC (plan de seguridad).

Agrega a ~/.claude/settings.json, sin tocar lo demás:
- reglas `deny` para que Claude no lea secretos en ninguna carpeta: .env, credenciales,
  llaves privadas, ~/.ssh, el token de gh, Bitwarden y los archivos «NO-SUBIR»;
- `disableBypassPermissionsMode`: nadie puede arrancar Claude saltándose los permisos.

Es idempotente: correrlo dos veces no duplica nada. Antes de escribir, guarda una copia
(settings.json.respaldo-AAAAMMDD-HHMMSS). Los cambios cuentan desde la próxima sesión.

Uso (cualquier PC con el plugin instalado), en PowerShell:
    python (Get-ChildItem "$HOME\.claude\plugins\cache\luptecx\luptecx\*\herramientas\asegurar_claude.py" | Select-Object -Last 1).FullName
"""

import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

AJUSTES = Path.home() / ".claude" / "settings.json"

# `//` es la raíz del disco (en Windows, las rutas se comparan como /c/Users/...); `~/` es
# la carpeta del usuario. Una regla de lectura también impide editar o escribir ese archivo.
NEGAR = [
    "Read(//**/.env)",
    "Read(//**/.env.local)",
    "Read(//**/.env.production)",
    "Read(//**/credentials*.json)",
    "Read(//**/*.pem)",
    "Read(//**/*.key)",
    "Read(//**/id_rsa)",
    "Read(//**/id_ed25519)",
    "Read(//**/*NO-SUBIR*)",
    "Read(~/.ssh/**)",
    "Read(~/.claude/.credentials.json)",
    "Read(~/AppData/Roaming/GitHub CLI/**)",
    "Read(~/.config/gh/**)",
    "Read(~/AppData/Roaming/Bitwarden/**)",
]


def aplicar(ajustes: dict) -> list[str]:
    """Agrega lo que falta y devuelve qué se agregó."""
    agregado = []
    permisos = ajustes.setdefault("permissions", {})
    negar = permisos.setdefault("deny", [])
    for regla in NEGAR:
        if regla not in negar:
            negar.append(regla)
            agregado.append(f"deny {regla}")
    if permisos.get("disableBypassPermissionsMode") != "disable":
        permisos["disableBypassPermissionsMode"] = "disable"
        agregado.append("disableBypassPermissionsMode = disable")
    return agregado


def main() -> int:
    ajustes = json.loads(AJUSTES.read_text(encoding="utf-8")) if AJUSTES.exists() else {}
    agregado = aplicar(ajustes)
    if not agregado:
        print(f"Nada que cambiar: {AJUSTES} ya tiene los ajustes de seguridad.")
        return 0
    if AJUSTES.exists():
        respaldo = AJUSTES.with_name(f"settings.json.respaldo-{datetime.now():%Y%m%d-%H%M%S}")
        shutil.copy2(AJUSTES, respaldo)
        print(f"Copia de antes: {respaldo}")
    AJUSTES.parent.mkdir(parents=True, exist_ok=True)
    AJUSTES.write_text(json.dumps(ajustes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Agregado a {AJUSTES}:")
    for linea in agregado:
        print(f"  {linea}")
    print("Cuenta desde la próxima sesión de Claude Code.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
