# Plantilla de `docs/ARQUITECTURA.md`

Responde *cómo* se construye: qué va dónde, cómo se conectan las partes y en qué orden se
construye. Si el repositorio sale de la plantilla de procesos (`luptecx-plantilla`), lo
común ya está (en Python, `app/`, `pruebas/` y, si se despliega, `herramientas/`): aquí va
lo propio del proyecto, como su base de datos, sus integraciones y sus módulos.

```markdown
# Arquitectura: <nombre del proyecto>

## Estructura de archivos
<Árbol con una línea por archivo importante: qué responsabilidad tiene.>

## Flujo de datos
### <Camino principal, por ejemplo: llega un pedido nuevo>
1. …
2. …
### <Otros caminos: alertas programadas, comandos de administración>

## Modelo de datos
<Tablas o entidades, sus campos importantes y relaciones. Qué vive en nuestra base y qué
en sistemas del cliente.>

## Estados de la conversación
<Si es un bot: los estados, qué los dispara y a dónde lleva cada uno.>

## Decisiones de diseño
- **<Decisión>:** <por qué>. Las difíciles de revertir, además, en `docs/decisiones/`.

## Dependencias entre módulos
- `<módulo>` → depende de `<módulo>`, `<módulo>`

## Costuras de prueba
| Costura | Qué comportamiento prueba | Qué atrapa | Qué no atrapa |
|---|---|---|---|

## Amenazas y datos
<Con `luptecx:revisar-seguridad` (paso 1). Si el proyecto no recibe nada de afuera ni
guarda datos personales, una línea que lo diga.>

| Frontera | Qué entra | Riesgos (STRIDE) | Control | Prueba de abuso |
|---|---|---|---|---|

**Activos:** <…> · **Datos personales:** <qué, dónde, cuánto tiempo, cómo se borra> ·
**Proveedores que reciben datos:** <…>

## Plan de piezas
| # | Pieza (comportamiento) | Depende de | Criterios (RF) | Costura | Estado |
|---|---|---|---|---|---|
| 1 | <El cliente escribe su pedido y recibe el resumen con el total> | — | RF-01, RF-03 | `procesar_mensaje` | ⬜ |
| 2 | … | 1 | … | … | ⬜ |
```

Estados de una pieza: ⬜ pendiente · 🟡 en curso · ✅ hecha (con el hash del commit).

## Rebanadas verticales, no capas

Mal plan (por capas o por archivos): `excepciones.py` → `configuracion.py` →
`procesador.py` → `pruebas/` → `README`. Nada funciona hasta el final, las pruebas llegan
de últimas y cada pieza se construye contra una interfaz imaginada.

Buen plan (por comportamientos): cada pieza toca las capas que necesita y termina en algo
que se puede demostrar y probar. Los archivos de apoyo (excepciones, configuración) nacen
dentro de la primera pieza que los necesita.

Excepción: un cambio mecánico que toca todo el código (renombrar una columna, cambiar un
tipo compartido) no cabe en una rebanada. Se hace en tres tiempos: **expandir** (agregar lo
nuevo junto a lo viejo, sin romper nada), **migrar** los usos por tandas, cada una con la
suite en verde, y **contraer** (quitar lo viejo cuando nadie lo usa).
