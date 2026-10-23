# Plugin LUPTECX

Todas las skills de LUPTECX en un solo paquete, para que los dos socios trabajen con
exactamente la misma versión. Si una skill cambia, cambia para los dos al instalar la
versión nueva.

## Cómo está organizado

Las skills van en carpetas por **etapa del cliente**, más una de **base** con las
disciplinas que usan todas las etapas:

```
plugins/luptecx/skills/
├── base/          entrevistar, modelar, depurar, probar, revisar, verificar…
├── vender/        diagnóstico → presentación → cotización → contrato
├── construir/     nuevo proyecto → planificar → construir por piezas → entrega → cierre
├── mantener/      reportar y corregir errores, funcionalidades, desplegar, reporte mensual
└── administrar/   comunicación con el cliente, cierre mensual, portafolio
```

Cada carpeta tiene su `README.md` con sus skills y cómo se encadenan. Las de etapa dicen
*qué* se hace; las de base, *cómo* se hace bien.
Una sola skill por función, y **ninguna es de un proyecto ni de un tipo de proyecto**.

El plugin general vive en `plugins/luptecx/` (manifiesto, skills, hooks, herramientas,
créditos y licencias). En la raíz quedan solo el marketplace, este README y
`empaquetar.py`: la app de claude.ai no carga un plugin cuya carpeta es la raíz del
repositorio, porque esa carpeta contiene también el marketplace y los plugins de tipo.

Lo que solo sirve a un tipo de proyecto va en un **plugin de tipo** aparte, en `extras/`,
que se activa solo en los proyectos de ese tipo. Hoy hay uno:
`extras/luptecx-bot-whatsapp` (proyectos que conversan por WhatsApp con la Cloud API de
Meta).

En Claude todas aparecen como `luptecx:<nombre>` (por ejemplo `luptecx:revisar-cambios`).

## Skills que ya existen

