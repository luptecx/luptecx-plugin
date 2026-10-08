---
name: luptecx-codigo
description: Convenciones de código y de trabajo de LUPTECX, la fuente única para todos los proyectos. Úsala al escribir, revisar o reorganizar código de un proyecto de LUPTECX; al crear archivos, módulos o pruebas nuevos; al decidir cómo nombrar algo o dónde ponerlo; al tocar un bot de WhatsApp (webhook, plantillas de Meta, fechas, deduplicación); o cuando `revisar-cambios` necesite los estándares de la empresa.
---

# Convenciones de LUPTECX

Valen para todos los proyectos. El `CLAUDE.md` de cada proyecto agrega lo suyo
(arquitectura, invariantes del negocio, comandos, decisiones del dueño) y **puede
desviarse** de una regla de aquí solo si deja escrita la decisión, con su fecha y el
porqué. Lo escrito en el proyecto gana.

Junto a cada regla se dice quién la vigila: 🔒 una máquina (hook, CI, prueba) o 👁 la
revisión (`luptecx:revisar-cambios`). Lo que puede vigilar una máquina no se deja a criterio.

## Stack por defecto

Python, FastAPI, SQLAlchemy con migraciones de Alembic, pytest, Docker con Caddy, y
PostgreSQL en producción (SQLite en desarrollo y pruebas). Un proyecto nuevo nace de
`luptecx/luptecx-plantilla`. Otro stack se puede usar, pero queda como decisión en
`docs/decisiones/`.

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
| El mensaje de commit empieza por un tipo: `inicio`, `funcionalidad`, `correccion`, `pruebas`, `documentacion`, `refactorizacion`, seguido de `: ` | 🔒 hook `commit-msg` |
| La suite pasa antes de subir | 🔒 hook `pre-push` y CI en cada push a `main` |
| A producción solo llega lo que se despliega con `herramientas/desplegar.py` | 🔒 el script (franja prohibida, pruebas, respaldo) |

- Los hooks viven en `.githooks/` y se activan una vez por clon:
  `git config core.hooksPath .githooks`.
- Antes de empezar, `git pull --rebase` (o `git config pull.rebase true` una vez): dos
  personas trabajan en la misma rama.
- **Nunca** `git push --force` a `main` ni `--no-verify`. Si un hook falla, se arregla la
  causa.
- Ramas solo para trabajo largo o experimental (`funcionalidad/<que-hace>`), que se
  integran a `main` con merge local y push.
- Commits pequeños, un propósito cada uno. Una reestructuración va en su propio commit
  `refactorizacion:`, sin cambiar comportamiento.
- Cada versión desplegada lleva su etiqueta (`v1.4.0`) y su entrada en `CHANGELOG.md`.
- Subir no es desplegar: al cliente solo llega lo que Camilo despliega.

La **definición de terminado** está en `luptecx:verificar-antes-de-terminar`.

## Estructura del repositorio 👁

```
app/            código de la aplicación
pruebas/        suite automatizada (pytest)
herramientas/   scripts de operación: desplegar, configurar, inspeccionar
migraciones/    Alembic
docs/           ESPECIFICACION, ARQUITECTURA, PUESTA_EN_PRODUCCION, GLOSARIO, decisiones/
.githooks/      commit-msg y pre-push
```

- `CLAUDE.md` en la raíz, corto: el bloque «Reglas de LUPTECX» y lo propio del proyecto.
- Configuración por variables de entorno, con `.env.ejemplo` versionado y `.env` nunca.
- Scripts de prueba manual desechables no se quedan en el repositorio: o se vuelven una
  prueba de la suite o se borran.

## Pruebas

El cómo está en `luptecx:probar-primero`. Las reglas de empresa:

- Viven en `pruebas/`, con nombres en español que dicen el comportamiento:
  `test_un_lote_sin_valor_se_rechaza`. 👁
- **Ninguna prueba sale a la red** (WhatsApp, Google, Meta van con dobles). 👁
- **Ninguna prueba depende de archivos que solo existen en un PC** (`.env`,
  `credentials.json`, `.venv`, una hoja real): si pasa en el PC y falla en el CI, la prueba
  está mal escrita. 🔒 CI
