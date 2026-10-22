---
name: luptecx-nuevo-proyecto
description: Arrancar un proyecto de LUPTECX después de que el cliente aceptó la propuesta. Úsala cuando el usuario diga «arranquemos el proyecto», «nuevo proyecto», «el cliente aceptó», «creemos el repo» o «montemos el proyecto de <cliente>», o cuando un cliente del CRM pase de Propuesta Enviada a En Ejecución.
---

# Arrancar un proyecto

Deja todo proyecto nuevo igual desde el primer día: el proyecto en Notion con sus tareas,
el repositorio generado con la **plantilla de procesos** (candados activados y CI en verde)
y la lista de accesos que hay que pedirle al cliente. Termina entregándole el turno a
`luptecx:planificar-desarrollo`.

Un **producto** (el mismo servicio vendido a varios clientes) se arranca así una sola vez,
con el nombre del producto y no el de un cliente: vive en un solo repositorio y un solo
despliegue. Un cliente nuevo de un producto que ya existe no pasa por el paso 3: entra como
filas y configuración validada en la base del producto, nunca como un repositorio, una
rama, un archivo copiado ni un `if` con su nombre.

La usan los dos socios. Hace falta `gh` con permiso en la organización `luptecx`, `uv`,
`prek` y acceso a Notion.

## 0. Hay una propuesta aceptada

Busca al cliente en el CRM de Notion (base Clientes, ver [notion.md](notion.md)) y el
producto en el Portafolio. Sin propuesta aceptada no se arranca: eso todavía es venta
(`luptecx:presentacion-ventas-contenido`).

**Terminado cuando:** tienes el cliente, el producto del Portafolio, el nivel vendido
(Esencial, Recomendado o Completo) y la propuesta aceptada (enlace o archivo), y el usuario
confirmó que la aceptaron.

## 1. Los datos del proyecto

Pregunta en **una sola ronda** lo que no salga de la propuesta. Son las preguntas de la
plantilla (`copier.yml`) y tres más:

| Dato | De dónde |
|---|---|
| nombre, slug, cliente, descripción | La propuesta; el cliente, como está en el CRM |
| tipo (`servicio`, `automatizacion`, `script`, `otro`) y stack (`python` u `otro`) | La propuesta; en la duda, se pregunta. `servicio` es lo que corre siempre: un bot, un agente o una API |
| servicio web y despliegue | Por defecto, sí para un servicio en Python |
| base de datos | Sí si el proyecto guarda datos propios (conversaciones, registros, estados). Trae PostgreSQL, migraciones y el respaldo cifrado; su puesta a punto (llaves de `age`, destino fuera del servidor) está en `docs/PUESTA_EN_PRODUCCION.md` |
| Plugins de tipo | Solo si el proyecto es de un tipo que ya tiene el suyo (hoy, `luptecx-bot-whatsapp` para lo que conversa por WhatsApp con Meta). Si no hay, ninguno |
| dominio, puerto y franja prohibida | Solo si se despliega. El puerto, distinto a los ocupados: mira la página Servidor de Notion |
| datos personales | Sí si toca teléfonos, cédulas o nombres |
| Carpeta | Donde están los otros repositorios de LUPTECX, fuera de una carpeta sincronizada |
| Correo al que el cliente invita a LUPTECX | El de quien lleva el proyecto |
| Quién le pide los accesos al cliente | Uno de los dos socios |

Muestra el resumen y espera un sí antes de crear nada: los pasos 2 y 3 crean cosas en
Notion y en GitHub.

```
Proyecto: Conciliación de pagos Ferretería López (conciliacion-lopez) · Cliente: Ferretería López
Tipo: servicio · Python · web · despliegue en conciliacion-lopez.luptecx.com:8002 · franja 6-9
Datos personales: sí · Plugins de tipo: ninguno · Carpeta: C:\…\LuptecX\conciliacion-lopez
Accesos: los pide Felipe; el cliente invita a <correo>
Notion: proyecto existente «…» (o se crea) · 3 tareas · Repositorio privado luptecx/conciliacion-lopez
```

**Terminado cuando:** el usuario aprobó el resumen.

## 2. Notion

Con la plantilla **Proyecto LUPTECX** y el procedimiento de [notion.md](notion.md):

1. **Proyecto**: si el cliente ya tiene un proyecto en Notion de la etapa de venta, se usa
   ese (se le aplica lo que falte de la plantilla) en vez de crear otro; si no, se crea.
   Project Name = nombre, Project Description = descripción,
   Fase = Construcción, Status = In progress, Clients, Portafolio y, si la propuesta trae
   fecha de entrega, Deadline.
