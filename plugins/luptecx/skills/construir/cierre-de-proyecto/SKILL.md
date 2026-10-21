---
name: cierre-de-proyecto
description: Auditoría y limpieza de un repositorio entero cuando un proyecto se cierra, se entrega o pasa a mantenimiento. Úsala siempre que el usuario diga que va a cerrar, terminar, entregar, «dejar bien» o «dejar limpio» un proyecto, que el código ya es la base y solo quedan cambios pequeños, que quiere quitar lo que sobra del repositorio (archivos basura, scripts desechables, código muerto, documentación vieja), revisar todo antes de producción, preparar la versión final o un traspaso a otro equipo, aunque no diga «auditoría». No es para revisar un solo cambio (eso es `luptecx:revisar-cambios`) ni para hacer un despliegue concreto.
---

# Cierre de proyecto

Al final de un proyecto el repositorio arrastra todo lo que sirvió para llegar hasta ahí:
scripts para probar una idea una vez, copias `_v2`, cuadernos de exploración, planes ya
cumplidos, código que dejó de llamarse, imports sobrantes, documentación que describe una
versión anterior. Nada de eso rompe el producto, pero lo vuelve difícil de entender para
quien llegue después y esconde lo que sí importa.

El objetivo es un repositorio en el que **todo lo que hay se usa y todo lo que se usa está
explicado**, revisado y listo para producción con un camino de vuelta atrás.

El riesgo está en el otro sentido: borrar algo que sí se usaba (una herramienta de
operación que solo se corre una vez al año, el payload guardado que usa una prueba, la
migración vieja) cuesta mucho más que dejar un archivo de sobra. Por eso esta skill
trabaja con evidencia, pide aprobación antes de borrar y deja todo recuperable.

## Principios

1. **Evidencia antes que opinión.** Cada archivo que se propone borrar lleva el porqué:
   quién lo cita (nadie), qué decía su último commit, qué lo reemplazó. «Parece viejo» no
   es evidencia.
2. **Nada se borra sin aprobación explícita, y todo borrado es recuperable.** Antes de
   tocar nada se crea un punto de retorno, y los borrados van en commits propios.
3. **«Prueba» no es «basura».** La suite automatizada (`tests/`, `pruebas/`) y sus datos
   son la garantía del proyecto: se quedan. Lo que sobra son los scripts de prueba
   **desechables**: los que se corrieron una vez a mano para ver si algo funcionaba. Lo
   mismo con el código de despliegue: el camino oficial se queda; sus versiones viejas,
   duplicados y atajos manuales se van.
4. **Las reglas del repositorio mandan.** Lee primero `CLAUDE.md`, `README`,
   `CONTRIBUTING` o el equivalente: tipos de commit, ramas, definición de terminado,
   invariantes, herramientas declaradas como oficiales. Si algo de esta skill choca con
   ellas, gana el repositorio.
5. **Limpiar no cambia el comportamiento.** Si en la revisión aparece un bug, se reporta
   y se arregla aparte, con su prueba (`luptecx:probar-primero`), no mezclado en un commit
   de limpieza. Así cada commit de limpieza se puede revertir sin miedo.

## Flujo

### Fase 0 · Punto de partida

1. `git status` limpio y la rama al día (`git pull`). Si hay cambios sin commitear,
   pregunta qué hacer con ellos antes de seguir.
2. Corre la suite completa y anota el resultado exacto (aprobadas / fallidas / saltadas).
   Ese número es la referencia: al final tiene que ser el mismo o mejor. Si algo falla ya
   al empezar, ese es el primer hallazgo (usa `luptecx:depurar`) y la limpieza espera.
3. Crea el punto de retorno: `git tag cierre-antes-AAAA-MM-DD`. Con eso cualquier
   cosa de esta sesión se deshace (`git revert` de los commits, o volver a la etiqueta).

### Fase 1 · Inventario

Corre el script incluido desde la raíz del repositorio. Solo lee, no toca nada:

```bash
python <ruta-de-esta-skill>/scripts/inventario.py --codigo-muerto > <carpeta-temporal>/inventario.md
```

