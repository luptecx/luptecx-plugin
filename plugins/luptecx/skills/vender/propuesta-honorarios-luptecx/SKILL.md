---
name: "propuesta-honorarios-luptecx"
description: "Hacer una cotización de LUPTECX (propuesta de honorarios) en PDF tipo carta comercial: alcance, desglose de precios, forma de pago, condiciones y firma de aceptación. Úsala solo cuando un cliente o posible cliente pida una cotización o haya que mandarle una propuesta de honorarios («hazme la cotización para…», «cotízale a…», «nos pidieron precios», «la propuesta de honorarios de…»). No es la presentación de ventas ni el contrato."
---

# Cotización (propuesta de honorarios) LUPTECX

Esta skill hace **cotizaciones**: el documento con qué se haría, cuánto cuesta cada concepto
y en qué condiciones, para un cliente que pidió precios o que ya conversó el precio y
necesita la propuesta de honorarios formal. Es una carta comercial en PDF tamaño carta, de
2 a 3 páginas, con membrete de LUPTECX. El cliente la acepta firmando; el contrato viene
después, con `luptecx:luptecx-contrato-servicio`.

**No es una presentación.** No usa el estilo de las slides (`luptecx-estilo-visual`): sin fondos negros, tarjetas, cifras gigantes ni portada. Debe verse como un documento de una firma de servicios profesionales: blanco, sobrio, texto corrido, secciones numeradas y tablas de líneas finas.

**Cuándo usarla:** solo para cotizaciones y propuestas de honorarios, de uno o varios
servicios (un asistente o agente, una automatización, un desarrollo, publicidad).

**Cuándo no:**
- **Para convencer a un cliente que todavía no decide:** eso es la presentación de ventas
  (`luptecx:presentacion-ventas-contenido`).
- **Para el contrato:** `luptecx:luptecx-contrato-servicio`. La cotización firmada es una
  aceptación comercial, no un contrato revisado por un abogado.

---

## Paso 1 · Reunir la información

Primero revisa lo que ya existe: la conversación, el cliente en el CRM de Notion, sus
reuniones y la presentación de ventas que se le mostró. Después pregunta **en una sola
tanda** lo que falte. Usa AskUserQuestion si está disponible.

**Los precios salen del Portafolio** de Notion, igual que en
`presentacion-ventas-contenido` (Paso 5): la ficha del producto, con sus tres niveles. Si el
producto no tiene ficha o le falta un precio, se pregunta y, con el permiso del usuario, se
escribe en la ficha antes de usarlo. Si el usuario quiere otro precio para este cliente, se
usa el suyo y se le dice cuál dice el Portafolio. Un servicio a la medida que no es un
producto lleva los precios que dé el usuario.

**Los datos de LUPTECX** (razón social, NIT, representante, dirección) salen de la sección
«Datos de LUPTECX» de `luptecx:luptecx-contrato-servicio`, la misma fuente del contrato. Lo
que diga `[POR CONFIRMAR]` va como marcador visible, nunca inventado.

| Dato | Pregunta | Si no hay respuesta |
|---|---|---|
| Destinatario | Nombre completo, cargo y empresa de quien recibe y firma | `[Apellido]`, `[Cargo]` |
| Servicios | ¿Qué servicios entran? | No se arma sin esto |
| Quién presta cada servicio | Si hay un aliado (por ejemplo, la publicidad): ¿va bajo LUPTECX y lo cobra LUPTECX, o se cobra aparte? | Pregunta siempre |
| Precio de cada concepto | Pago único y mensualidad de cada servicio, del Portafolio | `[PRECIO]` y avisar |
| IVA | ¿Precios con IVA incluido, más IVA, o LUPTECX no es responsable de IVA? | `[IVA por confirmar con el contador]` |
| Forma de pago | ¿50/50 el pago único? ¿Mensualidad anticipada? | La del Paso 4, avisando |
| Permanencia | ¿Sin permanencia o con un mínimo de meses? | Pregunta siempre |
| Número y vigencia | ¿Qué consecutivo sigue? ¿Cuántos días vale la oferta? | `LTX-AAAA-[NNN]`, 30 días |
| Datos de LUPTECX | Los de `luptecx-contrato-servicio` | `[Razón social]`, `[NIT]` |
| Quién firma por LUPTECX | Nombre y cargo | El representante legal |
| Contexto del cliente | Datos de la reunión para el entendimiento de la necesidad | Solo lo conocido |

