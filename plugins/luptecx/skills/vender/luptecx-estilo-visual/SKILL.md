---
name: "luptecx-estilo-visual"
description: "Estilo visual oficial de LUPTECX (dirección B \"Contraste\"). Úsala para diseñar cualquier presentación, deck, propuesta o PDF de slides de LUPTECX. Solo define lo visual, no el contenido."
---

# Estilo visual LUPTECX · Dirección B "Contraste"

Esta skill define **cómo se ve** cualquier presentación de LUPTECX: ventas, informes a clientes, capacitaciones, pitch o documentos en formato slide. **No define el contenido ni la estructura.** Eso lo pone el usuario u otra skill; para ventas, `presentacion-ventas-contenido`. Si las dos aplican, primero se arma el contenido y después se viste con esta skill.

Guía visual de referencia, con ejemplos renderizados y los logos: https://claude.ai/artifact/DVYbGuTpXnKVdiXzbCLcfY. Se lee con la herramienta Artifact (`action: "read"`).

La idea del estilo: fondo crema con texto negro en casi todo el deck. Unas pocas slides negras marcan los momentos clave, y el dorado se reserva para lo único que el público debe mirar en cada slide.

---

## 1. Logo

Los archivos están publicados junto a la guía. Descárgalos con Artifact `action: "read"`, `url: https://claude.ai/artifact/DVYbGuTpXnKVdiXzbCLcfY` y `path` igual a:

| Archivo | Qué es | Dónde se usa |
|---|---|---|
| `logo-claro.png` | "LT" negro y "x" dorada, con la palabra LUPTECX debajo; fondo transparente | Sobre crema o papel |
| `logo-oscuro.png` | "LT" crema y "x" dorada, con la palabra LUPTECX debajo; fondo transparente | Sobre negro |
| `logo-cuadro.png` | El logo dentro de su cuadro crema | Solo si hace falta un sello (avatar, esquina de un documento) |

Reglas:
- **Nunca redibujes el logo** en SVG, con texto o con formas. Si no puedes descargar los archivos, pídeselos al usuario.
- Va en la **portada** (arriba a la izquierda, 56 pt de lado) y en el **cierre** (centrado o arriba a la izquierda, 64 pt). Las slides interiores no llevan logo: llevan el pie de página (sección 6).
- No lo pongas dentro de un cuadro blanco sobre fondo negro. Sobre negro se usa `logo-oscuro.png`.

---

## 2. Color

| Token | Hex | Rol | Uso |
|---|---|---|---|
| `crema` | `#F7F3E8` | Base (≈60 %) | Fondo de la mayoría de slides |
| `papel` | `#FFFCF3` | Superficie | Relleno de tarjetas y de tablas destacadas |
| `negro` | `#141414` | Estructura (≈30 %) | Texto principal, slides negras, tarjeta destacada |
| `dorado` | `#D4A018` | Acento (≈10 %) | Rellenos, líneas, cifras y texto **sobre negro**, pill "Recomendado", barra destacada |
| `dorado-profundo` | `#86660C` | Acento en texto | Etiquetas y palabras doradas **sobre crema o papel** |
| `gris` | `#5E5A52` | Texto secundario | Descripciones, notas y pie sobre fondo claro |
| `gris-oscuro-txt` | `#A7A196` | Texto secundario en negro | Descripciones y pie sobre slides negras |
| `gris-dato` | `#CFC8B8` | Datos sin énfasis | Barras y series que no son el mensaje |
| `linea` | `#DDD6C6` | Divisores | Líneas de 1 pt y bordes de tarjeta |
| `linea-oscura` | `#3A3833` | Divisores en negro | Líneas dentro de slides o tarjetas negras |

