# Técnicas de depuración

Tres técnicas de apoyo para las fases 4 y 5 de `depurar`. Adaptadas de
[obra/superpowers](https://github.com/obra/superpowers) (MIT), con ejemplos en Python.

## Rastrear hacia atrás hasta el origen

Muchos errores se manifiestan en lo profundo de la cadena de llamadas (se escribe en la
pestaña equivocada, se guarda una fecha corrida un día). El instinto es arreglar donde
aparece el error; eso es tratar el síntoma.

1. **Observa el síntoma:** «el pago del pedido 103 quedó en la fila del 102».
2. **Encuentra la causa inmediata:** qué línea escribe en esa fila.
3. **Pregunta quién la llamó, y con qué valor:**
   `escribir_pago(pestana, fila)` ← `registrar_pagos()` ← `confirmar()` ← el webhook.
4. **Sigue subiendo** hasta encontrar dónde nació el valor malo (por ejemplo, un índice
   calculado antes de ordenar los pagos).
5. **Arregla en el origen**, no donde explotó.

Si no se puede rastrear a mano, instrumenta **antes** de la operación peligrosa:

```python
import sys, traceback

def escribir_pago(pestana: str, fila: int, valor: int) -> None:
    print(f"[DEPURAR-7c1e] escribir_pago pestana={pestana} fila={fila}", file=sys.stderr)
    traceback.print_stack(file=sys.stderr)
    ...
```

Corre con `pytest -s pruebas/... 2>&1 | grep DEPURAR-7c1e` y busca en las trazas qué
prueba o qué entrada dispara la llamada.

**Una prueba ensucia a otra** (algo aparece solo cuando corre toda la suite): corre los
archivos de prueba de a uno hasta encontrar el primero que deja el rastro:

```bash
for f in pruebas/test_*.py; do pytest -q "$f" >/dev/null 2>&1; [ -e <rastro> ] && { echo "Contamina: $f"; break; }; done
```

## Defensa en profundidad

Después de encontrar la causa, una sola validación se siente suficiente, pero otro camino
de código, un refactor o un doble de prueba se la pueden saltar. Para los errores caros
(dinero, datos del cliente, mensajes enviados a quien no era), valida en **cada capa** por
la que pasa el dato y vuelve el error **estructuralmente imposible**:

1. **Entrada:** rechaza lo obviamente inválido en la frontera (el webhook, el comando).
2. **Lógica de negocio:** comprueba que el dato tiene sentido para *esta* operación.
3. **Guardas de entorno:** impide lo peligroso en contextos concretos (por ejemplo, que las
   pruebas nunca escriban en una hoja que no sea la de prueba, o que nada mande mensajes
   reales si `ENTORNO != "production"`, el valor que usa la plantilla).
4. **Rastro:** un log con contexto justo antes de la operación peligrosa, para el forense.

Prueba cada capa: intenta saltarte la primera y comprueba que la segunda lo atrapa. Esto
no reemplaza arreglar la causa: se suma.

## Esperar por la condición, no por el tiempo

Las pruebas intermitentes suelen adivinar tiempos con `time.sleep(0.5)`: pasan en un PC
rápido y fallan en el CI. Espera **la condición** que importa:

```python
import time

def esperar(condicion, descripcion: str, limite_s: float = 5.0):
    inicio = time.monotonic()
    while True:
        resultado = condicion()
        if resultado:
            return resultado
        if time.monotonic() - inicio > limite_s:
            raise TimeoutError(f"Se agotó la espera de {descripcion} tras {limite_s}s")
        time.sleep(0.01)

# Antes:  time.sleep(0.5); assert proveedor.enviados
# Ahora:
esperar(lambda: proveedor.enviados, "el mensaje de confirmación")
```

La excepción es cuando se prueba el tiempo mismo (un reintento a los 30 segundos, una
alerta programada): ahí se controla el reloj (inyectando la hora o con una librería para
congelarla), nunca con esperas reales.
