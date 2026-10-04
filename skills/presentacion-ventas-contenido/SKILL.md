---
name: "presentacion-ventas-contenido"
description: "Estructura y contenido de presentaciones de venta y propuestas comerciales a clientes (sobre todo automatizaciones). Úsala para armar o revisar el guion de una propuesta. No define el diseño."
---

# Contenido de presentaciones de venta

Esta skill define **qué dice** una presentación de ventas y **en qué orden**. No define cómo se ve. Para una presentación de LUPTECX, combínala con la skill `luptecx-estilo-visual`: primero se arma el guion con esta skill y después se diseña con la otra. Si el usuario pide otra marca u otro formato, esta skill sigue sirviendo igual.

**Cuándo usarla:** propuestas comerciales, presentaciones para cerrar un cliente o ofrecer un servicio, y cotizaciones en formato de slides.
**Cuándo no:** informes de resultados a clientes actuales, capacitaciones, presentaciones de universidad, pitch a inversionistas ni presentaciones internas. Esas tienen otra lógica.

## En qué se basa

La estructura mezcla tres métodos que funcionan en venta B2B:
- **Diagnóstico + ROI**, el método de las agencias de automatización. Los números salen del cliente y la propuesta llega al precio con el cliente ya convencido.
- **Reencuadre**, de *The Challenger Sale*. Al inicio se le muestra al cliente algo que no había visto de su propio problema.
- **Tres niveles de precio.** El cliente deja de preguntarse "¿sí o no?" y pasa a preguntarse "¿cuál de las tres?". La mayoría elige la del medio.

Reglas de fondo:
1. **Se abre con el problema del cliente**, nunca con quién es LUPTECX, su historia o sus clientes.
2. **Cada título es una conclusión.** Leyendo solo los títulos, se entiende la propuesta completa.
3. **Una idea por slide.**
4. **Los números salen del cliente.** Si son estimaciones, se dice.
5. **No hay slide de "prueba"** (casos de éxito, testimonios, logos de clientes), salvo que el usuario la pida.

---

## Paso 1 · Reunir la información

Antes de escribir, revisa qué se sabe del cliente: la conversación, la memoria, sus archivos, notas de llamadas y su web. Necesitas:

| Dato | Para qué slide | Ejemplo de pregunta |
|---|---|---|
| Empresa, sector, ciudad y quién decide | 1, 10 | ¿A quién va dirigida y quién firma? |
| El proceso que duele hoy | 2, 3 | ¿Qué tarea repetitiva les quita más tiempo o les hace perder clientes? |
| Volumen | 3, 4 | ¿Cuántos chats, leads, pedidos o facturas al día o al mes? |
| Tiempo actual | 3, 4 | ¿Cuánto tardan en responder o en hacer esa tarea? ¿Quién la hace? |
| Costo de ese tiempo | 4, 9 | ¿Cuánto gana al mes la persona que lo hace, o cuánto vale una hora de su equipo? |
| Valor de un cliente o venta | 4, 9 | ¿Ticket promedio o margen por venta? ¿Cuántos leads cierran de cada 10? |
| Herramientas actuales | 5, 6 | ¿Usan WhatsApp Business, Excel, algún CRM o sistema contable? |
| Alcance que se ofrece | 5, 6, 8 | ¿Qué incluye cada nivel? |
| Precios y forma de pago | 8, 9 | Pago inicial, mensualidad y qué no está incluido |
| Siguiente paso deseado | 10 | ¿Reunión, piloto, firma? ¿Con qué fecha? |

- **Pregunta todo lo que haga falta** para hacer bien la presentación. No hay límite de preguntas: vale cualquier pregunta que cambie el contenido, las cifras, el tono o el alcance.
- Agrúpalas por tema (cliente, problema, números, alcance, precios, cierre) y hazlas en una sola tanda para no ir y volver. Si usas AskUserQuestion, puedes hacer varias rondas seguidas; si no, envía la lista completa en texto.
- Pregunta también lo que no esté en la tabla si el caso lo necesita: objeciones que ya puso el cliente, competencia que está evaluando, presupuesto que mencionó, quién más va a ver la propuesta, si se presenta en vivo o se envía.
- Solo si el usuario no está o no tiene el dato, sigue con marcadores visibles: `[POR CONFIRMAR: chats/día]`.
- **Nunca inventes cifras del cliente ni precios.** Una estimación va marcada como "estimado" y con su supuesto en el pie.

