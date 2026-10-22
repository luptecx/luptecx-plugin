---
type: llm
weight: 2
---
La revisión encuentra los dos problemas y los marca como graves: (1) el mensaje del cliente
va pegado dentro de las instrucciones del sistema (inyección de instrucciones: el cliente
puede pedir descuentos o cambiar el comportamiento); (2) `subprocess` con `shell=True` y un
valor que viene del cliente (inyección de comandos). Para cada uno propone el arreglo: el
texto del cliente separado como contenido del usuario y la regla de descuentos en el código;
`subprocess` con lista de argumentos, sin shell, y el nombre validado.