2. **Tareas de arranque** en Tasks, con Project = el proyecto y completed = Not started:

   | In | Tipo | Assignee | Due Date |
   |---|---|---|---|
   | Pedir accesos al cliente | Administrativa | Quien los pide (paso 1) | 2 días hábiles |
   | Especificación y arquitectura | Funcionalidad | Camilo | Sin fecha: la pone el plan |
   | Puesta en producción (solo si se despliega) | Funcionalidad | Camilo | El Deadline del proyecto, si hay |

3. **Cliente** en el CRM: Estado = En Ejecución.

**Terminado cuando:** abriste el proyecto, la plantilla está aplicada y las tareas se ven
en su vista de tareas.

## 3. El repositorio

En PowerShell, desde la carpeta padre. El origen es siempre `gh:luptecx/luptecx-plantilla`:
el proyecto guarda el origen en `.copier-answers.yml` y `copier update` lo usa después.
Solo para probar un cambio de la plantilla se genera desde el clon local (con
`--vcs-ref=HEAD`, para tomar lo que no tiene commit), y ese proyecto es desechable.

```powershell
uvx copier copy --defaults --data nombre="…" --data slug=… --data cliente="…" `
  --data descripcion="…" --data tipo=… --data stack=… <resto de datos> `
  gh:luptecx/luptecx-plantilla <slug>
cd <slug>
git init -b main
uv sync                      # solo stack Python: crea uv.lock, que se sube
prek install
git add -A
prek run --all-files         # si un candado arregla algo, git add -A y otra vez
git commit -m "inicio: proyecto desde la plantilla de procesos"
gh repo create luptecx/<slug> --private --description "<descripción>" --source . --remote origin --push
gh label create error --color d73a4a --description "Algo no funciona como debería" --force
gh label create funcionalidad --color a2eeef --description "Algo nuevo que debería hacer" --force
gh run list --workflow ci.yml --commit (git rev-parse HEAD)   # el id del CI del primer commit
gh run watch <id> --exit-status
```

`gh run watch` sin id puede tomar la ejecución de Dependabot, que arranca al mismo tiempo;
por eso se busca la del workflow `ci.yml`.

Las dos etiquetas las usan los formularios de issue; un repositorio nuevo no las trae. Si
un candado o el CI falla, se arregla la causa (en la plantilla, si el fallo viene de ahí:
se avisa al usuario) y nunca con `--no-verify`.

Si el resumen del paso 1 trae plugins de tipo, se agregan a `enabledPlugins` en
`.claude/settings.json` (`"luptecx-bot-whatsapp@luptecx": true`), en un commit
`inicio: plugin de tipo <nombre>`. El plugin general `luptecx` ya viene activado por la
plantilla.

Luego, en el proyecto de Notion: **Repositorio** = la URL del repositorio.

**Terminado cuando:** el CI del commit `inicio:` está en verde y Notion enlaza el
repositorio.

## 4. Los accesos

Lee [accesos.md](accesos.md) y arma la lista con las filas comunes, las de lo que use el
proyecto y las de sus plugins de tipo.

1. En la página del proyecto, debajo de «Accesos del cliente», como pendientes (`to_do`)
   bajo dos subtítulos: **Imprescindible para empezar** y **Puede llegar después**. El
   primer pendiente es para el equipo: «Crear la colección del cliente en Bitwarden».
   Las personas del cliente no van como pendiente: se piden en el mismo mensaje y se
   escriben en «Personas del cliente» cuando lleguen.
2. **Borrador del mensaje al cliente:** `luptecx:luptecx-comunicacion-cliente`,
   «Bienvenida y accesos», con la lista de arriba. Lo manda el socio del paso 1, después de
   leerlo; Claude no le escribe a nadie.

**Terminado cuando:** la lista está en Notion y el usuario tiene el borrador.

## 5. Planificar

El arranque termina aquí; lo que sigue es `luptecx:planificar-desarrollo` en modo
**proyecto nuevo**, con la propuesta aceptada como entrada. Pídele al usuario que abra una
sesión nueva de Claude Code **en la carpeta del repositorio**, para que cargue su
`CLAUDE.md`, y que empiece por ahí. La sección «Lo propio de este proyecto» del `CLAUDE.md`
se llena al terminar el plan: corta, y apuntando a los documentos en vez de copiarlos.

## Al terminar

Responde con este bloque:

```
Proyecto arrancado: <nombre> (<cliente>)
Notion: <URL del proyecto> · 3 tareas
Repositorio: <URL> · CI en verde · candados activos
Accesos: lista en Notion · borrador para <socio>
Sigue: sesión nueva en <carpeta> → luptecx:planificar-desarrollo con la propuesta
```
