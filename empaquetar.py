"""Empaqueta el plugin en dist/luptecx-<versión>.plugin, listo para instalar.

Uso:  python empaquetar.py
"""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
PLUGIN = RAIZ / "plugins" / "luptecx"  # el plugin general; los de tipo (extras/) van aparte
EXCLUIR = {"dist", "__pycache__", ".ruff_cache"}


def main() -> None:
    manifiesto = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    destino = RAIZ / "dist" / f"{manifiesto['name']}-{manifiesto['version']}.plugin"
    destino.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as paquete:
        for archivo in sorted(PLUGIN.rglob("*")):
            relativo = archivo.relative_to(PLUGIN)
            if archivo.is_dir() or set(relativo.parts) & EXCLUIR:
                continue
            paquete.write(archivo, relativo.as_posix())
    print(f"Listo: {destino}")


if __name__ == "__main__":
    main()
