---
name: luptecx-contrato-servicio
description: Armar el contrato de prestación de servicios de LUPTECX para un cliente que aceptó la propuesta. Úsala cuando el usuario diga «hagamos el contrato», «el cliente aceptó, mándale el contrato», «necesito el contrato de…», o cuando haya que cambiar las Condiciones Generales o el anexo de datos personales después de la revisión del abogado.
---

# Contrato de servicio

El contrato tiene tres partes, siempre las mismas:

| Parte | Qué es | Cambia |
|---|---|---|
| [Carátula](caratula.md) | Lo de este cliente: partes, producto, alcance, precios, plazo, horario, datos personales | En cada contrato |
| [Condiciones Generales](condiciones-generales.md) | Las reglas de LUPTECX: qué incluye la mensualidad, tiempos de respuesta, pagos, propiedad, salida, responsabilidad | Solo cuando las revisa el abogado |
| [Anexo de Transmisión de Datos Personales](anexo-datos-personales.md) | Lo que pide la Ley 1581 cuando LUPTECX trata datos de los clientes del cliente | Sus campos, en cada contrato que lo lleve |

El Word lo arma el generador de documentos del plugin,
[`herramientas/md_a_word.py`](../../../herramientas/md_a_word.py).

> **Hoy es un borrador.** Mientras las Condiciones Generales digan «Borrador pendiente de
> revisión legal», el contrato **no se manda a firmar**: se le lleva al abogado. Cada
> página lo dice, y lo pendiente sale resaltado en amarillo.

## 1. Lo que se vendió

Necesitas la propuesta aceptada (de `luptecx:presentacion-ventas-contenido`), el producto y
sus precios en el Portafolio de Notion, y el diagnóstico (Reuniones). Si el cliente no ha
aceptado, no hay contrato.

**Terminado cuando:** tienes la propuesta aceptada y el producto con su nivel.

## 2. Los datos de la carátula

Un valor por cada `{{campo}}` de la carátula (y del anexo, si el producto trata datos
personales):

| Datos | De dónde |
|---|---|
| Producto, nivel, alcance, qué no incluye, plan, entrega, precios y forma de pago | La propuesta aceptada. Los precios se cruzan con el Portafolio: si no coinciden, se pregunta |
| Razón social, NIT, representante, dirección y correo del cliente | El cliente. Si faltan, se le piden con `luptecx:luptecx-comunicacion-cliente` |
| Los mismos de LUPTECX | La sección «Datos de LUPTECX» de abajo |
| Horario, canales, días de pago, plazo inicial, franja sin mantenimiento | El usuario, para este cliente |
| Datos personales, titulares, datos, finalidades, dónde se guardan, proveedores | La especificación del proyecto o el diagnóstico; los proveedores son los que tocan los datos (las plataformas que usa el producto y el servidor) |
| Si autoriza mencionarlo como referencia | Se le pregunta al cliente; por defecto, «No» |

Un dato que nadie sabe va como `[POR CONFIRMAR: …]`, nunca vacío ni inventado. Escribe
los valores en `datos.json`, en una carpeta del cliente **fuera de cualquier repositorio**
(los datos del cliente no van a git).

**Terminado cuando:** `datos.json` tiene todos los campos.

## 3. Generar el Word

Desde la carpeta de esta skill:

```powershell
uv run --script ..\..\..\herramientas\md_a_word.py --datos <ruta>\datos.json `
  --salida "<ruta>\Contrato <cliente> <fecha>.docx" `
  --encabezado "BORRADOR · Pendiente de revisión legal · No firmar sin aprobación" `
  caratula.md condiciones-generales.md anexo-datos-personales.md
```

Sin `anexo-datos-personales.md` si el producto no trata datos personales. Si el script
dice que faltan datos, vuelve al paso 2. Si no lo puedes correr (sin `uv` o sin permiso), dale al usuario
el comando con la ruta completa; **no armes el contrato a mano** ni hagas una copia en otro
formato: el texto sale siempre de los tres archivos de la skill.

**Terminado cuando:** el script dice «Word: …» y el número de pendientes.

## 4. Revisar antes de entregar

Lee el Word como lo leería el cliente:

- [ ] Precios, fechas y alcance coinciden con la propuesta aceptada.
- [ ] Lo que no incluye está escrito, sobre todo los costos de terceros (mensajería, IA, nube).
- [ ] La renovación, la terminación y la salida de los datos se entienden sin abogado.
- [ ] Si trata datos personales, el anexo está y los proveedores están listados.
- [ ] Cada `[POR CONFIRMAR]` tiene a quién preguntárselo.

**Terminado cuando:** la lista está completa.

## 5. Entregar

Dale al usuario el Word y, aparte, **los puntos para el abogado**: cada `[POR DEFINIR]` de
las Condiciones Generales y cualquier cosa que este cliente pidió distinta. Claude no se lo
manda al cliente ni al abogado.

Cuando el abogado devuelva las Condiciones Generales o el anexo revisados, se pasan aquí:
el texto nuevo, la versión (`1.0`), la fecha, y el comando del paso 3 sin el encabezado
de borrador. Ese cambio va en el plugin, con su commit, y vale para todos los
contratos siguientes.

## Datos de LUPTECX

| Campo | Valor |
|---|---|
| Razón social | [POR CONFIRMAR] |
| NIT | [POR CONFIRMAR] |
| Representante legal | [POR CONFIRMAR] |
| Dirección | [POR CONFIRMAR] |
| Correo para notificaciones | [POR CONFIRMAR] |
