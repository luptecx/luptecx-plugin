---
name: bot-whatsapp
description: Reglas de LUPTECX para un proyecto que conversa por WhatsApp con la Cloud API de Meta. Úsala al diseñar, escribir, revisar, probar o desplegar el webhook, el envío de mensajes o plantillas de Meta, la deduplicación por message_id, o al pedirle al cliente los accesos de Meta. Se suma a luptecx:luptecx-codigo.
---

# Proyecto que conversa por WhatsApp

Para los proyectos que activan este plugin en su `.claude/settings.json`. Se suma a
`luptecx:luptecx-codigo` (las reglas de todo proyecto), no la reemplaza. Son lecciones que
costaron errores reales en el primer bot de LUPTECX; cada proyecto las cumple con su propio
código y su propio diseño, no copiando archivos de otro cliente.

## Arquitectura 👁

```
WhatsApp → router del webhook → deduplica por message_id → conversación (lógica del negocio)
        → servicios del proyecto → mensajes (redacta) → proveedor de WhatsApp (envía)
```

- El **router del webhook** solo autentica, traduce el payload, deduplica y descarta lo que
  llega tarde. Responde 200 de inmediato y atiende en segundo plano.
- La **conversación** es el único módulo que conoce a la vez la base de datos, los
  servicios del negocio y WhatsApp. El estado de cada conversación se guarda en la base de
  datos, nunca en memoria.
- **Mensajes** es el único que redacta textos para el usuario. La conversación decide qué
  mensaje toca; no redacta.
- El envío está tras una interfaz de **proveedor**: uno real (Cloud API de Meta) y uno de
  pruebas que acumula lo enviado. Nadie la esquiva.
- Cada excepción lleva el detalle técnico (para el log) y un mensaje para el usuario (para
  WhatsApp).

## Invariantes de todo bot

1. **Deduplicación por `message_id` con restricción única en la base de datos.** Meta
   reintenta los webhooks; sin esto una acción se ejecuta dos veces. Si la acción tiene
   confirmación, el estado se consume **antes** de ejecutar, para que una segunda
   confirmación no duplique. 👁
2. **Todo mensaje proactivo va por plantilla, nunca como texto libre.** Meta rechaza el
   texto libre pasadas 24 h desde el último mensaje del usuario (error 131047). Los
   parámetros de una plantilla no llevan saltos de línea. Una plantilla aprobada no se
   edita: un texto nuevo es una plantilla nueva. Nunca se configura el nombre de una
   plantilla que Meta no haya aprobado (error 132001: ese día no sale ningún aviso). 👁
3. **El webhook se autentica con la firma de Meta y con nada más.** Solo se acepta sin
   firma cuando el secreto de la app está vacío, y la configuración de producción no deja
   arrancar así. No se agrega una segunda vía de autenticación: la que sobra acaba siendo
   la que está vacía. 👁
4. **Desde el 01/10/2026 Meta cobra cada mensaje de servicio:** lo que se pueda decir en
   una sola burbuja (texto con sus botones) va en una. 👁
5. **Se prueba con el número de prueba de Meta**, nunca con el número real del cliente. 👁

## Antes de producción

- Una página de privacidad que describe lo que hace este bot (la exige Meta).
- Monitoreo: un endpoint `/salud` que responda a `GET` y a `HEAD`, y aviso externo de las
  tareas programadas.

## Costuras que casi siempre conviene tener 👁

Se suman al diseño de módulos de `luptecx:planificar-desarrollo`:

- El **proveedor de WhatsApp** (enviar mensaje, enviar plantilla), con su doble de pruebas.
- El **almacenamiento del cliente** (Google Sheets u otro), con su doble.
- El **reloj** (la hora de Bogotá inyectada), para probar fechas y alertas sin esperar.
- Un solo módulo de **textos al usuario**, para que lo que se le dice esté en un sitio.

## Accesos que se le piden al cliente

Se suman a las filas comunes de `accesos.md` de `luptecx-nuevo-proyecto`, con sus mismas
reglas (invitación, no contraseña; prueba antes que producción):

| Cuándo | Qué | Cómo |
|---|---|---|
| Imprescindible | Agregar a LUPTECX como socio en su portafolio comercial de Meta (Business Manager), con control total de la cuenta de WhatsApp Business | Invitación desde Meta |
| Imprescindible | El número que va a usar el servicio. Si ese número ya está en la app de WhatsApp, se decide con Camilo antes: usarlo en coexistencia o migrarlo | En el mensaje |
| Imprescindible | La empresa verificada en Meta (la hace el cliente con sus documentos; tarda días) | Que la inicie ya |
| Después | Un método de pago en la cuenta de WhatsApp (Meta cobra los mensajes) | Lo agrega el cliente |
| Después | Nombre visible y foto de perfil | Archivo e indicación |

## Cifras del reporte mensual

Se suman a `metricas.md` de `luptecx-reporte-mensual`:

| Cifra | De dónde sale |
|---|---|
| Conversaciones del mes | WhatsApp Manager de Meta (Insights), o la base del proyecto si lo registra |
| Costo de Meta en el mes, si el cliente lo paga | WhatsApp Manager (Facturación) |

## Antes de desplegar

Se suma a la lista previa de `luptecx-desplegar`:

- [ ] **Plantillas de Meta:** si la versión manda una plantilla nueva, Meta ya la aprobó y
      su nombre está en el `.env`. Nunca el nombre de una plantilla sin aprobar.
- [ ] Después de desplegar, lo que se ve en WhatsApp se prueba con un teléfono del equipo y
      el número de prueba. Nunca se escribe como si fuera el cliente ni desde su número.