---

## Paso 2 · Estructura base de 10 slides

| # | Slide | Objetivo | Cómo se escribe el título | Contenido |
|---|---|---|---|---|
| 1 | **Portada** | Que sienta que la propuesta es para él | "[Resultado] para [Cliente]" | Tipo de documento, nombre del cliente, ciudad y fecha. Sin eslogan de LUPTECX. |
| 2 | **Reencuadre** | Cambiar cómo ve su problema | Frase que contradice lo que el cliente cree: "No pierden ventas por precio; las pierden en los primeros 5 minutos" | Una frase y 1–2 líneas de apoyo. Nada más. |
| 3 | **Diagnóstico** | Mostrar que entendimos su caso, con sus datos | La cifra hecha frase: "4 de cada 10 chats esperan más de una hora" | Una gráfica o 2–3 datos del cliente, con la fuente en el pie |
| 4 | **Costo de no actuar** | Ponerle precio al problema | "Hoy se están yendo cerca de $X al mes" | Cálculo simple a la vista (ver Paso 4) y una cifra grande |
| 5 | **La solución** | Que entienda qué recibe, en su idioma | Beneficio, no herramienta: "Cada cliente recibe respuesta en menos de un minuto, a cualquier hora" | Cómo funciona en 3 pasos desde el punto de vista del cliente final. Sin jerga técnica. |
| 6 | **Implementación** | Mostrar que es concreto y rápido | "Funcionando en 4 semanas" | 3–5 fases con semanas, y qué entrega el cliente en cada una (accesos, datos, aprobaciones) |
| 7 | **Responsabilidades** | Dejar claro qué hace cada parte | "Nosotros ponemos X; ustedes ponen Y" | Dos columnas: [Empresa] se encarga de… / [Cliente] se encarga de… Máx. 4–5 puntos por lado. |
| 8 | **Inversión** | Que vea las opciones y lo que cuesta cada una | "Tres formas de empezar" o "Elijan cómo empezar" | 3 niveles, con el del medio recomendado (ver Paso 5) |
| 9 | **Retorno estimado** | Justificar el precio que acaba de ver | "La opción recomendada se recupera en N meses" | Ahorro o ganancia mensual contra el costo de la opción recomendada (o de cada opción), con los supuestos visibles |
| 10 | **Siguiente paso** | Que diga sí a algo concreto | Acción + fecha: "Arranquemos el lunes 6 de octubre" | Un solo paso, qué necesitamos del cliente para darlo y los datos de contacto |

**Anexos opcionales**, después del cierre y solo si hacen falta: detalle técnico, preguntas frecuentes, términos y condiciones. No cuentan en las 10.

**Versión corta (6 slides)**, para primer contacto o envío por WhatsApp: 1 Portada, 2 Reencuadre, 3 Diagnóstico + costo en una sola, 5 Solución, 8 Inversión, 10 Siguiente paso.

**Por qué la inversión va antes del retorno:** el cliente primero ve cuánto cuesta cada opción y enseguida ve cuánto le devuelve. Así el retorno se calcula sobre un precio que ya conoce, y la última impresión antes del cierre es la ganancia, no el costo.

Puedes quitar o fusionar slides si el caso no las necesita. Por ejemplo, sin datos de ROI se omite la 9. Pero **el orden no se cambia**: problema, costo del problema, solución, cómo, precio, retorno, acción.

---

## Paso 3 · Reglas de redacción

- **Títulos:** frase afirmativa de máximo 2 líneas (unas 12 palabras), con verbo y, si se puede, número. Prohibido titular con etiquetas como "El reto", "Nuestra solución" o "Beneficios". La etiqueta pequeña encima del título sí puede ser una palabra ("Diagnóstico").
- **Cuerpo:** máximo unas 30 palabras por slide y máximo 4 viñetas de 2 líneas. Lo que no cabe va a las notas del presentador.
- **Lenguaje del cliente:** usa sus palabras ("carros", "asesores", "citas") en lugar de "leads", "pipeline" o "workflow", salvo que el cliente las use.
- **Sin jerga técnica** (API, LLM, webhook, n8n, modelo de IA) salvo que el público sea técnico. Se dice qué pasa, no con qué se hace.
- **Trato:** mantén el que usa el usuario con ese cliente (tú o ustedes). Por defecto, "ustedes" para empresas.
- **Promesas:** solo lo que depende de quien vende y se puede medir ("respuesta en menos de 1 minuto, 24/7"). Nada de "garantizamos más ventas" ni "garantizamos leads al menor costo": el cierre depende del equipo del cliente, y eso ya queda dicho en la slide 7.
- **Palabras vacías prohibidas:** "soluciones innovadoras", "de vanguardia", "transformación digital", "potenciamos", "sinergia", "de clase mundial".

