# Formato de `docs/GLOSARIO.md`

## Estructura

```md
# Glosario · <nombre del proyecto>

<Una o dos frases: de qué negocio es este proyecto y para quién.>

## Personas

**Consultorio**:
Quien contrata el servicio y atiende a los pacientes.
_Evitar_: cliente, empresa

**Paciente**:
Persona que pide y recibe una cita.
_Evitar_: usuario, cliente

## Citas

**Cita**:
Hora reservada con un profesional que el paciente ya confirmó.
_Evitar_: turno, reserva

**Reprogramación**:
Cambio de hora o de profesional de una cita ya confirmada; no crea una cita nueva.
_Evitar_: cancelación, cita nueva
```

## Reglas

- **Toma partido.** Si hay varias palabras para lo mismo, elige la mejor y pon las otras
  en `_Evitar_`. Así el código, la especificación y los mensajes usan una sola.
- **Definiciones cortas.** Una o dos frases. Di qué *es*, no qué *hace*.
- **Solo términos de este negocio.** Conceptos generales de programación (reintento,
  zona horaria, webhook) no van, aunque el proyecto los use mucho. Antes de agregar un
  término pregúntate: ¿es propio de este cliente o es de programación?
- **Agrupa por temas** cuando aparezcan grupos naturales (Personas, Citas, Pagos). Si
  todos los términos son de un mismo tema, una lista plana está bien.
- **El nombre en el código sigue al glosario.** Si el glosario dice *cita*, la función es
  `agendar_cita`, no `crear_reserva`.