Reglas:
- **Nunca inventes precios, cifras del cliente, el NIT ni condiciones.** Usa marcadores visibles y lístalos al entregar.
- Los precios deben coincidir con lo que se le presentó al cliente. Si hay diferencia, pregunta.
- Por defecto, todo va bajo LUPTECX. Un aliado se nombra solo si el usuario lo pide, y lo
  que gana el aliado (`aliados.md` de `luptecx-cierre-mensual`) **nunca** va en la cotización:
  es un acuerdo interno.

---

## Paso 2 · Estructura y contenido

La propuesta se lee de corrido, de arriba abajo. **Objetivo: 2 a 3 páginas.** Si pasa de 3, se resume.

**Encabezado (primera página):**
1. **Membrete:**
   - a la izquierda, el logo;
   - a la derecha, la razón social de LUPTECX, NIT, ciudad, teléfono, correo y web;
   - debajo, una línea dorada fina.
2. **Ciudad y fecha:** `Bogotá D.C., 20 de octubre de 2026`.
3. **Destinatario:** tratamiento (Señor/Señora), nombre en negrita, cargo, empresa y ciudad, cada uno en su línea.
4. **Referencia:** `Propuesta de honorarios N.º LTX-AAAA-NNN · [servicios]`, entre dos líneas finas.
5. **Saludo:** `Respetado señor [Nombre]:`.
6. **Párrafo de introducción:** agradecer la reunión, decir qué se propone y qué encontrará el lector. Máximo 3 líneas.

**Secciones numeradas:**

| N.º | Sección | Contenido | Extensión |
|---|---|---|---|
| 1 | Entendimiento de la necesidad | La situación del cliente con sus datos, sin adjetivos | 1 párrafo, máx. 5 líneas |
| 2 | Objeto | Qué se va a hacer, en una frase | 1–2 líneas |
| 3 | Alcance de los servicios | Un subtítulo por servicio (3.1, 3.2…) con lo incluido en viñetas, y un último subtítulo **"No incluye"** | Máx. 5 viñetas por servicio |
| 4 | Honorarios | Tabla de desglose y nota de moneda, IVA y pauta | Ver Paso 4 |
| 5 | Forma de pago | Pago único, mensualidad y medio de pago | 3 viñetas |
| 6 | Plan de trabajo | Tabla: semana · actividades · lo que se requiere del cliente | 3–5 filas |
| 7 | Condiciones generales | Viñetas con título en negrita | Máx. 7 viñetas |
| 8 | Aceptación | Una frase de aceptación, "Cordialmente," y las dos firmas | — |

Los honorarios van **justo después del alcance**: el lector ve qué recibe y enseguida cuánto cuesta. Con un solo servicio, la sección 3 no lleva subtítulos.

---

## Paso 3 · Redacción

- **Tono formal y directo**: "usted" para el cliente; "LUPTECX" o "nosotros" para la empresa. Nada de lenguaje de venta ("increíble", "revolucionario", "potenciamos").
- **Títulos de sección descriptivos** ("Alcance de los servicios"). Aquí no se usan títulos-conclusión: es un documento, no una presentación.
- **Sin jerga técnica**: "responde por WhatsApp", no "webhook", "LLM" ni "API".
- **Plazos y cantidades contractuales en letras y número**: `cinco (5) días`, `treinta (30) días calendario`.
- **Pesos:** punto de miles y sin decimales. En las tablas, la moneda va en el encabezado (`Pago único (COP)`) y las celdas solo llevan la cifra: `3.500.000`.
- **Promesas solo de lo que depende de LUPTECX.** Nunca garantizar ventas ni cantidad de clientes.
- Párrafos de máx. 5 líneas; viñetas de máx. 2 líneas.

---

## Paso 4 · Honorarios, pago y condiciones

**Tabla de honorarios:**
- Columnas: `Concepto` · `Pago único (COP)` · `Mensual (COP)`.
- Una fila de grupo por servicio y, debajo, sus conceptos. Cada concepto lleva una línea de descripción en gris.
- "—" donde no aplica.
- Una fila **Total**, con doble línea gruesa y fondo suave. Si hay IVA aparte, van filas "Subtotal", "IVA (19 %)" y "Total".
- **Todas las sumas con código**, nunca de memoria.
- Un concepto opcional va marcado "(opcional)" y no se suma.
- Debajo, la nota: "Valores en pesos colombianos", la línea de IVA y la pauta sugerida si aplica.

**Forma de pago por defecto** (confirmar con el usuario):
- **Pago único:** 50 % a la aceptación y 50 % a la salida en vivo.
- **Mensualidad:** por anticipado, dentro de los primeros cinco (5) días de cada mes, desde la salida en vivo.
- **Medio:** transferencia a la cuenta de LUPTECX, contra cuenta de cobro o factura electrónica.

