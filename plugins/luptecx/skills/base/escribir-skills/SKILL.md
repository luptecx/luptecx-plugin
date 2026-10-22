---
name: escribir-skills
description: Cómo escribir documentos que lee un agente. Úsala al crear o editar una skill del plugin LUPTECX o de cualquier proyecto, al escribir o cambiar un `CLAUDE.md`, o al redactar una norma, plantilla o guía que Claude va a seguir.
---

# Escribir skills

Guía para todo documento que consume un agente: una skill, un `CLAUDE.md`, una norma o una
referencia a la que se llega por un puntero. El empaque cambia; la escritura no. La meta no
es que el agente produzca siempre la misma salida, sino que siga **el mismo proceso** cada
vez.

Si es una skill del plugin, lee además [mecanica-de-skills.md](mecanica-de-skills.md):
frontmatter, invocación, dónde va y cómo se publica.

## Primero, investigar lo que ya existe

Antes de escribir una skill, una plantilla, un candado o una norma nueva, busca lo que ya
usan los equipos profesionales; se escribe desde cero solo si nada sirve:

1. Busca con `npx skills find <tema>` y en las fuentes de confianza: `anthropics/skills`,
   `obra/superpowers`, `mattpocock/skills`, `addyosmani/agent-skills`, `getsentry/skills`,
   `trailofbits/skills` y el proveedor de la herramienta. Para herramientas, la
   documentación oficial. Filtra por fuente reconocida, mantenida en los últimos meses, con
   uso real y con una licencia que permita lo que se va a hacer.
2. Lee completo el `SKILL.md` de las finalistas y compáralo función por función con las
   skills que ya tiene el plugin.
3. Si algo se va a instalar o copiar, revísalo antes con `luptecx:skill-scanner` (de
   Sentry, viene con el plugin): instrucciones escondidas, scripts, permisos y secretos.
   Sus hallazgos se verifican a mano; muchos son ejemplos, no ataques.
4. Presenta al usuario qué encontraste y recomienda una opción: **usar tal cual**,
   **adaptar** (anotando en `CREDITOS.md` qué se tomó y qué se cambió, y la licencia en
   `licencias/`) o **escribir propia**. Que la licencia permita lo elegido: MIT y Apache
   se adaptan citando; CC BY-SA se prefiere instalar.
5. Anota la decisión en `CREDITOS.md`: lo adaptado en «De dónde sale cada una», lo que se
   usa tal cual en «Externas tal cual» y lo descartado, con su porqué, en «Lo que se
   comparó y no entró».

**Terminado cuando:** el usuario vio las opciones con su fuente y su licencia, y eligió.

## La descripción dice cuándo, no cómo

La descripción de una skill está cargada siempre: es lo que Claude lee para decidir si la
abre. Por eso:

- **Solo dice cuándo usarla**: situaciones, síntomas, frases que el usuario dice de verdad.
- **Nunca resume el proceso.** Si la descripción cuenta los pasos, el agente sigue la
  descripción y no abre la skill. Probado: una descripción que decía «revisión entre
  tareas» hizo que el agente revisara una vez, aunque el cuerpo pedía dos revisiones.
- **Una frase por rama.** Cada caso distinto que dispara la skill, una vez. Los sinónimos
  del mismo caso sobran.
- **La palabra clave adelante**, en tercera persona y en el idioma en que habla el equipo.

## Pasos y referencia

Un documento tiene dos tipos de contenido: **pasos** (lo que el agente hace, en orden) y
**referencia** (reglas, definiciones, datos que consulta cuando hace falta). Ordénalos por
lo inmediato que los necesita:

1. **Pasos en el archivo**: lo primero que se lee.
2. **Referencia en el archivo**: se consulta cuando toca.
3. **Referencia aparte**, en otro archivo, con un puntero que diga cuándo leerla. Lo que
   necesitan todos los caminos va adentro; lo que solo necesitan algunos, afuera.

El fallo típico es la **expansión**: un documento tan largo que la atención se diluye,
aunque cada línea sea cierta. Se cura bajando referencia a archivos aparte y partiendo por
caminos.

Lo que va junto, va junto: la definición de un concepto, sus reglas y sus excepciones
bajo el mismo título, no repartidas.

## Cada paso termina en un criterio

Cada paso termina en un **criterio de terminado** que diga sin ambigüedad cuándo está
hecho. Uno vago («hasta entender») invita a terminar antes de tiempo, porque los pasos
siguientes tiran. Los mejores criterios son **comprobables y exhaustivos**: «un comando que
ya corriste y se pone rojo con este error» o «cada requisito marcado con su evidencia».

## La forma según el fallo

Antes de escribir, identifica qué falla sin la guía y elige la forma que lo corrige:

| Qué falla | Forma que funciona | Forma que empeora |
|---|---|---|
| Conoce la regla y se la salta bajo presión | Ley + tabla de excusas + señales de alarma | Sugerencias suaves («prefiere…») |
| Cumple, pero la salida tiene la forma equivocada | Receta o plantilla: qué *es* la salida, sus partes y su orden | Lista de prohibiciones |
| Olvida un elemento | Un campo obligatorio en la plantilla que llena | Recordatorios en prosa |
| Depende de una condición | Un condicional sobre algo observable («si existe la especificación…») | Regla general + excepciones |

**Di lo que sí.** Prohibir algo lo pone en la cabeza del agente: «no expliques de más»
activa el explicar. Escribe el comportamiento que quieres («una línea por hallazgo»). Una
prohibición solo vale como candado duro que no se puede decir en positivo, y aun así va
junto al comportamiento correcto.

## Palabras que cargan significado

Usa palabras que el modelo ya entiende y que resumen un comportamiento entero: *rojo*,
*ajustado*, *rebanada vertical*, *frontera*, *costura*. Repetida como palabra, nunca como
frase, ancla el comportamiento con pocas palabras. Busca los tríos que se repiten
(«rápido, determinista y sin dependencias») y cámbialos por una palabra (*ajustado*).

## Podar

- **Una sola fuente de verdad** por idea: cambiar el comportamiento es editar un sitio.
- **El entorno ya es fuente de verdad**: lo que se ve en `pytest.ini`, en el árbol de
  carpetas o en `--help` no se copia; se copia solo lo que no se encuentra mirando (la
  convención no escrita, el porqué de una decisión, la trampa que nadie confiesa).
- **Borra lo que no cambia nada**: una instrucción que el agente ya cumple por defecto
  ocupa espacio sin efecto. Se borra la frase entera.
- **Sin sedimento**: lo que quedó viejo se quita. Agregar se siente seguro y quitar
  arriesgado; por eso los documentos crecen hasta que nadie encuentra lo vigente.

## Probar la skill

Una skill es código para un agente: se prueba. Antes de escribirla, mira qué hace Claude
**sin** ella en dos o tres casos reales; después, con ella. Si no cambia nada, sobra. Para
pruebas más serias (casos de evaluación, comparar versiones, afinar la descripción), usa la
skill `skill-creator` de Anthropic si está disponible.
