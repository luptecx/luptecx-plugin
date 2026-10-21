# Formato de las decisiones (`docs/decisiones/`)

Numeración secuencial: `0001-titulo-corto.md`, `0002-titulo-corto.md`. Para el número
siguiente, mira el más alto que exista y súmale uno.

## Plantilla

```md
# <Título corto de la decisión>

<DD/MM/AAAA> · <quién decidió>

<De una a tres frases: el contexto, qué se decidió y por qué.>
```

Eso es todo. Una decisión puede ser un solo párrafo: lo que vale es dejar escrito *que* se
decidió y *por qué*, no llenar secciones.

## Secciones opcionales

Solo cuando aportan de verdad:

- **Estado** (`propuesta`, `aceptada`, `reemplazada por 0007`): cuando la decisión se
  revisa más adelante. Una decisión nunca se borra; se marca como reemplazada.
- **Alternativas consideradas**: solo si las descartadas vale la pena recordarlas.
- **Consecuencias**: solo si hay efectos no evidentes que alguien debe conocer.

## Qué sí merece una decisión

- **La forma de la arquitectura:** «Cada cliente tiene su propia hoja de cálculo y
  el servicio escribe ahí; no hay base de datos central.»
- **Elecciones con amarre:** base de datos, proveedor externo, servidor, forma de
  despliegue. No cada librería: solo las que costaría semanas cambiar.
- **Límites y alcance:** «Los datos de los usuarios viven en el sistema del cliente;
  nuestra base solo guarda el identificador.» Los *no* valen tanto como los *sí*.
- **Desvíos a propósito del camino obvio:** «SQL a mano en vez de ORM en el reporte
  porque…». Evitan que el siguiente «arregle» algo que era deliberado.
- **Restricciones que no se ven en el código:** «Los avisos solo salen por el canal que el
  proveedor aprobó, porque si no bloquea la cuenta.» «Nada se despliega entre 6:00 y 9:00
  porque es la hora de más uso.»
- **Alternativas rechazadas por razones sutiles:** si no se escriben, alguien las volverá a
  proponer en seis meses.

## Qué no

- Lo fácil de revertir: si cambias de idea, lo cambias y ya.
- Lo obvio: si no había alternativa real, no hay nada que contar.
- Las reglas de negocio del cliente: esas van en `docs/ESPECIFICACION.md`.
