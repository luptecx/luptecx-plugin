# Base

Disciplinas que usan todas las etapas. Las skills de cada etapa dicen *qué* se hace; estas
dicen *cómo* se hace bien. Una sola skill por función: si dos hicieran lo mismo, Claude
cargaría las dos y seguiría procesos distintos.

| Skill | Cuándo | Se invoca | Origen |
|---|---|---|---|
| `entrevistar` | Definir algo con el usuario antes de construir | Sola o desde otra skill | mattpocock `grilling` + `desarrollo-riguroso` |
| `modelar-dominio` | Términos del negocio, `docs/GLOSARIO.md`, `docs/decisiones/` | Sola o desde otra skill | mattpocock `domain-modeling` |
| `depurar` | Cualquier error, antes de proponer arreglos | Sola o desde otra skill | Fusión: mattpocock `diagnosing-bugs` + superpowers `systematic-debugging` |
| `probar-primero` | Antes de escribir código de producción | Sola o desde otra skill | Fusión: superpowers `test-driven-development` + mattpocock `tdd` |
| `verificar-antes-de-terminar` | Antes de decir «listo» o subir algo | Sola o desde otra skill | superpowers `verification-before-completion` + definición de terminado de LUPTECX |
| `revisar-cambios` | Antes del push, antes de desplegar, al cerrar una pieza | Sola o desde otra skill | Fusión: mattpocock `code-review` + superpowers `requesting-` y `receiving-code-review` |
| `retrospectiva` | Después de una sesión que salió mal | Solo a mano: `/luptecx:retrospectiva` | mattpocock `retro` |
| `traspasar-sesion` | Seguir el trabajo en una sesión limpia | Solo a mano: `/luptecx:traspasar-sesion` | mattpocock `handoff` |
| `escribir-skills` | Crear o editar skills, `CLAUDE.md` o normas | Sola o desde otra skill | Fusión: mattpocock `writing-for-agents` + superpowers `writing-skills` |

## Cómo se encadenan

```
entrevistar ──► modelar-dominio          (definir: términos y decisiones mientras se habla)
depurar ──► probar-primero ──► verificar-antes-de-terminar     (un error)
probar-primero ──► revisar-cambios ──► verificar-antes-de-terminar   (un cambio)
retrospectiva ──► escribir-skills        (convertir lo aprendido en candados y normas)
```

## Y el `/code-review` de Claude Code

No está aquí a propósito. `revisar-cambios` revisa **estándares y especificación**;
`/code-review` caza **bugs de corrección**. Son complementarias: `revisar-cambios`
recomienda correr `/code-review` cuando el cambio toca dinero, fechas, el webhook o datos
del cliente.
