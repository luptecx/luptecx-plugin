---
name: luptecx-reportar-error
description: Registrar lo que reporta o pide un cliente de LUPTECX antes de que alguien toque código. Úsala cuando llegue un mensaje, audio o captura de un cliente con una falla («el bot no responde», «me sumó mal el pago», «no me llegó el aviso»), cuando alguien diga reportar un error, abrir un issue o «anótalo para Camilo», o cuando el cliente pida algo nuevo para su bot.
---

# Reportar un error

Convierte lo que manda el cliente en un **issue de GitHub** y una **tarea de Notion** que se
enlazan entre sí, siempre con los mismos campos, para que quien corrige empiece sin
preguntarle nada a nadie. La skill termina en el registro: el diagnóstico y el arreglo
empiezan en `luptecx:luptecx-corregir-error`, con el issue como entrada.

La usa sobre todo Felipe. No necesita el código, el servidor ni los logs.

## 1. Entender qué pasó

Saca del mensaje, audio o captura:

- **Proyecto:** el cliente en Notion → su proyecto en la base Proyectos → el repositorio en
  su campo **Repositorio** (ver «Referencia»).
- **Qué vio el cliente**, con sus palabras, y **qué esperaba** que pasara.
- **Cuándo**: fecha y hora de Bogotá, lo más exacta posible (con eso se busca en los logs).
- **Cómo reproducirlo**: el mensaje exacto que se le mandó al bot, desde qué número y qué
  respondió.

**¿Error o funcionalidad?** Es un **error** si el bot antes lo hacía bien o si
`docs/ESPECIFICACION.md` del proyecto dice que lo debe hacer. Es una **funcionalidad** si
es algo que el bot nunca hizo y la especificación no menciona. Si no se puede saber, se le
pregunta al usuario.

Si falta algo, pregunta en **una sola ronda** solo lo que falta. Si lo tiene que contestar
el cliente, redacta la pregunta para que el usuario se la mande.

**Terminado cuando:** el proyecto está identificado y «qué pasó» y «qué esperaba» tienen
valor (en una funcionalidad: «qué necesita el cliente»).

## 2. Severidad y plazo

Solo para errores. En la duda entre dos, la más alta.

| Severidad | Cuándo | Priority | Fecha límite en Notion |
|---|---|---|---|
| **Crítica** | El bot no responde, o escribió datos mal (pagos, fechas, la hoja del cliente) aunque siga respondiendo | High | Hoy, y aviso inmediato a Camilo |
| **Alta** | Una función no sirve y no hay forma de rodearla | High | 2 días hábiles |
| **Media** | Algo falla, pero hay forma de rodearlo | Medium | 7 días |
| **Baja** | Detalle: un texto, un formato | Low | Sin fecha: entra al repaso de los lunes |

Una funcionalidad va sin severidad, con Priority **Medium** y sin fecha: el plazo lo pone
`luptecx:luptecx-nueva-funcionalidad` al estimar.

**Terminado cuando:** hay severidad y una frase que dice por qué.

## 3. Enmascarar antes de escribir en GitHub

El issue lo leen Claude y cualquiera con acceso al repositorio; los datos de los clientes
del cliente no van ahí (Ley 1581 de 2012). El mensaje original completo va **solo** en el
cuerpo de la tarea de Notion.

| Dato | En el issue |
|---|---|
| Teléfono | Últimos 4 dígitos: `…4821` |
| Nombre de un usuario o cliente final | Iniciales: `J. R.` |
| Cédula, dirección, cuenta bancaria, foto de un documento | `[omitido]` |
| Identificadores del negocio, montos, fechas, el texto que se envió | Tal cual: hacen falta para encontrar el caso |
| Captura de pantalla | Se describe lo que se ve; la imagen se sube solo si no muestra ningún dato de las filas de arriba |

**Terminado cuando:** releíste el texto del issue y no queda ningún dato de las tres
primeras filas.

## 4. Buscar duplicados

- GitHub: `gh issue list -R <repo> --state open --search "<dos o tres palabras clave>"`.
- Notion: tareas del mismo proyecto con Tipo = Error que no estén en Done ni Cancelado.

Si ya existe, **no se crea otro**: se agrega un comentario al issue con la ocurrencia nueva
(cuándo, número enmascarado, qué mandó) y, si la severidad sube, se sube en los dos lados.

**Terminado cuando:** buscaste en los dos y sabes si es nuevo o repetido.

## 5. Registrar