Reglas de color:
1. **60 · 30 · 10.** Si el dorado ocupa más que un detalle, sobra dorado.
2. **Un solo foco dorado por slide:** la cifra clave, la opción recomendada, la palabra clave del título o la barra que prueba el título.
3. **Nunca uses texto `#D4A018` sobre crema o papel.** El contraste es 2,1 : 1 y no se lee. Sobre fondo claro, el texto dorado siempre es `#86660C` (4,8 : 1).
4. Sobre negro, el dorado `#D4A018` sí sirve para texto (7,8 : 1).
5. No hay otros colores. Tampoco rojo o verde "semántico", salvo en una tabla de semáforo que lo necesite de verdad; en ese caso usa tonos apagados (`#9B2C1F` y `#3F6B3A`) y siempre acompañados de texto.
6. Sin degradados, transparencias decorativas, sombras ni efecto vidrio.

---

## 3. Tipografía

Una sola familia: **Poppins** (Google Fonts), con los pesos 400, 500, 600 y 700. Si no está disponible, usa `"Segoe UI", Arial, sans-serif`.

La escala está en puntos sobre el lienzo de 960 × 540 pt:

| Rol | Tamaño | Peso | Detalles |
|---|---|---|---|
| Título de portada | 46 pt | 700 | Tracking −2 %, interlineado 1,08, máx. 3 líneas |
| Cifra grande | 72–120 pt | 700 | Tracking −3 %, interlineado 1 |
| Frase clave (slide negra) | 40–44 pt | 700 | Interlineado 1,1, máx. 4 líneas, ancho ≤ 88 % |
| Título de slide | 32 pt | 700 | Tracking −1,5 %, interlineado 1,12, **máx. 2 líneas** |
| Subtítulo | 16 pt | 400 | Interlineado 1,45 |
| Cuerpo | 14 pt | 400 | Interlineado 1,45, **nunca menos de 14 pt** |
| Precio o cifra de tarjeta | 28 pt | 700 | Números tabulares |
| Etiqueta (eyebrow) | 11 pt | 600 | MAYÚSCULAS, tracking +16 %, color `dorado-profundo` en claro y `dorado` en negro |
| Texto de tarjeta o viñeta | 12–14 pt | 400 | |
| Pie de página | 9,5–11 pt | 400 | Tracking +4 %, color `gris` |

- Todo alineado a la **izquierda**, sin texto justificado. En la portada y el cierre también se alinea a la izquierda, salvo que el cierre sea una sola línea centrada.
- Sin cursivas, subrayados ni MAYÚSCULAS en frases largas. El énfasis se hace con peso 600/700 o con color.
- Los títulos se balancean (`text-wrap: balance`) para no dejar palabras huérfanas.

---

## 4. Lienzo y retícula

- **Tamaño:** 960 × 540 pt (16:9). En PowerPoint equivale a 13,333 × 7,5 in, así que 1 pt de esta guía es 1 pt de PowerPoint.
- **Márgenes:** 48 pt a los lados, 40 pt arriba y 56 pt abajo, porque el pie ocupa la franja inferior.
- **Retícula:** 12 columnas con separación de 14 pt. Las tarjetas y columnas caen sobre la retícula.
- **Espacio vacío:** al menos un 20 % de cada slide. Si no cabe, divide la slide en dos.
- **Orden vertical habitual:** etiqueta, a 8 pt el título, a 24 pt el contenido, y el pie abajo.
- El contenido de las slides de gráfica o tarjetas se centra verticalmente en el espacio que queda bajo el título. No lo dejes pegado arriba con un hueco vacío abajo.

---

## 5. Ritmo claro / oscuro

| Slide | Fondo |
|---|---|
| Portada | **Negro** |
| Frase clave / reencuadre | **Negro** |
| Cifra de impacto (una sola cifra enorme) | **Negro** |
| Cierre / siguiente paso | **Negro** |
| Todas las demás | Crema |

- **Máximo 4 slides negras por cada 10** (40 %).
- No más de **2 negras seguidas**.
- En decks que no son de ventas, las portadas de sección también pueden ser negras, respetando el mismo máximo.

---

## 6. Componentes

**Etiqueta (eyebrow).** Una o dos palabras que ubican la slide ("Diagnóstico", "Inversión"). Va siempre arriba del título.