| División | Skill | Para qué |
|---|---|---|
| base | `entrevistar` | Preguntas por rondas, con recomendación, hasta que no quede nada supuesto |
| base | `modelar-dominio` | Glosario del negocio (`docs/GLOSARIO.md`) y decisiones de diseño (`docs/decisiones/`) |
| base | `depurar` | Lazo que se pone rojo con el error → hipótesis → arreglo con prueba de regresión |
| base | `probar-primero` | Prueba que falla, código mínimo, en las costuras acordadas |
| base | `verificar-antes-de-terminar` | Evidencia antes de decir «listo», con la definición de terminado |
| base | `revisar-cambios` | Revisión en dos ejes, estándares y especificación, antes del push y de desplegar |
| base | `revisar-seguridad` | Modelo de amenazas al planificar y revisión de seguridad de cada cambio que toca una frontera (entrada externa, datos personales, secretos, dependencias, IA), con OWASP y el `/security-review` de Claude Code |
| base | `retrospectiva` | Solo a mano. Convierte lo que salió mal en candados y normas |
| base | `traspasar-sesion` | Traspaso para seguir en una sesión limpia en vez de `/compact`: estado de git, intentos fallidos, decisiones y siguiente paso, encadenado con el anterior |
| base | `escribir-skills` | Cómo escribir skills, `CLAUDE.md` y normas para Claude |
| vender | `presentacion-ventas-contenido` | Guion de propuestas: diagnóstico + ROI, reencuadre y tres niveles de precio que salen del Portafolio |
| vender | `propuesta-honorarios-luptecx` | Solo cotizaciones (propuestas de honorarios) en PDF tipo carta comercial, con los precios del Portafolio |
| vender | `luptecx-diagnostico` | Prepara la reunión de diagnóstico y después ordena lo dicho, saca los datos de la propuesta y dice si el cliente encaja |
| vender | `luptecx-contrato-servicio` | Contrato en Word desde la propuesta aceptada: carátula, Condiciones Generales y anexo de datos personales. Borrador hasta la revisión del abogado |
| vender | `luptecx-estilo-visual` | Diseño de cualquier presentación o PDF de LUPTECX (dirección B «Contraste») |
| construir | `luptecx-codigo` | Convenciones de la empresa por capas: lo común a todo proyecto, más la referencia del stack Python, que se lee según lo que declare el `CLAUDE.md` |
| construir | `luptecx-nuevo-proyecto` | Arranque tras la propuesta aceptada: proyecto y tareas en Notion, repositorio con la plantilla de procesos y CI en verde, y la lista de accesos para el cliente |
| construir | `luptecx-entrega` | Manual del cliente (repositorio y PDF), capacitación en vivo, acta de entrega en Word y paso a Soporte |
| construir | `planificar-desarrollo` | Especificación, arquitectura y plan de piezas antes de programar |
| construir | `construir-por-piezas` | Una pieza: prueba, explicación, revisión, verificación y push |
| construir | `cierre-de-proyecto` | Auditoría y limpieza del repositorio al cerrar o entregar un proyecto |
| administrar | `luptecx-comunicacion-cliente` | Borradores de todo mensaje al cliente con la voz de LUPTECX: errores e incidentes, avances, cobro, decir que no e incentivar a comprar. Claude redacta; el socio aprueba y manda |
| administrar | `luptecx-caso-portafolio` | Ficha del Portafolio, caso de una página con cifras con fuente y post de LinkedIn; anónimo sin permiso, y siempre aprobado por el cliente |
| administrar | `luptecx-cierre-mensual` | Pagos esperados al empezar el mes; al cerrarlo, registrar, cuadrar contra extractos, revisar, liquidar 50/50 (lo calcula Notion) y cerrar. Las comisiones con aliados van como gasto antes del 50/50 (`aliados.md`) |
| mantener | `luptecx-reportar-error` | Lo que reporta o pide un cliente → issue de GitHub + tarea de Notion enlazados, con severidad y plazo; sin tocar código |
| mantener | `luptecx-corregir-error` | Del issue al cliente: depurar, prueba de regresión, revisión, CI, despliegue y cierre del issue con la versión |
| mantener | `luptecx-nueva-funcionalidad` | Del pedido al cliente: ¿encaja?, tamaño y prioridad, planificar, construir por piezas, desplegar y avisar |
| mantener | `luptecx-reporte-mensual` | Reporte del mes al cliente en PDF: resultados con su fuente, trabajo de LUPTECX contra los tiempos del contrato y una recomendación |
| mantener | `luptecx-desplegar` | Lista previa, despliegue con `desplegar.py`, prueba de humo, aviso al cliente y cómo revertir |

## Herramientas

`plugins/luptecx/herramientas/md_a_word.py` arma en Word (y en PDF, si el PC tiene Word) cualquier
documento de LUPTECX escrito en Markdown: el contrato, el acta de entrega y el manual del
cliente. Llena los `{{campos}}` desde un `datos.json`, se niega si falta uno y resalta en
amarillo lo pendiente. Se corre con `uv run --script`.

`plugins/luptecx/herramientas/asegurar_claude.py` aplica los ajustes de seguridad de
LUPTECX a Claude Code en el PC donde se corre (ver «Cómo se instala»).

`plugins/luptecx/herramientas/evaluar.py` corre las evaluaciones de las skills críticas con
el plugin cargado de verdad (ver «Cómo se cambia una skill»).

## Skills externas (de terceros, tal cual)

El plugin trae también skills de otros equipos que nos sirven y no se pisan con las
nuestras. **No se editan**: se usan como vienen, en inglés, fijadas a un commit revisado.

