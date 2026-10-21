"""Empaqueta el plugin en dist/luptecx-<versión>.plugin, listo para instalar.

Uso:  python empaquetar.py
"""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
EXCLUIR = {".git", "dist", "__pycache__", ".github", ".ruff_cache", "extras"}  # extras: plugins de tipo, van aparte
FUERA_DEL_PAQUETE = {"empaquetar.py"}


def main() -> None:
    manifiesto = json.loads((RAIZ / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    destino = RAIZ / "dist" / f"{manifiesto['name']}-{manifiesto['version']}.plugin"
    destino.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as paquete:
        for archivo in sorted(RAIZ.rglob("*")):
            relativo = archivo.relative_to(RAIZ)
            if archivo.is_dir() or set(relativo.parts) & EXCLUIR or relativo.name in FUERA_DEL_PAQUETE:
                continue
            paquete.write(archivo, relativo.as_posix())
    print(f"Listo: {destino}")


if __name__ == "__main__":
    main()
