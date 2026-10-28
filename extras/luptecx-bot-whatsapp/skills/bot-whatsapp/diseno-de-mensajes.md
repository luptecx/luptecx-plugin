# Diseño de los mensajes que lee el usuario

Cómo se ve y cómo suena lo que manda el bot: qué componente usar, sus límites, el tono y
el ritmo. La meta es que cada mensaje se lea como el de un buen asesor que escribe por
WhatsApp, bien armado y sin tics de máquina. Límites revisados en la documentación de la
Cloud API de Meta el 27/10/2026; ante un rechazo de Meta, se vuelve a revisar la fuente
(al final).

## 1. Qué componente usar

| Situación | Componente | Por qué |
|---|---|---|
| Responder, explicar, confirmar | Texto | Lo más humano; nada que tocar |
| Dar un dato y ofrecer de 1 a 3 siguientes pasos | **Botones** (con imagen arriba si es un producto) | Una sola burbuja con la foto, el dato y las opciones |
| Escoger entre 4 y 10 opciones, o rangos | **Lista** | Ordenada y sin llenar el chat |
| Varios productos para comparar con su foto | **Carrusel** (2 a 10 tarjetas) | Se desliza como una vitrina; si Meta lo rechaza, lista |
| Fotos de un producto | Imágenes, una por mensaje, con pie corto | Se ven como un álbum |
| Un enlace a una página propia | Texto con `preview_url: true`, o botón de URL | Muestra la vista previa |

Reglas que valen para todos:

- **Una burbuja bien armada antes que tres cortas.** Meta cobra cada mensaje, y tres
  burbujas seguidas se leen como un bot.
- **Los botones ofrecen, no obligan.** Lo que el usuario escriba a mano siempre se
  entiende: nunca «Por favor, seleccione una opción».
- **Opciones que se responden con una palabra** van en botones. Las preguntas abiertas
  («¿qué carro busca?») van en texto.

## 2. Límites de cada componente

| Componente | Límites |
|---|---|
| Texto | Cuerpo de hasta 4096 caracteres |
| Botones (`interactive.type: button`) | Hasta 3 botones con título de 20 caracteres, únicos, e `id` de hasta 256. Cuerpo obligatorio de 1024, pie opcional de 60. Encabezado opcional: `text`, `image`, `video` o `document` |
| Lista (`interactive.type: list`) | Un botón de 20 caracteres que abre la lista. Encabezado solo de texto (60), cuerpo de 4096, pie de 60. De 1 a 10 secciones con título de 24; 10 filas en total, con título de 24, descripción de 72 e `id` de 200 |
| Carrusel (`interactive.type: carousel`) | De 2 a 10 tarjetas con encabezado de imagen o video, cuerpo de 160 caracteres con hasta 2 saltos de línea, y un botón de URL o botones de respuesta (20 caracteres, `id` de 256). Todas las tarjetas llevan el mismo tipo y número de botones. Cuerpo del mensaje obligatorio de 1024; sin encabezado ni pie |
| Imagen | JPEG o PNG de hasta 5 MB, de 8 bits, RGB o RGBA (WebP solo para stickers). Se sube a `POST /<PHONE_NUMBER_ID>/media` y se manda por su `id`: el `link` lo desaconseja Meta |
| `media_id` | Dura 30 días desde que se sube; los que llegan en un webhook, 7. Se guarda con su vencimiento y se vuelve a subir antes |

**El código corta, no Meta.** Cada título se arma con su límite y se recorta con criterio
(«Mazda CX-5 Touring 2020» cabe en 24; «Chevrolet Onix Premier 2022» no, y queda en
«Chevrolet Onix 2022»). Una prueba revisa los límites con los datos más largos posibles:
Meta rechaza el mensaje entero si un título se pasa por un carácter.

## 3. Cómo se lee humano

**Escribe como un buen vendedor que contesta desde su celular:**

1. **Responde primero lo que le preguntaron**, en la primera frase. Después, una sola
   pregunta, al final.
2. **Frases cortas**, un párrafo de dos o tres líneas. Se lee en una pantalla sin bajar.
3. **El mismo registro que el usuario.** Si escribe corto, se le contesta corto; si
   escribe largo y con detalle, con detalle. El trato (usted o tú) es el de la
   configuración.
4. **Cada mensaje empieza distinto.** Arranca por lo que importa («Sí, sigue disponible»,
   «Ese salió en 2021»), no por la misma muletilla.
5. **El nombre del usuario, poco:** al saludar y en los momentos que importan (un
   resultado, el paso a una persona). El nombre del perfil puede ser un apodo o el de un
   negocio; si no parece un nombre de persona, no se usa.
6. **Negrita solo para la cifra o el dato clave** (`*$62.500.000*`). Formatos de WhatsApp:
   `*negrita*`, `_cursiva_`, `~tachado~`, listas con `- ` o `1. ` y citas con `> `.
