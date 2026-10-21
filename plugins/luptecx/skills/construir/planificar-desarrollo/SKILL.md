---
name: planificar-desarrollo
description: Definir qué se va a construir y cómo, antes de escribir código. Úsala al empezar un proyecto, un script, una automatización, un bot o una herramienta que se va a mantener; al agregar una funcionalidad grande a un proyecto existente; o cuando el usuario diga «nuevo proyecto», «quiero construir», «vamos a desarrollar», «planifiquemos» o pida ayuda para pensar el código antes de escribirlo. No se usa si el usuario pide explícitamente un prototipo desechable o «modo rápido».
---

# Planificar el desarrollo

La IA escribe el código; el **criterio** para juzgarlo lo pone quien desarrolla. Este flujo
deja por escrito qué se construye, cómo se estructura y en qué piezas se divide, para que
la construcción sea pieza por pieza y no «hazme toda la app».

Mantén los pasos 1 a 5 en **una sola conversación**, sin limpiar el contexto: la
entrevista, la especificación y el plan se construyen sobre el mismo razonamiento. La
construcción, en cambio, va pieza por pieza con `luptecx:construir-por-piezas`, cada una en
una sesión limpia.

## Qué modo

- **Proyecto nuevo:** se crean `docs/ESPECIFICACION.md` y `docs/ARQUITECTURA.md`. Si el
  repositorio sale de `luptecx-plantilla`, la estructura de carpetas ya está decidida:
  se parte de ella.
- **Cambio en un proyecto existente:** se actualizan las secciones afectadas de los dos
  documentos y se agregan las piezas nuevas al plan. No se reescribe lo que no cambia.
- **Modo rápido**, solo si el usuario lo pide con palabras claras («es un prototipo», «solo
  quiero probar», «no necesita durar»): sin documentos, pero igual se confirma el alcance
  antes de escribir. Nunca lo actives por tu cuenta.

## 1. Contexto

Lee lo que ya existe antes de preguntar: `CLAUDE.md`, `docs/` (especificación,
arquitectura, `GLOSARIO.md`, `decisiones/`), la propuesta aceptada o la tarea de Notion si
el usuario la da, y el código que se va a tocar.

Antes de preguntar nada, **escribe los supuestos** que estás haciendo y muéstralos: lo que
no se dice en voz alta es el malentendido más caro.

```
SUPUESTOS:
1. Lo usa el dueño desde su celular, no sus empleados
2. Los datos siguen en la hoja del cliente, no en una base nueva
→ Corrígeme ahora o sigo con estos.
```

Si el pedido trae **varias capacidades que se pueden probar por separado** (por ejemplo,
registro, recordatorios y reportes), primero propón un mapa corto, una tabla con cada
capacidad, de cuál depende y en qué orden se construye, y que el usuario lo apruebe. Cada
capacidad sigue después este flujo por su cuenta.

**Terminado cuando** puedes decir en dos líneas qué existe hoy y qué se quiere cambiar, y el
usuario vio tus supuestos.

## 2. Entrevista

Invoca `luptecx:entrevistar`, con `luptecx:modelar-dominio` activa para anotar los términos
del negocio y las decisiones de diseño mientras se habla. Ramas que casi siempre aparecen:

- ¿Qué problema resuelve y para quién? ¿Quién lo usa: el equipo, el dueño, sus empleados,
  los clientes del cliente?
- ¿Qué entra y qué sale? ¿Por qué canal (mensajería, correo, hoja de cálculo, web)?
- ¿Qué está dentro del alcance del proyecto y qué ya sería otro producto? (Las funcionalidades nuevas del mismo producto no se cobran aparte: van en la mensualidad.)
- ¿Qué pasa cuando algo falla: quién se entera y cómo?
- ¿Qué datos personales toca, dónde se guardan y por cuánto tiempo (Ley 1581)?
- Restricciones: integraciones con terceros y sus límites, horario en que no se puede tocar producción,
  dependencias permitidas, servidor.

**Terminado cuando** la frontera de la entrevista está vacía y el usuario confirmó el
resumen de decisiones.

## 3. Especificación