En este orden, porque cada uno necesita el enlace del anterior:

1. **Tarea en Notion**, en la base Tasks. Un error se crea con la plantilla **Error** y el
   procedimiento de `luptecx-nuevo-proyecto/notion.md` (en `skills/construir/`); una
   funcionalidad, sin plantilla:

   | Campo | Valor |
   |---|---|
   | In (título) | Qué falla, en una línea, en palabras del cliente |
   | Tipo | Error o Funcionalidad |
   | Severidad | La del paso 2 (vacía si es funcionalidad) |
   | Priority | La de la tabla del paso 2 |
   | Project | El proyecto del paso 1 |
   | Assignee | Camilo |
   | Due Date | La de la tabla del paso 2 |
   | completed | Not started |
   | Cuerpo | El mensaje original sin enmascarar (o la transcripción del audio) y quién lo reportó; en un error, debajo de «Mensaje original» |

2. **Issue en GitHub**, con el mismo título que la tarea y el cuerpo de la plantilla de
   abajo:
   `gh issue create -R <repo> --title "[Error] <título>" --label error --body-file <archivo>`
   Si `gh` dice que la etiqueta no existe, créala y repite:
   `gh label create error --color d73a4a --description "Algo no funciona como debería"`
   (para funcionalidades: `funcionalidad`, color `a2eeef`).

3. **Enlace GitHub** de la tarea de Notion = la URL del issue.

Sin `gh` (por ejemplo, en el chat de claude.ai): usa el conector de GitHub si está; si no,
dale al usuario el cuerpo listo y el formulario
`https://github.com/<repo>/issues/new/choose` para que lo pegue, y el paso 3 se hace
cuando te pase la URL.

**Cuerpo del issue de error.** Usa los mismos títulos que el formulario
`.github/ISSUE_TEMPLATE/error.yml`, para que un issue escrito a mano y uno escrito aquí se
lean igual:

```markdown
### Severidad

Alta — <la frase del paso 2>

### Qué pasó

<lo que vio el cliente, enmascarado>

### Qué debería haber pasado

<lo que esperaba>

### Cómo reproducirlo

<mensaje exacto que se le mandó al bot, desde …4821, y qué respondió>

### Cuándo pasó

<DD/MM/AAAA HH:MM, hora de Bogotá>

### Tarea de Notion

<URL de la tarea>
```

**Cuerpo del issue de funcionalidad** (`[Funcionalidad] <título>`, etiqueta
`funcionalidad`), con los títulos de `funcionalidad.yml`: «Qué necesita el cliente» (el
problema, no la solución; quién lo pidió y para qué), «¿Encaja en este proyecto?»
(`Sí, mejora lo que ya hace`, `No, es otro producto` o `No sé, hay que revisarlo`: lo
decide `luptecx-nueva-funcionalidad` en su paso 1; las funcionalidades van dentro de la
mensualidad), «Criterios de aceptación» y «Tarea de Notion».

**Terminado cuando:** abriste la URL del issue y la de la tarea, y cada una enlaza a la
otra.

## 6. Avisar

Son borradores. El usuario los lee, los ajusta y los manda él; Claude no le escribe a nadie.

- **Acuse al cliente**, si lo reportó un cliente (un error que vio el equipo en los logs o
  en el monitor no lleva acuse): `luptecx:luptecx-comunicacion-cliente`, «Acuse de un
  reporte» (en una Crítica, «Incidente en curso»).
- **Crítica:** además, un mensaje para Camilo por WhatsApp, ya:
  `[Crítica] <proyecto>: <qué pasa en una línea>. Issue: <URL>`.

**Terminado cuando:** el usuario tiene los borradores.

## Al terminar

Responde con este bloque:

```
Registrado: [Error · Alta] <título>
Issue: <URL>
Tarea: <URL>   Plazo: <fecha o «repaso de los lunes»>
Borradores: acuse al cliente (+ aviso a Camilo si es Crítica)
Sigue: luptecx:luptecx-corregir-error con el issue
```

## Referencia

- **Bases Tasks y Proyectos** (campos Clients, Fase y Repositorio): sus identificadores
  están en la página «Mapa de Notion para Claude» de Recursos (búscala por ese nombre con el conector de Notion).
- Si un proyecto no tiene **Repositorio** en Notion, se pregunta cuál es y se llena el
  campo, para que la próxima vez no haga falta.
- Los títulos del cuerpo son los del formulario del repositorio. Si el formulario cambia,
  esta plantilla cambia con él.
