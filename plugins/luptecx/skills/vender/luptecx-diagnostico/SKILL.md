---
name: luptecx-diagnostico
description: Preparar y aprovechar la reunión de diagnóstico con un posible cliente de LUPTECX. Úsala antes de la reunión («prepárame la reunión con…», «qué le pregunto a…», «tengo una cita con un posible cliente») y después («ya hablé con…», «estas son las notas de la reunión», «te mando el audio de la reunión»), o cuando falten datos del cliente para armar una propuesta.
---

# Diagnóstico

La reunión de diagnóstico es donde se gana o se pierde la propuesta: de ahí salen el
problema del cliente **en sus palabras** y **las cifras que él mismo dice**, que después
justifican el precio (`luptecx:presentacion-ventas-contenido`). Esta skill tiene dos
momentos: **antes** (la hoja de la reunión) y **después** (ordenar lo que se dijo, decidir
si encaja y dejarlo en Notion).

La reunión dura **30 minutos** por defecto. La hoja es un mapa, no un guion: se sigue lo
que el cliente responde.

## Antes de la reunión

### 1. Lo que ya se sabe

Busca al cliente en el CRM (Clientes) y la reunión en Reuniones (la crea el calendario; ver
[notion.md](../../construir/luptecx-nuevo-proyecto/notion.md)). Lee lo que haya: cómo
llegó, mensajes anteriores, su web y redes. Lo que se puede averiguar no se pregunta en la
reunión. **No inventes datos del cliente**: lo que no se sabe queda como pregunta.

**Terminado cuando:** sabes empresa, sector, ciudad, cómo llegó y quién va a la reunión.

### 2. Hipótesis de dolor

Escribe **dos o tres** dolores probables, cada uno como algo a comprobar, no a confirmar:
«creemos que pierden clientes porque contestan WhatsApp tarde fuera de horario». Para cada
uno, qué producto del Portafolio lo resolvería. Pregúntale al usuario cuál va primero.

**Terminado cuando:** el usuario eligió el orden de las hipótesis.

### 3. La hoja de la reunión

Con [preguntas.md](preguntas.md), arma la hoja para 30 minutos: unas **seis preguntas
principales**, cada una con dos o tres repreguntas y qué escuchar. Si va a estar el dueño
o un gerente, menos preguntas y más directas.

```
DIAGNÓSTICO · <empresa> · <fecha y hora> · 30 min · <quién va de LUPTECX>
Objetivo: <qué tiene que quedar claro al salir>
Hipótesis: 1. … 2. … 3. …
Acuerdo inicial: <una línea: para qué es la reunión, cuánto dura, cómo puede terminar>
Preguntas, por etapa: <principal> → <repreguntas> · escuchar: <…> · pasar cuando: <…>
Si pasa…: <las ramas de preguntas.md que apliquen>
Cierre: resumen con sus palabras y siguiente paso con fecha
```

Si la reunión ya existe en Reuniones, aplícale la plantilla **Diagnóstico** (ver
«Aplicar una plantilla a una página que ya existe» en notion.md) y escribe la hoja debajo
de «Preparación». Si no existe, créala con la plantilla, con Tipo = Clientes, Clients y
Meeting Date.

**Terminado cuando:** la hoja está en la reunión de Notion y el usuario la tiene.

## Después de la reunión

### 4. Ordenar lo que se dijo

Pide las notas: escritas, o un audio **transcrito** (WhatsApp transcribe los audios en el
teléfono; Claude no escucha audios aquí). Ordénalas por etapa: proceso, problema, causa,
impacto, urgencia, quién decide. Las cifras van **con las palabras del cliente** y marcando
quién las dijo; lo que el usuario dedujo va como estimado.

**Terminado cuando:** cada etapa tiene lo que se dijo o dice «no salió».

### 5. Los datos para la propuesta

Llena la tabla de datos de `luptecx:presentacion-ventas-contenido` (paso 1) con lo que salió
de la reunión: empresa y quién decide, proceso que duele, volumen, tiempo actual, costo de
ese tiempo, valor de un cliente o venta, herramientas actuales y siguiente paso. Lo que
falta queda como `[POR CONFIRMAR: …]` con la pregunta para hacérsela al cliente.

**Terminado cuando:** cada dato tiene valor y fuente, o la pregunta que falta.

### 6. ¿Encaja?

| Criterio | Encaja si |
|---|---|
| Dolor | Hay un problema concreto con al menos **una cifra dicha por el cliente** |
| Quién decide | Se sabe quién firma, y estuvo en la reunión o hay cómo llegarle |
| Producto | Lo resuelve un producto del Portafolio, o los socios deciden hacer uno nuevo |
| Retorno | Lo que el problema le cuesta al mes es **mayor que la mensualidad Esencial** de ese producto |
| Por qué ahora | Hay un motivo para actuar ya. Si no lo hay, no descarta: baja la prioridad |

- **Hacer propuesta:** cumple los cuatro primeros. Sigue `presentacion-ventas-contenido`.
- **Falta un dato:** se pide al cliente antes de proponer (`luptecx:luptecx-comunicacion-cliente`).
- **No encaja:** se le dice con respeto y, si se puede, a quién le sirve
  (`luptecx-comunicacion-cliente`, «Decir que no»); en el CRM, Estado = Perdido.

La decisión es del usuario; tú la recomiendas con el criterio que falla.

**Terminado cuando:** el usuario decidió.

### 7. Dejarlo en Notion

- **Reunión:** debajo de cada título de la plantilla, lo de los pasos 4 a 6;
  Estado = Terminada.
- **Cliente (CRM):** Ultimo Contacto = la fecha de la reunión y, si no encaja,
  Estado = Perdido. Propuesta Enviada lo pone quien envía la propuesta.
- **Siguiente paso:** el mensaje al cliente con `luptecx-comunicacion-cliente` (resumen corto
  con sus palabras y el siguiente paso con fecha), y la tarea en Tasks si hay algo que hacer
  (Tipo = Comercial).

**Terminado cuando:** la reunión, el cliente y el siguiente paso están en Notion y el usuario
tiene el borrador del mensaje.

## Al terminar

```
Diagnóstico: <empresa> · <fecha>
Dolor principal: <en palabras del cliente> · Cifra: <la que dijo>
Encaja: <sí / falta un dato / no> — <criterio>
Notion: <URL de la reunión> · CRM al día
Sigue: <propuesta con presentacion-ventas-contenido / pedir dato / cerrar>
```
