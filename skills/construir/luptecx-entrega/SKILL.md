---
name: luptecx-entrega
description: Entregarle al cliente un proyecto de LUPTECX que ya está funcionando en producción. Úsala cuando el usuario diga «entreguemos el proyecto», «hagamos el acta», «hay que capacitar al cliente», «el manual del cliente», «ya está en vivo, ¿qué sigue?», o cuando una funcionalidad nueva cambie cómo usa el cliente algo que ya conocía y haya que actualizar su manual.
---

# Entrega

La entrega cierra la construcción: el cliente recibe su manual, aprende a usar el sistema,
firma el acta y desde ahí corre la mensualidad (cláusula 3.1 del contrato). Va **después**
de `luptecx:cierre-de-proyecto` (repositorio limpio y auditado) y de
`luptecx:luptecx-desplegar` (versión en producción): se entrega lo que ya funciona.

Los Word y los PDF los arma el generador del plugin,
[`herramientas/md_a_word.py`](../../../herramientas/md_a_word.py), desde la carpeta de esta
skill o del proyecto.

## 0. Listo para entregar

- La versión está en producción con su etiqueta (`luptecx-desplegar`) y la prueba de humo
  pasó.
- `cierre-de-proyecto` no dejó nada 🔴 abierto.
- Está el contrato firmado: su carátula dice qué se acordó.

**Terminado cuando:** tienes la versión, la fecha en que salió en vivo y la carátula.

## 1. El manual

El manual vive en el repositorio, en `docs/MANUAL.md`, para que cada funcionalidad nueva lo
actualice (`luptecx:luptecx-nueva-funcionalidad`). Si no existe, se crea desde
[plantilla-manual.md](plantilla-manual.md).

1. **Primero el índice:** quién usa qué y las tareas frecuentes de cada persona (de la
   especificación y de lo que el cliente hace en el día a día). El usuario lo aprueba antes
   de escribir.
2. **Cada parte para lo que es:** «Primeros pasos» enseña, «Cómo…» resuelve una tarea,
   «Qué hace el sistema» se consulta y «Si algo falla» dice qué hacer. No se mezclan.
3. **Cómo se escribe:** las palabras del cliente y la voz de
   `luptecx:luptecx-comunicacion-cliente`; títulos que dicen el resultado («Cómo cambiar el
   horario»); pasos numerados; párrafos cortos; el mensaje exacto que ve el usuario cuando
   algo falla. Sin datos reales de los clientes del cliente.
4. No queda ningún texto de guía `<…>` de la plantilla. Commit `documentacion:` y push.
5. El PDF, en la carpeta del cliente (fuera del repositorio):

   ```powershell
   uv run --script <plugin>\herramientas\md_a_word.py --pdf `
     --salida "<carpeta del cliente>\Manual <producto> v<versión>.docx" docs\MANUAL.md
   ```

   Si el PC no tiene Word, el script lo dice: se abre el `.docx` y se guarda en PDF.

**Terminado cuando:** el manual está en `main` y el PDF en la carpeta del cliente.

## 2. La capacitación

Sigue [capacitacion.md](capacitacion.md): una sesión en vivo de 30 a 45 minutos en la que
cada persona hace sola sus tareas. Prepara el guion con las tareas del manual y lo que
hace falta tener listo.

Después de la sesión, lo que costó entender o no estaba en el manual se agrega al manual
(y se regenera el PDF).

**Terminado cuando:** la sesión se hizo y sabes quiénes asistieron y qué practicó cada uno.

## 3. El acta

Escribe `datos.json` (en la carpeta del cliente) con un valor por cada `{{campo}}` de
[acta-de-entrega.md](acta-de-entrega.md):

- `tabla_entregado`: una tabla con **cada punto del alcance de la carátula**, cómo se
  comprobó (la prueba, quién la hizo) y la fecha. Lo que no se cumplió no va aquí: va en
  pendientes.
- `pendientes`: lo que falta y **no impide usar el sistema**, con fecha; o «Ninguno».
  Si algo impide usarlo, no hay entrega: se termina primero.
- `inicio_mensualidad`: el día de la firma, salvo que la carátula diga otra cosa.
- Lo que nadie sabe: `[POR CONFIRMAR: …]`, nunca inventado.

```powershell
uv run --script ..\..\..\herramientas\md_a_word.py --datos <carpeta del cliente>\datos.json `
  --salida "<carpeta del cliente>\Acta de entrega <cliente> <fecha>.docx" acta-de-entrega.md
```

**Terminado cuando:** el acta está en Word sin pendientes resaltados.

## 4. Entregar y avisar

1. El acta y el manual se le mandan al cliente con
   `luptecx:luptecx-comunicacion-cliente`, «Salida en vivo y bienvenida». Claude solo
   redacta; el socio lo manda.
2. **Notion**, cuando el cliente firme el acta:
   - Proyecto: Fase = Soporte. Mientras el acta está por firmar, Fase = Entregado.
   - Tareas de construcción que quedaron abiertas: Done, o pasan a pendientes del acta con
     su fecha.
   - Cliente en el CRM: Estado = Cliente Activo.
   - El acta firmada y el manual se adjuntan en **Project Files** (a mano).
3. Si la carátula autoriza mencionarlo como referencia, propón
   `luptecx:luptecx-caso-portafolio`.

**Terminado cuando:** el cliente tiene el acta y el manual, y Notion dice Soporte o
Entregado.

## Al terminar

```
Entrega: <producto> v<versión> · <cliente>
Manual: docs/MANUAL.md + PDF · Capacitación: <fecha>, <n> personas
Acta: <ruta> · Pendientes: <n o ninguno> · Mensualidad desde: <fecha>
Notion: Fase <Entregado / Soporte> · CRM: <Estado>
```
