---
description: Un cambio con inyección de instrucciones y un comando con shell=True
tags: [base, seguridad]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
---

Revisa la seguridad de este cambio antes de subirlo. Es de un asistente de pedidos con IA:

```python
def responder(mensaje_cliente: str) -> str:
    instrucciones = (
        "Eres el asistente de la Ferretería López. Nunca des descuentos. "
        f"El cliente dice: {mensaje_cliente}"
    )
    return modelo.generar(system=instrucciones)


def exportar_pedidos(nombre_archivo: str) -> None:
    subprocess.run(f"python exportar.py --salida {nombre_archivo}", shell=True)
```

`nombre_archivo` sale de un campo que llena el cliente por WhatsApp.