- Si cambió un modelo, hay migración. 🔒 `pruebas/test_migraciones.py`
- La suite también corre contra PostgreSQL cuando lo que se prueba depende del motor.

## Datos y secretos

- **Ningún secreto en el repositorio**, en los logs ni en los mensajes. Los secretos viven
  en Bitwarden; el repositorio solo dice *dónde* están. 👁 · 🔒 pendiente: escáner de
  secretos en el pre-push y el CI.
- **Ningún dato real de clientes en el repositorio**, ni siquiera anonimizado. 👁
- **Nunca se apuntan herramientas ni pruebas a datos de producción** de un cliente ni a su
  número real de WhatsApp: siempre a una copia y al número de prueba. 👁
- Datos personales (teléfonos, cédulas, nombres): solo lo necesario, nunca en logs, y con
  el tratamiento que diga la especificación (Ley 1581 de 2012). 👁
- `.env`, credenciales y `respaldos/` en `.gitignore`. 🔒 `.gitignore` de la plantilla

## Detalles de plataforma

- Los `.sh` llevan finales de línea LF. 🔒 `.gitattributes`
- **Un solo worker de Uvicorn**: el planificador de tareas y los límites por usuario viven
  en memoria. Con varios workers cada tarea corre N veces. 👁

## Si el proyecto es un bot de WhatsApp

### Arquitectura 👁

```
WhatsApp → whatsapp_router → deduplica por message_id → conversacion (lógica del negocio)
        → servicios del proyecto → mensajes (redacta) → whatsapp_service (envía)
```

- `whatsapp_router` solo autentica, traduce el payload, deduplica y descarta lo que llega
  tarde. Responde 200 de inmediato y atiende en segundo plano.
- `conversacion` es el **único** módulo que conoce a la vez base de datos, servicios del
  negocio y WhatsApp. El estado de cada conversación se guarda en la base de datos, nunca
  en memoria.
- `mensajes` es el **único** que redacta textos para el usuario. La conversación decide qué
  mensaje toca; no redacta.
- El envío está tras `ProveedorWhatsApp`: un proveedor real (Cloud API de Meta) y uno de
  pruebas que acumula. Nadie lo esquiva.
- Cada excepción lleva el detalle técnico (para el log) y un `mensaje_usuario` (para
  WhatsApp).

### Invariantes de todo bot

1. **Fechas de negocio en `America/Bogota`, marcas de auditoría en UTC.** Nunca
   `datetime.now()` sin zona: el servidor corre en UTC y después de las 7 p. m. en
   Colombia ya es el día siguiente. 👁 · 🔒 pendiente: regla `DTZ` de `ruff`.
2. **Deduplicación por `message_id` con restricción única en la base de datos.** Meta
   reintenta los webhooks; sin esto una acción se ejecuta dos veces. Si la acción tiene
   confirmación, el estado se consume **antes** de ejecutar, para que una segunda
   confirmación no duplique. 👁
3. **Todo mensaje proactivo va por `enviar_plantilla`, nunca por `enviar_texto`.** Meta
   rechaza el texto libre pasadas 24 h desde el último mensaje del usuario (error 131047).
   Los parámetros de una plantilla no llevan saltos de línea. Una plantilla aprobada no se
   edita: un texto nuevo es una plantilla nueva. Nunca se pone en el `.env` el nombre de una
   plantilla que Meta no haya aprobado (error 132001: ese día no sale ningún aviso). 👁
4. **El webhook se autentica con la firma de Meta y con nada más.** Solo se acepta sin
   firma cuando `META_APP_SECRET` está vacío, y la configuración de producción no deja
   arrancar así. No se agrega una segunda vía de autenticación: la que sobra acaba siendo
   la que está vacía. 👁
5. **Desde el 01/10/2026 Meta cobra cada mensaje de servicio:** lo que se pueda decir en
   una sola burbuja (texto con sus botones) va en una. 👁

### Producción

- Antes de publicar, `web/privacidad.html` describe lo que hace este bot (lo exige Meta).
- Monitoreo: endpoint `/salud` y aviso a Healthchecks de las tareas programadas.
