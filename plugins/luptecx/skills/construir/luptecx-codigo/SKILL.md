---
name: luptecx-codigo
description: Convenciones de código y de trabajo de LUPTECX, la fuente única para todos los proyectos. Úsala al escribir, revisar o reorganizar código de un proyecto de LUPTECX; al crear archivos, módulos o pruebas nuevos; al decidir cómo nombrar algo o dónde ponerlo; o cuando `revisar-cambios` necesite los estándares de la empresa.
---

# Convenciones de LUPTECX

Cada proyecto de LUPTECX es distinto. Lo que sigue vale para **todos**; lo propio de un
stack o de un tipo de proyecto está en referencias aparte, y se lee solo la que toca.

El `CLAUDE.md` de cada proyecto agrega lo suyo (arquitectura, invariantes del negocio,
comandos, decisiones del dueño) y **puede desviarse** de una regla de aquí solo si deja
escrita la decisión, con su fecha y el porqué. Lo escrito en el proyecto gana.

Junto a cada regla se dice quién la vigila: 🔒 una máquina (hook, CI, prueba) o 👁 la
revisión (`luptecx:revisar-cambios`). Lo que puede vigilar una máquina no se deja a criterio.

## Qué referencias leer

El `CLAUDE.md` del proyecto declara, en su bloque «Reglas de LUPTECX», su **stack** y su
**tipo**. Lee las referencias que correspondan antes de escribir o revisar código:

| El proyecto declara | Lee |
|---|---|
| Stack: Python | [stack-python.md](stack-python.md) y, si usa FastAPI, la skill oficial `fastapi` |
| Automatización con n8n | La skill `n8n-workflow-patterns` de `czlonkowski/n8n-skills`, si está instalada |
| Otro stack | Nada más: se decide con el usuario y queda en `docs/decisiones/` |

Lo propio de un **tipo** de proyecto no vive aquí. Si se repite en varios proyectos, va en
un plugin de tipo aparte (por ejemplo, `luptecx-bot-whatsapp`), que el proyecto activa en
su `.claude/settings.json` y cuyas reglas se suman a estas. Si no hay plugin para el tipo,
lo propio del proyecto queda en su especificación y en `docs/decisiones/`.

Si el `CLAUDE.md` no lo declara, pregúntalo y agrégalo.

## Idioma 👁

Todo en español: código, nombres de variables, funciones, clases y **archivos**,
comentarios, mensajes de error, documentación y mensajes de commit. Excepciones:
tecnicismos sin traducción natural (API, webhook, script, commit, token) y nombres de
librerías. Las palabras del negocio salen de `docs/GLOSARIO.md`.

## Cómo se trabaja

Sin pull requests (decisión del 04/10/2026): commit y push normal a `main`. Lo que protege
producción son tres candados que se cumplen solos:

| Regla | Quién la vigila |
|---|---|
| El mensaje de commit empieza por un tipo: `inicio`, `funcionalidad`, `correccion`, `pruebas`, `documentacion`, `refactorizacion`, seguido de `: ` | 🔒 candado de commit y CI |
| La suite pasa antes de subir | 🔒 candado de push y CI en cada push a `main` |
| A producción solo llega lo que se despliega con `herramientas/desplegar.py` | 🔒 el script (franja prohibida, CI en verde, respaldo, etiqueta) |

- Los candados viven en `.pre-commit-config.yaml` y se activan una vez por clon con
  `prek install` (los proyectos anteriores a la plantilla de procesos usan `.githooks/` y
  `git config core.hooksPath .githooks`). El CI los repite, así que no activarlos no los
  salta: solo hace que el error aparezca más tarde.
- Antes de empezar, `git pull --rebase` (o `git config pull.rebase true` una vez): dos
  personas trabajan en la misma rama.
- **Nunca** `git push --force` a `main` ni `--no-verify`. Si un hook falla, se arregla la
  causa. 🔒 el hook del plugin se lo impide a Claude (también `reset --hard`, `clean -f`,
  `branch -D`, `checkout .` y `restore .`).
