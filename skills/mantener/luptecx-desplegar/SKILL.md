---
name: luptecx-desplegar
description: Llevar una versión a producción, o volver a una anterior, en un proyecto de LUPTECX. Úsala cuando el usuario diga desplegar, «subir a producción», «sacar la versión», «que le llegue al cliente», revertir o «volver a la versión anterior», o cuando otra skill (corregir un error, una funcionalidad nueva) llegue al paso de desplegar.
---

# Desplegar

Subir a `main` no es desplegar: al cliente solo llega lo que pasa por
`herramientas/desplegar.py`. El script ya es el candado (franja prohibida, commit en
`origin/main`, CI en verde, versión del CHANGELOG, confirmación, respaldo, salud,
etiqueta); esta skill es lo que lo rodea: preparar la versión, que la persona correcta lo
corra y comprobar después. Lo que hace el script, paso a paso, está en su docstring.

**Despliega Camilo.** Felipe solo en una emergencia, siguiendo `docs/RECUPERACION.md`.

## 1. Lista previa

Cada punto con su evidencia (`luptecx:verificar-antes-de-terminar`):

- [ ] **Hora:** fuera de la franja prohibida de `despliegue.ini`.
- [ ] **Todo subido:** árbol limpio y `HEAD` igual a `origin/main` (`git status`,
      `git fetch` y `git rev-parse HEAD origin/main`).
- [ ] **CHANGELOG:** una entrada nueva `## [X.Y.Z] — DD/MM/AAAA` arriba, con lo de
      `[Sin publicar]` movido ahí y escrito para quien lo lea dentro de un año. La versión:
      solo correcciones → sube el último número (`1.3.0` → `1.3.1`); funcionalidad nueva →
      el del medio (`1.4.0`); algo que obliga al cliente a cambiar cómo lo usa → el primero.
      Si falta, se escribe con el usuario, commit `documentacion:` y push.
- [ ] **Revisión de lo que sale:** `luptecx:revisar-cambios` con punto fijo en la última
      etiqueta (`git describe --tags --abbrev=0`). Un 🔴 detiene el despliegue.
- [ ] **CI en verde** para ese commit: `gh run list --commit <hash>`.
- [ ] **Migración:** si la versión trae una, la suite corrió también contra PostgreSQL y el
      usuario sabe que volver atrás será restaurar el respaldo, no `--version`.
- [ ] **Configuración nueva:** cada variable nueva ya está en el `.env` del servidor (desde
      Bitwarden) antes de desplegar; si no, el arranque de producción se detiene.
- [ ] **Plantillas de Meta:** si la versión manda una plantilla nueva, Meta ya la aprobó y su
      nombre está en el `.env`. Nunca el nombre de una plantilla sin aprobar.

Presenta la lista con ✅ / ❌ y para en el primer ❌.

## 2. La llave y el despliegue los maneja el usuario

La frase de la llave SSH y la confirmación del despliegue son de quien despliega; Claude no
las escribe.

1. Pide al usuario que, en su terminal de **PowerShell**, cargue la llave una vez por sesión:
   `C:\Windows\System32\OpenSSH\ssh-add.exe $env:USERPROFILE\.ssh\id_ed25519`
   (el `ssh` de Git Bash no usa ese agente).
2. Pide que corra, en la carpeta del proyecto:
   `.\.venv\Scripts\python.exe herramientas\desplegar.py`
   y que responda la confirmación después de leer la lista de commits que salen.
3. Si tienes acceso a su terminal, lee la salida; si no, pídele que te la pegue.

Si el script se niega, su mensaje dice por qué y qué hacer: se arregla la causa. Nunca se
fuerza (`--ahora` solo con una razón que el usuario diga en voz alta, y queda anotada).

## 3. Prueba de humo

El script ya comprobó `/salud`. Además:

- [ ] `git log -1 --oneline` en el servidor coincide con la etiqueta nueva.
- [ ] Los trabajos programados son los mismos que antes (los lista `/salud`).
- [ ] El log de la app, sin errores en los primeros minutos.
- [ ] Si el cambio se ve en WhatsApp, probarlo con un teléfono del equipo. Nunca se escribe
      como si fuera el cliente ni desde su número.

## 4. Después

1. La tarea de Notion pasa a Done, con el enlace a la etiqueta o al commit en
   **Enlace GitHub**.
2. Si el cliente pidió el cambio o lo va a notar, se le avisa. Usa
   `luptecx:luptecx-comunicacion-cliente` si está instalada; si no, redacta un mensaje
   corto y el usuario lo aprueba antes de mandarlo.
3. El usuario descarga la llave del agente: `ssh-add -D`.

## Si algo sale mal

- **La salud no responde o el bot falla:** volver a la versión anterior,
  `herramientas\desplegar.py --version <anterior>` (el script la sugiere en su mensaje).
- **Hay una migración en medio:** el script se niega a volver por código. Se restaura el
  respaldo previo siguiendo «Recuperación ante desastre» del README del proyecto, y se
  despliega desde ahí.
- Se abre una tarea de tipo Error en Notion con lo que pasó. Si el error era evitable,
  `/luptecx:retrospectiva` en esta misma sesión, para convertirlo en candado.