| Skill | De | Cómo viene | La usa |
|---|---|---|---|
| `luptecx:fastapi` | FastAPI (oficial), MIT | Copia en `plugins/luptecx/skills/externas/` | `luptecx-codigo` (stack Python) |
| `luptecx:skill-scanner` | Sentry, Apache-2.0 | Copia en `plugins/luptecx/skills/externas/` | `escribir-skills`, antes de instalar o copiar una skill |
| `insecure-defaults` (comando `/insecure-defaults:audit`) | Trail of Bits, CC BY-SA 4.0 | Dependencia: plugin propio en el marketplace | `revisar-seguridad`, modo proyecto entero |
| `supply-chain-risk-auditor` | Trail of Bits, CC BY-SA 4.0 | Dependencia | `revisar-seguridad`, al agregar una dependencia |
| `property-based-testing` | Trail of Bits, CC BY-SA 4.0 | Dependencia | `probar-primero`, para reglas que valen para todas las entradas |

- **Copias** (`plugins/luptecx/externas.json`): skills sueltas con licencia que permite
  copiarlas. Se traen o actualizan con `python herramientas/traer_externas.py` (desde
  `plugins/luptecx`), que las baja en el commit fijado con su licencia.
- **Dependencias** (`.claude-plugin/marketplace.json`, fuente `git-subdir` con `sha`):
  plugins completos con comandos, agentes o scripts, o con licencia que pide no mezclarlos
  (CC BY-SA). `luptecx` los declara en `dependencies`: **al instalar `luptecx` en Claude
  Code se instalan solos**. En claude.ai, si se sube el plugin como archivo, no vienen.
- **Para actualizar una:** se cambia su commit (en `externas.json` o en el `sha` del
  marketplace), se revisa el cambio con `luptecx:skill-scanner` y leyéndolo, y se sube con
  su commit. Nunca se apunta a una rama sin fijar.
- **Revisadas y no incluidas** (21/10/2026): `shipping-and-launch` (Addy Osmani: se pisa con
  `luptecx-desplegar`, que se quedó con lo que le servía), `differential-review` y `fp-check` (se pisan con `revisar-seguridad`),
  `modern-python` (sus hooks cambian `pip` y `python` por debajo; ya seguimos uv),
  `sharp-edges`, CodeQL y las de contratos inteligentes, C y Rust (no aplican hoy).

## El flujo de desarrollo

```
luptecx-nuevo-proyecto         (una vez, al aceptar la propuesta)
  Notion → repositorio con la plantilla de procesos → accesos del cliente
        │
        ▼
planificar-desarrollo          (una conversación)
  entrevistar + modelar-dominio → ESPECIFICACION → ARQUITECTURA → plan de piezas
        │
        ▼
construir-por-piezas           (una sesión limpia por pieza)
  probar-primero → explicar → revisar-cambios → verificar-antes-de-terminar → commit y push
        │
        ▼
cierre-de-proyecto             (antes de la primera puesta en producción)
        │
        ▼
luptecx-desplegar ──► luptecx-entrega ──► mantener
```

Ante un error mientras se construye: `depurar` → `probar-primero` →
`verificar-antes-de-terminar`. Ante uno que reportó un cliente: `luptecx-reportar-error` →
`luptecx-corregir-error`, que encadena las mismas.
Después de una sesión que salió mal: `/luptecx:retrospectiva`.
Para seguir en una sesión limpia (al cerrar una pieza, al cambiar de tarea o hacia el 60 %
del contexto, antes de que llegue el `/compact` automático): `luptecx:traspasar-sesion`.

## `revisar-cambios` y el `/code-review` de Claude Code

No se pisan. `revisar-cambios` revisa si el cambio cumple **nuestras normas y la
especificación**; `/code-review` busca **bugs de corrección**. `revisar-cambios` es la que
se usa en cada cambio, y recomienda correr también `/code-review` cuando el cambio toca
dinero, fechas, el webhook o datos del cliente. Por eso no se llama `code-review`: ese
nombre ya lo usa Claude Code y taparía al nuestro.

## Cómo se instala

El repositorio es también un marketplace (`.claude-plugin/marketplace.json`). Es
**público**: no lleva datos de clientes, secretos ni identificadores de Notion (esos viven
en la página «Mapa de Notion para Claude»). Los proyectos y la plantilla sí son privados.

**En Claude Code, para todos los proyectos** (una vez por PC; queda en el usuario):

