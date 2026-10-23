---
type: llm
weight: 2
---
La revisión encuentra los dos problemas y los marca como graves (🔴 o «no se sube»):
(1) el mensaje del cliente va pegado dentro de las instrucciones del sistema (inyección de
instrucciones: el cliente puede pedir descuentos o cambiar el comportamiento); (2)
`subprocess` con `shell=True` y un valor que viene del cliente (inyección de comandos). Para
el (1) propone mandar el texto del cliente separado, como contenido del usuario; para el
(2), `subprocess` con lista de argumentos, sin shell, y el nombre validado. Que reporte
además otros hallazgos, o que deje alguna regla en las instrucciones del sistema junto a los
controles en el código, no la hace fallar.