**Condiciones generales por defecto** (confirmar con el usuario; quitar las que no apliquen):
1. **Duración y terminación:** según la permanencia acordada. Si no hay, cualquiera de las partes termina con aviso escrito de treinta (30) días.
2. **Obligaciones del cliente:** accesos, información, contenido y atención a los clientes remitidos.
3. **Resultados:** LUPTECX responde por la prestación del servicio. El cierre de ventas depende del equipo del cliente.
4. **Propiedad:** el desarrollo es de LUPTECX y se presta como servicio. Los datos, números y cuentas publicitarias son del cliente.
5. **Datos personales:** el cliente es responsable y LUPTECX es encargado del tratamiento (Ley 1581 de 2012).
6. **Confidencialidad.**
7. **Vigencia de la oferta:** treinta (30) días calendario desde la fecha.

Al entregar, recuérdale al usuario que el IVA, la retención y las condiciones legales conviene validarlos con el contador o un abogado.

---

## Paso 5 · Diseño

| Elemento | Especificación |
|---|---|
| Página | Carta (8,5 × 11 in). Márgenes: 22 mm arriba y a los lados, 24 mm abajo. Fondo blanco. |
| Tipografía | **Títulos, membrete, tablas (encabezados) y referencia:** Poppins 600. **Cuerpo:** Source Serif 4, 10,5 pt, interlineado 1,45. Nada por debajo de 7,5 pt. |
| Color | Texto `#1A1A1A`; secundario `#5E5A52`; líneas `#D9D4C7`; fondo de encabezados de tabla y fila total `#F6F4EF`. **Dorado solo en dos lugares:** la línea del membrete (`#D4A018`) y el número de cada sección (`#86660C`). |
| Secciones | Título de 11,5 pt con su número en dorado y una línea fina debajo. Subtítulos de 9,5 pt. |
| Tablas | Sin bordes verticales. Encabezado en mayúsculas pequeñas sobre fondo suave, con línea negra debajo. Filas separadas por líneas finas. Números alineados a la derecha, en cifras tabulares. Una tabla nunca se parte entre páginas. |
| Pie (todas las páginas) | `LUPTECX · Cotización LTX-AAAA-NNN` a la izquierda; `Página X de Y` a la derecha. |
| Prohibido | Fondos de color o negros, tarjetas, sombras, íconos, cifras grandes, portada, más de un color de acento. |

**Logo:** usa `logo-claro.png` de la guía de estilo (Artifact `action: "read"`, `url: https://claude.ai/artifact/DVYbGuTpXnKVdiXzbCLcfY`, `path: "logo-claro.png"`). Cópialo a la carpeta de la propuesta. Nunca lo redibujes. Si no se puede descargar, pídeselo al usuario.

### Plantilla

Trabaja en una carpeta propia (`propuesta-<cliente>/`). Guarda esto como `propuesta.html` y reemplaza lo que está entre corchetes. No cambies el CSS salvo para un ajuste puntual.

