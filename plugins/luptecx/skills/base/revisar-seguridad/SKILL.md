---
name: revisar-seguridad
description: "Seguridad del código de un proyecto de LUPTECX. Úsala al planificar algo que recibe datos de afuera, guarda datos personales o usa un modelo de IA (modelo de amenazas); al construir o cambiar código que toca entrada externa, autenticación, secretos, archivos subidos, datos personales, dependencias o IA; antes de desplegar un cambio así; cuando el usuario pida «revisa la seguridad», «¿esto es seguro?» o una auditoría; o cuando otra skill necesite revisar la seguridad del proyecto entero."
---

# Revisar seguridad

**Toda entrada de afuera es hostil, todo secreto es sagrado y toda autorización se
comprueba en el código.** Esta skill lo vuelve proceso en tres momentos: al planificar (qué
se protege y de quién), al cambiar el código (qué controles toca el cambio) y al revisar el
proyecto entero. Lo que puede vigilar una máquina ya lo vigilan los candados (detect-secrets,
ruff `S`, zizmor, pip-audit, Dependabot): aquí va lo que necesita criterio.

Las referencias se leen según el momento:

- [amenazas.md](amenazas.md): el modelo de amenazas y su plantilla.
- [controles.md](controles.md): los controles por frente (entrada, autorización, secretos,
  archivos, datos personales, dependencias, IA…). Se lee solo la sección del frente que se
  toca.

## Qué momento

| Momento | Lo pide | Qué se hace |
|---|---|---|
| Planificar | `planificar-desarrollo`, antes de la arquitectura | Paso 1 |
| Un cambio | `construir-por-piezas` o `luptecx-corregir-error`, antes del push; `luptecx-desplegar`, contra la última etiqueta | Pasos 2 a 4 |
| Proyecto entero | `cierre-de-proyecto`, la primera puesta en producción o el usuario | Pasos 2 a 4 sobre todo el código, más `insecure-defaults` |

## 1. Modelo de amenazas (al planificar)

Con [amenazas.md](amenazas.md): las **fronteras de confianza** (por dónde entra algo que no
escribimos nosotros), los **activos** (qué se protege), los riesgos de cada frontera con
STRIDE y un **caso de abuso** por cada riesgo alto. Queda en `docs/ARQUITECTURA.md`, sección
«Amenazas y datos», y cada caso de abuso pasa a ser la primera prueba de la pieza que toca
esa frontera.

Si no se pueden nombrar las fronteras, la funcionalidad todavía no está lista para
construirse: se vuelve a la especificación.

**Terminado cuando:** la sección existe, cada frontera tiene sus riesgos y su control, y el
usuario la vio.

## 2. Qué toca el cambio

Fija el punto como en `luptecx:revisar-cambios` (por defecto `origin/main`; antes de
desplegar, la última etiqueta) y lee el diff completo, con los archivos nuevos. Marca qué
**frentes** toca, con la línea que lo muestra:

| Frente | Se nota en el diff |
|---|---|
| Entrada externa | Rutas nuevas, webhooks, formularios, mensajes de usuarios, lectura de archivos o URLs que vienen de afuera |
| Autorización | Quién puede ver o cambiar qué: identificadores en la URL, roles, tokens |
| Secretos | Variables de configuración nuevas, llaves, tokens, conexiones |
| Archivos subidos | Fotos, PDF, documentos que manda un usuario |
| Datos personales | Teléfonos, cédulas, nombres, correos, datos financieros: guardarlos, mostrarlos, enviarlos, registrarlos |
| Dependencias | `pyproject.toml` o `uv.lock` cambiaron |
| IA | Llamadas a un modelo, instrucciones del sistema, herramientas que el modelo puede usar |
| Configuración | CORS, encabezados, `/docs`, Docker, modo de depuración, valores por defecto |

Si no toca ninguno, la revisión de seguridad termina aquí y el informe lo dice.

**Terminado cuando:** cada frente marcado tiene su línea de evidencia, o el informe dice
«no toca fronteras».

## 3. Revisar

1. Por cada frente marcado, lee su sección de [controles.md](controles.md) y comprueba cada
   control contra el código. Cada hallazgo lleva archivo, línea y el control que incumple.
2. Corre la revisión de seguridad de Claude Code (la skill `security-review`, el comando
   `/security-review`) sobre el mismo cambio. Lo que encuentre se verifica igual que lo
   propio: se busca el camino real de explotación antes de reportarlo.
3. Si cambiaron las dependencias, cada paquete nuevo pasa por `supply-chain-risk-auditor`
   de Trail of Bits si está instalado; si no, por la sección «Dependencias» de los
   controles.