**Título.** Una frase que afirma algo, no una etiqueta. El contenido del título lo decide quien escribe, pero si llega como etiqueta ("El reto"), avisa.

**Pie de página**, en todas las slides menos portada y cierre:
- Izquierda: `LUPTECX · [Tipo de documento] para [Cliente]`, o `Fuente: …` cuando la slide tiene datos.
- Derecha: número de slide con 2 dígitos (`03`).
- Posición: 20 pt del borde inferior, entre los márgenes laterales, en 9,5 pt con color `gris` (o `gris-oscuro-txt` en slides negras).

**Tarjeta.** Fondo `papel`, borde de 1 pt `linea`, **radio de 10 pt**, relleno de 20 × 22 pt y sin sombra.
- Solo sirve para agrupar **2 a 4 elementos comparables** (opciones, fases, beneficios paralelos) o para enmarcar una gráfica.
- Nunca pongas una tarjeta sola alrededor de texto, ni tarjetas dentro de tarjetas.
- Todas las tarjetas de una fila tienen el mismo ancho, alto y relleno.

**Tarjeta destacada.** Fondo `negro` con texto crema, cifra o precio en `dorado` y descripción en `gris-oscuro-txt`. **Solo una por slide:** la opción recomendada o el elemento clave.

**Pill.** Etiqueta en fondo `dorado` con texto `negro`, 9,5 pt en peso 600 y MAYÚSCULAS, radio completo. Se usa para "Recomendado", "Nuevo" o "Fase actual". Máximo una por slide.

**Divisor.** Línea de 1 pt `linea`, o `linea-oscura` sobre negro. Separa contenidos dentro de tarjetas y columnas sin tarjeta.

**Viñetas.** Punto de 5 pt al 50 % de opacidad del color del texto, **máximo 4 por bloque** y máximo 2 líneas cada una.

**Tabla.**
- Sin bordes verticales ni relleno de celdas.
- Encabezado en etiqueta de 11 pt color `gris` con línea inferior negra de 1 pt; filas separadas por líneas `linea` de 1 pt.
- Máximo 4 columnas y 6 filas. La fila o columna destacada lleva fondo `papel` o texto en peso 600.

**Íconos.** Una sola familia lineal (Lucide), trazo de 2 pt, color `negro` (o `crema` sobre negro), a 20–24 pt. Úsalos solo si ayudan a escanear una lista de 3–4 elementos. **Nunca emojis.**

**Imágenes.** Fotos reales del cliente o capturas del producto (bot, CRM, dashboard, flujo). Van a sangre completa o dentro de una tarjeta con radio de 10 pt. Nada de fotos de stock ni ilustraciones genéricas de IA.

**Radio.** 10 pt en todo el deck. Las pills llevan radio completo. Nada más tiene esquinas redondeadas.

---

## 7. Gráficas

1. El **título de la slide es la conclusión** que la gráfica prueba.
2. Todo va en `gris-dato` y solo el dato que prueba el título se destaca: en slide crema, relleno `dorado` con etiqueta `negro`; dentro de una tarjeta negra, relleno `dorado`.
3. **Etiquetas directas** sobre o al lado de cada barra (14 pt en peso 700). Sin leyenda, cuadrícula, ejes innecesarios, bordes ni 3D.
4. Las barras empiezan en cero y van ordenadas. Si las categorías tienen nombres largos, van horizontales: barras de 40 pt de alto, separadas 20 pt, etiqueta de categoría de 14 pt a la izquierda y la categoría destacada en peso 600.
5. Tipos permitidos:
   - barras
   - línea para antes/después o evolución (línea gris de 2 pt y la serie clave en dorado de 3 pt con punto final)
   - cifra grande
   - tabla simple
   - Nunca tortas de más de 2 partes, radar ni gráficas apiladas complejas.
