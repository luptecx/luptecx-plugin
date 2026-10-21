---
name: luptecx-reporte-mensual
description: Preparar el reporte mensual de resultados para un cliente de LUPTECX con mensualidad. Úsala cuando el usuario diga «el reporte del mes», «el informe para <cliente>», «qué le mandamos a <cliente> este mes», «cómo le fue al bot este mes», o al empezar el mes para los clientes en Soporte.
---

# Reporte mensual

El cliente paga cada mes por algo que funciona sin que lo vea. El reporte le muestra **qué
logró el sistema**, **qué hizo LUPTECX** y **qué sigue**, en un PDF de dos o tres páginas y
un mensaje corto. Lo prepara sobre todo Felipe.

**Cuándo:** en los primeros 5 días hábiles del mes, uno por cada proyecto en Fase Soporte
(Notion), **antes** del recordatorio de cobro: primero se muestra el valor, después se cobra.

Basado en `performance-report` (Anthropic): una cifra principal arriba, la tabla con el mes
anterior y una recomendación que sale de los datos.

## 1. Lo que hizo LUPTECX

Sale solo, de lo que ya está registrado (el mes que se reporta, del 1 al último día):

- **Notion, Tasks** del proyecto con completed = Done en el mes: errores (con su
  severidad), funcionalidades nuevas y soporte.
- **GitHub:** issues cerrados en el mes
  (`gh issue list -R <repo> --state closed --search "closed:AAAA-MM-01..AAAA-MM-31"`) y
  versiones desplegadas (etiquetas y `CHANGELOG.md`).
- **Tiempos del contrato:** para cada error, del reporte (creación del issue) al cierre,
  contra la cláusula 5 de las Condiciones Generales. Si uno no se cumplió, **se dice** y
  se explica en una línea.

Escrito para el cliente: qué cambió para él, no el nombre técnico («el bot ya no suma dos
veces los pagos», no «corrección del deduplicador»). Si no hubo errores, se dice: también es
un resultado.

**Terminado cuando:** tienes la lista del mes y la tabla de errores con su tiempo.

## 2. Lo que logró el sistema

Si el proyecto salió de la plantilla de procesos, sus eventos salen solos:
`GET https://<dominio>/metricas?mes=AAAA-MM` con el encabezado
`Authorization: Bearer <token>` (Bitwarden, «<proyecto> · token de métricas»), o
`python -m app.metricas AAAA-MM` en el servidor. Lo que el proyecto no registra, y los
proyectos anteriores a la plantilla, se piden a mano: lee [metricas.md](metricas.md) para
el tipo del proyecto y pídele a Felipe, en **una sola lista**, las cifras del mes con dónde
sacar cada una. Busca también:

- la cifra del **diagnóstico** (Reuniones en Notion, «Datos para la propuesta»);
- las cifras del **mes anterior**, en el `datos.json` del reporte pasado (carpeta del
  cliente, `Reportes\AAAA-MM\`).

Arma la tabla: cifra · este mes · mes anterior · antes de LUPTECX (si hay) · de dónde sale.
Lo que no se midió dice «no se midió»; nada se estima.

**Terminado cuando:** cada cifra tiene valor y fuente, o dice «no se midió».

## 3. Lo que sigue

- Lo programado para el mes que empieza: tareas del proyecto en Not started o In progress.
- **Una** recomendación que salga de una cifra del paso 2 («el 30 % de las conversaciones
  pasan a una persona por preguntas de repuestos: si nos mandan la lista de precios, el bot
  las puede contestar»).
- Si la recomendación es **otro producto o subir de nivel**, en el PDF va solo la
  recomendación; la oferta se manda aparte con `luptecx:luptecx-comunicacion-cliente`
  («Ofrecer más a un cliente actual»), y nunca con un incidente abierto o un pago vencido.

**Terminado cuando:** hay lo que sigue y una recomendación con su cifra.

## 4. El PDF

Escribe `datos.json` en `<carpeta del cliente>\Reportes\AAAA-MM\` con un valor por cada
`{{campo}}` de [plantilla-reporte.md](plantilla-reporte.md):

- `resumen`: dos o tres líneas con **la cifra principal** del mes y lo más importante que
  pasó.
- `tabla_resultados`, `tabla_soporte`: tablas en Markdown (la de soporte: qué pasó · qué
  hicimos · tiempo · ¿dentro del contrato?), o una frase si no hubo casos.
- Las cifras, también por separado (`conversaciones`, `citas`…), para que el próximo mes
  se comparen.

```powershell
uv run --script <plugin>\herramientas\md_a_word.py --pdf --datos <carpeta>\datos.json `
  --salida "<carpeta>\Reporte <cliente> <AAAA-MM>.docx" <carpeta de esta skill>\plantilla-reporte.md
```

Antes de entregarlo, léelo como el cliente: ¿se entiende en dos minutos qué ganó este mes?

**Terminado cuando:** el PDF está en la carpeta del mes.

## 5. Mandarlo

1. El mensaje con `luptecx:luptecx-comunicacion-cliente`, «Reporte del mes», con el PDF
   adjunto. Lo manda Felipe.
2. **Notion:** el PDF en Project Files del proyecto (a mano) y, en el CRM, Ultimo Contacto
   = la fecha del envío.

## Al terminar

```
Reporte <mes>: <cliente> · <producto>
Cifra principal: <la del resumen>
Soporte: <n> casos, <n> dentro del tiempo del contrato
Recomendación: <una línea>
PDF: <ruta> · Mensaje: borrador listo
```
