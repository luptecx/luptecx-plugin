# Formato de `docs/GLOSARIO.md`

## Estructura

```md
# Glosario · <nombre del proyecto>

<Una o dos frases: de qué negocio es este proyecto y para quién.>

## Personas

**Dueño de flota**:
Quien contrata el bot y administra los vehículos que alquila.
_Evitar_: cliente, administrador

**Conductor**:
Persona que alquila un vehículo y paga el canon semanal.
_Evitar_: arrendatario (en conversación), usuario

## Cobros

**Canon**:
Pago semanal que hace un conductor por el vehículo que alquila.
_Evitar_: cuota, mensualidad

**Lote**:
Un solo mensaje de WhatsApp con varios cobros, uno por línea, que se confirma de una vez.
_Evitar_: paquete, batch
```

## Reglas

- **Toma partido.** Si hay varias palabras para lo mismo, elige la mejor y pon las otras
  en `_Evitar_`. Así el código, la especificación y los mensajes usan una sola.
- **Definiciones cortas.** Una o dos frases. Di qué *es*, no qué *hace*.
- **Solo términos de este negocio.** Conceptos generales de programación (reintento,
  zona horaria, webhook) no van, aunque el proyecto los use mucho. Antes de agregar un
  término pregúntate: ¿es propio de este cliente o es de programación?
- **Agrupa por temas** cuando aparezcan grupos naturales (Personas, Cobros, Vehículos). Si
  todos los términos son de un mismo tema, una lista plana está bien.
- **El nombre en el código sigue al glosario.** Si el glosario dice *canon*, la función es
  `registrar_canon`, no `registrar_pago`.