6. Si son 1 o 2 cifras, no hace falta gráfica: se muestra una **cifra grande** con su frase.
7. La gráfica puede ir sobre la slide o dentro de una tarjeta `papel`.
8. La **fuente** va en el pie ("Fuente: datos de [cliente], sep 2026", "Estimado LUPTECX").

---

## 8. Layouts

Elige para cada slide el layout que corresponde a su contenido. Los nombres sirven para acordar con el usuario.

| Código | Layout | Fondo | Composición |
|---|---|---|---|
| **L01 Portada** | Portada | Negro | `logo-oscuro` arriba a la izquierda; abajo a la izquierda: etiqueta ("Propuesta comercial"), título de 46 pt con el **nombre del cliente en dorado**, subtítulo con ciudad y fecha en `gris-oscuro-txt` |
| **L02 Frase clave** | Reencuadre o idea central | Negro | Etiqueta arriba; frase de 40–44 pt en la mitad inferior con la palabra clave en dorado; debajo, 1–2 líneas de apoyo de 14 pt a máx. 55 % de ancho |
| **L03 Cifra de impacto** | Un número que duele o que convence | Negro | Cifra de 96–120 pt en dorado a la izquierda; a su derecha o debajo, una frase de 18–22 pt que la explica y la fuente en el pie |
| **L04 Sección** | Separador de capítulos (decks largos) | Negro | Número de sección en etiqueta dorada y título de 40 pt; nada más |
| **L05 Contenido** | Idea con 2–4 puntos | Crema | Título; debajo, viñetas o 2–3 columnas sin tarjeta separadas por divisores |
| **L06 Tarjetas** | 2–4 elementos comparables | Crema | Título; una fila de 2–4 tarjetas iguales; si hay una destacada, es la tarjeta negra |
| **L07 Gráfica** | Dato que prueba el título | Crema | Título-conclusión; gráfica centrada verticalmente, opcionalmente dentro de una tarjeta papel; fuente en el pie |
| **L08 Dos columnas** | Comparar dos lados (LUPTECX / cliente, antes / después) | Crema | Dos tarjetas iguales lado a lado, o dos columnas con un divisor vertical; encabezado de cada columna en 16 pt peso 600 |
| **L09 Cronograma** | Fases con tiempos | Crema | Línea horizontal de 2 pt `linea` con 3–5 hitos (círculos de 12 pt; el actual o clave en dorado); debajo de cada hito, semana en etiqueta, nombre en 14 pt peso 600 y 1 línea de descripción |
| **L10 Tabla** | Detalle que se compara en filas | Crema | Título; tabla según la sección 6 |
| **L11 Captura + texto** | Mostrar el producto | Crema | Captura en tarjeta con radio de 10 pt ocupando 7 columnas; a la derecha, 3 puntos cortos que explican lo que se ve |
| **L12 Opciones de precio** | Inversión en niveles | Crema | Título; 3 tarjetas iguales; la del medio es la tarjeta negra con pill "Recomendado" y el precio en dorado; en cada una, etiqueta del nivel, precio de 28 pt, 1 línea de descripción, divisor y máx. 3 viñetas de lo que incluye; la nota de lo que no incluye va en el pie o debajo en 11 pt `gris` |
| **L13 Cierre** | Siguiente paso y contacto | Negro | Título con la acción concreta (32–40 pt); 1 línea de detalle; nombre del contacto en dorado de 16 pt peso 600; teléfono y correo en crema de 12 pt; `logo-oscuro` |

---

## 9. Cómo producirla según el formato

Primero decide el formato con las reglas generales: un deck nuevo sin formato pedido se hace con el tipo de artifact **Slides** cuando exista; un .pptx o un PDF, solo si el usuario lo pide.

**A. Tipo de artifact Slides (por defecto).** Crea el deck con el tipo Slides y sigue sus instrucciones. Aplica los tokens de las secciones 2–4 a su tema, sus fuentes y sus colores. Construye cada slide con los layouts de la sección 8. Si el tipo trae un sistema de diseño por defecto, **reemplázalo** con este estilo.