- Ramas solo para trabajo largo o experimental (`funcionalidad/<que-hace>`), que se
  integran a `main` con merge local y push.
- Los workflows de GitHub pasan por actionlint y zizmor (🔒 candado de commit y CI), y
  las acciones van fijadas por hash.
- Commits pequeños, un propósito cada uno, con un título que diga qué cambió. Una
  reestructuración va en su propio commit `refactorizacion:`, sin cambiar comportamiento.
- Cada versión desplegada lleva su etiqueta (`v1.4.0`) y su entrada en `CHANGELOG.md`.
- Subir no es desplegar: al cliente solo llega lo que Camilo despliega.

La **definición de terminado** está en `luptecx:verificar-antes-de-terminar`.

## Documentos del repositorio 👁

Todo proyecto tiene, sin importar su stack:

```
CLAUDE.md                 corto: «Reglas de LUPTECX» (con stack y tipo) y lo propio del proyecto
CHANGELOG.md              qué cambió en cada versión, para quien lo lea dentro de un año
docs/ESPECIFICACION.md    qué hace y para quién (planificar-desarrollo)
docs/ARQUITECTURA.md      cómo está hecho y el plan de piezas
docs/PUESTA_EN_PRODUCCION.md  si se despliega, con docs/RECUPERACION.md
docs/GLOSARIO.md          palabras del negocio (modelar-dominio)
docs/decisiones/          decisiones difíciles de revertir, con fecha
.pre-commit-config.yaml   los candados (prek)
.secrets.baseline         lo que detect-secrets ya revisó
.env.ejemplo              cada variable de configuración, sin valores reales
```

- El `CLAUDE.md` apunta a estos documentos en vez de copiarlos, y no pasa de ~100 líneas:
  lo que se puede ver en el código, en `--help` o en los documentos no se repite.
- Configuración por variables de entorno, con `.env.ejemplo` versionado y `.env` nunca.
- Scripts de prueba manual desechables no se quedan en el repositorio: o se vuelven una
  prueba de la suite o se borran.

## Pruebas

El cómo está en `luptecx:probar-primero`. Las reglas de empresa:

- Nombres en español que dicen el comportamiento: `test_un_lote_sin_valor_se_rechaza`. 👁
- **Ninguna prueba sale a la red**: cada integración externa (mensajería, una hoja de
  cálculo, un modelo de IA, una API del cliente) va con un doble. 👁
- **Ninguna prueba depende de archivos que solo existen en un PC** (`.env`, credenciales,
  el entorno virtual, una hoja real): si pasa en el PC y falla en el CI, la prueba está mal
  escrita. 🔒 CI
- Si el proyecto tiene base de datos y cambió un modelo, hay migración, y una prueba lo
  vigila. 🔒

## Fechas 👁

Los clientes están en Colombia. **Fechas de negocio en `America/Bogota`, marcas de
auditoría en UTC.** Nunca una fecha u hora sin zona: el servidor corre en UTC y después de
las 7 p. m. en Colombia ya es el día siguiente. Cada stack dice cómo lo vigila una máquina.

## Datos y secretos

- **Ningún secreto en el repositorio**, en los logs ni en los mensajes. Los secretos viven
  en Bitwarden; el repositorio solo dice *dónde* están. 👁 · 🔒 detect-secrets en el
  candado de commit y en el CI. Un falso positivo se marca en la línea con
  `# pragma: allowlist secret` y el porqué.
- **Ningún dato real de clientes en el repositorio**, ni siquiera anonimizado. 👁
- **Nunca se apuntan herramientas ni pruebas a datos de producción** de un cliente: siempre
  a una copia y a cuentas o números de prueba. 👁
- Datos personales (teléfonos, cédulas, nombres): solo lo necesario, nunca en logs, y con
  el tratamiento que diga la especificación (Ley 1581 de 2012). 👁
- `.env`, credenciales y respaldos en `.gitignore`. 🔒 `.gitignore` de la plantilla
- Una dependencia nueva se justifica: ¿la librería estándar o una que ya está no alcanza?
  👁 · 🔒 pip-audit en el CI (stack Python) y Dependabot.
