# Controles por frente

Se lee en el paso 3 de `revisar-seguridad`, **solo la sección del frente que toca el
cambio**. Cada control es comprobable en el código. Los ejemplos son del stack Python de
LUPTECX (FastAPI, pydantic, uv); en otro stack se busca el equivalente. Entre paréntesis, la
categoría de OWASP Top 10:2025 (A) o de OWASP para aplicaciones con LLM 2025 (LLM).

## Entrada externa (A05, A06)

- Cada ruta y cada webhook reciben un **modelo de pydantic**, no un `dict`: tipos, largos
  máximos (`max_length`), formatos y valores permitidos. El código de abajo usa solo el valor
  ya validado.
- Una petición demasiado grande se rechaza antes de leerla (la plantilla trae el tope).
- Nada de afuera se pega en SQL, en un comando (`subprocess` con lista de argumentos y sin
  `shell=True`), en una ruta de archivo ni en HTML.
- URLs que da un usuario (descargar una imagen, un enlace): solo `https`, host en una lista
  permitida, sin redirecciones y nunca hacia IP privadas o `169.254.169.254` (SSRF).
- Lo que llega tarde, repetido o en desorden se maneja a propósito (un webhook se reintenta):
  deduplicar por el identificador del proveedor con restricción única en la base.

## Autorización (A01)

- Cada operación comprueba que quien la pide **tiene permiso sobre ese recurso**, no solo
  que está autenticado. Un identificador en la URL o en el mensaje no prueba nada.
- El remitente se identifica por lo que garantiza la plataforma (la cuenta o el número
  que firmó la plataforma), nunca por lo que el usuario escribe («soy el administrador»).
- Endpoints internos (`/metricas`, administración) con token de Bitwarden comparado con
  `secrets.compare_digest`; sin token configurado, el endpoint no existe.

## Webhooks y autenticación (A07)

- Cada webhook verifica la **firma** del proveedor sobre el cuerpo crudo, con comparación en
  tiempo constante. Sin firma válida, 401 y nada más.
- Producción no arranca si falta un secreto de autenticación: nada de valores por defecto
  (`os.getenv("SECRETO", "dev")` es un 🔴).
- Contraseñas, si las hay: argon2 o bcrypt, nunca guardadas ni comparadas en claro.

## Secretos

- Vienen del entorno (`configuracion.py`), viven en Bitwarden y en el `.env` del servidor;
  `.env.ejemplo` dice el nombre, nunca el valor.
- No aparecen en logs, errores, métricas, issues ni en el contexto de un modelo de IA.
- Un secreto que llegó a GitHub (aunque se borre) está comprometido: se cambia primero en su
  origen y después se limpia, como dice `docs/RECUPERACION.md`.

## Archivos subidos (A06)

- Lista de tipos permitidos comprobada por el **contenido** (los primeros bytes), no por la
  extensión ni por el tipo que declara el cliente. Tope de tamaño.
- Se guardan con un nombre generado por el sistema, fuera de cualquier carpeta pública, y
  nunca se ejecutan ni se abren con herramientas que interpretan macros.
- Si el documento solo hay que pasarlo a otro (por ejemplo, al cliente para su estudio de
  crédito), se pasa y no se guarda; si se guarda, tiene fecha de borrado.

## Configuración y respuestas (A02, A10)

- En producción: `/docs`, `/redoc` y `/openapi.json` apagados (la plantilla lo hace con
  `ENTORNO=production`).
- CORS cerrado: solo si una página web propia lo necesita, con la lista exacta de orígenes y
  nunca `*`.
- Encabezados de seguridad en cada respuesta (la plantilla los trae).
- Un error inesperado responde un mensaje genérico; la traza va al log, tachada. Un
  `except` que se traga el error alrededor de una verificación es un 🔴 (A10).
- Docker sin root, sistema de archivos de solo lectura y sin privilegios extra (la plantilla
  los trae); solo escucha en `127.0.0.1`.

## Datos personales (Ley 1581 de 2012)

- **Lo mínimo:** cada dato que se guarda tiene una finalidad escrita en la especificación;
  lo que no tiene finalidad no se guarda.
- **Cuánto tiempo:** cada categoría tiene plazo de borrado, y el borrado es real (base,
  respaldos y copias), no un campo «inactivo».
- **Logs y métricas:** sin datos personales; el registro de la plantilla tacha teléfonos,
  cédulas y correos, pero lo correcto es no mandarlos.
- **Proveedores que los reciben** (servidor, mensajería, modelo de IA): listados en la
  carátula del contrato y en «Amenazas y datos». Un proveedor nuevo es «preguntar antes».
- Datos financieros y documentos de identidad son la categoría más delicada: cifrados en
  reposo si se guardan, y accesibles solo por la parte del sistema que los necesita.

## Dependencias (A03)

- Una dependencia nueva se justifica (¿la librería estándar o una que ya está no alcanza?)
  y se revisa: quién la mantiene, cuántos la usan, cuándo salió la versión y qué trae.
- `uv` espera 7 días antes de aceptar una versión recién publicada (la plantilla lo trae);
  si una corrección urgente necesita una más nueva, se exceptúa ese paquete solo, con el
  porqué en el commit.
- pip-audit en el CI y Dependabot vigilan lo ya reportado; un paquete malicioso nuevo no lo
  ven, por eso la espera.

## IA (OWASP para aplicaciones con LLM 2025)

- **Inyección de instrucciones (LLM01):** todo lo que escribe o manda un usuario (texto,
  imágenes, documentos) es dato. Va separado y marcado como contenido del usuario, nunca
  pegado dentro de la instrucción del sistema. La instrucción del sistema no es una
  frontera: lo que el modelo no debe poder hacer, el código no se lo deja hacer.
- **Información sensible (LLM02, LLM07):** en el contexto, solo lo que la conversación
  necesita; nada de secretos, ni datos de otros clientes o usuarios, ni más de lo necesario
  de los documentos. Se asume que la instrucción del sistema puede filtrarse: no lleva nada
  que no se pueda leer.
- **Salida del modelo (LLM05):** se valida contra un esquema (salida estructurada) antes de
  usarla, y nunca se ejecuta como SQL, comando, ruta o HTML.
- **Agencia excesiva (LLM06):** el modelo tiene solo las herramientas que necesita, cada una
  con el mínimo permiso y con sus argumentos validados en el código. Lo que escribe, borra,
  paga, decide sobre una persona o le escribe a alguien nuevo pasa por una persona o por
  una regla del código.
- **Consumo sin tope (LLM10):** tope de tokens por respuesta, de turnos por conversación y
  de conversaciones por remitente; límite de gasto en la cuenta del proveedor.
- **Desinformación (LLM09):** lo que el modelo afirma sobre precios, inventario o
  condiciones sale de los datos del cliente, no de su memoria; si no está en los datos, dice
  que no sabe y pasa a una persona.
- Las pruebas usan un doble del modelo; los casos de abuso de inyección se prueban contra
  el código que arma el contexto y el que valida la salida.
