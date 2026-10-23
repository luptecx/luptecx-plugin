# Mantener

Todo lo que pasa después de la entrega: errores, mejoras, despliegues y reportes al
cliente. Es donde un cambio sin método daña producción.

Todo arreglo o mejora vuelve a entrar por `luptecx-desplegar`, que es el único punto donde
algo llega al cliente.

| Skill | Qué produce siempre igual | Usa | Quién | Estado |
|---|---|---|---|---|
| `luptecx-reportar-error` | Convierte el mensaje, audio o captura del cliente (o un error del monitor) en un issue de GitHub y una tarea de Notion enlazados, con severidad, plazo y datos personales enmascarados; deja el borrador del acuse al cliente. Si es algo nuevo, lo registra como funcionalidad. No toca código | — | Felipe | ✅ |
| `luptecx-corregir-error` | Del issue al cliente: tomar el caso (mitigar primero si es Crítica), depurar, prueba de regresión y arreglo, revisión contra `origin/main`, push con CI en verde, CHANGELOG y despliegue, y cierre del issue con la versión, la tarea en Done y el aviso al cliente; si era evitable, recomienda la retrospectiva | `depurar`, `probar-primero`, `revisar-cambios`, `revisar-seguridad`, `verificar-antes-de-terminar`, `luptecx-desplegar` | Camilo | ✅ |
| `luptecx-nueva-funcionalidad` | Del pedido al cliente, sin cobro aparte (va en la mensualidad): ¿encaja en el proyecto o es otro producto?, tamaño y prioridad, especificación y plan, piezas con bandera de activación si hace falta, despliegue, encendido y aviso | `planificar-desarrollo` (modo cambio), `construir-por-piezas`, `luptecx-desplegar` | Camilo | ✅ |
| `luptecx-desplegar` | Lista previa (CHANGELOG, revisión contra la última etiqueta, CI, migraciones, configuración y plantillas), despliegue con `desplegar.py` corrido por quien despliega, prueba de humo, aviso y cómo revertir | `revisar-cambios`, `revisar-seguridad`, `verificar-antes-de-terminar` | Camilo | ✅ |
| `luptecx-reporte-mensual` | PDF de dos o tres páginas y un mensaje corto: lo que logró el sistema (este mes, el anterior y antes de LUPTECX, cada cifra con su fuente), lo que hizo LUPTECX (errores con su tiempo contra el contrato, funcionalidades, versiones) y lo que sigue con una recomendación; en los primeros 5 días hábiles, antes del cobro | `luptecx-comunicacion-cliente`, `herramientas/md_a_word.py` | Felipe | ✅ |

Al crear una skill de esta lista: carpeta `skills/mantener/<nombre>/SKILL.md`, siguiendo
`luptecx:escribir-skills`, y se actualiza esta tabla. Las de mantener encadenan skills de
base: no repiten su contenido, las invocan.
