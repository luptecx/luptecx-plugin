---
name: construir-por-piezas
description: Construir una pieza del plan de un proyecto, de la prueba al push. Úsala cuando haya un plan de piezas aprobado en `docs/ARQUITECTURA.md` y el usuario pida construir, seguir o empezar una pieza («sigamos con la pieza 3», «construye lo siguiente», «implementa esto según el plan»), o cuando una tarea ya especificada esté lista para programarse.
---

# Construir por piezas

Una pieza por vez: se construye, se explica, se revisa, se verifica y se sube antes de
pasar a la siguiente. Ladrillo a ladrillo, comprobando cada uno, en vez de pedir toda la
app y rezar.

## 1. Ubicar la pieza

1. `git pull --rebase` para partir de lo último.
2. Lee la pieza en el plan de `docs/ARQUITECTURA.md`: qué entrega, sus criterios, su
   costura y de qué depende. Comprueba que sus dependencias están ✅; si no, dilo y
   pregunta antes de seguir.
3. Lee los requisitos que cita en `docs/ESPECIFICACION.md`, el glosario y las decisiones
   del área que vas a tocar, y la interfaz de las piezas anteriores que vas a usar.
4. Márcala 🟡 en el plan y anuncia: «Pieza N de M: <título>».

Si el usuario pidió algo sin plan (una tarea suelta ya especificada), la «pieza» es esa
tarea y sus criterios son los de la tarea.

**Terminado cuando** puedes decir qué comportamiento queda funcionando al final y en qué
costura se prueba.

## 2. Construir con prueba primero

Invoca `luptecx:probar-primero` en la costura acordada. Mientras construyes, corre seguido
el archivo de pruebas que estás tocando; al final, la suite completa.

Si a mitad de la pieza descubres que la especificación está mal o le falta algo,
**detente**: no improvises un requisito. Plantéalo al usuario y, si cambia el
comportamiento, se actualiza la especificación antes de seguir. Si descubres un error en
una pieza anterior, dilo en ese momento, con su impacto y cómo corregirlo: la
transparencia vale más que parecer perfecto.

## 3. Explicar lo construido

Explícale al desarrollador, corto y concreto:

- Qué hace cada parte importante.
- Qué decisiones tomaste y por qué.
- Qué casos borde cubre y cuáles **no**.

Esto no es cortesía: es lo que construye el criterio de quien desarrolla. Si quiere más
detalle sobre algo, dáselo antes de seguir.

## 4. Revisar

Invoca `luptecx:revisar-cambios` con el punto fijo en el commit anterior a la pieza (u
`origin/main`). Atiende los hallazgos como dice esa skill. Si el informe recomienda
`/code-review`, ofrécelo.

**Terminado cuando** no queda ningún 🔴 y el usuario decidió qué hacer con los 🟠.

## 5. Verificar

Invoca `luptecx:verificar-antes-de-terminar` con la definición de terminado del proyecto.

## 6. Subir

1. Si la pieza cambió el comportamiento, una línea en `CHANGELOG.md`.
2. Commit con tipo, y en el cuerpo la pieza:
   ```
   funcionalidad: el bot resume el lote antes de confirmarlo

   Pieza 2 de 7 — resumen del lote
   ```
3. `git push`. El hook corre la suite; si falla, se arregla la causa. Nunca `--no-verify`.
4. Marca la pieza ✅ en el plan con el hash del commit. Si hay tarea en Notion, pon el
   enlace al commit.

## 7. La siguiente

Recomienda **limpiar el contexto** antes de la siguiente pieza: cada pieza está completa
en los documentos, así que la conversación anterior ya no hace falta y una sesión limpia
razona mejor. Di cuál es la siguiente pieza que ya se puede empezar.

## El desarrollador tiene la última palabra

Tú analizas y recomiendas; él decide si integra, cambia o descarta. Si algo te parece mal,
dilo aunque sea incómodo. Si decide saltarse un paso, se respeta y queda escrito como
riesgo asumido en el commit o en la tarea.
