"""Inventario de un repositorio para el cierre de proyecto. Solo lee: no toca nada.

Reúne la evidencia que hace falta para decidir qué sobra, sin opinar todavía:

- Archivos versionados con su tamaño, último commit y **quién los menciona** (otros
  archivos del repositorio que citan su nombre). Un archivo que nadie menciona es
  candidato a sobrar; uno citado en la documentación o el CI casi nunca lo es.
- Nombres con pinta de basura (``*.bak``, ``*_old.py``, ``prueba2.py``, ``scratch``…),
  archivos grandes y archivos de datos (xlsx, csv, sql) que pueden llevar datos reales.
- Archivos sin seguimiento y archivos versionados que el ``.gitignore`` debería excluir.
- Posibles secretos (enmascarados) y restos de depuración (``breakpoint()``,
  ``console.log``, ``TODO``/``FIXME``).
- Con ``--codigo-muerto``: ``ruff`` (imports y variables sin usar) y ``vulture``
  (funciones sin usar), si están disponibles.

USO (desde la raíz del repositorio)
    python inventario.py                 # informe en Markdown por la salida estándar
    python inventario.py --codigo-muerto # además, ruff y vulture
    python inventario.py --json          # lo mismo en JSON, para compararlo después

Solo usa la biblioteca estándar, para que funcione en cualquier proyecto.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath

# Nombres que casi siempre son restos de trabajo, no parte del producto.
PATRONES_BASURA = [
    (re.compile(r"\.(bak|old|orig|tmp|temp|swp|rej)$", re.I), "copia o temporal"),
    (re.compile(r"~$"), "copia de editor"),
    (re.compile(r"(_|-|\b)(old|viejo|antiguo|backup|copia|copy|v\d+|final\d*|nuevo\d*)\.\w+$", re.I), "versión anterior o copia"),
    (re.compile(r"(^|/)(scratch|borrador|tmp|temp|sandbox|playground|pruebas?_?rapid\w*)[^/]*$", re.I), "borrador"),
    (re.compile(r"(^|/)(prueba|test|probar|try|demo|ejemplo)\d+[^/]*$", re.I), "prueba numerada"),
    (re.compile(r"\.ipynb$", re.I), "cuaderno de exploración"),
    (re.compile(r"(^|/)(\.DS_Store|Thumbs\.db|desktop\.ini)$", re.I), "basura del sistema operativo"),
    (re.compile(r"\.(pyc|pyo|class|o|log)$", re.I), "archivo generado"),
    (re.compile(r"(^|/)(__pycache__|\.pytest_cache|\.mypy_cache|\.ruff_cache|node_modules|dist|build|coverage|htmlcov)/", re.I), "carpeta generada"),
]
EXTENSIONES_DATOS = {".xlsx", ".xls", ".csv", ".tsv", ".sql", ".dump", ".db", ".sqlite", ".sqlite3", ".json.gz", ".parquet"}
EXTENSIONES_ARCHIVADO = {".zip", ".rar", ".7z", ".tar", ".gz", ".tgz"}
NOMBRES_SENSIBLES = re.compile(r"(^|/)(\.env(\..+)?|credentials?\.json|.*\.pem|.*\.key|id_rsa.*|.*secret.*)$", re.I)
EJEMPLO_ENV = re.compile(r"\.(example|ejemplo|sample|template|plantilla)$", re.I)

PATRONES_SECRETOS = [
    ("clave privada", re.compile(r"-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----")),
    ("AWS", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b")),
    ("token de Meta", re.compile(r"\bEAA[A-Za-z0-9]{60,}\b")),
    ("OpenAI/Anthropic key", re.compile(r"\bsk-(ant-)?[A-Za-z0-9_\-]{20,}\b")),
    ("asignación de secreto", re.compile(
        r"""(?i)\b(password|passwd|contrase[ñn]a|secret|secreto|token|api_?key)\b\s*[:=]\s*['"]([^'"\s]{8,})['"]""")),
]
PATRONES_DEPURACION = [
    ("breakpoint", re.compile(r"\b(breakpoint\(\)|pdb\.set_trace\(\)|ipdb\.set_trace\(\))")),
    ("console.log", re.compile(r"\bconsole\.(log|debug)\(")),
    ("debugger", re.compile(r"^\s*debugger;?\s*$")),
    # Solo dentro de un comentario: en español «TODO» es una palabra («levantar TODO»).
    ("TODO/FIXME", re.compile(r"(#|//|/\*|<!--|--)\s*(TODO|FIXME|XXX|HACK)\b")),
]
# Los restos de depuración solo se buscan en código: en la documentación se citan a
# propósito (esta misma skill los nombra para explicar qué buscar).
EXTENSIONES_CODIGO = {".py", ".js", ".ts", ".tsx", ".jsx", ".mjs", ".cjs", ".go", ".rs", ".java",
                      ".kt", ".rb", ".php", ".cs", ".sh", ".bash", ".ps1"}
CARPETA_SKILL = Path(__file__).resolve().parent.parent

EXTENSIONES_TEXTO = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".mjs", ".cjs", ".go", ".rs", ".java", ".kt", ".rb", ".php",
    ".cs", ".sh", ".bash", ".ps1", ".bat", ".cmd", ".md", ".rst", ".txt", ".toml", ".yaml", ".yml",
    ".json", ".ini", ".cfg", ".conf", ".env", ".html", ".css", ".scss", ".sql", ".mako", ".j2",
    ".dockerfile", ".gitignore", ".gitattributes", "",
}
# Raíces de nombre demasiado comunes para contar como referencia a un archivo concreto.
RAICES_GENERICAS = {"main", "index", "__init__", "app", "test", "tests", "utils", "config", "readme",
                    "license", "setup", "conftest", "env", "init", "base", "models", "settings"}
LIMITE_GRANDE = 1_000_000

# Archivos que el ecosistema carga por convención: nadie los cita y no por eso sobran.
CONVENCIONES = [
    (re.compile(r"(^|/)(tests?|pruebas|spec|__tests__)/|(^|/)(test_[^/]+|[^/]+_test)\.\w+$|\.(spec|test)\.\w+$", re.I), "prueba automatizada"),
    (re.compile(r"(^|/)(migraciones|migrations|alembic)/", re.I), "migración"),
    (re.compile(r"(^|/)\.(github|gitlab|circleci|githooks|husky|devcontainer)/", re.I), "CI, hooks o plantillas del repositorio"),
    (re.compile(r"(^|/)\.(claude|agents|cursor)/", re.I), "configuración de agentes"),
    (re.compile(r"(^|/)(LICENSE|LICENCE|COPYING|NOTICE)[^/]*$", re.I), "licencia"),
]


def git(*argumentos: str) -> str:
    return subprocess.run(
        ["git", *argumentos], capture_output=True, text=True, encoding="utf-8", errors="replace", check=True
    ).stdout


def es_texto(ruta: Path) -> bool:
    nombre = ruta.name.lower()
    if nombre in {"dockerfile", "makefile", "procfile", "caddyfile"} or nombre.startswith(".env"):
        return True
    return ruta.suffix.lower() in EXTENSIONES_TEXTO


def leer(ruta: Path) -> str | None:
    try:
        if ruta.stat().st_size > 2_000_000:
            return None
        return ruta.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def ultimo_commit_por_archivo() -> dict[str, tuple[str, str]]:
    """Fecha y asunto del último commit de cada archivo, en una sola pasada por el log."""
    resultado: dict[str, tuple[str, str]] = {}
    salida = git("log", "--name-only", "--format=\x01%cs\x02%s", "--no-renames")
    fecha = asunto = ""
    for linea in salida.splitlines():
        if linea.startswith("\x01"):
            fecha, _, asunto = linea[1:].partition("\x02")
        elif linea.strip() and linea not in resultado:
            resultado[linea] = (fecha, asunto)
    return resultado


def _es_de_la_skill(ruta: str) -> bool:
    try:
        Path(ruta).resolve().relative_to(CARPETA_SKILL)
        return True
    except ValueError:
        return False


def enmascarar(valor: str) -> str:
    return valor[:4] + "…" + f"({len(valor)} caracteres)"


def inventariar(codigo_muerto: bool) -> dict:
    versionados = [l for l in git("ls-files", "-z").split("\0") if l]
    sin_seguimiento = [l for l in git("ls-files", "--others", "--exclude-standard").splitlines() if l]
    ignorados_versionados = [l for l in git("ls-files", "-ci", "--exclude-standard").splitlines() if l]
    commits = ultimo_commit_por_archivo()

    contenidos: dict[str, str] = {}
    for ruta in versionados:
        p = Path(ruta)
        if p.is_file() and es_texto(p):
            texto = leer(p)
            if texto is not None:
                contenidos[ruta] = texto

    # Índice de palabras para buscar menciones sin recorrer todo el texto por cada archivo.
    menciones: dict[str, set[str]] = defaultdict(set)
    palabra = re.compile(r"[A-Za-z0-9_\-.]+")
    for ruta, texto in contenidos.items():
        for token in set(palabra.findall(texto)):
            menciones[token.lower()].add(ruta)
            for parte in re.split(r"[./\\-]", token):
                if parte:
                    menciones[parte.lower()].add(ruta)

    contenidos_min = {ruta: texto.lower() for ruta, texto in contenidos.items()}
    archivos = []
    for ruta in versionados:
        p = Path(ruta)
        if not p.is_file():
            continue
        nombre, raiz = p.name.lower(), p.stem.lower()
        citado_por = set(menciones.get(nombre, set()))
        if len(raiz) >= 4 and raiz not in RAICES_GENERICAS:
            citado_por |= menciones.get(raiz, set())
        if not citado_por - {ruta}:
            # Nombres con espacios o paréntesis («Cuentas (1).xlsx») no salen como palabra.
            citado_por = {otro for otro, texto in contenidos_min.items() if nombre in texto}
        citado_por.discard(ruta)
        convencion = next((motivo for patron, motivo in CONVENCIONES if patron.search(ruta)), "")
        senales = [motivo for patron, motivo in PATRONES_BASURA if patron.search(ruta)]
        sufijo = "".join(PurePosixPath(ruta).suffixes[-2:]).lower()
        if p.suffix.lower() in EXTENSIONES_DATOS or sufijo in EXTENSIONES_DATOS:
            senales.append("archivo de datos: revisar si lleva datos reales")
        if p.suffix.lower() in EXTENSIONES_ARCHIVADO:
            senales.append("archivo comprimido")
        if NOMBRES_SENSIBLES.search(ruta) and not EJEMPLO_ENV.search(ruta):
            senales.append("nombre de archivo sensible versionado")
        tamano = p.stat().st_size
        if tamano > LIMITE_GRANDE:
            senales.append(f"grande ({tamano // 1024} KB)")
        fecha, asunto = commits.get(ruta, ("", ""))
        archivos.append({
            "ruta": ruta, "tamano": tamano, "ultimo_commit": fecha, "asunto": asunto,
            "citado_por": sorted(citado_por), "senales": senales, "convencion": convencion,
        })

    secretos, depuracion = [], defaultdict(list)
    for ruta, texto in contenidos.items():
        for n, linea in enumerate(texto.splitlines(), 1):
            for nombre, patron in PATRONES_SECRETOS:
                m = patron.search(linea)
                if m:
                    valor = m.group(m.lastindex or 0)
                    # Valores de ejemplo y referencias a variables no son secretos.
                    if re.search(r"(?i)(xxx|example|ejemplo|placeholder|changeme|<|\$\{|os\.environ|getenv)", linea):
                        continue
                    en_pruebas = any(patron.search(ruta) for patron, motivo in CONVENCIONES[:1])
                    secretos.append({"ruta": ruta, "linea": n, "tipo": nombre, "valor": enmascarar(valor),
                                     "en_pruebas": en_pruebas})
            if Path(ruta).suffix.lower() not in EXTENSIONES_CODIGO or _es_de_la_skill(ruta):
                continue
            for nombre, patron in PATRONES_DEPURACION:
                if patron.search(linea):
                    depuracion[nombre].append(f"{ruta}:{n}")

    resultado = {
        "total_versionados": len(archivos),
        "archivos": archivos,
        "sin_seguimiento": sin_seguimiento,
        "ignorados_pero_versionados": ignorados_versionados,
        "secretos": secretos,
        "depuracion": dict(depuracion),
    }
    if codigo_muerto:
        resultado["codigo_muerto"] = analizar_codigo_muerto()
    return resultado


def ejecutar_herramienta(nombre: str, argumentos: list[str]) -> str:
    """Corre ruff o vulture si están: como ejecutable, con ``python -m`` o con ``uvx``."""
    candidatos = []
    if shutil.which(nombre):
        candidatos.append([nombre, *argumentos])
    candidatos.append([sys.executable, "-m", nombre, *argumentos])
    if shutil.which("uvx"):
        candidatos.append(["uvx", nombre, *argumentos])
    for orden in candidatos:
        try:
            r = subprocess.run(orden, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        except (OSError, subprocess.TimeoutExpired):
            continue
        if "No module named" in r.stderr:
            continue
        return (r.stdout + r.stderr).strip() or "(sin hallazgos)"
    return f"{nombre} no está disponible. Instálalo en una carpeta temporal, no en el entorno del proyecto: " \
           f"python -m pip install --target <carpeta_temporal> {nombre}"


def analizar_codigo_muerto() -> dict[str, str]:
    if not any(Path(r).suffix == ".py" for r in git("ls-files").splitlines()):
        return {"nota": "No hay Python: usa la herramienta equivalente del lenguaje (ts-prune, knip, deadcode…)."}
    return {
        "ruff (F401 imports, F811 redefiniciones, F841 variables sin usar)": ejecutar_herramienta(
            "ruff", ["check", "--select", "F401,F811,F841", "--output-format", "concise", "--no-cache", "."]),
        # Sobre las pruebas solo da ruido (las fixtures de pytest se piden por su efecto) y
        # sobre las migraciones también (upgrade/downgrade los llama Alembic). Al 60 % sobre
        # el resto aparecen funciones y clases sin usar; cada una se confirma buscándola.
        "vulture (confianza >= 60 %, sin pruebas ni migraciones)": ejecutar_herramienta(
            "vulture", [".", "--min-confidence", "60", "--exclude",
                        ".venv,venv,node_modules,.git,tests,pruebas,test_*.py,*_test.py,"
                        "migraciones,migrations,alembic"]),
    }


def a_markdown(d: dict) -> str:
    l = [f"# Inventario del repositorio", "", f"Archivos versionados: **{d['total_versionados']}**", ""]

    sin_menciones = [a for a in d["archivos"] if not a["citado_por"] and not a["convencion"]]
    por_convencion = defaultdict(int)
    for a in d["archivos"]:
        if not a["citado_por"] and a["convencion"]:
            por_convencion[a["convencion"]] += 1
    con_senales = [a for a in d["archivos"] if a["senales"]]

    l += ["## Archivos con señales de sobrar", "",
          "| Archivo | Señales | Lo citan | Último commit |", "|---|---|---|---|"]
    for a in con_senales:
        citan = ", ".join(a["citado_por"][:3]) + (" …" if len(a["citado_por"]) > 3 else "") or "nadie"
        l.append(f"| `{a['ruta']}` | {'; '.join(a['senales'])} | {citan} | {a['ultimo_commit']} {a['asunto'][:50]} |")
    if not con_senales:
        l.append("| (ninguno) | | | |")

    l += ["", "## Archivos que ningún otro archivo menciona", "",
          "No significa que sobren: un punto de entrada (main, Dockerfile, CI) o un archivo cargado por "
          "convención (conftest.py, migraciones) tampoco suele citarse. Es la lista por revisar a mano.", "",
          "| Archivo | Tamaño | Último commit |", "|---|---|---|"]
    for a in sin_menciones:
        l.append(f"| `{a['ruta']}` | {a['tamano']} B | {a['ultimo_commit']} {a['asunto'][:60]} |")
    if not sin_menciones:
        l.append("| (ninguno) | | |")
    if por_convencion:
        l += ["", "Sin menciones pero cargados por convención (no se listan): " + ", ".join(
            f"{n} de tipo {tipo}" for tipo, n in sorted(por_convencion.items())) + "."]

    l += ["", "## Sin seguimiento (no están en git)", ""]
    l += [f"- `{r}`" for r in d["sin_seguimiento"]] or ["- (ninguno)"]
    l += ["", "## Versionados aunque el .gitignore los excluye", ""]
    l += [f"- `{r}`" for r in d["ignorados_pero_versionados"]] or ["- (ninguno)"]

    l += ["", "## Posibles secretos (valores enmascarados)", ""]
    l += [f"- `{s['ruta']}:{s['linea']}` — {s['tipo']}: {s['valor']}"
          + (" (en pruebas: probablemente ficticio, confirmar)" if s["en_pruebas"] else "")
          for s in d["secretos"]] or ["- (ninguno)"]

    l += ["", "## Restos de depuración", ""]
    if d["depuracion"]:
        for nombre, sitios in d["depuracion"].items():
            muestra = ", ".join(sitios[:8]) + (f" … (+{len(sitios) - 8})" if len(sitios) > 8 else "")
            l.append(f"- **{nombre}** ({len(sitios)}): {muestra}")
    else:
        l.append("- (ninguno)")

    if "codigo_muerto" in d:
        l += ["", "## Código muerto (herramientas)", ""]
        for nombre, salida in d["codigo_muerto"].items():
            l += [f"### {nombre}", "", "```", salida[:6000], "```", ""]

    l += ["", "## Todos los archivos", "", "| Archivo | Tamaño | Lo citan | Tipo | Último commit |",
          "|---|---|---|---|---|"]
    for a in d["archivos"]:
        l.append(f"| `{a['ruta']}` | {a['tamano']} | {len(a['citado_por'])} | {a['convencion']} | {a['ultimo_commit']} |")
    return "\n".join(l)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    analizador = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizador.add_argument("--json", action="store_true", help="salida en JSON")
    analizador.add_argument("--codigo-muerto", action="store_true", help="corre ruff y vulture si están")
    args = analizador.parse_args()
    try:
        git("rev-parse", "--show-toplevel")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Hay que ejecutarlo dentro de un repositorio git.", file=sys.stderr)
        return 1
    datos = inventariar(args.codigo_muerto)
    print(json.dumps(datos, ensure_ascii=False, indent=2) if args.json else a_markdown(datos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
