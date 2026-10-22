"""Trae al plugin, tal cual, las skills de terceros listadas en externas.json.

Cada una se descarga de su repositorio en el commit fijado y queda en
skills/externas/<nombre>/, junto con su licencia en licencias/. Nunca se editan a mano:
para actualizar una, se cambia su commit en externas.json, se corre esto, se revisa el
diff (con skill-scanner) y se sube con su commit.

Uso, desde plugins/luptecx (necesita gh con sesión iniciada):
    python herramientas/traer_externas.py            # trae todas
    python herramientas/traer_externas.py fastapi    # solo una
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "skills" / "externas"
LICENCIAS = {"fastapi/fastapi": "LICENSE", "getsentry/skills": "LICENSE"}


def gh(*argumentos: str) -> bytes:
    resultado = subprocess.run(["gh", "api", *argumentos], capture_output=True, check=True)
    return resultado.stdout


def traer(externa: dict) -> list[str]:
    repo, ruta, commit = externa["repositorio"], externa["ruta"], externa["commit"]
    arbol = json.loads(gh(f"repos/{repo}/git/trees/{commit}?recursive=1"))
    archivos = [
        e["path"] for e in arbol["tree"] if e["type"] == "blob" and e["path"].startswith(ruta + "/")
    ]
    if not any(a.endswith("/SKILL.md") for a in archivos):
        raise SystemExit(f"{repo}:{ruta}@{commit[:7]} no tiene SKILL.md")
    carpeta = DESTINO / externa["nombre"]
    if carpeta.exists():
        shutil.rmtree(carpeta)
    for archivo in archivos:
        contenido = gh(
            f"repos/{repo}/contents/{archivo}?ref={commit}", "-H", "Accept: application/vnd.github.raw"
        )
        destino = carpeta / archivo.removeprefix(ruta + "/")
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(contenido)
    licencia = gh(
        f"repos/{repo}/contents/{LICENCIAS[repo]}?ref={commit}", "-H", "Accept: application/vnd.github.raw"
    )
    (RAIZ / externa["archivo_de_licencia"]).write_bytes(licencia)
    return archivos


def main(nombres: list[str]) -> int:
    registro = json.loads((RAIZ / "externas.json").read_text(encoding="utf-8"))
    for externa in registro["skills"]:
        if nombres and externa["nombre"] not in nombres:
            continue
        archivos = traer(externa)
        print(f"{externa['nombre']}: {len(archivos)} archivos de {externa['repositorio']}@{externa['commit'][:7]}")
    print("Revisa el diff (git diff) y pasa skill-scanner antes de subir.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