```powershell
claude plugin marketplace add luptecx/luptecx-plugin
claude plugin install luptecx@luptecx
```

**En la app de escritorio o claude.ai (chat y Cowork):** primero se quita el `luptecx`
que esté subido como archivo. Luego **Customize › Plugins › Add marketplace**, escribir
`luptecx/luptecx-plugin` e instalar `luptecx`. Si el marketplace no carga, se sube el
archivo:
`python empaquetar.py` deja `dist/luptecx-<versión>.plugin` (sin los plugins de tipo de
`extras/`), y en **Customize › Plugins** se sube ese archivo. Subido así no se actualiza
solo: cada versión nueva se vuelve a subir.

Con `luptecx` se instalan solas sus dependencias de Trail of Bits (`insecure-defaults`,
`supply-chain-risk-auditor` y `property-based-testing`); la skill de FastAPI y
`skill-scanner` ya vienen adentro. No hay que instalar nada aparte.

**Si ya tenías `luptecx` de antes de la 0.25.0:** actualizar no instala dependencias nuevas
y el plugin no carga («Dependency … is not installed»). Se arregla una vez así:

```powershell
claude plugin marketplace update luptecx
claude plugin uninstall luptecx@luptecx
claude plugin install luptecx@luptecx
```

Debe decir `(+ 3 dependencies: …)`. Las dependencias se descargan por HTTPS desde GitHub;
no hace falta llave SSH.

**En cada proyecto**, además, la plantilla de procesos genera `.claude/settings.json` con
el marketplace y `luptecx@luptecx` activado: quien abra el repositorio en Claude Code y no
lo tenga recibe el aviso para instalarlo. Un plugin de tipo se activa ahí mismo
(`"luptecx-bot-whatsapp@luptecx": true`), solo en los proyectos que lo necesitan.

**Ajustes de seguridad de cada PC** (una vez por PC, después de instalar el plugin):
Claude no lee secretos en ninguna carpeta (.env, credenciales, llaves, `~/.ssh`, el token de
`gh`, Bitwarden) y nadie lo arranca saltándose los permisos. En PowerShell:

```powershell
python (Get-ChildItem "$HOME\.claude\plugins\cache\luptecx\luptecx\*\herramientas\asegurar_claude.py" | Select-Object -Last 1).FullName
```

Es idempotente, guarda una copia de la configuración de antes y cuenta desde la próxima
sesión. El aislamiento (`/sandbox`) de Claude Code no funciona en Windows nativo, solo en
WSL2: por eso los permisos y el hook de secretos son la barrera.

**Las versiones nuevas**, en Claude Code (el primer comando solo trae el catálogo; los
otros instalan, cada uno en el alcance donde está el plugin):

```powershell
claude plugin marketplace update luptecx
claude plugin update luptecx@luptecx --scope user
claude plugin update luptecx@luptecx --scope project              # desde la carpeta de cada proyecto
claude plugin update luptecx-bot-whatsapp@luptecx --scope project # solo en los proyectos que lo activan
```

y se reinicia Claude Code. En la app: **Check for updates**. `python empaquetar.py` sigue
sirviendo para subir el plugin como archivo si alguna vez el marketplace no está disponible.

**El Python de cada PC** (una vez): los proyectos usan el Python que instala uv, nunca el del
sistema ni el de conda, para que un `.venv` no se caiga cuando ese otro Python cambie:
`uv python install 3.12` y, en `%APPDATA%\uv\uv.toml`, `python-preference = "only-managed"`.

## Cómo se cambia una skill

**Evaluaciones de las skills críticas** (`plugins/luptecx/evals/`): seis casos que
comprueban lo que más cuesta si falla (un issue sin datos personales, no desplegar con el CI
en rojo, una cotización sin precios inventados ni comisiones, la revisión de seguridad que
encuentra la inyección, un aviso sin jerga, una funcionalidad que no se cobra aparte). Al
cambiar una de esas skills, antes de subirla, desde `plugins/luptecx`:

```powershell
python herramientas/evaluar.py -j 3
```

