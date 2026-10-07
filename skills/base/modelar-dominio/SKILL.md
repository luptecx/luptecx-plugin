---
name: modelar-dominio
description: Construir y afinar el vocabulario del negocio de un proyecto y registrar sus decisiones de diseño. Úsala al definir o discutir términos del cliente (qué es un conductor, un canon, un lote), al escribir o editar `docs/GLOSARIO.md`, al registrar o cambiar una decisión en `docs/decisiones/`, o cuando una conversación de diseño usa palabras ambiguas o contradictorias.
---

# Modelar el dominio

Construye el modelo del dominio **mientras** se diseña: cuestionar términos, inventar
escenarios límite y escribir el glosario y las decisiones en el momento en que se aclaran.
Solo *leer* `docs/GLOSARIO.md` para usar sus palabras no es esta skill: eso lo hace
cualquiera. Esta es para cuando el modelo cambia.

Por qué importa: con un vocabulario compartido, Claude nombra igual en la conversación, en
la especificación y en el código, gasta menos palabras en explicar y comete menos errores
de interpretación. «El lote del martes» dice en tres palabras lo que sin glosario lleva una
frase.

## Dónde vive

```
docs/
├── GLOSARIO.md              ← los términos del negocio del cliente
└── decisiones/
    ├── 0001-sheets-del-cliente-como-fuente.md
    └── 0002-martes-global-con-ajuste-manual.md
```

Crea los archivos solo cuando haya algo que escribir: el glosario con el primer término
resuelto, la carpeta con la primera decisión. Si el proyecto tiene varios contextos
claramente separados (dos bots distintos en un mismo repositorio), pregunta si van en
glosarios separados.

## Durante la sesión

- **Contrasta con el glosario.** Si el usuario usa un término que choca con
  `docs/GLOSARIO.md`, dilo en el momento: «El glosario define *canon* como el cobro
  semanal, pero aquí parece que hablas del total del mes. ¿Cuál es?»
- **Afina el lenguaje difuso.** Ante una palabra vaga o con dos sentidos, propón el término
  preciso: «Dices *cliente*: ¿el dueño de la flota que nos contrata o el conductor que paga
  el canon? Son dos cosas distintas.»
- **Pon escenarios concretos.** Cuando se discuten relaciones del dominio, ponlas a prueba
  con casos límite inventados que obliguen a precisar dónde termina un concepto y empieza
  otro: «Si un conductor cambia de moto a mitad de semana, ¿el canon de esa semana es de
  cuál moto?»
- **Contrasta con el código.** Si el usuario dice cómo funciona algo, comprueba si el
  código está de acuerdo. Si no, muéstralo: «El código registra un lote completo o nada,
  pero acabas de decir que se pueden confirmar líneas sueltas. ¿Cuál es la correcta?»
- **Actualiza el glosario en el momento**, sin acumular, con el formato de
  [formato-glosario.md](formato-glosario.md). El glosario no lleva detalles de
  implementación: no es especificación ni borrador. Es un glosario y nada más.

## Decisiones: pocas y buenas

Propón registrar una decisión solo si se cumplen **las tres** condiciones:

1. **Difícil de revertir:** cambiar de idea después cuesta de verdad.
2. **Sorprendente sin contexto:** quien lea el código dentro de un año se preguntará «¿por
   qué lo hicieron así?».
3. **Fruto de una elección real:** había alternativas genuinas y se eligió una por razones
   concretas.

Si falta una, no se registra. Formato y ejemplos en
[formato-decision.md](formato-decision.md).

Las **reglas de negocio** (cómo se calcula la fecha de cobro, qué se cobra aparte) van en
`docs/ESPECIFICACION.md`, con la fecha de la decisión del dueño, como ya se hace. En
`docs/decisiones/` van las decisiones **de diseño**: por qué está construido así.