```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Propuesta de honorarios LTX-AAAA-NNN · [Cliente]</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<style>
:root{--tinta:#1A1A1A;--gris:#5E5A52;--linea:#D9D4C7;--suave:#F6F4EF;--dorado:#D4A018;--dorado-p:#86660C}
@page{size:letter;margin:22mm 22mm 24mm 22mm}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Source Serif 4",Georgia,serif;font-size:10.5pt;line-height:1.45;color:var(--tinta);background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.mem{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:10px;border-bottom:1.5px solid var(--dorado)}
.mem img{height:46px}
.mem .emp{font-family:Poppins,Arial,sans-serif;font-size:7.5pt;line-height:1.5;color:var(--gris);text-align:right}
.mem .emp b{font-weight:600;color:var(--tinta);letter-spacing:.06em}
.carta{margin-top:22px}
.carta p{margin-top:0}
.carta p+p{margin-top:8px}
.fecha{margin-bottom:16px}
.dest{margin-bottom:14px;line-height:1.4}
.ref{margin:14px 0;padding:8px 0;border-top:1px solid var(--linea);border-bottom:1px solid var(--linea);font-family:Poppins,Arial,sans-serif;font-size:9pt}
.ref b{font-weight:600}
p{margin-top:7px;text-align:left;hyphens:auto}
h2{font-family:Poppins,Arial,sans-serif;font-size:11.5pt;font-weight:600;margin:20px 0 4px;padding-bottom:4px;border-bottom:1px solid var(--linea);break-after:avoid}
h2 .num{color:var(--dorado-p);margin-right:8px}
h3{font-family:Poppins,Arial,sans-serif;font-size:9.5pt;font-weight:600;margin:12px 0 2px;break-after:avoid}
ul{margin:5px 0 0 18px}
li{margin-top:3px;padding-left:2px}
li::marker{color:var(--gris)}
table{width:100%;border-collapse:collapse;margin-top:8px;font-size:9.5pt;break-inside:avoid}
th{font-family:Poppins,Arial,sans-serif;font-size:7.5pt;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--gris);text-align:left;padding:6px 8px;background:var(--suave);border-bottom:1px solid var(--tinta)}
td{padding:6px 8px;border-bottom:1px solid var(--linea);vertical-align:top}
.n{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
tr.grupo td{font-family:Poppins,Arial,sans-serif;font-size:8pt;font-weight:600;padding-top:10px;border-bottom:0}
tr.sub td{font-weight:600}
tr.total td{font-weight:600;border-top:1.5px solid var(--tinta);border-bottom:1.5px solid var(--tinta);background:var(--suave)}
td .d{display:block;color:var(--gris);font-size:8.5pt;line-height:1.35}
.nota{font-size:8.5pt;color:var(--gris);margin-top:6px}
.firmas{display:grid;grid-template-columns:1fr 1fr;gap:48px;margin-top:46px;break-inside:avoid}
.firmas div{border-top:1px solid var(--tinta);padding-top:6px;font-size:9.5pt;line-height:1.4}
.firmas span{color:var(--gris);font-size:8.5pt}
.cierre{margin-top:18px;break-inside:avoid}
</style>
</head>
<body>

<div class="mem">
  <img src="logo-claro.png" alt="LUPTECX">
  <div class="emp"><b>[Razón social]</b><br>NIT [NIT] · Bogotá D.C., Colombia<br>[celular] · [correo]@luptecx.com · luptecx.com</div>
</div>

<div class="carta">
  <p class="fecha">Bogotá D.C., [día] de [mes] de [año]</p>
  <p class="dest">[Señor/Señora]<br><b>[Nombre completo]</b><br>[Cargo]<br>[Empresa]<br>[Ciudad]</p>
  <div class="ref"><b>Referencia:</b> Propuesta de honorarios N.º LTX-AAAA-NNN · [Servicios]</div>
  <p>Respetado [señor/señora] [Nombre]:</p>
  <p>[Agradecimiento, qué se propone y qué encontrará en el documento. Máx. 3 líneas.]</p>
</div>

<h2><span class="num">1.</span>Entendimiento de la necesidad</h2>
<p>[Situación del cliente con sus datos. Máx. 5 líneas.]</p>

<h2><span class="num">2.</span>Objeto</h2>
<p>[Qué se va a hacer, en una frase.]</p>

<h2><span class="num">3.</span>Alcance de los servicios</h2>
<h3>3.1 [Servicio A]</h3>
<ul><li>[Incluye]</li><li>[Incluye]</li></ul>
<h3>3.2 [Servicio B]</h3>
<ul><li>[Incluye]</li><li>[Incluye]</li></ul>
<h3>3.3 No incluye</h3>
<ul><li>[Exclusión]</li><li>[Exclusión]</li></ul>

<h2><span class="num">4.</span>Honorarios</h2>
<table>
  <thead><tr><th>Concepto</th><th class="n" style="width:20%">Pago único (COP)</th><th class="n" style="width:20%">Mensual (COP)</th></tr></thead>
  <tbody>
    <tr class="grupo"><td colspan="3">[Servicio A]</td></tr>
    <tr><td>[Concepto]<span class="d">[Qué incluye]</span></td><td class="n">[0.000.000]</td><td class="n">—</td></tr>
    <tr><td>[Concepto]<span class="d">[Qué incluye]</span></td><td class="n">—</td><td class="n">[0.000.000]</td></tr>
    <tr class="grupo"><td colspan="3">[Servicio B]</td></tr>
    <tr><td>[Concepto]<span class="d">[Qué incluye]</span></td><td class="n">[0.000.000]</td><td class="n">—</td></tr>
    <tr><td>[Concepto]<span class="d">[Qué incluye]</span></td><td class="n">—</td><td class="n">[0.000.000]</td></tr>
    <tr class="total"><td>Total</td><td class="n">[0.000.000]</td><td class="n">[0.000.000]</td></tr>
  </tbody>
</table>
<p class="nota">Valores en pesos colombianos. [Línea de IVA]. [Pauta sugerida, si aplica.]</p>

<h2><span class="num">5.</span>Forma de pago</h2>
<ul>
  <li><b>Pago único:</b> [ … ]</li>
  <li><b>Mensualidad:</b> [ … ]</li>
  <li><b>Medio:</b> [ … ]</li>
</ul>

<h2><span class="num">6.</span>Plan de trabajo</h2>
<table>
  <thead><tr><th style="width:18%">Semana</th><th>Actividades</th><th style="width:34%">Lo que requerimos del cliente</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>[Actividades]</td><td>[Requerimiento]</td></tr>
    <tr><td>2</td><td>[Actividades]</td><td>[Requerimiento]</td></tr>
  </tbody>
</table>

<h2><span class="num">7.</span>Condiciones generales</h2>
<ul>
  <li><b>[Condición]:</b> [ … ]</li>
</ul>

<h2><span class="num">8.</span>Aceptación</h2>
<p>La firma de este documento constituye la aceptación del alcance, los honorarios y las condiciones aquí descritos.</p>
<div class="cierre">
  <p>Cordialmente,</p>
  <div class="firmas">
    <div><b>[Nombre]</b><br>[Cargo]<br><span>[Razón social]</span></div>
    <div><b>Acepto,</b><br>Nombre y C.C.: ________________________<br><span>[Empresa del cliente] · Fecha: ____________</span></div>
  </div>
</div>

</body>
</html>
```