4. En el modo **proyecto entero**, además, `insecure-defaults` de Trail of Bits si está
   instalado (valores inseguros por defecto que solo se ven en producción).

Un hallazgo sin camino de explotación posible en este proyecto es ⚪, no 🔴: lo que se
reporta es lo explotable.

**Terminado cuando:** cada control de cada frente marcado está comprobado o tiene un
hallazgo, y la revisión de Claude Code corrió.

## 4. Informe

Severidad:

- 🔴 **No se sube:** explotable desde afuera (inyección, autorización faltante, secreto en
  el código o en un log, datos personales expuestos), o algo de la columna «Nunca».
- 🟠 **Se arregla antes de desplegar:** un control faltante con camino de explotación que
  necesita algo más (un usuario autenticado, una condición rara).
- 🟡 **Endurecer:** defensa en profundidad que falta, sin camino directo.
- ⚪ **Teórico** en este proyecto.

```markdown
## Seguridad · <punto fijo>..HEAD
Frentes: <entrada externa, datos personales, …> · Revisión de Claude Code: <corrió, N hallazgos>

| # | Sev. | Dónde | Frente · control | Cómo se explota | Arreglo |

**Veredicto:** se puede subir · se sube después de corregir los 🔴 · no se sube
Preguntar antes: <lo de la columna «Preguntar antes» que el cambio hace, o «nada»>
```

Los hallazgos se atienden como en el paso 5 de `luptecx:revisar-cambios`: verificados
contra el código, en orden y cada uno con su prueba. Un 🔴 de seguridad lleva su prueba de
abuso (la que lo explotaba ahora falla). Si el usuario decide no arreglar algo, queda en
el informe como riesgo asumido, con su nombre.

## Siempre, preguntar antes, nunca

| Siempre | Preguntar antes al usuario | Nunca |
|---|---|---|
| Validar toda entrada externa en la frontera con un modelo de pydantic (forma, largo, formato) | Una forma nueva de autenticar, o cambiar la que hay | Un secreto en el código, en un log, en un mensaje o en el contexto de un modelo de IA |
| Comprobar en el código que quien pide algo tiene permiso sobre **eso** (no solo que inició sesión) | Guardar una categoría nueva de datos personales (financieros, documentos de identidad) | Construir SQL, comandos o rutas de archivos pegando texto que viene de afuera |
| Consultas parametrizadas; nunca `shell=True` con texto de afuera | Conectar un servicio externo nuevo que recibe datos personales | Datos personales en logs, en issues o en las métricas |
| Autenticar cada webhook con la firma del proveedor | Abrir CORS, cambiar encabezados o publicar `/docs` | Mostrarle al usuario una traza o un error interno |
| Errores genéricos hacia afuera; el detalle, al log sin datos personales | Un manejador nuevo de archivos subidos | Tomar la salida de un modelo de IA como orden (SQL, comando, ruta, HTML) |
| Topes: tamaño de petición, cantidad de pedidos por remitente, tokens de IA por conversación | Darle al modelo de IA una herramienta que escribe, borra, paga o le escribe a alguien | Desactivar un candado o una verificación de firma «para probar» |

## Excusas y señales de alarma

| Excusa | Realidad |
|---|---|
| «Es interno, nadie lo va a encontrar» | Los escáneres prueban cada servidor nuevo en horas; un webhook es una puerta pública |
| «La seguridad la agregamos después» | Después significa en producción, con datos reales adentro |
| «El framework ya lo hace» | FastAPI valida tipos, no permisos ni el sentido del dato |
| «Es solo texto lo que devuelve el modelo» | Es entrada de afuera: alguien pudo escribir las instrucciones que la produjeron |
| «La instrucción del sistema le prohíbe hacerlo» | Una instrucción no es una frontera; se salta con inyección. El permiso va en el código |
| «La auditoría de dependencias pasó» | Solo conoce lo ya reportado; un paquete malicioso nuevo no aparece |
| «Guardemos el documento por si acaso» | Lo que no se guarda no se filtra; la Ley 1581 pide solo lo necesario |

**Señales de alarma** en el diff: `except Exception: pass` alrededor de una verificación;
un valor por defecto en un secreto (`os.getenv("TOKEN", "dev")`); `allow_origins=["*"]`;
`subprocess` con texto de afuera; un archivo subido guardado con el nombre que mandó el
usuario; `print` o `logger` con el mensaje completo de un usuario; el texto de un usuario
pegado dentro de la instrucción del sistema.
