# Plantilla de `docs/ESPECIFICACION.md`

Responde *qué* se construye, desde el punto de vista de quien lo usa. Sin rutas de archivo
ni código: eso envejece rápido y va en la arquitectura. Si un prototipo dejó algo que lo
dice mejor que la prosa (una tabla de estados, la forma de un mensaje), se incluye solo lo
esencial y se anota que salió del prototipo.

```markdown
# Especificación: <nombre del proyecto>

> Aprobada por <quién> el <DD/MM/AAAA>. Cada cambio de comportamiento se refleja aquí.

## Problema
<Qué hace hoy el usuario, por qué le duele y qué cambia con el sistema. Un ejemplo
concreto de uso vale más que tres párrafos.>

## Alcance
### Lo que SÍ incluye
- …
### Lo que NO incluye
- … <tan importante como lo anterior: aquí se apoya «esto se cobra aparte»>

## Requisitos funcionales
Agrupados por tema. Cada uno verificable.
### <Tema>
- **RF-01** <descripción clara>
- **RF-02** …

## Criterios de aceptación
Al menos uno medible por requisito:
- **RF-01** → se cumple cuando <condición concreta y observable>

## Reglas de negocio
### <Nombre de la regla>  *(decisión del dueño, DD/MM/AAAA)*
<La regla, con un ejemplo con números.>

## Casos borde
- ¿Qué pasa si llega vacío, duplicado, en otro formato o fuera de horario?
- ¿Qué pasa si una integración (Meta, Google) no responde a mitad del proceso?
- ¿Qué pasa si el mismo mensaje llega dos veces?
- <los propios del proyecto>

## Datos personales
Qué datos se guardan, dónde, por cuánto tiempo, quién los ve y cómo se borran a pedido
(Ley 1581 de 2012).

## Restricciones técnicas
- Lenguaje y versión, dependencias permitidas, servidor.
- Integraciones y sus límites (plantillas de Meta, cuotas de Google).
- Horario en que no se toca producción.
```
