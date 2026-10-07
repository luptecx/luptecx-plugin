# Diseño de módulos

Vocabulario para decidir dónde van los módulos y qué expone cada uno. Adaptado de la skill
`codebase-design` de [mattpocock/skills](https://github.com/mattpocock/skills) (MIT), que
a su vez sigue a John Ousterhout (*A Philosophy of Software Design*) y Michael Feathers.

## Términos

- **Módulo:** cualquier cosa con interfaz e implementación: una función, una clase, un
  archivo de `app/`.
- **Interfaz:** todo lo que quien llama tiene que saber para usarlo bien: la firma, pero
  también sus reglas, el orden de llamada, los errores que lanza y la configuración que
  necesita.
- **Profundidad:** cuánto comportamiento se obtiene por cada cosa que hay que aprender de
  la interfaz. Un módulo **profundo** esconde mucho detrás de una interfaz pequeña; uno
  **superficial** tiene una interfaz casi tan complicada como lo que hace.
- **Costura:** el lugar donde se puede cambiar el comportamiento sin editar ese lugar; ahí
  vive la interfaz, y ahí se prueba.
- **Adaptador:** lo concreto que cumple una interfaz en una costura. El proveedor real de
  Meta y su doble de pruebas son dos adaptadores de la misma costura.

## Principios

- **Profundo sobre superficial.** Al diseñar una interfaz pregunta: ¿puedo tener menos
  funciones? ¿Parámetros más simples? ¿Esconder más adentro?
- **La prueba de borrado.** Imagina que borras el módulo. Si la complejidad desaparece,
  solo pasaba cosas de un lado a otro. Si reaparece repartida en quienes lo llaman, se
  estaba ganando su lugar.
- **La interfaz es la superficie de prueba.** Quien llama y la prueba cruzan la misma
  costura. Si quieres probar *por debajo* de la interfaz, el módulo tiene la forma
  equivocada.
- **Un adaptador es una costura hipotética; dos, una real.** No crees una costura si nada
  cambia a través de ella. El proveedor de WhatsApp sí la merece: tiene el real y el doble
  de pruebas.
- **Recibe las dependencias, no las crees.** `procesar_lote(lote, proveedor)` se prueba;
  una función que construye su propio cliente de Meta por dentro, no.
- **Devuelve resultados en vez de producir efectos** cuando se pueda: calcular por un
  lado, escribir por otro.

## Para los bots de WhatsApp de LUPTECX

Las costuras que casi siempre conviene tener, porque se repiten en cada bot:

- El **proveedor de WhatsApp** (enviar mensaje, enviar plantilla), con su doble de pruebas.
- El **almacenamiento del cliente** (Google Sheets u otro), con su doble.
- El **reloj** (la hora de Bogotá inyectada), para probar fechas y alertas sin esperar.
- Un solo módulo de **textos al cliente** (`mensajes.py`), para que lo que se le dice al
  cliente esté en un sitio.
