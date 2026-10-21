# Accesos que se le piden al cliente

Se lee en el paso 4 de `luptecx-nuevo-proyecto`. Se toman las filas **comunes** y las de
cada cosa que **use** el proyecto según su propuesta (una plataforma, un sistema del
cliente, sus datos, una herramienta). Si el proyecto activa un plugin de tipo (por ejemplo
`luptecx-bot-whatsapp`), sus filas se suman. Lo que no esté aquí se agrega con las mismas
reglas.

## Reglas

- **Invitación, no contraseña.** El cliente invita al correo de LUPTECX en cada plataforma,
  con el rol más bajo que alcance para el trabajo. Una contraseña no se pide por WhatsApp
  ni por correo.
- Si un servicio solo funciona con usuario y contraseña o con una llave, el cliente la
  manda por **Bitwarden Send** (enlace que caduca); se le prepara el enlace para pedírsela.
- **Lo que llega va a Bitwarden**, en la colección del cliente. En Notion solo se marca
  recibido y dónde quedó; nunca el valor.
- **Imprescindible** es lo que bloquea la primera pieza; **después** es lo que hace falta
  solo para la puesta en producción. Se pide todo en el mismo mensaje, separado así, para
  que el cliente empiece por lo que nos frena.
- **Pruebas antes que producción**: primero una copia, una cuenta o un ambiente de prueba.
  Lo de producción se pide para la puesta en producción, no antes.
- **Las cuentas de terceros quedan a nombre del cliente** (Condiciones Generales, 3.3): si
  una plataforma cobra por uso, el método de pago es del cliente.

## Comunes a todo proyecto

| Cuándo | Qué | Cómo |
|---|---|---|
| Imprescindible | Quién decide, quién aprueba las entregas y el contacto técnico, con nombre y WhatsApp | En el mensaje; se anotan en «Personas del cliente», no como pendiente |
| Imprescindible | Ejemplos representativos de lo que se va a procesar (mensajes, archivos, hojas) | Inventados o con los datos personales borrados; nunca reales |
| Imprescindible | Las reglas del negocio que el sistema tiene que seguir, si no salieron en el diagnóstico | En el mensaje o en una llamada corta |
| Después | Si quiere un dominio propio en vez de `<slug>.luptecx.com`: que su proveedor de DNS cree el registro que le indiquemos | Instrucción para su proveedor |

## Según lo que use el proyecto

| Si usa… | Cuándo | Qué | Cómo |
|---|---|---|---|
| Una plataforma externa (mensajería, CRM, pagos, IA, anuncios) | Imprescindible | Usuario de LUPTECX en la cuenta del cliente, con el rol mínimo, y una cuenta o ambiente de prueba si la plataforma lo tiene | Invitación |
| Una plataforma que exige verificar la empresa | Imprescindible | Que el cliente inicie la verificación ya (la hace con sus documentos; suele tardar días) | En el mensaje |
| Una plataforma que cobra por uso | Después | Método de pago del cliente en esa cuenta | Lo agrega el cliente |
| Un sistema o API del cliente | Imprescindible | Documentación y credenciales de un ambiente de pruebas | Enlace o archivo; credenciales por invitación o Bitwarden Send |
| Un sistema o API del cliente | Después | Credenciales de producción y, si filtra por IP, autorizar la del servidor | Bitwarden Send; la IP se le da en el mensaje |
| Datos del cliente en una hoja o una base | Imprescindible | Una **copia**, compartida con la cuenta de servicio o el usuario de LUPTECX | Compartir desde la herramienta |
| Datos del cliente en una hoja o una base | Después | La hoja o base real, para la puesta en producción | Compartir desde la herramienta |
| Herramientas que se conectan entre sí (correo, CRM, n8n del cliente) | Imprescindible | Dónde entra lo que se automatiza y dónde tiene que quedar | En el mensaje |
| Algo que corre fuera de nuestro servidor | Imprescindible | Dónde va a correr (su PC, un servidor suyo) y quién lo corre | En el mensaje |
