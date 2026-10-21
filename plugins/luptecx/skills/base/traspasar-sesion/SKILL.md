---
name: traspasar-sesion
description: Resume la conversación en un documento de traspaso para seguir el trabajo en una sesión limpia de Claude.
argument-hint: "¿Para qué se va a usar la próxima sesión?"
disable-model-invocation: true
---

Escribe un documento de traspaso que resuma esta conversación para que una sesión nueva
de Claude pueda seguir el trabajo sin haberla leído.

**Dónde se guarda:** en la carpeta temporal del sistema (`%TEMP%` en Windows, `$TMPDIR` o
`/tmp` en Linux y Mac), nunca dentro del repositorio. Di la ruta completa al terminar, para
que el usuario la pegue en la sesión nueva.

**Qué lleva:**

- El objetivo y el estado actual: qué está hecho (con su evidencia) y qué falta.
- Las decisiones tomadas y por qué, si no están ya escritas en otro lado.
- Lo que se intentó y no funcionó, para no repetirlo.
- El siguiente paso concreto.
- Una sección «Skills sugeridas» con las skills que la próxima sesión debería invocar
  (`luptecx:construir-por-piezas`, `luptecx:depurar`…).

**Qué no lleva:** lo que ya está en otro artefacto (especificación, arquitectura,
decisiones, commits, la tarea de Notion, el issue): se cita por ruta o enlace, no se
copia. Tampoco secretos ni datos personales: tokens, contraseñas, teléfonos, cédulas y
nombres de clientes van como `<TACHADO>`.

Si el usuario pasó argumentos, son el foco de la próxima sesión: ajusta el documento a eso.

Este traspaso es para retomar en una sesión limpia de Claude. Entre socios, el traspaso
sigue siendo la tarea de Notion.
