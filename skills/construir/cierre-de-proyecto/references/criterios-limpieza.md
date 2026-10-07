# Criterios de limpieza: qué se queda y qué se va

La pregunta para cada archivo no es «¿se ve viejo?» sino **«¿alguien o algo lo necesita
hoy, o lo va a necesitar para operar el proyecto?»**. Alguien: una persona que sigue la
documentación. Algo: el código, las pruebas, el CI, el despliegue, el contenedor.

## No se borra sin preguntar

Aunque nadie lo cite y parezca viejo:

- **Migraciones de base de datos.** Aunque sean antiguas, son la historia del esquema:
  borrarlas rompe `upgrade` en una base nueva y `downgrade` en una existente.
- **Licencias, avisos de terceros y atribuciones** (`LICENSE`, `NOTICE`, `LICENSE-*`).
- **Archivos de bloqueo de dependencias** (`requirements*.txt` fijados, `poetry.lock`,
  `package-lock.json`, `uv.lock`).
- **Configuración del CI, hooks de git, `.gitattributes`, `.dockerignore`,
  `.editorconfig`**: suelen no citarse porque los lee una herramienta.
- **Scripts de operación** (respaldo, restauración, rotación de credenciales,
  recuperación): se usan poco y justo el día que hacen falta.
- **Datos que usa una prueba** (payloads guardados, fixtures, archivos de ejemplo).
- **Cualquier cosa que el `CLAUDE.md` o el README declaren como oficial o importante.**

## Por tipo de archivo

| Tipo | Se queda si… | Se va si… |
|---|---|---|
| Suite de pruebas automatizada (`tests/`, `pruebas/`, `*_test.*`, `*.spec.*`) | Siempre, mientras pase | Una prueba duplicada exacta, o que prueba código ya borrado (entonces se va con él) |
| Script de prueba manual (`probar_x.py`, `test2.py` fuera de la suite, `demo.py`) | Está documentado como herramienta (p. ej. «verificar credenciales contra la API real») y sigue funcionando | Se escribió para comprobar algo una vez, nadie lo cita, o lo reemplazó una prueba automatizada |
| Código de despliegue o «subir cambios» (`deploy.sh`, `subir.bat`, `desplegar.py`) | Es el camino oficial que dice la documentación | Es una versión anterior, un duplicado, o un atajo manual que salta los controles del camino oficial |
| Copias y versiones (`*_old`, `*_v2`, `copia de`, `*.bak`, `final2`) | Casi nunca: git ya guarda las versiones | Por defecto; confirma antes que la versión «buena» es la que se usa |
| Cuadernos (`*.ipynb`) y borradores (`scratch`, `borrador`, `tmp`) | Son la documentación de un análisis que el proyecto cita | Fueron exploración |
| Archivos generados versionados (`__pycache__`, `*.pyc`, `dist/`, `build/`, `coverage`, logs) | Nunca | Siempre: se sacan de git (`git rm --cached`) y se añaden al `.gitignore` |
| Datos (`*.xlsx`, `*.csv`, `*.sql`, `*.db`, dumps) | Son de ejemplo, **ficticios**, y algo los usa o la documentación los explica | Son reales, son un volcado de producción, o nadie los usa. Datos personales reales: 🔴 siempre |
| Documentación de planes y fases (`PLAN_*.md`, `TODO.md`, notas de sesión) | Sigue siendo la referencia vigente | Describe trabajo ya cumplido: se borra o se mueve a `docs/historico/` (pregunta cuál) |
| Documentación de decisiones (ADR, «por qué se hizo así») | Casi siempre: explica el código actual | Describe un sistema que ya no existe y nada la cita |
| Assets (imágenes, fuentes, plantillas) | Los usa el código, la documentación o el producto | Ningún archivo los referencia |
| Configuración de servicios retirados | Nunca | El servicio ya no se usa (quita también sus variables de entorno y su documentación) |
| Archivos sin seguimiento en la carpeta | — | No se borran: son del usuario. Se listan y él decide si van a git, al `.gitignore` o fuera |

## Cómo confirmar que algo no se usa

1. Busca el nombre del archivo y el nombre del módulo (sin extensión) en todo el
   repositorio, incluida la documentación, el CI y los Dockerfile.
2. Mira su último commit (`git log -1 --format='%cs %s' -- <ruta>`) y el commit que lo
   creó: el mensaje suele decir para qué era.
3. Si es código, busca usos dinámicos (cadenas con su nombre, registros, plugins).
4. Si sigue en duda, va a **Preguntar**, con lo que encontraste.

## Archivos con secretos o datos reales

Borrar el archivo lo quita de la versión actual, no del historial de git. Lo que protege
de verdad es **rotar** el secreto (cambiarlo en el servicio). Reescribir el historial
(`git filter-repo`) exige forzar el push y que todo el equipo vuelva a clonar: propónlo
solo si el repositorio es o será público, y que lo decida el usuario.
