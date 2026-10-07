# Revisión del código entero

Una revisión de cierre lee el proyecto como lo leerá quien lo mantenga dentro de un año.
No busca el estilo perfecto: busca lo que va a fallar en producción, lo que va a confundir
y lo que sobra. Recorre los apartados en orden; los primeros pesan más.

## 1. Corrección

- Las invariantes del proyecto (reglas que el `CLAUDE.md` o el README declaran que no se
  pueden romper): compruébalas **una por una** contra el código actual.
- Casos borde que el código no cubre: entradas vacías, nulos, duplicados, reintentos,
  zonas horarias, redondeos de dinero, concurrencia.
- Manejo de errores: ¿qué ve el usuario cuando falla una dependencia externa? ¿Se tragan
  excepciones en silencio (`except: pass`)? ¿Un fallo de un cliente tumba a los demás?
- Idempotencia de lo que se puede repetir (webhooks, jobs, reintentos): ¿un reintento
  duplica datos?

## 2. Seguridad

- Ningún secreto en el código, en la configuración versionada ni en los logs.
- Cada endpoint expuesto: ¿quién puede llamarlo y cómo se autentica? Un endpoint
  administrativo sin autenticación es 🔴.
- Validación de entradas que vienen de fuera; consultas parametrizadas (sin SQL armado
  con cadenas); nada de `eval` sobre datos de usuario.
- Configuración de producción: el arranque se niega a seguir sin las variables
  obligatorias, el modo de depuración está apagado, los valores por defecto son seguros.
- Dependencias: auditoría del ecosistema (`pip-audit`, `npm audit`, `cargo audit`…) y
  versiones fijadas.
- Datos personales: qué se guarda, cuánto tiempo, y que no aparezcan en logs.

## 3. Código muerto y restos

- Lo que encontró la fase 3 de la skill, confirmado.
- `print`/`console.log` de depuración, `breakpoint()`, banderas de depuración activas.
- `TODO`/`FIXME`: cada uno se resuelve, se convierte en una tarea (issue) o se borra si ya
  no aplica. Un TODO de hace meses en código de producción es una decisión pendiente.
- Banderas de función (feature flags) que ya están al 100 %: se quita la bandera y el
  camino viejo.

## 4. Pruebas

- La suite pasa en una máquina limpia: ninguna prueba depende de archivos que solo están
  en un PC (`.env`, credenciales, datos locales) ni de la red.
- Las partes críticas (dinero, datos del cliente, autenticación, fechas) tienen pruebas.
- Pruebas que se saltan siempre o que fallan de forma intermitente: se arreglan o se
  documenta por qué se saltan.

## 5. Claridad para quien mantenga

- Nombres que dicen lo que hacen, en el idioma que fija el repositorio.
- Comentarios que explican el porqué; los que repiten el qué, o describen algo que ya no
  es así, sobran.
- Módulos con una responsabilidad clara; dependencias entre módulos sin ciclos.
- Duplicación evidente (la misma lógica copiada en dos sitios que ya divergen).

## 6. Operación

- Logs útiles en los puntos donde algo puede fallar, sin datos sensibles.
- Un endpoint o comando de salud, y algo que avise si un job programado no corre.
- Respaldo de la base de datos y que alguien haya probado restaurarlo.

## Cómo reportar cada hallazgo

`archivo:línea` · severidad · qué pasa · qué pasaría si no se arregla · propuesta.
Si no puedes describir un escenario concreto en el que falla, no es 🔴 ni 🟠.
