# Base de olores de código

Va siempre en el eje de estándares, aunque el proyecto no documente nada. Son olores de
Martin Fowler (*Refactoring*, cap. 3), traídos de la skill `code-review` de
[mattpocock/skills](https://github.com/mattpocock/skills) (MIT).

Dos reglas la gobiernan:

- **El proyecto manda.** Una norma documentada siempre gana; si el proyecto avala algo que
  la base marcaría, no se marca.
- **Siempre es criterio, nunca violación.** Cada olor se reporta como «posible <olor>»,
  nunca como error, y nunca pasa de 🟡. Lo que ya vigila una herramienta se omite.

Cada olor: *qué es* → *cómo se arregla*.

- **Nombre misterioso:** una función, variable o tipo cuyo nombre no dice qué hace o qué
  guarda, o que no usa la palabra del glosario. → Renombrar; si no sale un nombre honesto,
  el diseño está turbio.
- **Código duplicado:** la misma forma de lógica en más de un sitio del cambio. → Extraer
  la forma común y llamarla desde ambos.
- **Envidia de funcionalidad:** una función que usa más los datos de otro objeto que los
  suyos. → Moverla junto a los datos que envidia.
- **Grupos de datos:** los mismos campos o parámetros viajan siempre juntos (un tipo que
  quiere nacer). → Agruparlos en un tipo y pasar ese.
- **Obsesión por los primitivos:** un texto o número que representa un concepto del
  negocio que merece su propio tipo (un valor en pesos, un número de teléfono). → Darle un
  tipo pequeño propio.
- **Condicionales repetidos:** el mismo `if`/`match` sobre el mismo tipo en varios sitios.
  → Polimorfismo, o un solo diccionario que compartan.
- **Cirugía a escopetazos:** un cambio lógico obliga a tocar muchos archivos. → Reunir en
  un módulo lo que cambia junto.
- **Cambio divergente:** un archivo se toca por varias razones sin relación. → Separarlo
  para que cada módulo cambie por una sola razón.
- **Generalidad especulativa:** abstracciones, parámetros o ganchos para necesidades que
  la especificación no tiene. → Borrarlos; volver a lo simple hasta que haga falta.
- **Cadenas de mensajes:** navegación larga `a.b().c().d()` de la que no debería depender
  quien llama. → Esconder el recorrido detrás de una función del primer objeto.
- **Intermediario:** una clase o función que casi solo delega. → Quitarla y llamar al
  destino real.
- **Herencia rechazada:** una subclase que ignora o sobrescribe casi todo lo que hereda.
  → Quitar la herencia y usar composición.
