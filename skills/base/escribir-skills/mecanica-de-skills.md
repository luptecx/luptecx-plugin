# Mecánica de las skills del plugin LUPTECX

## Dónde va

Cada skill vive en `skills/<división>/<nombre>/SKILL.md`. La división es la etapa del
cliente donde se usa:

| División | Qué va ahí |
|---|---|
| `base` | Disciplinas que usan todas las etapas: entrevistar, depurar, probar, revisar… |
| `vender` | Diagnóstico, propuesta, presentación, contrato |
| `construir` | Planificar, construir, entregar y cerrar un proyecto |
| `mantener` | Errores, funcionalidades, despliegue, reportes al cliente |
| `administrar` | Cierre mensual, comunicación con el cliente, portafolio |

Una división nueva se agrega también a la lista `skills` de `.claude-plugin/plugin.json`;
sin eso no carga. Al agregar o quitar una skill, se actualiza la tabla del `README.md` de
su división y la del `README.md` del plugin.

## Nombre

- En español, minúsculas y guiones, empezando por verbo cuando se pueda:
  `revisar-cambios`, `planificar-desarrollo`.
- El nombre de la carpeta es exactamente el `name:` del frontmatter.
- Las skills de un proceso propio de la empresa en una etapa llevan el prefijo `luptecx-`
  (`luptecx-desplegar`). Las disciplinas generales no lo llevan: el plugin ya las nombra
  `luptecx:<nombre>`.
- Nunca el nombre de un comando que ya trae Claude Code (`code-review`, `init`,
  `security-review`…): el del sistema tapa al nuestro.

## Frontmatter e invocación

```yaml
---
name: revisar-cambios
description: <cuándo usarla; ver SKILL.md de escribir-skills>
---
```

Dos formas de invocarla, que se pagan distinto:

- **Por el modelo** (lo normal): sin más campos. Claude la abre solo cuando la situación
  encaja, y otras skills pueden invocarla. El precio es que su descripción ocupa contexto
  siempre: que cada palabra cuente.
- **Solo a mano**: `disable-model-invocation: true`. Solo se ejecuta cuando alguien
  escribe `/luptecx:<nombre>`. No ocupa contexto, pero alguien tiene que acordarse de que
  existe, y ninguna otra skill puede invocarla. La descripción pasa a ser un resumen de una
  línea para personas. Úsalo para lo que se decide a propósito (`retrospectiva`,
  `traspasar-sesion`).

Si una referencia la necesitan dos skills que se invocan solo a mano, no puede vivir en
ninguna de las dos: va en un archivo aparte al que ambas apuntan.

## Referencias entre skills

Dentro del plugin, una skill se nombra con su nombre completo: «invoca
`luptecx:probar-primero`». Si alguna vez se copia una skill fuera del plugin (a
`.claude/skills/` de un proyecto), se quita el prefijo `luptecx:` en la copia.

## Material de terceros

Si una skill se basa en otra de un repositorio externo, se comprueba su licencia, se copia
la licencia a `licencias/` y se anota en `CREDITOS.md` de dónde viene y qué se cambió.

## Publicar un cambio

El proceso está en el `README.md` del plugin: subir la versión en `plugin.json`, commit con
tipo, push, empaquetar con `python empaquetar.py` y avisar al otro socio para que los dos
instalen la versión nueva. Antes de empaquetar, `claude plugin validate .` tiene que pasar.