---

## Paso 6 · Renderizar a PDF

Guarda este script como `render_doc.py`, fuera de la carpeta de la propuesta. Úsalo con:

```
python3 render_doc.py propuesta-<cliente>/propuesta.html LTX-AAAA-NNN
```

El script hace tres cosas:
- genera el PDF con el pie numerado;
- crea una imagen por página (`pagina-1.png`, `pagina-2.png`…) para revisar;
- usa Chromium, que ya viene con Playwright (no ejecutes `playwright install`), y `pdftoppm` (de poppler-utils).

```python
import sys, pathlib, subprocess
from playwright.sync_api import sync_playwright

html = pathlib.Path(sys.argv[1]).resolve()
numero = sys.argv[2] if len(sys.argv) > 2 else ""
pdf = html.with_suffix(".pdf")
pie = ('<div style="width:100%;font-family:Arial,sans-serif;font-size:7.5pt;color:#5E5A52;'
       'padding:0 22mm;display:flex;justify-content:space-between">'
       f'<span>LUPTECX · Cotización {numero}</span>'
       '<span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>')
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto(html.as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.pdf(path=str(pdf), format="Letter", print_background=True, prefer_css_page_size=True,
           display_header_footer=True, header_template="<span></span>", footer_template=pie)
    b.close()
subprocess.run(["pdftoppm", "-png", "-r", "80", str(pdf), str(html.parent / "pagina")], check=True)
print(pdf)
```

Si Google Fonts no carga (sin red), instala `@fontsource/poppins` y `@fontsource/source-serif-4` con npm. Luego declara los `.woff2` con `@font-face` en el `<style>`.

---

## Paso 7 · Revisión antes de entregar

Mira **cada página** con la herramienta Read y verifica:

1. ¿Son 2 a 3 páginas, sin huecos grandes en blanco? Si una tabla saltó de página y dejó media página vacía, reordena o recorta texto.
2. ¿Ninguna tabla está partida entre páginas, ni hay un título solo al final de una página?
3. ¿La suma de cada columna es igual al total? Verifícalo con código. ¿Los precios coinciden con los que se le presentaron al cliente?
4. ¿El dorado aparece solo en la línea del membrete y en los números de sección?
5. ¿El número de propuesta es el mismo en la referencia y en el pie? ¿La fecha y la vigencia son coherentes?
6. ¿Quedan marcadores entre corchetes? Si sí, lístalos para el usuario.
7. ¿Hay alguna frase que prometa ventas o que suene a anuncio? Quítala.

---

## Paso 8 · Entrega y versiones

- Nombre del archivo: `Cotizacion-LUPTECX-<Cliente>-<NNN>.pdf`. Envíalo con SendUserFile. Si hay una carpeta conectada en el computador del usuario, guárdalo también ahí.
- **Nunca sobrescribas una versión anterior.** Cada cambio va en un archivo nuevo (`…-v2`), y se guarda el HTML de cada versión.
- **Nunca borres archivos sin preguntar.**
- **Rastro en Notion:** en el CRM, el cliente pasa a **Propuesta Enviada** (si estaba antes
  en el embudo), Ultimo Contacto = hoy, y en su ficha una línea con el número de la
  cotización, los totales y la vigencia. Si el usuario todavía no la va a enviar, se anota
  igual y se dice «sin enviar».
- En la respuesta, en pocas líneas:
  - qué incluye la propuesta y los totales;
  - los marcadores pendientes;
  - el recordatorio sobre el IVA y las condiciones legales.
