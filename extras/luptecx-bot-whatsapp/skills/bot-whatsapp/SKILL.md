---
name: bot-whatsapp
description: Reglas de LUPTECX para un proyecto que conversa por WhatsApp con la Cloud API de Meta. Úsala al diseñar, escribir, revisar, probar o desplegar el webhook, el envío de mensajes o plantillas de Meta, la deduplicación por message_id, al pedirle al cliente los accesos de Meta, o al sumar un cliente a un producto que atienden varios. También al redactar o diseñar lo que lee el usuario (textos, botones, listas, carrusel, fotos, el tono del bot o las instrucciones de un modelo que conversa), o cuando un mensaje «suena a bot». Se suma a luptecx:luptecx-codigo.
---

# Proyecto que conversa por WhatsApp

Para los proyectos que activan este plugin en su `.claude/settings.json`. Se suma a
`luptecx:luptecx-codigo` (las reglas de todo proyecto), no la reemplaza. Son lecciones que
costaron errores reales en el primer bot de LUPTECX.

## Un cliente o varios

- **El código se puede reutilizar** de un proyecto a otro. Lo que nunca pasa de un cliente
  a otro son sus datos, su configuración ni sus secretos. 👁
- **Producto** (el mismo servicio vendido a varios clientes, decisión del 22/10/2026): un
  producto de LUPTECX vive en un solo repositorio y un solo despliegue. Sus clientes son
  filas y configuración validada, nunca un repositorio, una rama, un archivo copiado ni un
  `if` con su nombre. La plantilla `copier` genera el repositorio del producto, no uno por
  cliente. 👁

En los dos casos lo de un cliente nunca se mezcla con lo de otro. En un producto eso no lo
garantizan repositorios separados sino la base de datos y las pruebas:

- Cada tabla de negocio lleva el id del cliente (`concesionario_id`, `cliente_id`…),
  obligatorio, y toda consulta filtra por él. 👁
- El cliente se identifica en el borde, antes de tocar nada: en WhatsApp, por el
  `phone_number_id` del webhook. Lo que llega a un número que no es de ningún cliente se
  descarta. 👁
- La configuración de cada cliente se valida con pydantic y se guarda en la base, no en el
  repositorio, porque trae datos reales. 👁
- Una prueba de aislamiento con dos clientes corre en el CI: lo que entra por el número de
  uno nunca lee, escribe ni responde con datos del otro. 🔒

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
6. **El bot nunca dice ser una persona.** Suena humano, pero si le preguntan, dice que es
   automático y ofrece pasar con alguien: las políticas de WhatsApp prohíben engañar y
   piden una vía directa a una persona. 👁

## Los mensajes que lee el usuario

Antes de redactar o cambiar un texto fijo, un mensaje con botones, una lista, un carrusel,
el envío de fotos o las instrucciones de un modelo que conversa, lee
[diseno-de-mensajes.md](diseno-de-mensajes.md): qué componente usar, los límites de cada
uno, cómo se lee humano, el ritmo (el indicador de «escribiendo…») y cómo se revisa en un
celular. **Terminado cuando** cada mensaje nuevo cabe en sus límites con los datos más
largos posibles y se vio en el número de prueba.

## Antes de producción

- Una página de privacidad que describe lo que hace este bot (la exige Meta).
- Monitoreo: un endpoint `/salud` que responda a `GET` y a `HEAD`, y aviso externo de las
  tareas programadas.

## Costuras 👁

Además de las que tiene casi todo proyecto (`diseno-de-modulos.md` de
`luptecx:planificar-desarrollo`: almacenamiento del cliente, reloj y textos al usuario),
el **proveedor de WhatsApp** (enviar mensaje, enviar plantilla), con su doble de pruebas.

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
      su nombre está en el `.env` (en un producto, en la configuración de ese cliente).
      Nunca el nombre de una plantilla sin aprobar.
- [ ] Después de desplegar, lo que se ve en WhatsApp se prueba con un teléfono del equipo y
      el número de prueba. Nunca se escribe como si fuera el cliente ni desde su número.