**B. HTML → PDF** (cuando piden PDF directo). Cada slide es un `<section>` de 960 × 540 px, con 1 px = 1 pt. Se renderiza con Playwright/Chromium en `page.pdf({width:'960px', height:'540px', printBackground:true})`. Base de CSS:

```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
:root{--crema:#F7F3E8;--papel:#FFFCF3;--negro:#141414;--dorado:#D4A018;--dorado-p:#86660C;
--gris:#5E5A52;--gris-o:#A7A196;--gris-dato:#CFC8B8;--linea:#DDD6C6;--linea-o:#3A3833}
@page{size:960px 540px;margin:0}
body{margin:0;font-family:Poppins,"Segoe UI",Arial,sans-serif}
.slide{width:960px;height:540px;position:relative;overflow:hidden;box-sizing:border-box;
padding:40px 48px 56px;display:flex;flex-direction:column;background:var(--crema);color:var(--negro);page-break-after:always}
.slide.dark{background:var(--negro);color:var(--crema)}
.eb{font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--dorado-p)}
.dark .eb{color:var(--dorado)}
.h{font-size:32px;font-weight:700;letter-spacing:-.015em;line-height:1.12;margin:8px 0 0;text-wrap:balance}
.card{background:var(--papel);border:1px solid var(--linea);border-radius:10px;padding:20px 22px}
.card.ink{background:var(--negro);color:var(--crema);border-color:var(--negro)}
.pill{display:inline-block;background:var(--dorado);color:var(--negro);font-size:9.5px;font-weight:600;
letter-spacing:.1em;text-transform:uppercase;padding:3px 8px;border-radius:20px}
.ft{position:absolute;left:48px;right:48px;bottom:20px;display:flex;justify-content:space-between;
font-size:9.5px;letter-spacing:.04em;color:var(--gris)}
.dark .ft{color:var(--gris-o)}
```

Los logos se incrustan como `data:` URI (base64) para que el PDF no dependa de la red.

**C. PowerPoint (.pptx), solo si lo piden.** Lee primero la skill `pptx`. Tamaño de 13,333 × 7,5 in; los puntos de esta guía se usan tal cual. Fuente Poppins con fallback Segoe UI, y avísale al usuario que debe tener Poppins instalada o que se reemplazará. Las formas llevan borde de 1 pt y esquinas redondeadas de 10 pt, sin sombras ni efectos.

---

## 10. Prohibido

- Texto dorado `#D4A018` sobre fondo claro
- Tarjetas en todos los bloques, tarjetas solas alrededor de un párrafo o tarjetas anidadas
- Logo en cada slide, logo en cuadro blanco sobre negro o logo redibujado
- Sombras, degradados, glassmorphism, bordes de más de 1 pt (salvo la línea del cronograma)
- Emojis, fotos de stock, ilustraciones genéricas o íconos de varias familias
- Más de 4 slides negras de 10, o 3 negras seguidas
- Texto de cuerpo menor a 14 pt, texto justificado o centrado en slides de contenido
- Leyendas, cuadrículas o colores múltiples en gráficas
- Animaciones o transiciones decorativas

---

## 11. Revisión final

Antes de entregar, **renderiza el deck y míralo** (captura de cada slide o del PDF):

1. ¿El dorado aparece una sola vez como foco en cada slide y nunca como texto pequeño sobre crema?
2. ¿Hay 4 o menos slides negras, en portada, frase clave, cifra de impacto y cierre?
3. ¿Portada y cierre tienen el logo, y el resto tiene el pie con cliente y número?
4. ¿Nada se sale de los márgenes de 48/40 pt y no queda un hueco grande abajo en slides de gráfica o tarjetas?
5. ¿Las tarjetas de una fila son iguales y hay solo una tarjeta negra por slide?
6. ¿Todo el texto mide 14 pt o más, salvo etiquetas, pills y pie?
7. ¿Las gráficas tienen etiquetas directas, un solo color de foco y la fuente en el pie?