7. **Cifras y fechas como se escriben en el país:** `$62.500.000`, `38.000 km`,
   `mar. 2027`. Nunca `62500000` ni `2027-03-31`.
8. **Emojis: los de la configuración**, como mucho uno y al final de la frase, nunca en
   botones ni en cifras.

**Lo que delata a un bot, y qué escribir en su lugar:**

| Suena a bot | Suena a persona |
|---|---|
| «¡Claro! Con gusto le ayudo con su consulta sobre el vehículo.» | «Sí, la tenemos: …» |
| «Entiendo que usted desea saber el precio.» (repetir la pregunta) | El precio, directo |
| «¿Hay algo más en lo que pueda ayudarle?» al final de cada mensaje | Una pregunta concreta del siguiente paso, o nada |
| «Por favor seleccione una de las siguientes opciones: 1) … 2) …» | Botones o lista, sin numerar en el texto |
| «Estimado cliente», «Cordialmente», firmar cada mensaje | Sin encabezado ni firma |
| Pedir disculpas en cada respuesta | Una disculpa cuando hubo un error de verdad |
| Todo en negrita, viñetas para dos datos | Una línea con los datos separados por `·` |
| Botón «Opción 1», «Sí» / «No» sin contexto | Botón con lo que diría el usuario: «Ver fotos», «Quiero verlo» |

**Humano no es fingir ser una persona.** Las políticas de WhatsApp Business prohíben
engañar a quien escribe y piden una vía clara y directa a una persona. El bot no se
inventa un nombre de persona ni dice ser una. Si le preguntan, dice que es el asistente
automático del negocio y ofrece pasar con una persona. Que se presente o no al saludar lo
decide el cliente en su configuración.

## 4. El ritmo

- **Indicador de «escribiendo…»** apenas se va a responder algo que tarda (una llamada al
  modelo): `POST /<PHONE_NUMBER_ID>/messages` con
  `{"messaging_product": "whatsapp", "status": "read", "message_id": "<wamid entrante>",
  "typing_indicator": {"type": "text"}}`. Marca el mensaje como leído (y los anteriores),
  y se apaga al responder o a los 25 segundos. Solo cuando de verdad se va a responder: un
  «escribiendo…» sin respuesta se ve peor que nada. Va con el `wamid` de un mensaje
  entrante, nunca saliente.
- **Sin esperas de adorno.** El indicador cubre lo que tarda el proceso de verdad; se
  responde en cuanto la respuesta está lista.
- **Varios mensajes del usuario seguidos** («hola» · «la mazda» · «¿precio?») se juntan y
  se responden en una sola respuesta.
- **Varias burbujas en orden** (las fotos y después los botones): cada envío sale cuando
  Meta respondió al anterior. Meta no garantiza el orden de entrega de mensajes enviados
  casi al tiempo; lo que tiene que llegar de último va de último y se comprueba en el
  número de prueba.
- **Citar el mensaje** (`"context": {"message_id": "<wamid>"}`) solo cuando se responde
  uno que no es el último, o uno entre varios. Citar cada respuesta se ve mecánico.
- **Una reacción** (`type: reaction`) puede reemplazar una burbuja de cortesía: un 👍 al
  «gracias, lo pienso». No se cita una reacción.

## 5. Lo que vuelve

- La respuesta a un botón llega como `interactive.button_reply` (`id`, `title`); la de una
  lista, como `interactive.list_reply` (`id`, `title`, `description`). Las dos traen
  `context.id` con el mensaje que la originó.
- **Se decide por el `id`, nunca por el título.** El `id` dice qué y sobre qué
  (`fotos:ARX-012`), así sirve aunque el usuario toque un botón de hace días. El código
  vuelve a mirar el estado de lo que nombra el `id` (el carro pudo venderse).
- El título del botón que tocó se guarda como su texto: así se lee la conversación igual
  que la vio el usuario.

## 6. Antes de darlo por bueno

- Cada mensaje nuevo se mira en el número de prueba, en un Android y en un iPhone, con el
  tema claro y el oscuro: títulos cortados, saltos de línea de más, la foto del encabezado
  bien recortada.
- Una prueba con los datos más largos posibles revisa los límites de la sección 2.
- Las frases de la tabla «Suena a bot» se buscan en los textos fijos y en las
  instrucciones del modelo.

## Fuentes

Documentación de Meta para la Cloud API (`developers.facebook.com/documentation/business-messaging/whatsapp/`):
`messages/interactive-reply-buttons-messages`, `messages/interactive-list-messages`,
`messages/interactive-media-carousel-messages`, `typing-indicators`,
`business-phone-numbers/media`, `messages/contextual-replies` y
`messages/reaction-messages`. Políticas: `whatsappbusiness.com/policy` (no engañar, vía a
una persona). Revisadas el 27/10/2026.
