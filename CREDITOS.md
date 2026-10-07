# Créditos

Varias skills de `base/` y `construir/` parten de skills de dos repositorios con licencia
MIT. Se compararon una por una con las que ya tenía LUPTECX (07/10/2026): donde dos hacían
lo mismo, se fusionaron en una sola, traducida al español y adaptada a cómo trabaja la
empresa (Python y pytest, push directo a `main`, bots de WhatsApp, Ley 1581).

| Repositorio | Versión usada | Licencia |
|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | v6.3.0 | MIT · [licencias/LICENSE-superpowers](licencias/LICENSE-superpowers) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | commit `f3fc563` (07/10/2026) | MIT · [licencias/LICENSE-mattpocock](licencias/LICENSE-mattpocock) |

## De dónde sale cada una

| Skill LUPTECX | Origen | Qué se tomó de cada una | Qué se cambió |
|---|---|---|---|
| `entrevistar` | mattpocock `grilling` + `desarrollo-riguroso` (propia) | Matt: árbol de decisiones, rondas con recomendación, los hechos los busca el agente. Propia: «nunca asumas» | Funciona sin subagentes; llama a `modelar-dominio` |
| `modelar-dominio` | mattpocock `domain-modeling` | Todo el método | `GLOSSARY.md` → `docs/GLOSARIO.md`; `docs/adr/` → `docs/decisiones/` con fecha; separa reglas de negocio (especificación) de decisiones de diseño; ejemplos del negocio de flotas |
| `depurar` | mattpocock `diagnosing-bugs` + superpowers `systematic-debugging` | Matt: el lazo ajustado que se pone rojo, minimizar, 3–5 hipótesis refutables, logs etiquetados, tachar secretos. superpowers: ley de causa raíz, buscar un ejemplo que funcione, fronteras entre capas, regla de los tres intentos, señales de alarma, técnicas de apoyo | Nunca reproducir contra producción; datos personales; `git log` desde la última etiqueta; ejemplos en Python; script del lazo con humano en Python |
| `probar-primero` | superpowers `test-driven-development` + mattpocock `tdd` | superpowers: ley de hierro, verificar rojo y verde, excusas, `writing-good-tests` (comprobación de mutaciones). Matt: costuras acordadas, rebanadas verticales, dobles solo en los bordes, pruebas tautológicas | Ejemplos en pytest; refactorización grande va en su propio commit |
| `verificar-antes-de-terminar` | superpowers `verification-before-completion` | La compuerta y la tabla de afirmaciones | Se le suma la definición de terminado de LUPTECX (CI, migración, glosario, Notion) |
| `revisar-cambios` | mattpocock `code-review` + superpowers `requesting-code-review` y `receiving-code-review` | Matt: dos ejes separados, base de olores de Fowler. superpowers: severidades, cómo atender los hallazgos (verificar antes de aplicar, rebatir con evidencia, YAGNI) | Puntos fijos del flujo LUPTECX (`origin/main`, última etiqueta, proyecto entero); funciona sin subagentes; renombrada para no chocar con `/code-review` y deslindada de ella. Antes vivía una copia dentro de `cierre-de-proyecto` |
| `retrospectiva` | mattpocock `retro` | Categorías, mecánico → candado, criterio → norma | Candados de LUPTECX (`.githooks/`, CI); normas a `luptecx-codigo` o al `CLAUDE.md` del proyecto |
| `traspasar-sesion` | mattpocock `handoff` | Todo | `%TEMP%` en Windows; datos personales tachados |
| `escribir-skills` | mattpocock `writing-for-agents` + superpowers `writing-skills` | Matt: punteros, jerarquía de información, criterios de terminado, palabras ancla, poda. superpowers: la descripción dice cuándo y no cómo, la forma según el fallo | Reglas del plugin LUPTECX (divisiones, nombres, versiones) en `mecanica-de-skills.md` |
| `planificar-desarrollo` | `desarrollo-riguroso` (propia) + mattpocock `to-spec`, `to-tickets` y `codebase-design` | Propia: pasos 1 y 2, plantillas, modo rápido. Matt: costuras de prueba en el plan, rebanadas verticales con dependencias, vocabulario de módulos profundos | Sin gestor de issues: el plan vive en `docs/ARQUITECTURA.md` (y en Notion si se quiere); el plan de piezas pasa de cortar por archivos a cortar por comportamientos |
| `construir-por-piezas` | `desarrollo-riguroso` (propia) + mattpocock `implement` | Propia: pasos 3 y 4 (explicar cada pieza, la última palabra es del desarrollador). Matt: prueba primero, revisión al cerrar, contexto limpio entre piezas | Las «tres preguntas» de la revisión pasan a `revisar-cambios` y a `/code-review` |

## Lo que se comparó y no entró

- **mattpocock:** `triage`, `wayfinder`, `to-tickets` e `implement-spec` como skills
  aparte (piden un gestor de issues y trabajo con ramas); `pr` (no hay pull requests);
  `prototype`, `wizard`, `teach`, `to-questionnaire`, `wait-what`, `ask-matt` (sin uso hoy).
- **superpowers:** las ocho que ya se habían descartado en nómina (`using-superpowers`,
  `brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`,
  `dispatching-parallel-agents`, `using-git-worktrees`, `finishing-a-development-branch`).
- **`shipping-and-launch`** (addyosmani): queda como skill personal; `cierre-de-proyecto` la
  usa de complemento. La lista de despliegue de LUPTECX será `luptecx-desplegar`.
