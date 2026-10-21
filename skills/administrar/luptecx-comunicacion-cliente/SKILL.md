---
name: luptecx-comunicacion-cliente
description: Redactar cualquier mensaje de LUPTECX para un cliente o un posible cliente, por WhatsApp o por correo. Úsala cuando haya que avisar un error, una caída o un mantenimiento; contar un avance, una entrega o algo nuevo; cobrar o confirmar un pago; decir que no, anunciar un retraso o dar una mala noticia; hacer seguimiento a una propuesta, responder una objeción, ofrecer algo más o pedir un referido; o cuando otra skill de LUPTECX llegue al paso de avisarle al cliente.
---

# Comunicación con el cliente

Todo lo que sale de LUPTECX hacia un cliente suena igual, sin importar quién lo escriba:
la misma voz, la misma estructura y los mismos cuidados. **Claude redacta borradores; el
usuario los lee, los ajusta y los manda él.** Claude no le escribe a nadie.

## 1. El contexto

Saca de lo que te dan (y de Notion: CRM, proyecto, tarea o issue) antes de preguntar:

- **Quién lo recibe:** el contacto, su cargo y si decide, aprueba o usa. Si es un grupo.
- **La situación:** qué pasó o qué se quiere lograr, con fechas y cifras confirmadas.
- **La relación:** cliente nuevo (menos de 3 meses), establecido o molesto, y si hay algo
  pendiente con él (un error abierto, un pago vencido).
- **Quién firma:** Camilo o Felipe. El mensaje sale en primera persona de ese socio.

Si falta un dato que cambia el mensaje (una fecha, un monto, una hora), pregúntalo. **Nunca
inventes** fechas, montos, cifras de resultados, datos de pago ni causas de un error.

**Terminado cuando:** sabes a quién, qué, desde quién y con qué datos confirmados.

## 2. El mensaje tipo

Busca el caso en el catálogo y lee **solo** el archivo de su grupo:

| Grupo | Mensajes | Archivo |
|---|---|---|
| Errores e incidentes | Acuse de un reporte, incidente en curso, actualización, incidente resuelto, error corregido | [mensajes/errores-e-incidentes.md](mensajes/errores-e-incidentes.md) |
| Avances y novedades | Bienvenida y accesos, avance del proyecto, salida en vivo y bienvenida, reporte del mes, funcionalidad nueva, mantenimiento programado | [mensajes/avances-y-novedades.md](mensajes/avances-y-novedades.md) |
| Cobro | Recordatorio, pago vencido, pago recibido | [mensajes/cobro.md](mensajes/cobro.md) |
| Decir que no | Pedido que es otro producto, retraso, mala noticia | [mensajes/decir-que-no.md](mensajes/decir-que-no.md) |
| Incentivar a comprar | Seguimiento de una propuesta, respuesta a una objeción, ofrecer más, pedir un referido, aprobación de un caso, reactivar | [mensajes/incentivar-compra.md](mensajes/incentivar-compra.md) |

Los ejemplos muestran la **forma**: sus nombres, cifras, montos y casos son inventados y
nunca pasan a un mensaje real. Si el caso no está, usa la estructura general: **reconocer** (una línea) → **lo que hay
que decir** → **qué sigue**, con quién y cuándo → cierre corto.

**Terminado cuando:** tienes el mensaje tipo o la estructura general.

## 3. Redactar con la voz

Lee [voz.md](voz.md) y escribe para el canal:

- **WhatsApp** para el día a día.
- **Correo** para lo que tiene que quedar como registro: propuesta, contrato, acta de
  entrega, cobro vencido por segunda vez, y lo que el cliente pida por correo.

**Terminado cuando:** el borrador está escrito en la voz y el formato del canal.

## 4. Revisar antes de entregar

- [ ] Cada fecha, hora, monto y cifra está confirmada; nada inventado.
- [ ] Promete solo lo que depende de LUPTECX y está autorizado; nada de causas sin
      confirmar.
- [ ] Dice qué sigue, quién lo hace y cuándo (con día y hora, no «pronto»).
- [ ] Sin jerga, sin palabras vacías, sin secretos, sin datos personales de terceros.
- [ ] El largo es el del canal.

**Terminado cuando:** la lista está completa.

## 5. Entregar

Responde con el borrador listo para copiar y, aparte, las notas internas:

```
Para: <contacto> · Canal: <WhatsApp / correo> · Firma: <socio>
[Asunto: <solo en correo>]

<borrador>

Notas internas (no se mandan):
- Por qué este enfoque: <una línea>
- Verificar antes de mandar: <datos a confirmar, o «nada»>
- Después de mandarlo: <seguimiento con fecha, o «nada»>
```

Si el usuario confirma que lo mandó, ofrece anotar la fecha en **Ultimo Contacto** del
cliente en el CRM de Notion.