---

## Paso 4 · Cálculos (slides 4 y 9)

Haz todas las cuentas **con código**, nunca de memoria, y deja los supuestos escritos en el pie o en las notas.

**Costo de no actuar (mensual)**, con las piezas que apliquen:
- Tiempo perdido = horas/mes en la tarea × costo hora
- Ventas perdidas = leads/mes × % que se pierde por demora × % de cierre × margen por venta
- Errores = errores/mes × costo de cada error

**Retorno:**
- Beneficio mensual = costo de no actuar × % que la automatización recupera. Sé **conservador**: usa entre el 50 % y el 70 % del potencial y di que es conservador.
- Meses para recuperar la inversión = pago inicial ÷ (beneficio mensual − mensualidad)
- Usa los precios de la slide 8: calcula el retorno de la opción recomendada y, si ayuda a decidir, el de las tres en una tabla corta.
- Si el resultado es menos de 1 mes o suena increíble, baja los supuestos. Una cifra creíble vende más que una espectacular.

Muestra la cuenta en palabras simples: "100 chats/día × 30 días × 40 % sin respuesta rápida × 5 % de cierre = 60 ventas en riesgo al mes".

---

## Paso 5 · Precios (slide 8)

- **Tres niveles:** Esencial, Recomendado y Completo, o nombres propios del servicio. El del medio es el que se quiere vender y va marcado como recomendado.
- Se diseña de arriba hacia abajo: primero el Completo, que ancla el precio alto; luego se quita alcance para el Recomendado y el Esencial. Cada nivel incluye todo el anterior y añade 1–3 cosas visibles.
- Cada nivel lleva nombre, precio (pago inicial y mensualidad si aplica), una frase de para quién es y máximo 3 puntos de lo que incluye.
- **Qué no está incluido**, en una línea visible: pauta publicitaria, costos de terceros como la API de WhatsApp o licencias, contenido que debe entregar el cliente.
- Vigencia de la propuesta ("Precios válidos hasta el 31 de octubre de 2026") e IVA incluido o no.
- **Si el usuario no ha dado precios, no los inventes:** deja `[PRECIO]` y avisa.
- Si el usuario pide un solo precio, respétalo.

---

## Paso 6 · Entrega del guion

Antes de diseñar, arma el guion con este formato para cada slide:

```
### Slide N · [Nombre]
Etiqueta: …
Título: …
Contenido: … (viñetas, cifras, datos de gráfica con su fuente)
Visual sugerido: cifra grande / gráfica de barras / 3 tarjetas / dos columnas / cronograma / frase sola
Notas del presentador: 2–4 frases de lo que se dice en voz alta
```

- Si la presentación es de LUPTECX, pasa este guion a `luptecx-estilo-visual` para diseñarlo. En el campo "Visual sugerido" usa los layouts de esa skill (L01…L13).
- Si el usuario solo pidió el contenido, entrega el guion y ofrece diseñarlo.

---

## Paso 7 · Revisión

1. **Prueba de títulos:** lee solo los títulos en orden. ¿Cuentan la historia completa, del problema a la acción?
2. ¿La primera slide después de la portada habla del cliente y no de quien vende?
3. ¿Cada número tiene fuente o está marcado como estimado? ¿Las cuentas se hicieron con código?
4. ¿Ninguna slide tiene más de una idea, más de 30 palabras de cuerpo o más de 4 viñetas?
5. ¿Hay promesas que dependen del cliente? Quítalas.
6. ¿La inversión (slide 8) tiene 3 niveles con uno recomendado, lo que no incluye y la vigencia? ¿El retorno (slide 9) usa exactamente esos precios?
7. ¿El cierre pide **una** acción concreta con fecha?
8. ¿Hay marcadores `[POR CONFIRMAR]` o `[PRECIO]` pendientes? Avísale al usuario.