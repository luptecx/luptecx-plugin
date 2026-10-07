# Mantener

Todo lo que pasa después de la entrega: errores, mejoras, despliegues y reportes al
cliente. Es donde un cambio sin método daña producción, por eso es la prioridad de la
fase 2 del plan de estandarización.

Todo arreglo o mejora vuelve a entrar por `luptecx-desplegar`, que es el único punto donde
algo llega al cliente.

| Skill | Qué produce siempre igual | Usa | Quién | Estado | Prioridad |
|---|---|---|---|---|---|
| `luptecx-reportar-error` | Convierte el mensaje, audio o captura del cliente en un issue estándar en GitHub y una tarea en Notion, con severidad. No toca código | — | Felipe | Pendiente | 1 |
| `luptecx-corregir-error` | Reproducir → prueba que falla → arreglo → revisión contra `origin/main` → push con la suite en verde → CI en verde → despliegue → aviso al cliente → registro; si el error era evitable, retrospectiva | `depurar`, `probar-primero`, `revisar-cambios`, `verificar-antes-de-terminar`, `luptecx-desplegar`, `retrospectiva` | Camilo | Pendiente | 1 |
| `luptecx-nueva-funcionalidad` | Decide si está en el alcance o se cobra, estima, actualiza la especificación y el plan, programa con bandera de activación y deja el CHANGELOG | `planificar-desarrollo` (modo cambio), `construir-por-piezas` | Camilo | Pendiente | 1 |
| `luptecx-desplegar` | Lista previa, CI en verde, commits que van a salir y su revisión contra la última etiqueta, horario prohibido, respaldo, despliegue con `desplegar.py`, etiqueta, prueba de humo y cómo revertir | `revisar-cambios`, `verificar-antes-de-terminar` | Camilo | Pendiente | 1 |
| `luptecx-reporte-mensual` | Informe de resultados al cliente (métricas del bot y de publicidad) con el estilo visual | `luptecx-estilo-visual`, `luptecx-comunicacion-cliente` | Felipe | Pendiente | 3 |

Al crear una skill de esta lista: carpeta `skills/mantener/<nombre>/SKILL.md`, siguiendo
`luptecx:escribir-skills`, y se actualiza esta tabla. Las de mantener encadenan skills de
base: no repiten su contenido, las invocan.
