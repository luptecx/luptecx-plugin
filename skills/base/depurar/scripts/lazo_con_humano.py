"""Lazo de reproducción con una persona en medio (plantilla).

Para errores que solo se reproducen si alguien hace algo a mano, por ejemplo mandar un
mensaje desde el número de prueba de WhatsApp. Claude copia este archivo fuera del
repositorio, edita los pasos y lo corre; la persona sigue las instrucciones en la
terminal y al final las respuestas quedan impresas como CLAVE=valor para que Claude las lea.

Uso:  python lazo_con_humano.py

Lo que se captura se imprime en la terminal: pide observaciones, nunca contraseñas ni
códigos. Iniciar sesión en algo es un `paso`, no una `captura`.
"""

from __future__ import annotations

capturas: dict[str, str] = {}


def paso(instruccion: str) -> None:
    """Muestra una instrucción y espera a que la persona pulse Enter."""
    print(f"\n>>> {instruccion}")
    input("    [Enter cuando esté hecho] ")


def captura(clave: str, pregunta: str) -> None:
    """Hace una pregunta y guarda la respuesta bajo `clave`."""
    print(f"\n>>> {pregunta}")
    capturas[clave] = input("    > ").strip()


# --- editar desde aquí ---------------------------------------------------------

paso("Desde el número de prueba, manda al bot el mensaje:  M1 190k")
captura("RESPONDIO", "¿El bot respondió con el resumen del lote? (s/n)")
captura("TEXTO", "Copia la respuesta del bot (o escribe 'ninguna'):")

# --- editar hasta aquí ---------------------------------------------------------

print("\n--- Capturado ---")
for clave, valor in capturas.items():
    print(f"{clave}={valor}")
