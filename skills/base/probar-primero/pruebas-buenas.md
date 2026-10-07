# Pruebas que atrapan errores

Léelo al escribir o cambiar pruebas, al agregar dobles o utilidades de prueba. Dos
principios lo gobiernan todo:

1. **Cada prueba nombra el fallo que atrapa.**
2. **Cada prueba ejercita lo real.**

Adaptado de [obra/superpowers](https://github.com/obra/superpowers) y
[mattpocock/skills](https://github.com/mattpocock/skills) (MIT).

## Nombrar el fallo

Antes de escribir el cuerpo de la prueba, responde: **¿qué cambio en el código de
producción la haría fallar, y ese cambio es un error o una decisión?** Una prueba se gana
su lugar atrapando una rama equivocada, un efecto que no ocurrió, un argumento mal pasado,
un caso límite o un contrato roto.

**Expectativas escritas a mano.** El valor esperado sale de una fuente independiente: un
literal, un ejemplo calculado a mano, la especificación. Nunca del mismo código que se
prueba:

```python
# ❌ Tautológica: el valor esperado se calcula igual que lo calcula el código
def test_total_suma_cobros():
    cobros = [190_000, 185_000]
    assert total(cobros) == sum(cobros)

# ✅ Literal comprobado a mano
def test_total_suma_cobros():
    assert total([190_000, 185_000]) == 375_000
```

**Sin detectores de cambios.** Si solo una decisión intencional puede hacer fallar la
prueba (el valor de una constante, la redacción exacta de un mensaje), salta en cada
rediseño y duerme ante los errores. Prueba el comportamiento que depende de la decisión:
no `assert REINTENTOS == 3`, sino «una llamada que falla se reintenta 3 veces y la cuarta
nunca ocurre».

**Comportamiento, no texto.** Que un script o una plantilla *contenga* cierta línea no
prueba nada. Córrelo con entradas controladas y afirma salidas, efectos o códigos de
salida.

**Tu código, no el del framework.** Prueba el contrato que tu código hace en sus bordes (la
ruta que registras, la fila que escribes, el mensaje que mandas), no que FastAPI llame a tu
función o que SQLAlchemy guarde. Constructores, getters y constantes solo se prueban cuando
validan, normalizan, calculan o causan efectos.

**A través de la interfaz.** Verifica por la misma costura que usa quien llama, no por un
canal lateral:

```python
# ❌ Se salta la interfaz para verificar
def test_registrar_conductor_lo_guarda():
    registrar_conductor(nombre="Ana", moto="M1")
    fila = db.execute("SELECT * FROM conductores WHERE nombre = 'Ana'").first()
    assert fila is not None

# ✅ Verifica por la interfaz
def test_conductor_registrado_se_puede_consultar():
    conductor = registrar_conductor(nombre="Ana", moto="M1")
    assert buscar_conductor(conductor.id).moto == "M1"
```

## Ejercitar lo real

**El doble no gana aserciones.** Una aserción sobre el doble pasa cuando el doble está y
falla cuando no está: no dice nada del componente. Afirma el comportamiento real; si lo que
estás comprobando es el doble, quítalo o borra la aserción.

**Dobles al nivel correcto.** Antes de reemplazar algo, conoce todos sus efectos. Dobla
la operación lenta o externa (la llamada HTTP a Meta) y deja real lo que la prueba
necesita (el registro del mensaje en la base, que la deduplicación lee).

**Dobles específicos.** Cuando los argumentos, el número de llamadas o el orden son parte
del contrato, afírmalos: un doble que acepta cualquier cosa no verifica nada. Cada rama
(éxito, error, respuesta malformada) con su propio caso.

**Datos con la estructura completa.** Un payload de webhook de prueba lleva todos los
campos que Meta manda de verdad, no solo los que la prueba lee: un doble a medias falla en
silencio cuando el código de abajo lee el campo que faltaba. Guarda payloads reales
(tachados) como fixtures.

**Lo de prueba se queda en las pruebas.** Un método que solo llaman las pruebas (limpiar,
reiniciar) va en las utilidades de prueba, nunca en la clase de producción.

**Prefiere componentes reales a dobles complicados.** Cuando preparar el doble ocupa más
que la prueba, cambia a una prueba de integración con los componentes reales (base SQLite
de prueba, el doble del proveedor de WhatsApp).

## Diseñar para poder probar

- **Recibe las dependencias, no las crees adentro:** `procesar_lote(lote, proveedor)` se
  prueba; una función que hace `ProveedorMeta(os.environ["TOKEN"])` por dentro no.
- **Una función por operación externa** (`enviar_plantilla`, `marcar_leido`) en vez de un
  `llamar_api(endpoint, opciones)` genérico: cada doble devuelve una sola forma y se ve qué
  operaciones usa cada prueba.
- **Devuelve resultados en vez de producir efectos** cuando se pueda: calcular el total y
  luego escribirlo, no las dos cosas dentro de la misma función.

## La comprobación de mutaciones

Antes de terminar, muta mentalmente el código de producción. Al menos una prueba tiene que
fallar con cada mutación realista:

- Una constante o un argumento equivocado.
- La rama equivocada de un `if`.
- Un efecto que no ocurre (no se escribe la fila, no se manda el mensaje).
- Un retorno vacío o por defecto.
- Falta validar cero, vacío, `None`, no autorizado o malformado.

Una mutación que nadie atrapa marca un comportamiento sin proteger, o una prueba
tautológica.

## Señales de alarma

- La preparación y la aserción comparten el mismo objeto, así que la igualdad está
  garantizada.
- La prueba solo puede fallar por una excepción, nunca por un valor equivocado.
- Falla con cada cambio intencional y nunca con un error de verdad.
- El valor esperado está escondido detrás de bucles o funciones auxiliares.
- Existe para subir la cobertura, sin comprobar ningún efecto ni resultado.
- El doble ocupa más de la mitad de la prueba, o no sabes explicar por qué hace falta.
