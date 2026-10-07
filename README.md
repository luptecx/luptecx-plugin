# Plugin LUPTECX

Todas las skills de LUPTECX en un solo paquete, para que los dos socios trabajen con
exactamente la misma versión. Si una skill cambia, cambia para los dos al instalar la
versión nueva.

## Cómo está organizado

Las skills van en carpetas por **etapa del cliente**, más una de **base** con las
disciplinas que usan todas las etapas:

```
skills/
├── base/          entrevistar, modelar, depurar, probar, revisar, verificar…
├── vender/        diagnóstico → propuesta → contrato
├── construir/     nuevo proyecto → planificar → construir por piezas → entrega → cierre
├── mantener/      reportar y corregir errores, funcionalidades, desplegar, reporte mensual
└── administrar/   comunicación con el cliente, cierre mensual, portafolio
```

Cada carpeta tiene su `README.md` con las skills que ya existen y las pendientes del plan
de estandarización. Las de etapa dicen *qué* se hace; las de base, *cómo* se hace bien.
Una sola skill por función.

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
| base | `retrospectiva` | Solo a mano. Convierte lo que salió mal en candados y normas |
| base | `traspasar-sesion` | Solo a mano. Resume la sesión para seguir en una limpia |
| base | `escribir-skills` | Cómo escribir skills, `CLAUDE.md` y normas para Claude |
| vender | `presentacion-ventas-contenido` | Guion de propuestas: diagnóstico + ROI, reencuadre y tres niveles de precio |
| vender | `luptecx-estilo-visual` | Diseño de cualquier presentación o PDF de LUPTECX (dirección B «Contraste») |
| construir | `planificar-desarrollo` | Especificación, arquitectura y plan de piezas antes de programar |
| construir | `construir-por-piezas` | Una pieza: prueba, explicación, revisión, verificación y push |
| construir | `cierre-de-proyecto` | Auditoría y limpieza del repositorio al cerrar o entregar un proyecto |

## El flujo de desarrollo

```
planificar-desarrollo          (una conversación)
  entrevistar + modelar-dominio → ESPECIFICACION → ARQUITECTURA → plan de piezas
        │
        ▼
construir-por-piezas           (una sesión limpia por pieza)
  probar-primero → explicar → revisar-cambios → verificar-antes-de-terminar → commit y push
        │
        ▼
cierre-de-proyecto             (al entregar)
```

Ante un error: `depurar` → `probar-primero` → `verificar-antes-de-terminar`.
Después de una sesión que salió mal: `/luptecx:retrospectiva`.

## `revisar-cambios` y el `/code-review` de Claude Code

No se pisan. `revisar-cambios` revisa si el cambio cumple **nuestras normas y la
especificación**; `/code-review` busca **bugs de corrección**. `revisar-cambios` es la que
se usa en cada cambio, y recomienda correr también `/code-review` cuando el cambio toca
dinero, fechas, el webhook o datos del cliente. Por eso no se llama `code-review`: ese
nombre ya lo usa Claude Code y taparía al nuestro.

## Cómo se cambia una skill

1. `git pull` y cambio en `skills/<división>/<skill>/`, siguiendo
   `luptecx:escribir-skills` (y su `mecanica-de-skills.md`).
2. Si es nueva o cambió de lugar, actualizar la tabla del `README.md` de su división y la
   de este archivo. Una división nueva va también en la lista `skills` de
   `.claude-plugin/plugin.json`.
3. `claude plugin validate .` tiene que pasar.
4. Subir la versión en `.claude-plugin/plugin.json` (`0.2.0` → `0.3.0` si agrega o cambia
   comportamiento; `0.2.1` si solo corrige redacción).
5. Commit con tipo (`funcionalidad: …`, `correccion: …`) y push a `main`.
6. Avisar al otro socio, empaquetar (`python empaquetar.py`) y que los dos instalen el
   `.plugin` nuevo.

Las skills que vienen de repositorios de terceros, y qué se les cambió, están en
[CREDITOS.md](CREDITOS.md); sus licencias, en `licencias/`.

## Acuerdos del equipo que las skills dan por hechos

- Sin pull requests (decisión del 04/10/2026): se trabaja con commit y push normal a `main`.
  En los proyectos, los hooks de `.githooks/` exigen el tipo de commit y corren la suite
  antes de cada push, el CI corre en cada push y solo Camilo despliega, con
  `herramientas/desplegar.py`. Nunca `git push --force` a `main` ni `--no-verify`.
- Los secretos viven en Bitwarden, nunca en chats, Notion, repositorios ni OneDrive.
- Nada se prueba contra datos reales ni contra el número real de WhatsApp de un cliente.
