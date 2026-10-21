# Cifras del sistema por tipo de proyecto

Se lee en el paso 2. Se toman las del tipo del proyecto (el que declara su `CLAUDE.md`) y,
primero, **la cifra del diagnóstico**: el dolor que el cliente midió antes de empezar es la
que más importa mostrar.

## Reglas

- Cada cifra lleva **de dónde salió** («panel de la plataforma, 1 al 31 de octubre»). Sin fuente,
  no va.
- Lo que no se midió dice «no se midió este mes». **Nunca se estima ni se completa.**
- Se compara con el mes anterior (del reporte pasado) y, si existe, con la cifra del
  diagnóstico: «antes contestaban la mitad; este mes, el bot contestó todas».
- Pocas cifras y que importen al cliente: 3 a 5. Las técnicas (errores del servidor,
  memoria) no van; van sus efectos («el bot estuvo disponible todo el mes salvo 40
  minutos el día 12»).

## Eventos recomendados

Los proyectos de la plantilla de procesos registran sus cifras solas con
`registrar_evento()` (`app/metricas.py`). Este es el catálogo de donde cada proyecto elige
las suyas y las anota en «Qué se mide» de su especificación. Nombres objeto_acción; el
contexto va en propiedades; nunca datos personales.

| Tipo | Evento | Propiedades | Cifra del reporte |
|---|---|---|---|
| Conversa (bot o agente) | `conversacion_atendida` | `fuera_de_horario` (sí/no) | Conversaciones del mes y fuera de horario |
| Conversa (bot o agente) | `conversacion_derivada` | `motivo` (texto corto) | Las que pasaron a una persona, y por qué |
| Todos | `<resultado>_<acción>` del negocio: `cita_agendada`, `pago_registrado`, `pedido_tomado` | Las que el negocio necesite, sin datos personales | Lo que el sistema hizo por el negocio |
| Automatización | `proceso_ejecutado` | `registros` (número), `exito` (sí/no) | Veces que corrió y registros procesados |
| Consulta de datos | `consulta_realizada` | `cambios` (número) | Consultas y cambios encontrados |
| Consulta de datos | `aviso_enviado` | — | Avisos por cambios importantes |

## Servicio que conversa (bot o agente)

Un plugin de tipo de proyecto (por ejemplo, `luptecx-bot-whatsapp`) puede sumar cifras
propias de su plataforma.

| Cifra | De dónde sale hoy |
|---|---|
| Conversaciones atendidas en el mes | Los eventos del proyecto o el panel de la plataforma |
| Conversaciones fuera del horario del cliente | La base del proyecto o los registros; si no se puede, «no se midió» |
| Conversaciones que pasaron a una persona | La base del proyecto o lo que diga el equipo del cliente |
| Lo que el servicio hizo por el negocio (citas agendadas, pagos registrados, pedidos tomados) | La hoja o el sistema del cliente donde quedan |
| Tiempo sin servicio | Los incidentes del mes en Notion (tareas Error de severidad Crítica) |
| Costo de las plataformas en el mes (mensajería, IA), si el cliente lo paga | La facturación de cada plataforma |

## Automatización

| Cifra | De dónde sale hoy |
|---|---|
| Veces que corrió y cuántos registros procesó | Los registros de la automatización o la hoja de destino |
| Horas de trabajo manual que reemplazó | Registros procesados × el tiempo por registro que el cliente dijo en el diagnóstico |
| Fallas y cómo se resolvieron | Las tareas Error del mes en Notion |

## Consulta de datos (scraping)

| Cifra | De dónde sale hoy |
|---|---|
| Consultas hechas y cambios encontrados | Los registros de la herramienta o el reporte que ya recibe el cliente |
| Avisos enviados por cambios importantes | Los registros de la herramienta |
| Días sin consulta por falla del sitio de origen | Las tareas Error del mes en Notion |
