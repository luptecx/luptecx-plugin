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

1. Rama nueva en `luptecx/luptecx-plugin`, cambio en `skills/<skill>/SKILL.md`.
2. Subir la versión en `.claude-plugin/plugin.json` (`0.1.0` → `0.2.0` si agrega o cambia
   comportamiento; `0.1.1` si solo corrige redacción).
3. Pull request y revisión del otro socio.
4. Empaquetar (`python empaquetar.py`) y que los dos instalen el `.plugin` nuevo.

## Acuerdos del equipo que las skills dan por hechos

- Nadie sube directo a `main`: todo entra por pull request con el CI en verde y la revisión
  de Camilo. Es un acuerdo, no una regla de GitHub (el plan gratuito no protege ramas en
  repos privados).
- Los secretos viven en Bitwarden, nunca en chats, Notion ni repositorios.
