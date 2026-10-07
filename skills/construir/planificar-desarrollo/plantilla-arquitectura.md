# Plantilla de `docs/ARQUITECTURA.md`

Responde *cómo* se construye: qué va dónde, cómo se conectan las partes y en qué orden se
construye. Si el repositorio sale de `luptecx-plantilla`, la estructura base (`app/`,
`pruebas/`, `herramientas/`, `docs/`, `migraciones/`) ya está decidida: aquí solo va lo
propio del proyecto.

```markdown
# Arquitectura: <nombre del proyecto>

## Estructura de archivos
<Árbol con una línea por archivo importante: qué responsabilidad tiene.>

## Flujo de datos
### <Camino principal, por ejemplo: llega un lote por WhatsApp>
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

## Plan de piezas
| # | Pieza (comportamiento) | Depende de | Criterios (RF) | Costura | Estado |
|---|---|---|---|---|---|
| 1 | <El dueño manda `M1 190k` y recibe el resumen del lote> | — | RF-01, RF-03 | `procesar_mensaje` | ⬜ |
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
