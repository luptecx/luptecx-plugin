---
name: entrevistar
description: Entrevista implacable sobre un plan, una decisión o una idea hasta que no quede nada supuesto. Úsala cuando el usuario pida que lo entrevisten o le hagan preguntas («entrevístame», «hazme preguntas», «grill me», «ayúdame a aterrizar esto»), cuando haya que definir qué se va a construir o cambiar y falten decisiones, o cuando otra skill necesite cerrar decisiones con el usuario antes de seguir.
---

# Entrevistar

Entrevista al usuario hasta llegar a un entendimiento compartido. La regla de oro: **nunca
asumas.** Una pregunta de más cuesta un minuto; una suposición equivocada se descubre tres
piezas después.

## El árbol de decisiones

Piensa el tema como un **árbol de decisiones**: cada decisión abre las que dependen de ella.
La **frontera** son las decisiones cuyas dependencias ya están resueltas: las preguntas que
se pueden hacer *ahora* sin adivinar respuestas que todavía no has oído.

Trabaja por **rondas**. En cada ronda pregunta toda la frontera junta, numera las preguntas
y da tu respuesta recomendada en cada una. Luego espera las respuestas.

```
❓ **P1 · <título de la pregunta>**: <la pregunta; puede tener varios párrafos y opciones>

➡️ <tu respuesta recomendada y por qué, en una o dos líneas>

---

❓ **P2 · <título>**: <pregunta>

➡️ <recomendación>
```

Redacta cada pregunta para que **«sí»** acepte tu recomendación: así el usuario responde
rápido lo que le parece bien y se detiene solo en lo que no.

Cada respuesta cambia el árbol: lo resuelto empuja la frontera hacia afuera y destapa las
preguntas que dependían de ello. Recalcula la frontera y haz la siguiente ronda. Una
pregunta que depende de otra que sigue abierta en esta misma ronda va en una ronda
*posterior*.

## Hechos y decisiones

- **Los hechos los buscas tú.** Lo que se puede averiguar mirando (el código, `docs/`, el
  `CLAUDE.md`, la especificación, la tarea de Notion, la configuración) no se le pregunta al
  usuario: se mira. Si puedes lanzar subagentes, manda uno a buscarlo y sigue con las
  preguntas que no dependen de ese dato; si no, búscalo tú antes de la ronda.
- **Las decisiones son del usuario.** Alcance, prioridades, qué incluye el servicio, qué
  pasa cuando algo falla, qué se deja fuera: se proponen con recomendación y se espera la
  respuesta.

Cuando una respuesta usa un término del negocio que no está claro, o que choca con el
glosario del proyecto, invoca `luptecx:modelar-dominio` para afinarlo y anotarlo.

## Cuándo termina

La entrevista termina cuando **la frontera está vacía**: cada rama del árbol visitada y
nada en silencio supuesto. Entonces:

1. Resume las decisiones tomadas, una por línea.
2. Pregunta si ese resumen es el entendimiento compartido.
3. No actúes sobre él hasta que el usuario lo confirme.
