# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Revisa el encabezado (frontmatter) de cada SKILL.md del repositorio.

`claude plugin validate` no lo hace: un encabezado que no es YAML válido deja la skill sin
cargar, y un `#` o un `: ` dentro de la descripción la corta o la rompe sin avisar (pasó el
21/10/2026 con `revisar-cambios` y `luptecx-corregir-error`). Si la descripción lleva esos
caracteres, va entre comillas dobles.

Uso, desde la raíz del repositorio (revisa todos sus plugins, también los de extras/):

    uv run --script plugins/luptecx/herramientas/revisar_encabezados.py
"""

import re
import sys
from pathlib import Path

import yaml

RAIZ = Path.cwd()


def revisar(archivo: Path) -> list[str]:
    texto = archivo.read_text(encoding="utf-8")
    partes = texto.split("---", 2)
    if len(partes) < 3 or partes[0].strip():
        return ["no empieza con un encabezado entre ---"]
    try:
        datos = yaml.safe_load(partes[1]) or {}
    except yaml.YAMLError as error:
        return [f"el encabezado no es YAML válido: {str(error).splitlines()[0]}"]
    problemas = []
    if datos.get("name") != archivo.parent.name:
        problemas.append(f"name ({datos.get('name')!r}) no coincide con la carpeta")
    descripcion = datos.get("description")
    if not isinstance(descripcion, str) or not descripcion.strip():
        return [*problemas, "falta la descripción"]
    cruda = re.search(r"^description:\s*(.*)$", partes[1], re.M)
    if cruda:
        texto_crudo = cruda.group(1).strip().strip("\"'")
        if texto_crudo and len(descripcion) < len(texto_crudo) - 2:
            problemas.append(f"la descripción quedó cortada en «…{descripcion[-40:]}»")
    return problemas


def main() -> int:
    archivos = sorted(RAIZ.glob("**/SKILL.md"))
    fallas = 0
    for archivo in archivos:
        for problema in revisar(archivo):
            fallas += 1
            print(f"✗ {archivo.relative_to(RAIZ).as_posix()}: {problema}")
    print(f"{len(archivos)} skills revisadas, {fallas} problemas")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
