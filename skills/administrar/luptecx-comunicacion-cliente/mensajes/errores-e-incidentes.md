# Errores e incidentes

Un **error** es algo que falla y tiene arreglo programado (lo registra
`luptecx-reportar-error` con su severidad y plazo). Un **incidente** es un error Crítico
en curso: el bot no responde o escribió datos mal, y el cliente lo está viviendo ahora.

Reglas de todos:

- **Solo lo confirmado.** Lo que se sospecha no se dice; la causa se cuenta cuando se sabe.
- **Siempre cuándo es el siguiente mensaje**, con hora, aunque no haya novedad.
- Lo que el cliente puede hacer mientras tanto, o «por ahora no hace falta que hagan nada».

## Acuse de un reporte

Cuando un cliente reporta algo (no cuando lo vio el equipo en los logs). Tres partes:
recibido; qué entendimos, en una línea; cuándo le escribimos, según el plazo de la
severidad. Nada de causas ni de promesas de arreglo.

| Severidad | Cuándo le escribimos |
|---|---|
| Crítica | Es un incidente: usa el mensaje de abajo |
| Alta | «antes del [día] a las [hora]» (2 días hábiles) |
| Media | «antes del [día]» (7 días) |
| Baja o funcionalidad | «le contamos cuando esté en una actualización» |

> Hola, Andrés. Recibido, gracias por avisar. Entendemos que el asistente le está
> anotando dos veces el pedido cuando el cliente lo confirma con una foto. Lo revisamos y le
> escribo *antes del viernes 18 a las 12:00 m.* con la solución.

## Incidente en curso

En cuanto se confirma, sin esperar a tener la causa. Partes: qué está pasando, en palabras
del cliente; qué sí funciona; qué pueden hacer mientras tanto; a qué hora llega el
siguiente mensaje (**una hora como máximo** mientras dure). «Los mensajes no se pierden» y
«lo demás funciona» son lo que más tranquiliza, y por eso solo se dicen si están
confirmados.

> Hola, Andrés. Desde las 9:40 a. m. el asistente no está respondiendo los mensajes de
> sus clientes. Los mensajes no se pierden: le llegan y los va a contestar cuando vuelva.
> Ya estamos en esto. Mientras tanto, si un cliente necesita algo urgente, que escriba a
> su número de siempre. Le escribo de nuevo *antes de las 10:45 a. m.*

## Actualización

Cada mensaje de seguimiento, hasta resolver: qué cambió desde el anterior (o «seguimos en
lo mismo») y la hora del siguiente. Si ya se arregló pero falta confirmarlo, se dice: «el
bot volvió a responder a las 10:20 a. m.; lo estamos vigilando antes de darlo por
resuelto».

## Incidente resuelto

Partes: desde qué hora funciona; cuánto duró y qué afectó, con cifras si las hay; una
disculpa concreta; qué se hizo para que no se repita (o cuándo se lo contamos); si el
cliente tiene que hacer algo.

> Andrés, el bot está funcionando con normalidad desde las 10:20 a. m. Estuvo sin
> responder 40 minutos y quedaron 23 mensajes en espera, que ya contestó. Le pido
> disculpas: la actualización de anoche dejó mal una configuración. Ya la corregimos y
> agregamos una revisión para que no vuelva a pasar. No tienen que hacer nada.

## Error corregido

Cuando se despliega el arreglo de un error que reportó el cliente (no Crítico). Partes:
qué pasaba; que ya quedó; desde cuándo; si tiene que hacer algo (por ejemplo, revisar los
registros de esos días).

> Hola, Andrés. Ya quedó corregido lo del pago que se sumaba dos veces: desde hoy a las
> 2:00 p. m. el bot lo registra una sola vez. Los tres pagos duplicados de esta semana ya
> los ajustamos en la hoja; no tienen que hacer nada.
