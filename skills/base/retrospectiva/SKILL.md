---
name: retrospectiva
description: Retrospectiva de una sesión de trabajo para mejorar el entorno de Claude (candados, normas, CLAUDE.md, herramientas), no el código.
disable-model-invocation: true
---

# Retrospectiva

Propón mejoras al **entorno** en que trabaja Claude, para que el próximo cambio salga mejor.
No se arregla el código del proyecto: se arregla lo que dejó pasar el error. Es la regla de
fondo de LUPTECX aplicada a sí misma: **cada cosa que se repite tiene una plantilla, y cada
cosa que puede romper producción tiene un candado.**

## Pasos

1. Invoca `luptecx:escribir-skills`: es la guía para todo lo que se escribe para un agente
   (`CLAUDE.md`, skills, normas).
2. Lee las fuentes de la sesión que indique el usuario. Si no indica ninguna, la sesión
   actual. Si ya se limpió el contexto, búscala en los registros de sesiones de este PC.
3. Busca candidatos en estas categorías:

- **Navegación.** ¿Le costó encontrar el archivo o el dato correcto? ¿Hay dependencias
  escondidas entre archivos? → Un puntero en el `CLAUDE.md` del proyecto. *Cuando* la
  sesión tardó en encontrar algo.
- **Candados automáticos.** ¿Una comprobación automática habría atrapado el error? Mira
  primero lo que el proyecto ya tiene (`.pre-commit-config.yaml` o `.githooks/`, el workflow del CI, `pytest.ini`,
  `ruff`): un candado que existe pero no está conectado o está roto es el hallazgo, no
  inventar otro. Un proyecto sin hooks activos o sin CI es un hallazgo por sí solo. *Cuando*
  Claude cometió un error que una máquina podía ver.
- **Normas.** ¿La revisión (`luptecx:revisar-cambios`) dejó pasar algo? Clasifica el
  error primero:
  - **Mecánico** (un patrón fijo, una función prohibida, una forma de import, dónde va un
    archivo): se vuelve **comprobación automática**, siempre. Una regla en el linter, un
    hook nuevo o un paso del CI, lo que sea más barato en ese proyecto.
  - **De criterio** (coherencia entre archivos, «como el resto del código», cómo se le
    habla al cliente): se vuelve **norma escrita**: en `luptecx-codigo` si vale para todos
    los proyectos, o en el `CLAUDE.md` del proyecto si es solo suya.
- **`CLAUDE.md` demasiado grande.** ¿Hay instrucciones que deberían ser normas de revisión
  o comprobaciones automáticas? *Cuando* el archivo pasa de unas pocas pantallas.
- **Lo que no cambia nada.** Instrucciones que Claude ya cumple sin que se las digan:
  sobran y diluyen las que sí importan.
- **Economía de herramientas.** ¿Hubo llamadas caras que se podían evitar (leer archivos
  enteros, comandos con salida enorme)? → Un script o un comando más preciso.
- **Acceso a información.** ¿Faltó un dato crucial? Logs del servidor, acceso de solo
  lectura a la hoja de prueba, el estado del CI. → Cómo dárselo a Claude sin exponer
  secretos.

4. Presenta los candidatos **del más grave al menos grave**, cada uno con: qué pasó en la
   sesión (la evidencia), qué cambio propones, dónde va y qué tipo de candado es.
5. No apliques nada hasta que el usuario elija. Un cambio a una skill del plugin sigue el
   proceso del README del plugin (versión nueva, commit con tipo, avisar al otro socio).

## Por qué las normas van en la revisión

Todo trabajo pasa por dos etapas: implementar y revisar. Quien implementa carga con la
mayor **presión de contexto**: explora, escribe código y depura. Quien revisa recibe un
diff y casi no tiene presión. Por eso las normas las hace cumplir la revisión, no quien
implementa: el `CLAUDE.md` debe quedar corto, con punteros, y las normas de criterio van
donde las lee `luptecx:revisar-cambios`.