Da, para cada archivo versionado, quién lo cita y su último commit, y además: nombres con
pinta de basura, archivos de datos, archivos sin seguimiento, versionados que el
`.gitignore` excluye, posibles secretos (enmascarados), restos de depuración y, con
`--codigo-muerto`, la salida de `ruff` y `vulture` si están disponibles. Si no lo están,
instálalos en una carpeta temporal (`pip install --target`), nunca en el entorno del
proyecto. Guarda el inventario fuera del repositorio: es material de trabajo.

Mientras corre, lee la documentación principal para saber qué herramientas y archivos el
proyecto declara como suyos.

### Fase 2 · Clasificar los archivos

Pon cada candidato en una de cuatro cajas: **Conservar**, **Eliminar**, **Mover**
(por ejemplo, un plan cumplido a `docs/historico/`) o **Preguntar**. Los criterios por tipo
de archivo, y la lista de lo que no se borra sin preguntar, están en
`references/criterios-limpieza.md`: léelo antes de clasificar.

La regla que más errores evita: un archivo citado desde la documentación, el CI, el
Dockerfile, los hooks, el código o las pruebas **no es basura**, salvo que la cita misma
esté obsoleta; entonces se van juntos, archivo y cita.

### Fase 3 · Código muerto

Parte de la salida de `ruff` (F401, F811, F841) y `vulture` (al 60 %, sin pruebas ni
migraciones: ahí solo da falsos positivos), pero confirma cada hallazgo con una búsqueda
en todo el repositorio, pruebas incluidas: muchas cosas se usan sin que un analizador lo vea (rutas registradas
con decoradores, fixtures de pytest, entradas de consola, `getattr`, plantillas,
`env.py` de migraciones, señales, tareas programadas). Busca además, a mano:

- Bloques de código comentado.
- Funciones, clases y ramas que solo existían para algo que ya se retiró (un proveedor
  viejo, una versión anterior de una API, una bandera de función que ya está al 100 %).
- Claves de configuración que nada lee, y variables de entorno de ejemplo sin uso.
- Dependencias declaradas que ningún import usa.

### Fase 4 · Revisión del código entero

Esto no es la revisión de un cambio: es leer el proyecto como lo leería quien lo va a
mantener. Tiene dos partes, y las dos se hacen:

1. **Calidad y riesgos** — `references/revision-codigo.md`: corrección, seguridad,
   código muerto, pruebas, claridad y operación.
2. **Coherencia en dos ejes** — invoca `luptecx:revisar-cambios` con alcance **proyecto
   entero** (o, si el usuario lo pide, desde la última etiqueta): ¿el código cumple los
   estándares documentados del repositorio, más una base de olores de código? y ¿hace lo
   que dicen la especificación y las decisiones registradas? Sus dos tablas, Estándares y
   Especificación, pasan tal cual al informe de cierre, por separado, para que un eje no
   tape al otro.

Si tienes `/code-review`, acepta una carpeta como objetivo y sirve de segunda mirada sobre
el código de la aplicación. Cada hallazgo va con `archivo:línea` y qué pasaría si no se
arregla.

Si el repositorio declara invariantes (reglas que no se pueden romper), compruébalas una
por una contra el código actual: es donde un cierre de proyecto encuentra los errores
caros.

### Fase 5 · Documentación

- Cada comando que aparece en el README o el CLAUDE.md existe y arranca (basta `--help`).
- Los números que da la documentación (cuántas pruebas, cuántos archivos, versiones)
  coinciden con la realidad.
- Las rutas, nombres de archivo y variables de entorno citados existen; el archivo de
  ejemplo de variables (`.env.example`) coincide con lo que la configuración lee.
- Documentos que describen planes ya cumplidos o sistemas retirados: se borran (git
  guarda la historia) o se mueven a un histórico con una línea que diga que lo son.
  Pregunta qué prefiere el usuario.
- El CHANGELOG tiene la entrada de lo que se hizo.

### Fase 6 · Producción y vuelta atrás

