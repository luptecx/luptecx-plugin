# Notion: bases, plantillas y cómo escribir en ellas

Se lee en el paso 2 de `luptecx-nuevo-proyecto`, en el paso 5 de
`luptecx-reportar-error` y en `luptecx-diagnostico`.

## Bases

Los identificadores (base, origen de datos y el de Camilo como persona) están en
la página «Mapa de Notion para Claude» de Recursos (búscala por ese nombre con el conector de Notion). No se copian al plugin: su repositorio es público.

| Base | Campos que se usan |
|---|---|
| Proyectos | Project Name, Project Description, Fase, Status, Priority, Deadline, Clients, Portafolio, Repositorio |
| Tasks | In, Tipo, Severidad, Priority, Project, Assignee, Due Date, completed, Enlace GitHub |
| Clientes (CRM) | Empresa, Estado, Proyectos, Ultimo Contacto, Reuniones |
| Reuniones | Todas Las reuniones (título), Clients, Project, Meeting Date, Tipo, Estado |
| Portafolio | El producto vendido |

## Plantillas

El contenido de las plantillas vive **en Notion**, no en el plugin: se editan allí y las
usan igual una persona que crea la página a mano y una skill.

| Base | Plantilla | La skill escribe debajo de |
|---|---|---|
| Proyectos | **Proyecto LUPTECX** | «Accesos del cliente» |
| Tasks | **Error** | «Mensaje original» |
| Reuniones | **Diagnóstico** | «Preparación», «Lo que dijo el cliente», «Datos para la propuesta», «¿Encaja?» y «Siguiente paso» |

El identificador se busca **por nombre** cada vez (no se copia aquí):
`GET /v1/data_sources/<data_source_id>/templates`. Si la plantilla no está, para y pídele
al usuario que la cree; no la reemplaces escribiendo el contenido tú.

## Crear una página desde una plantilla

Con la API de Notion (versión `2025-09-03` o posterior; con Composio, `proxy_execute`):

1. `POST /v1/pages` con `parent: {"type": "data_source_id", "data_source_id": …}`,
   `template: {"type": "template_id", "template_id": …, "timezone": "America/Bogota"}` y
   las propiedades. **Sin `children`**: con plantilla, la API no los acepta. Las
   propiedades que mandas ganan a las de la plantilla.
2. La plantilla se aplica **en segundo plano** (en la prueba del 15/10/2026, en medio
   segundo). Lee los hijos de la página (`GET /v1/blocks/<page_id>/children`) cada 3
   segundos, hasta 60 segundos, hasta que aparezca el título esperado de la tabla de
   arriba.
3. Escribe debajo de ese título:
   `PATCH /v1/blocks/<page_id>/children` con `children` y
   `position: {"type": "after_block", "after_block": {"id": <id del título>}}`
   (el parámetro `after` está obsoleto).

Si en 60 segundos la plantilla no aparece, **no la vuelvas a aplicar** (duplicaría lo que
alcanzó a copiar): dale al usuario el enlace de la página y lo que faltaba escribir.

## Aplicar una plantilla a una página que ya existe

Pasa con las reuniones, que las crea la sincronización con el calendario:
`PATCH /v1/pages/<page_id>` con `template: {"type": "template_id", "template_id": …,
"timezone": "America/Bogota"}`. El contenido de la plantilla se **suma** al que ya tiene la
página. **Nunca** se manda `erase_content`: borra todo lo que hay en la página y no se puede
deshacer. Después, igual que arriba: esperar los títulos y escribir debajo.

Una lista de pendientes va como bloques `to_do`. Un subtítulo dentro de una sección va como
párrafo en negrilla: los títulos de la plantilla ya son `heading_3`, el nivel más bajo.

Si una plantilla no tiene el título que la skill busca (por ejemplo, porque se pegó como
texto o como viñeta), para y dile al usuario qué título falta; no escribas en otro lado.
