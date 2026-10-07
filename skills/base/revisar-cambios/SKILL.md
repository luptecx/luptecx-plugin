---
name: revisar-cambios
description: Revisión de un cambio en dos ejes, estándares del proyecto y especificación, contra un punto fijo. Úsala antes de hacer push de un cambio que toca `app/`, antes de desplegar (contra la última etiqueta), al terminar una pieza, cuando se pida revisar si un cambio cumple las normas o lo que se pidió, o cuando otra skill necesite revisar el proyecto entero. No es para cazar bugs línea por línea: eso es `/code-review`.
---

# Revisar cambios

Revisa un cambio desde un **punto fijo** en dos ejes, por separado:

- **Estándares:** ¿está escrito como el proyecto dice que se escribe?
- **Especificación:** ¿hace lo que se pidió, ni más ni menos?

Un cambio puede pasar un eje y fallar el otro. Si sigue todas las normas pero hace otra
cosa, falla la especificación aunque cumpla los estándares. Si hace justo lo pedido pero
rompe las convenciones, pasa la especificación pero falla los estándares. Por eso se
revisan y se reportan aparte: mezclados, un eje tapa al otro.

## Esta revisión y `/code-review`

Son complementarias y no se reemplazan:

| | `luptecx:revisar-cambios` | `/code-review` de Claude Code |
|---|---|---|
| Pregunta | ¿Cumple nuestras normas y la especificación? | ¿Hay bugs de corrección? |
| Lee | El diff + `CLAUDE.md`, estándares, especificación, decisiones | El diff |
| Cuándo | En cada cambio, antes del push y antes de desplegar | Cuando el cambio toca lógica delicada |

Esta skill **no** caza bugs línea por línea. Si el cambio toca dinero, fechas, el webhook,
la deduplicación o datos del cliente, termina el informe recomendando correr también
`/code-review` sobre el mismo cambio. No reimplementes aquí lo que hace esa revisión.

## 1. Fijar el punto y el alcance

| Momento | Punto fijo |
|---|---|
| Antes del push (por defecto) | `origin/main`, después de `git fetch` |
| Antes de desplegar | La última etiqueta: `git describe --tags --abbrev=0` |
| Al terminar una pieza | El commit anterior a la pieza |
| Lo que diga el usuario | Un commit, una etiqueta, una rama |
| Proyecto entero (lo pide `cierre-de-proyecto`) | Todo el código versionado de la aplicación y sus herramientas |

Con un punto fijo `P`:

- El cambio es `git diff P` (incluye lo que aún no tiene commit), más los archivos nuevos
  sin seguimiento que muestre `git status --short` (`??`): léelos aparte, porque el diff
  no los incluye.
- La lista de commits es `git log P..HEAD --oneline`.

Antes de seguir, comprueba que `P` existe (`git rev-parse P`) y que el cambio no está
vacío. Un punto malo o un diff vacío se detectan aquí, no a mitad de la revisión.

## 2. Reunir las fuentes

**Especificación**, en este orden:

1. `docs/ESPECIFICACION.md` y, si se está construyendo por piezas, la pieza en el plan de
   `docs/ARQUITECTURA.md`.
2. Las **invariantes** del `CLAUDE.md` («reglas que no se pueden romper») y
   `docs/decisiones/`.
3. La tarea de Notion o el issue de GitHub citados en los commits o en la conversación.
4. Si no hay nada, pregunta. Si no existe especificación, este eje se omite y el informe
   lo dice: «sin especificación».

**Estándares:**

1. El `CLAUDE.md` del proyecto (idioma, cómo se trabaja, invariantes, comandos) y
   cualquier `CONTRIBUTING.md` o guía de estilo dentro de los módulos (por ejemplo, la guía
   de mensajes al cliente).
2. La skill `luptecx:luptecx-codigo`, si está instalada: las convenciones de la empresa.
3. Siempre, aunque nada esté documentado: **ningún secreto ni dato real de clientes en el
   cambio** (🔴 si aparece), y la [base de olores de código](base-de-olores.md).

