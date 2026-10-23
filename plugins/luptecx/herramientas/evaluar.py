"""Corre las evaluaciones del plugin (evals/) con el plugin cargado de verdad.

`claude plugin eval .` arranca cada caso en una sesión aislada, sin los plugins del PC. Ahí
las dependencias de Trail of Bits no están instaladas, el plugin no carga («Dependency …
is not installed») y cada caso mide al modelo solo: así pasó hasta el 23/10/2026. Esto
evalúa una copia temporal del plugin sin `dependencies`, que son plugins aparte y ningún
caso los evalúa, y deja los resultados en evals/results/ (ignorada por git).

Uso, desde plugins/luptecx (los argumentos van tal cual a `claude plugin eval`):
    python herramientas/evaluar.py                               # 3 corridas por caso, con y sin plugin
    python herramientas/evaluar.py --runs 1 --ablation none      # una pasada rápida
    python herramientas/evaluar.py --case comunicacion-caida-sin-jerga
"""

import json
import shutil
import subprocess
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def main() -> int:
    # En Windows, claude es un .cmd que subprocess no encuentra solo por el nombre.
    claude = shutil.which("claude")
    if not claude:
        print("No encuentro el comando claude en el PATH.", file=sys.stderr)
        return 1
    marca = datetime.now(UTC).strftime("%Y-%m-%dT%H-%M-%SZ")
    resultados = RAIZ / "evals" / "results" / marca
    with tempfile.TemporaryDirectory(prefix="luptecx-eval-") as temporal:
        copia = Path(temporal) / "luptecx"
        shutil.copytree(
            RAIZ, copia, ignore=shutil.ignore_patterns("results", "__pycache__")
        )
        manifiesto = copia / ".claude-plugin" / "plugin.json"
        datos = json.loads(manifiesto.read_text(encoding="utf-8"))
        datos.pop("dependencies", None)
        manifiesto.write_text(
            json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        comando = [
            claude,
            "plugin",
            "eval",
            str(copia),
            "--no-publish",
            "--trust-plugin",
            "--output-dir",
            str(resultados),
            "--report",
            str(resultados / "report.html"),
            *sys.argv[1:],
        ]
        return subprocess.run(comando, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
