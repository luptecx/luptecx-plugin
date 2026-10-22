---
name: traspasar-sesion
description: Traspaso para seguir el trabajo en una sesión limpia de Claude, en vez de /compact. Úsala cuando el usuario diga «traspaso», «handoff», «cerremos la sesión», «el contexto va lleno» o «sigamos en otra sesión», o cuando otra skill cierre una pieza y la siguiente vaya en una sesión nueva.
argument-hint: "¿Para qué se va a usar la próxima sesión? (agrega «plan» si la próxima sesión va a ejecutar un plan)"
---

Escribe un documento de traspaso para que una sesión nueva de Claude siga el trabajo sin
haber leído esta conversación. Reemplaza a `/compact`: se hace **antes** de que el
contexto esté lleno, porque con el contexto lleno el resumen también sale peor.

## 1. Reunir el estado real

Lo que se puede consultar se consulta. Si hay repositorio, corre en paralelo:

- `git branch --show-current`, `git status --short`, `git log --oneline -10`,
  `git diff --stat` y la última etiqueta (`git describe --tags --abbrev=0`).
- Pruebas: el último resultado real de la sesión, o «no se corrieron».

Busca el traspaso anterior del mismo proyecto en la carpeta de traspasos (paso 4). Si
existe, léelo: lo que seguía abierto allí y no se cerró hoy pasa a este traspaso, que lleva
el número siguiente de la cadena.

**Terminado cuando:** tienes la salida de los comandos de git (o sabes que no hay
repositorio) y sabes si hay traspaso anterior.

## 2. Repasar la conversación completa

Recorre la sesión de principio a fin, no solo el final. Saca:

1. El objetivo y por qué se está haciendo.
2. Lo terminado, cada cosa con su evidencia (commit, prueba que pasa, ruta del archivo).
3. **Lo que se intentó y falló**: qué se probó, qué pasó (error exacto) y por qué se
   descartó. Es la sección más valiosa: es lo más caro de redescubrir.
4. Decisiones tomadas, con su porqué, y las alternativas descartadas.
5. Datos concretos: mensajes de error, números, comandos que funcionaron, versiones.
6. Correcciones o preferencias que el usuario dio durante la sesión.
7. Archivos creados o modificados.
8. Lo que quedó abierto, a medias o en duda, y los riesgos.

**Terminado cuando:** cada uno de los ocho puntos tiene contenido o un «no aplica»
consciente.

## 3. Escribir el documento

Plantilla (en español, máximo ~150 líneas; la sección que no aplica se quita):

```markdown
# Traspaso: <tema> — <AAAA-MM-DD HH:MM> (cadena #<n>)
Proyecto: <repo o proyecto> · Rama: <rama> · Tarea/issue: <enlace Notion o #issue>
Traspaso anterior: <ruta o «ninguno»>

## Objetivo
<1–3 líneas: qué se resuelve y por qué>

## Dónde estamos
- [x] <hecho> — evidencia: <commit / prueba / ruta>
- [ ] <a medias> — falta: <qué>
- Sin verificar: <lo que se cree pero no se comprobó>

## Lo que se intentó y no funcionó
| Intento | Qué pasó | Por qué se descartó |
|---|---|---|

## Decisiones
- <decisión> — porque <razón>. Descartado: <alternativa> porque <razón>.

## Datos y evidencia
<errores exactos, cifras, comandos que sí funcionaron>

## Lo que pidió o corrigió el usuario
- <preferencia o corrección>

## Archivos tocados
- <ruta> — <qué cambió>

## Abierto y riesgos
- <pendiente, duda o riesgo>

## Siguiente paso
<UNA acción concreta, con el primer comando o archivo a abrir>

## Plan por fases            ← solo si el argumento incluye «plan»
1. <fase> — criterio de terminado: <cómo se sabe>

## Skills sugeridas
- `luptecx:...` — para <qué>
```

Reglas de contenido:

- **Solo lo comprobado va como hecho.** Lo que se cree pero no tiene evidencia va en «Sin
  verificar»: un hueco rellenado con una suposición manda la sesión nueva en la dirección
  equivocada.
- **Citar, no copiar.** Lo que ya vive en otro lado (especificación, arquitectura,
  decisiones, commits, la tarea de Notion, el issue) se cita por ruta o enlace.
- **Secretos y datos personales tachados:** tokens, contraseñas, teléfonos, cédulas y
  nombres de clientes van como `<TACHADO>`.
- Si el usuario pasó argumentos, son el foco de la próxima sesión: ordena el documento
  para eso.

**Terminado cuando:** el documento sigue la plantilla y cabe en ~150 líneas.

## 4. Guardarlo

Fuera del repositorio (nunca se sube a git), en una carpeta que no se borra sola:

- Windows: `%USERPROFILE%\.claude\traspasos\<proyecto>\`
- Linux y Mac: `~/.claude/traspasos/<proyecto>/`

Nombre: `AAAA-MM-DD_HHMM_<tema-corto>.md`. Los traspasos anteriores se quedan: son la
cadena.

**Terminado cuando:** el archivo existe en esa carpeta.

## 5. Revisar antes de entregar

Relee el archivo y comprueba:

- Cada «hecho» tiene evidencia; «Lo que se intentó y no funcionó» tiene filas si hubo
  errores en la sesión.
- El siguiente paso es una sola acción concreta, con su primer comando o archivo.
- Todo secreto o dato personal está como `<TACHADO>`.

**Terminado cuando:** las tres comprobaciones pasan sobre el archivo guardado.

## 6. Entregar

Di la ruta completa y deja listo, en un bloque de código, el mensaje para pegar en la
sesión nueva:

```
Lee <ruta del traspaso> y sigue desde «Siguiente paso». Antes de cambiar nada,
dime en 3 líneas dónde estamos y qué vas a hacer primero.
```

Si en la sesión se tocó una tarea de Notion o un issue, pregunta si se actualiza su estado:
entre socios, el traspaso sigue siendo la tarea de Notion; este documento es para Claude.

**Terminado cuando:** el usuario tiene la ruta y el mensaje para pegar.