Omite lo que ya vigila una herramienta (el hook de commit, `ruff`, el formateador).

## 3. Revisar cada eje

Si puedes lanzar subagentes, lanza los dos en paralelo, cada uno solo con su contexto, para
que no se contaminen. Si no, hazlos tú **uno detrás de otro, con listas separadas**:
termina el de estándares antes de abrir la especificación.

**Eje de estándares.** Recibe: el diff y la lista de commits, las fuentes de estándares y
la base de olores completa. Encargo: «Reporta, por archivo y línea, (a) cada sitio que
incumple una norma documentada, citando la norma (archivo y regla); y (b) cada olor de la
base que veas, nombrándolo y citando el código. Separa los incumplimientos de normas, que
pueden ser firmes, de los olores, que son siempre cuestión de criterio. Una norma del
proyecto anula la base. Omite lo que vigila una herramienta.»

**Eje de especificación.** Recibe: el diff y la lista de commits, y la especificación.
Encargo: «Reporta (a) lo pedido que falta o está a medias; (b) lo que nadie pidió (alcance
de más); (c) lo que parece implementado pero está implementado mal. Cita la línea de la
especificación en cada hallazgo. Comprueba una por una las invariantes que el cambio toca.»

## 4. Informe

Severidad, asignada dentro de cada eje:

- 🔴 **No se sube:** secreto o dato real en el cambio, una invariante rota, un requisito
  mal implementado que corrompe datos o le escribe al cliente equivocado.
- 🟠 **Se arregla antes de desplegar:** falta parte de lo pedido, alcance de más que
  cambia el comportamiento, una norma firme incumplida.
- 🟡 **Limpieza:** olores, nombres, duplicación pequeña. Un olor nunca pasa de 🟡.
- ⚪ **Opcional.**

```markdown
## Revisión · <punto fijo>..HEAD · <N> commits

### Estándares
| # | Sev. | Dónde | Norma u olor | Hallazgo | Propuesta |

### Especificación
| # | Sev. | Requisito (cita) | Falta · sobra · mal implementado | Propuesta |

**Estándares:** <N> hallazgos, el peor: <…> · **Especificación:** <N> hallazgos, el peor: <…>

**Veredicto:** se puede subir · se sube después de corregir los 🔴 · no se sube
<Si aplica: «Toca <dinero/fechas/webhook/datos>: corre también `/code-review`.»>
```

No mezcles ni reordenes los ejes entre sí, y no elijas un «peor de todos»: es la mezcla
que esta separación evita. Una tabla sin hallazgos dice «Nada que reportar». No inventes
hallazgos para llenar.

## 5. Atender los hallazgos

El que implementó y el que revisó responden al usuario; ninguno de los dos tiene la razón
por defecto.

1. **Lee todo antes de tocar nada.** Si algún hallazgo no está claro, pregunta primero:
   los hallazgos suelen estar relacionados y entender a medias lleva a arreglar mal.
2. **Verifica cada hallazgo contra el código** antes de aplicarlo. ¿Es correcto para
   *este* proyecto? ¿Rompe algo que funciona? ¿Hay una razón para cómo está?
3. **Si un hallazgo es incorrecto, dilo con evidencia** (el código, la prueba, la decisión
   registrada que lo justifica). Si choca con una decisión del usuario, se le pregunta a él.
4. **Si propone algo «más profesional» que nadie usa**, busca si se usa. Si no se usa, la
   respuesta es quitarlo, no completarlo.
5. **Arregla en orden:** 🔴, luego lo simple, luego lo complejo. Uno a la vez, con la
   prueba correspondiente en verde después de cada uno.
6. **Responde con hechos:** «Corregido: <qué cambió y dónde>». Sin agradecimientos ni
   «¡tienes toda la razón!»: el código muestra que se atendió.

Si el usuario decide no arreglar algo, queda escrito en el informe como riesgo asumido.
