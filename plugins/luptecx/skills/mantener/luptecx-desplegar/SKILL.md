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

**Despliega Camilo.** Felipe solo en una emergencia (un caso Crítico y Camilo sin responder
en 1 hora), siguiendo `docs/RECUPERACION.md` del proyecto.

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
- [ ] **Seguridad de lo que sale:** `luptecx:revisar-seguridad` con el mismo punto fijo si
      lo que sale toca alguna frontera (entrada externa, datos personales, secretos,
      dependencias, IA). La **primera** puesta en producción la revisa en modo proyecto
      entero. Un 🔴 detiene el despliegue.
- [ ] **CI en verde** para ese commit: `gh run list --commit <hash>`.
- [ ] **Migración:** si la versión trae una, la suite corrió también contra PostgreSQL y el
      usuario sabe que volver atrás será restaurar el respaldo, no `--version`.
- [ ] **Configuración nueva:** cada variable nueva ya está en el `.env` del servidor (desde
      Bitwarden) antes de desplegar; si no, el arranque de producción se detiene.
- [ ] **Aprobaciones externas:** si la versión usa algo que una plataforma tiene que
      aprobar (una plantilla de mensaje, un permiso, una app), ya está aprobado y su
      nombre está en el `.env`. Nunca el nombre de algo sin aprobar.
- [ ] **Plugins de tipo:** si el proyecto activa uno (por ejemplo
      `luptecx-bot-whatsapp`), su lista «Antes de desplegar» también.
- [ ] **Vuelta atrás lista:** se sabe a qué etiqueta se vuelve (la anterior) y cómo (con
      `--version`, o restaurando el respaldo si hay migración), y alguien puede mirar la
      **primera hora** después del despliegue. Si nadie va a estar, se despliega otro día.
- [ ] **Lo riesgoso, apagable:** una funcionalidad grande o delicada sale detrás de su
      bandera de activación apagada (`construir-por-piezas`); encenderla es un cambio de
      configuración, y apagarla es la vuelta atrás más rápida.

Presenta la lista con ✅ / ❌ y para en el primer ❌.

## 2. La llave y el despliegue los maneja el usuario

La frase de la llave SSH y la confirmación del despliegue son de quien despliega; Claude no
las escribe.

1. Pide al usuario que, en su terminal de **PowerShell**, cargue la llave una vez por sesión:
   `C:\Windows\System32\OpenSSH\ssh-add.exe $env:USERPROFILE\.ssh\id_ed25519`
   (el `ssh` de Git Bash no usa ese agente).
2. Pide que corra, en la carpeta del proyecto:
   `uv run python herramientas\desplegar.py` (en los proyectos anteriores a la plantilla
   de procesos, `.\.venv\Scripts\python.exe herramientas\desplegar.py`)
   y que responda la confirmación después de leer la lista de commits que salen.
3. Si tienes acceso a su terminal, lee la salida; si no, pídele que te la pegue.

Si el script se niega, su mensaje dice por qué y qué hacer: se arregla la causa. Nunca se
fuerza (`--ahora` solo con una razón que el usuario diga en voz alta, y queda anotada).

## 3. Prueba de humo y la primera hora

El script ya comprobó `/salud`. Además, enseguida:

- [ ] `git log -1 --oneline` en el servidor coincide con la etiqueta nueva.
- [ ] Los trabajos programados son los mismos que antes (los lista `/salud`).
- [ ] El camino principal del cliente funciona de punta a punta, probado con una cuenta o
      un teléfono del equipo. Nunca se actúa como si fuera el cliente ni desde sus cuentas.

Y durante la **primera hora**, quien desplegó mira el log de la app: sin errores nuevos,
sin respuestas lentas, y los registros llegan y se leen.

**Se vuelve atrás sin discutir** (sección «Si algo sale mal») cuando pasa cualquiera de
estas: `/salud` falla; aparece un error nuevo que le llega al usuario; el camino principal
no funciona; hay datos dañados o guardados mal; aparece una falla de seguridad. Primero se
vuelve atrás y después se investiga: volver atrás no es un fracaso, dejar al cliente con
algo roto sí.

## 4. Después

1. La tarea de Notion pasa a Done, con el enlace a la etiqueta o al commit en
   **Enlace GitHub**. Si ese campo ya apunta a un issue, se deja el issue y el issue se
   cierra con la versión (`luptecx:luptecx-corregir-error`, paso 6).
2. Si el cliente pidió el cambio o lo va a notar, se le avisa con
   `luptecx:luptecx-comunicacion-cliente` («Funcionalidad nueva» o «Error corregido»). Si
   el despliegue detiene el servicio, el aviso previo es «Mantenimiento programado». El
   usuario lo aprueba y lo manda.
3. El usuario descarga la llave del agente: `ssh-add -D`.

## Señales de alarma

Desplegar un viernes por la tarde o antes de un festivo; desplegar sin nadie mirando la
primera hora; configuración de producción hecha de memoria y no desde Bitwarden y el
`.env.ejemplo`; una versión enorme con muchas cosas a la vez (mejor varias pequeñas, cada
una con su etiqueta).

## Si algo sale mal

- **La salud no responde o el bot falla:** volver a la versión anterior,
  `herramientas\desplegar.py --version <anterior>` (el script la sugiere en su mensaje).
- **Hay una migración en medio:** el script se niega a volver por código. Se restaura el
  respaldo previo siguiendo `docs/RECUPERACION.md` (caso 3; en los proyectos anteriores a
  la plantilla de procesos, «Recuperación ante desastre» del README), y se despliega desde
  ahí.
- Se abre una tarea de tipo Error en Notion con lo que pasó. Si el error era evitable,
  `/luptecx:retrospectiva` en esta misma sesión, para convertirlo en candado.
