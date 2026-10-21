---
name: probar-primero
description: Desarrollo guiado por pruebas, con el ciclo rojo-verde. Úsala al implementar cualquier funcionalidad, corrección de error o cambio de comportamiento, antes de escribir el código de producción, y siempre que el usuario mencione TDD, «prueba primero», «rojo-verde» o pruebas de integración.
---

# Probar primero

Escribe la prueba. Mírala fallar. Escribe el código mínimo para que pase.

Si no la viste fallar, no sabes si prueba lo que crees.

**Ley de hierro: ningún código de producción sin una prueba que haya fallado primero.**
¿Escribiste código antes de la prueba? Bórralo y empieza de nuevo. No lo guardes «de
referencia», no lo «adaptes» mientras escribes la prueba: borrar es borrar.

Excepciones, solo si el usuario las aprueba: un prototipo desechable, código generado,
archivos de configuración.

## Dónde van las pruebas: las costuras

Una **costura** es la frontera pública donde se observa el comportamiento sin meterse
adentro: la función que recibe el mensaje del webhook, el servicio que registra un pedido, el
comando. Las pruebas viven en costuras, nunca contra los internos.

- **Funcionalidad nueva:** antes de la primera prueba, propón las costuras con una línea de
  qué atrapa y qué no atrapa cada una, y confírmalas con el usuario (si vienes de
  `luptecx:planificar-desarrollo`, ya están en el plan de piezas). Prefiere la costura más
  alta posible y las que ya existen sobre las nuevas: cuantas menos, mejor.
- **Corrección de error:** la costura es donde el síntoma se observa tal como lo vio el
  usuario; el caso mínimo de `luptecx:depurar` es la primera prueba.

Si una prueba es difícil de escribir, el diseño es difícil de usar: escucha a la prueba y
simplifica la interfaz.

## El ciclo

Trabaja en **rebanadas verticales**: una prueba → el código que la hace pasar → la
siguiente prueba, cada una respondiendo a lo que enseñó la anterior. Escribir todas las
pruebas primero y todo el código después prueba comportamiento *imaginado*.

### 1. Rojo: una prueba que falla

Un comportamiento, nombre claro en español, código real.

```python
def test_pedido_con_descuento_resta_el_descuento_del_total():
    pedido = interpretar_pedido("3 tornillos 6000 descuento 1000")

    assert pedido.total_neto == 5_000
```

### 2. Verificar el rojo (obligatorio)

```bash
pytest pruebas/test_pedidos.py::test_pedido_con_descuento_resta_el_descuento_del_total -q
```

Confirma que **falla** (no que da error de sintaxis o de importación) y que falla **por la
razón esperada**: falta el comportamiento. ¿Pasa de una vez? Estás probando algo que ya
existe: corrige la prueba.

### 3. Verde: el código mínimo

Lo más simple que haga pasar esa prueba. Sin parámetros «por si acaso», sin mejorar otras
partes de paso.

### 4. Verificar el verde (obligatorio)

Corre la prueba y su archivo completo. Todo en verde y la salida limpia, sin errores ni
advertencias nuevas. ¿Falla? Arregla el código, no la prueba.

### 5. Ordenar

Solo con todo en verde: quitar duplicación, mejorar nombres. Sin agregar comportamiento.
Una reestructuración grande no va aquí: va en su propio commit `refactorizacion:`, con la
suite en verde antes y después.

Repite con la siguiente prueba.

## Dobles de prueba: solo en los bordes

Usa dobles **solo en los bordes del sistema**: una API externa (el proveedor y su doble de
pruebas), una hoja de cálculo, la red, el reloj. Nunca dobles de tus propios módulos. Las
pruebas no salen a la red ni tocan datos reales de clientes.

Las reglas para que una prueba atrape errores de verdad (nombrar el fallo que atrapa,
expectativas escritas a mano, dobles con la estructura completa, la comprobación de
mutaciones) están en [pruebas-buenas.md](pruebas-buenas.md): léelas al escribir o cambiar
pruebas.

## Excusas frecuentes

| Excusa | Realidad |
|---|---|
| «Es muy simple para probarlo» | Lo simple también se rompe. La prueba toma 30 segundos. |
| «La escribo después» | Una prueba escrita después pasa de una: no prueba nada. |
| «Ya lo probé a mano» | A mano no queda registro ni se puede repetir cuando el código cambie. |
| «Borrar horas de trabajo es un desperdicio» | Ese tiempo ya se gastó. Lo que desperdicia es quedarse con código que no se puede confiar. |
| «Primero exploro» | Bien. Luego bota la exploración y empieza con la prueba. |
| «El código viejo no tiene pruebas» | Lo estás mejorando: agrégale pruebas. |

## Señales para borrar y empezar de nuevo

Código antes que la prueba · una prueba que pasa de una · no puedes explicar por qué falló
· «solo por esta vez» · «es el espíritu, no el ritual» · «lo dejo de referencia».

## Antes de dar la pieza por terminada

- [ ] Cada función o comportamiento nuevo tiene su prueba.
- [ ] Viste fallar cada prueba, por la razón esperada, antes de implementar.
- [ ] Escribiste el código mínimo para cada una.
- [ ] Toda la suite pasa y la salida está limpia.
- [ ] Las pruebas usan código real; los dobles solo en los bordes.
- [ ] Casos borde y errores cubiertos.

¿No puedes marcarlas todas? Te saltaste el método: vuelve al rojo.