Escribe o actualiza `docs/ESPECIFICACION.md` con la plantilla de
[plantilla-especificacion.md](plantilla-especificacion.md). Usa las palabras del glosario.
Cada requisito es verificable y tiene al menos un criterio de aceptación medible. Un pedido
vago se convierte en criterios medibles y se le pregunta al usuario si son los correctos:
«que sea más rápido» pasa a «el comprobante llega en menos de 3 segundos con 20 vehículos».
Las decisiones del dueño van con su fecha, junto a la regla que deciden.

Preséntala con sus preguntas abiertas y **para ahí**: ni arquitectura ni código en el mismo
turno. Se sigue cuando el usuario la aprueba. Si hay cambios, se actualiza y se vuelve a
presentar.

**Terminado cuando** el usuario aprobó la especificación tal como quedó escrita.

## 4. Arquitectura

Escribe o actualiza `docs/ARQUITECTURA.md` con la plantilla de
[plantilla-arquitectura.md](plantilla-arquitectura.md): estructura, flujo de datos, modelo
de datos, decisiones de diseño, **costuras de prueba** (dónde se va a probar cada
comportamiento) y **amenazas y datos**. Para decidir dónde van los módulos y sus interfaces,
usa el vocabulario de [diseno-de-modulos.md](diseno-de-modulos.md).

Si lo que se planifica recibe datos de afuera, guarda datos personales o usa un modelo de
IA, la sección «Amenazas y datos» sale del paso 1 de `luptecx:revisar-seguridad`, y sus
casos de abuso pasan al plan de piezas como pruebas.

Tú propones; el usuario decide. Si hay varias formas razonables, preséntalas con pros y
contras y una recomendación. Las decisiones difíciles de revertir van además a
`docs/decisiones/`.

**Terminado cuando** el usuario aprobó la arquitectura, costuras y amenazas incluidas.

## 5. Plan de piezas

Divide el trabajo en **rebanadas verticales** (*balas trazadoras*): cada pieza atraviesa
todas las capas que necesita (modelo, servicio, webhook, mensaje, prueba) para entregar un
comportamiento completo, angosto pero verificable de punta a punta.

- **Una pieza = un comportamiento que se puede demostrar**, no un archivo. «El cliente
  escribe su pedido y recibe el resumen con el total» es una pieza; «escribir
  `configuracion.py`» no lo es.
- Cada pieza cabe en **una sesión** de trabajo.
- Si conviene reorganizar algo antes («hacer fácil el cambio, y luego hacer el cambio
  fácil»), esa reorganización es la primera pieza.
- Cada pieza dice de cuáles **depende**: una pieza sin dependencias pendientes se puede
  empezar ya.

Presenta el plan como lista numerada (título, qué entrega, depende de, criterios de
aceptación con sus RF, costura de prueba) y pregunta: ¿el tamaño está bien? ¿Las
dependencias son las reales? ¿Hay que unir o partir alguna? Itera hasta que lo apruebe y
escríbelo en la sección «Plan de piezas» de `docs/ARQUITECTURA.md`. Si el proyecto lleva
las tareas en Notion, ofrece crear una tarea por pieza.

**Terminado cuando** el plan está aprobado y escrito.

## 6. Cerrar

1. Commit con tipo: `documentacion: especificación y arquitectura de <qué>`, y push.
2. Di al usuario cómo sigue: «Para construir, una pieza por sesión:
   `luptecx:construir-por-piezas` con la pieza 1». Recomiéndale limpiar el contexto
   antes de empezar la primera.

## Reglas transversales

- **Todo en español:** documentación, nombres de variables y funciones, comentarios,
  mensajes de error y de commit. Excepciones: tecnicismos sin traducción natural (API,
  webhook, commit) y nombres de librerías, salvo que el proyecto decida otra cosa en su
  `CLAUDE.md`.
- **Pregunta siempre que** haya más de una forma razonable, el requisito sea ambiguo, no
  sepas si una dependencia es aceptable o no esté claro el alcance.
- **Si el usuario quiere saltarse un paso**, recuérdale para qué existe. Si insiste,
  respeta su decisión y déjala escrita como riesgo asumido en el documento.