No se usa `claude plugin eval .` directo: cada caso corre en una sesión aislada sin las
dependencias de Trail of Bits, el plugin no carga y el caso mide al modelo solo (pasó hasta
el 23/10/2026). `evaluar.py` evalúa una copia sin `dependencies` y le pasa tal cual el resto
de argumentos. Llama al modelo con las credenciales del PC: la primera vez hay que iniciar
sesión en el `claude` de la terminal. Por defecto corre cada caso 3 veces con el plugin y 3
sin él, y muestra cuánto mejora el plugin (el 23/10/2026: 1.00 con plugin en los seis,
+0.50 de media); para probar rápido, `--runs 1 --ablation none`, y un solo caso con
`--case <nombre>`. Cuesta unos 5 USD la suite completa. Los resultados quedan en
`evals/results/` (ignorada por git).

Este repositorio tiene los mismos candados que los proyectos: una vez por clon,
`uvx prek install`. Al hacer commit revisan el formato, los secretos y el tipo del mensaje;
al hacer push, que el plugin valide, los encabezados de las skills y los casos del hook de
secretos. El CI (`.github/workflows/plugin.yml`) lo repite en cada push, y `main` está
protegida: no acepta push forzado ni que la borren.

1. `git pull` y cambio en `plugins/luptecx/skills/<división>/<skill>/`, siguiendo
   `luptecx:escribir-skills` (y su `mecanica-de-skills.md`).
2. Si es nueva o cambió de lugar, actualizar la tabla del `README.md` de su división y la
   de este archivo. Una división nueva va también en la lista `skills` de
   `plugins/luptecx/.claude-plugin/plugin.json`.
3. Desde la raíz del repositorio, `claude plugin validate .` y
   `uv run --script plugins/luptecx/herramientas/revisar_encabezados.py` tienen que pasar.
   El segundo revisa lo que el primero no ve: que el encabezado de cada `SKILL.md` sea YAML
   válido y que la descripción no quede cortada (un `#` o un `: ` en el texto la rompen;
   entonces va entre comillas dobles).
4. Subir la versión en `plugins/luptecx/.claude-plugin/plugin.json` (`0.4.0` → `0.5.0` si agrega o cambia
   comportamiento; `0.4.1` si solo corrige redacción).
5. Commit con tipo (`funcionalidad: …`, `correccion: …`) y push a `main`.
6. Avisar al otro socio. Cada uno actualiza como dice «Las versiones nuevas» (Claude Code)
   o, en la app, **Customize › Plugins** › marketplace `luptecx` › **Check for updates**.

Las skills que vienen de repositorios de terceros, y qué se les cambió, están en
[CREDITOS.md](plugins/luptecx/CREDITOS.md); sus licencias, en `plugins/luptecx/licencias/`.

## Acuerdos del equipo que las skills dan por hechos

- Sin pull requests (decisión del 04/10/2026): se trabaja con commit y push normal a `main`.
  En los proyectos, los candados de prek (`.pre-commit-config.yaml`) exigen el tipo de commit y corren la suite
  antes de cada push, el CI corre en cada push y solo Camilo despliega, con
  `herramientas/desplegar.py`. Nunca `git push --force` a `main` ni `--no-verify`: el
  hook del plugin (`hooks/`) se lo impide a Claude en Claude Code, junto con
  `reset --hard`, `clean -f`, `branch -D`, `checkout .` y `restore .`. GitHub no lo puede
  impedir: en el plan gratis, `main` de un repositorio privado no se puede proteger.
- Los secretos viven en Bitwarden, nunca en chats, Notion, repositorios ni OneDrive. El
  hook `bloquear-secretos.sh` le impide a Claude leerlos o imprimirlos por comando (.env,
  credenciales, llaves, variables con tokens, `gh auth token`); sus casos están en
  `hooks/probar_bloquear_secretos.py`, que se corre antes de cambiarlo.
- Nada se prueba contra datos reales ni contra las cuentas o números reales de un cliente.
