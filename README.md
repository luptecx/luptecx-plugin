# Plugin LUPTECX

Todas las skills de LUPTECX en un solo paquete, para que los dos socios trabajen con
exactamente la misma versión. Si una skill cambia, cambia para los dos al instalar la
versión nueva.

## Skills

| Skill | Para qué |
|---|---|
| `presentacion-ventas-contenido` | Guion de propuestas comerciales: diagnóstico + ROI, reencuadre y tres niveles de precio |
| `luptecx-estilo-visual` | Diseño de cualquier presentación o PDF de LUPTECX (dirección B «Contraste») |
| `desarrollo-riguroso` | Especificación → arquitectura → piezas → revisión antes de escribir código |

Las skills de las fases 2 y 3 del plan de estandarización (corregir errores, nuevas
funcionalidades, desplegar, entrega, reportes…) se agregan aquí a medida que se terminan.

## Cómo se cambia una skill

1. `git pull` y cambio en `skills/<skill>/SKILL.md`.
2. Subir la versión en `.claude-plugin/plugin.json` (`0.1.0` → `0.2.0` si agrega o cambia
   comportamiento; `0.1.1` si solo corrige redacción).
3. Commit con tipo (`funcionalidad: …`, `correccion: …`) y push a `main`.
4. Avisar al otro socio, empaquetar (`python empaquetar.py`) y que los dos instalen el
   `.plugin` nuevo.

## Acuerdos del equipo que las skills dan por hechos

- Sin pull requests (decisión del 04/10/2026): se trabaja con commit y push normal a `main`.
  En los proyectos, los hooks de `.githooks/` exigen el tipo de commit y corren la suite
  antes de cada push, el CI corre en cada push y solo Camilo despliega, con
  `herramientas/desplegar.py`. Nunca `git push --force` a `main` ni `--no-verify`.
- Los secretos viven en Bitwarden, nunca en chats, Notion, repositorios ni OneDrive.
