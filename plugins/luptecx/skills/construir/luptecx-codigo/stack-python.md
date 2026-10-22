# Stack: Python

Para los proyectos cuyo `CLAUDE.md` declara «Stack: Python». Se suma a lo común de
`SKILL.md`; lo del proyecto gana si deja escrita la decisión.

## Lo que se usa por defecto

| Para | Se usa | En vez de |
|---|---|---|
| Versión | Python 3.11 o superior (`requires-python` en `pyproject.toml`) | — |
| Dependencias y entorno | **uv**: `uv add`, `uv sync`, `uv run`; `uv.lock` versionado | pip, `requirements.txt`, activar el entorno a mano |
| Lint y formato | **ruff** (`ruff check` y `ruff format`) | flake8, black, isort |
| Tipos | **ty** (`ty check`, 🔒 candado de push y CI) | mypy, pyright |
| Pruebas | **pytest** | unittest |
| API web | **FastAPI**, siguiendo la skill oficial `fastapi` | — |
| Base de datos | SQLAlchemy con migraciones de **Alembic**; PostgreSQL en producción | Crear tablas a mano en producción |
| Configuración | `pydantic-settings`, leída de variables de entorno | Constantes con valores de producción |
| Cifras del reporte mensual | `registrar_evento()` de `app/metricas.py` (plantilla de procesos), con los eventos de «Qué se mide» de la especificación | Contar a mano en la hoja del cliente, o un servicio externo de analítica |
| Despliegue | Docker con Caddy delante | — |

Decisión del 15/10/2026 para proyectos **nuevos**; los que ya existen siguen con lo que
tienen hasta que se migren a propósito. Herramientas de Astral (uv, ruff, ty), como las
recomiendan la skill oficial de FastAPI y `modern-python` de Trail of Bits.

**Con la skill oficial `fastapi`** (instalada por usuario con
`npx skills add fastapi/fastapi -s fastapi -g -a claude-code --copy`): se siguen sus
prácticas de FastAPI (`Annotated`, tipos de retorno, `def` salvo que todo sea async, un
router con su prefijo). Donde choque con esta tabla o con lo común de `SKILL.md`, gana
LUPTECX: el código va en español, una dependencia nueva se justifica (también Asyncer) y la
base de datos es SQLAlchemy con Alembic aunque la skill prefiera SQLModel, salvo que el
proyecto deje escrita otra decisión.

Las herramientas de desarrollo van en grupos de `pyproject.toml`
(`[dependency-groups]`: `dev`, `test`), no como dependencias del proyecto. Todo comando se
corre con `uv run`, que usa el entorno del proyecto sin activarlo.

## Estructura

```
app/            código de la aplicación (un paquete)
pruebas/        suite de pytest
herramientas/   scripts de operación: desplegar, configurar, inspeccionar
migraciones/    Alembic (si hay base de datos)
pyproject.toml  dependencias, ruff, ty y pytest en un solo archivo
```

## Reglas del stack

- **Fechas con zona.** `datetime.now(ZoneInfo("America/Bogota"))` o `datetime.now(UTC)`,
  nunca `datetime.now()` ni `date.today()` sueltos. 🔒 regla `DTZ` de ruff.
- **ruff con reglas amplias**: además de las básicas, `DTZ` (fechas), `S` (seguridad),
  `B` (errores comunes) y `UP` (sintaxis actual). Una excepción a una regla va en la línea,
  con el porqué (`# noqa: S603  el comando es fijo`). 🔒 candado de commit y CI.
- **Un solo worker de Uvicorn** si el proyecto tiene un planificador de tareas o candados
  en memoria: con varios, cada tarea corre N veces y los candados no protegen. 👁
- Los `.sh` llevan finales de línea LF. 🔒 `.gitattributes`
- Las pruebas que dependen del motor de base de datos corren también contra PostgreSQL en
  el CI. 🔒 CI
