---
name: luptecx-nueva-funcionalidad
description: Agregar una funcionalidad a un proyecto de LUPTECX que ya está en marcha, desde el pedido hasta que el cliente la usa. Úsala cuando el cliente o el equipo pida algo nuevo para un proyecto existente («que el bot también…», «agrégale…», «necesitamos que…»), cuando haya un issue con la etiqueta `funcionalidad` o una tarea de Notion de tipo Funcionalidad, o cuando `luptecx-reportar-error` registre un pedido nuevo.
---

# Agregar una funcionalidad

Las funcionalidades nuevas **no se cobran aparte**: van dentro de la mensualidad y el
soporte. Lo que se decide no es el precio, sino si el pedido encaja en el proyecto, cuánto
pesa y cuándo se hace. Esta skill encadena las de construir y mantener en un orden fijo;
el cómo de cada paso está en la skill que se invoca.

```
pedido ─► ¿encaja? ─► tamaño y prioridad ─► planificar ─► construir por piezas ─► desplegar ─► avisar
```

## 0. Tomar el pedido

Lee el issue (`gh issue view <N> -R <repo>`) y la tarea de Notion enlazada. Si el pedido no
tiene issue, primero `luptecx:luptecx-reportar-error`, que también registra pedidos nuevos.
`git pull` con el árbol limpio.

**Terminado cuando:** puedes decir en una frase qué necesita el cliente y para qué, con
sus palabras, no con la solución que imaginó.

## 1. ¿Encaja en este proyecto?

Lee el problema y el alcance en `docs/ESPECIFICACION.md`. Si no existe o está vacía (un
proyecto anterior a la plantilla, o uno que nunca se planificó), dilo: se decide con el
usuario a partir de lo que el proyecto hace hoy, y en el paso 3 se escribe primero el
problema y el alcance, no solo el requisito nuevo.

- **Mejora o amplía lo que el proyecto ya hace** (el mismo usuario, el mismo canal, los
  mismos datos): sigue.
- **Es otro producto** (otro problema, otro usuario u otro sistema): no es una
  funcionalidad sino un proyecto nuevo. Para y díselo al usuario; va por la etapa de
  vender (`luptecx:luptecx-diagnostico` cuando exista), y el mensaje al cliente es «Pedido
  que es otro producto» de `luptecx:luptecx-comunicacion-cliente`.
- **Choca con algo que la especificación excluye a propósito** (una decisión del dueño, la
  Ley 1581, un límite de una plataforma externa): para y pregunta, citando la línea.

**Terminado cuando:** el usuario confirmó que encaja.

## 2. Tamaño y prioridad

Divide el pedido en rebanadas verticales, como en el paso 5 de
`luptecx:planificar-desarrollo`, solo para medirlo:

| Tamaño | Piezas | Qué cambia |
|---|---|---|
| Pequeña | 1 | Especificación de dos líneas con su criterio medible |
| Mediana | 2 a 4 | Especificación y plan de piezas |
| Grande | 5 o más | Primero el mapa de capacidades de `planificar-desarrollo` |

Con el usuario, decide cuándo se hace frente a lo que ya está abierto en Notion. Deja el
tamaño en el issue (`gh issue comment`) y la prioridad y la fecha en la tarea (Priority y
Due Date): con eso Felipe le puede decir al cliente cuándo la tiene.

**Terminado cuando:** el tamaño está en el issue y la tarea tiene prioridad y fecha.

## 3. Planificar

Invoca `luptecx:planificar-desarrollo` en el modo «cambio en un proyecto existente»: el
requisito nuevo entra a `docs/ESPECIFICACION.md` con su fecha y sus casos borde, y las
piezas nuevas al plan de `docs/ARQUITECTURA.md`. Si el usuario pidió algo vago, ahí se
convierte en criterios medibles.

Decide aquí si lleva **bandera de activación**: sí cuando cambia algo que el cliente ya usa
o se construye en varias piezas; no cuando es pequeña y aislada. Cómo se hace, en
`luptecx:construir-por-piezas`.

**Terminado cuando:** especificación y plan aprobados, con commit `documentacion:` y push.

## 4. Construir

Invoca `luptecx:construir-por-piezas`, una pieza por sesión. La tarea de Notion pasa a
**In progress** con la primera pieza. Cada commit de pieza lleva `Refs #<N>` en el cuerpo:
el issue se cierra cuando el cliente la tiene, no al llegar a `main`.

**Terminado cuando:** todas las piezas están ✅ en el plan y el CI está en verde.

## 5. Desplegar y encender

1. El CHANGELOG lleva la funcionalidad en `### Agregado`, escrita para el cliente: qué
   puede hacer ahora y cómo se usa.
2. Invoca `luptecx:luptecx-desplegar`.
3. **Con bandera:** se despliega apagada. Se enciende después, en el `.env` del proyecto,
   y se prueba con un teléfono o una cuenta del equipo antes de contarle al cliente. La
   bandera y el código viejo se retiran en la versión siguiente.

**Terminado cuando:** la funcionalidad está desplegada y, si lleva bandera, encendida y
probada.

## 6. Cerrar

1. **Issue:** `gh issue close <N> -R <repo> -c "Disponible desde vX.Y.Z."`
2. **Notion:** la tarea pasa a **Done**.
3. **Cliente:** `luptecx:luptecx-comunicacion-cliente`, «Funcionalidad nueva»: qué puede
   hacer ahora, con un ejemplo de cómo pedirlo. El usuario lo aprueba y lo manda. Si cambia
   cómo usa algo que ya conocía, se actualiza también su manual (`luptecx:luptecx-entrega`).

**Terminado cuando:** el issue está cerrado con la versión, la tarea en Done y el cliente
tiene el borrador del aviso.

## Al terminar

```
Funcionalidad: #<N> <título>
Tamaño: <pequeña / mediana / grande> · Piezas: <n> · Bandera: <no / FUNCION_X, encendida>
Versión: vX.Y.Z
Issue cerrado · Tarea en Done · Aviso al cliente: <borrador listo>
```
