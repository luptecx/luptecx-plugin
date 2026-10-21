---
name: luptecx-corregir-error
description: "Corregir un error de un proyecto de LUPTECX de punta a punta, desde el issue hasta que el cliente tiene el arreglo. Úsala cuando haya que arreglar un error ya reportado (un issue con la etiqueta `error`, una tarea de Notion de tipo Error), cuando el usuario diga «arregla el issue #N», «corrige esto» o «está fallando en…», o cuando `luptecx-reportar-error` termine y toque arreglarlo."
---

# Corregir un error

Un error está corregido cuando **el cliente tiene el arreglo**, no cuando el código cambió.
Esta skill encadena las de base en un orden fijo y dice dónde parar; el cómo de cada paso
está en la skill que se invoca, no aquí.

```
issue ─► depurar ─► probar-primero ─► revisar-cambios ─► push + CI ─► desplegar ─► cerrar
```

## 0. Tomar el caso

1. Lee el issue (`gh issue view <N> -R <repo>`) y la tarea de Notion enlazada. Si el error
   no tiene issue, primero `luptecx:luptecx-reportar-error`: todo arreglo cuelga de un issue.
2. `git pull` con el árbol limpio. La tarea de Notion pasa a **In progress**.
3. **Crítica con el servicio caído:** antes de depurar se mitiga. Si la versión anterior
   funcionaba, se vuelve a ella con `luptecx:luptecx-desplegar` («Si algo sale mal») y
   después se depura con calma.

**Terminado cuando:** leíste el issue, el repositorio está al día y la tarea está In progress.

## 1. Diagnosticar

Invoca `luptecx:depurar` y sigue sus fases 1 a 4: un comando que se pone rojo con este
error y la causa raíz comprobada.

Deja la causa en el issue, en dos o tres líneas y sin datos personales:
`gh issue comment <N> -R <repo> --body "Causa: …"`. Así queda la historia para quien
encuentre algo parecido, y Felipe ve el avance sin preguntar.

**Terminado cuando:** el comando rojo existe y la causa está escrita en el issue.

## 2. Arreglar con prueba

Sigue la fase 5 de `luptecx:depurar`, que invoca `luptecx:probar-primero`: prueba de
regresión roja, un solo arreglo en la causa raíz, prueba verde y la suite completa en local.

Commit con este formato:

```
correccion: <qué deja de pasar, en una línea>

Causa: <la causa raíz, en una o dos frases>.
Refs #<N>
```

Se usa `Refs`, no `Closes`: el issue se cierra cuando el cliente tiene el arreglo (paso 6),
no al llegar a `main`.

**Para y pregunta** si el arreglo necesita una migración, una variable de configuración
nueva o algo que una plataforma externa tenga que aprobar: cambian cómo se despliega.

**Terminado cuando:** la prueba nueva falló sin el arreglo y pasa con él, la suite está en
verde y el commit está hecho.

## 3. Revisar

Invoca `luptecx:revisar-cambios` contra `origin/main`. Si el arreglo toca dinero, fechas,
el webhook o datos del cliente, corre también `/code-review`; si toca entrada externa,
autenticación, secretos, datos personales, dependencias o IA, también
`luptecx:revisar-seguridad`. Un 🔴 vuelve al paso 2.

**Terminado cuando:** la revisión no tiene 🔴.

## 4. Verificar y subir

1. `luptecx:verificar-antes-de-terminar`.
2. `git push`. El hook corre la suite; si falla, se arregla la causa (nunca `--no-verify`).
3. Espera el CI de ese commit: `gh run list --commit <hash>` hasta que termine. Si falla,
   es un error nuevo: vuelve al paso 1 con él.

**Terminado cuando:** el CI de ese commit está en verde.

## 5. Desplegar

1. Agrega el arreglo a `## [Sin publicar]` del `CHANGELOG.md`, en `### Corregido`, escrito
   para el cliente: qué notaba y qué pasa ahora. Commit `documentacion:` y push.
2. **Cuándo sale:** Crítica y Alta, ya. Media y Baja pueden esperar la próxima versión; lo
   decide el usuario.
3. El despliegue lleva **todo** lo que está en `[Sin publicar]`. Si hay otros cambios
   esperando, díselo al usuario antes: salen juntos.
4. Invoca `luptecx:luptecx-desplegar`.

**Terminado cuando:** la etiqueta desplegada contiene el commit
(`git tag --contains <hash>`) y la prueba de humo pasó. Si el usuario decidió esperar,
la skill termina aquí y el paso 6 se hace con el despliegue que lo lleve.

## 6. Cerrar

1. **Issue:** se cierra con la versión:
   `gh issue close <N> -R <repo> -c "Corregido en vX.Y.Z (<hash>)."`
2. **Notion:** la tarea pasa a **Done**. Enlace GitHub sigue apuntando al issue; el issue
   ya lleva el commit y la versión.
3. **Cliente:** si lo reportó un cliente, se le avisa con
   `luptecx:luptecx-comunicacion-cliente`: «Error corregido» (o «Incidente resuelto» si fue
   Crítica). El usuario lo aprueba y lo manda.
4. **¿Era evitable?** Si un candado o una norma lo habría atajado (una regla de `ruff`, una
   prueba que faltaba, una revisión que no se hizo), recomienda al usuario correr
   `/luptecx:retrospectiva` en esta sesión para convertirlo en candado.

**Terminado cuando:** el issue está cerrado con la versión, la tarea en Done y, si aplica,
el cliente tiene el borrador del aviso.

## Al terminar

```
Corregido: #<N> <título>
Causa: <una línea>
Commit: <hash>   Versión: vX.Y.Z (o «sale en la próxima versión»)
Issue cerrado · Tarea en Done · Aviso al cliente: <borrador listo / no aplica>
¿Evitable?: <no / sí: recomendada la retrospectiva>
```