Sigue `references/produccion-y-marcha-atras.md`: la lista previa a producción adaptada al
tipo de proyecto y el plan de vuelta atrás (cómo volver a la versión anterior del código,
de la base de datos y de la configuración, y cuánto tarda cada cosa). Si está instalada la
skill `shipping-and-launch`, úsala como complemento para monitoreo y despliegue por
etapas; sus apartados de web (Core Web Vitals, accesibilidad) solo aplican si el proyecto
tiene interfaz web.

### Fase 7 · Informe y aprobación

Entrega un único informe con la plantilla de abajo y **detente**. No borres ni cambies
nada hasta que el usuario apruebe: puede aceptar todo, por grupos o archivo por archivo.
Si el informe es largo o lo va a leer más gente, ofrece publicarlo como página.

### Fase 8 · Ejecutar y verificar

1. Un commit por categoría, con el tipo de commit del repositorio (por ejemplo:
   `refactorizacion: elimina scripts de prueba desechables`,
   `refactorizacion: quita código muerto`, `documentacion: pone al día el README`).
   Si se borran archivos, el cuerpo del commit dice qué los reemplaza o por qué sobraban:
   es lo que leerá quien los busque dentro de un año.
2. Corre la suite después de cada commit. Si baja el número de pruebas que pasan, ese
   commit se revierte y se investiga; no se sigue encima.
3. Si un archivo que se borra contenía un secreto, borrarlo no lo saca del historial:
   el secreto se rota (se cambia en el servicio). Reescribir el historial exige forzar el
   push; eso lo decide el usuario y casi nunca vale la pena frente a rotar.
4. Vuelve a correr el inventario y muestra el antes y el después: archivos versionados,
   hallazgos de código muerto, restos de depuración.
5. Pon al día el CHANGELOG, sube los cambios según las reglas del repositorio (su hook o
   su CI tienen que quedar en verde) y comprueba antes de decir «listo»
   (`luptecx:verificar-antes-de-terminar`).

## Plantilla del informe

Usa siempre esta estructura. Las severidades:

- 🔴 **Bloquea producción**: secretos o datos reales en el repositorio, pruebas que
  fallan, despliegue roto, una invariante del proyecto rota, un bug que corrompe datos.
- 🟠 **Importante**: un bug, código muerto que confunde (parece en uso y no lo está),
  documentación que haría correr un comando equivocado, sin plan de vuelta atrás.
- 🟡 **Limpieza**: archivos que sobran, imports sin usar, restos de depuración.
- ⚪ **Opcional**: estilo, mejoras que pueden esperar.

```markdown
# Cierre de proyecto: <nombre> · <fecha>

## Resumen
<3 a 5 líneas: estado general, cuántos hallazgos por severidad, si está listo para
producción y qué lo impide.>

Punto de partida: <N> pruebas aprobadas, <N> saltadas · etiqueta `cierre-antes-<fecha>`

## 🔴 Bloquea producción
| # | Dónde | Qué pasa | Qué propongo |

## Archivos que propongo eliminar
| # | Archivo | Por qué sobra | Evidencia (quién lo cita, último commit) | Riesgo |

## Archivos que propongo mover o renombrar
| # | Archivo | A dónde | Por qué |

## Necesito tu decisión
<Archivos o hallazgos de la caja «Preguntar», cada uno con la pregunta concreta.>

## Código muerto
| # | Dónde | Qué es | Cómo se confirmó |

## Revisión del código
### Calidad y riesgos
| # | Severidad | Dónde | Hallazgo | Propuesta |

### Estándares
| # | Severidad | Dónde | Norma u olor | Hallazgo | Propuesta |

### Especificación
| # | Severidad | Requisito (cita) | Falta · sobra · mal implementado | Propuesta |

<Una línea por eje: cuántos hallazgos y el peor de ese eje. Sin mezclar los ejes.>

## Documentación
| # | Archivo | Qué está desactualizado o sobra | Propuesta |

## Producción y vuelta atrás
<Lista previa con ✅/⚠️/❌ y el plan de vuelta atrás.>

## Plan de ejecución
<Los commits que haría, en orden, y qué se comprueba después de cada uno.>
```

No inventes hallazgos para llenar secciones: una sección vacía se queda con «Nada que
reportar». Un informe corto y cierto vale más que uno largo con relleno.
