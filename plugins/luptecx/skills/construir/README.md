# Construir

De la propuesta aceptada al proyecto entregado y en mantenimiento.

| Skill | Qué produce siempre igual | Usa | Estado |
|---|---|---|---|
| `luptecx-nuevo-proyecto` | Arranque: proyecto en Notion (plantilla «Proyecto LUPTECX») con sus tareas, repositorio generado con la plantilla de procesos (`luptecx-plantilla`, con Copier) con los candados activados y el CI en verde, y la lista de accesos para el cliente con su borrador de mensaje; luego entrega el turno a `planificar-desarrollo` | `planificar-desarrollo` | ✅ |
| `planificar-desarrollo` | `docs/ESPECIFICACION.md`, `docs/ARQUITECTURA.md` con sus costuras y el plan de piezas, glosario y decisiones | `entrevistar`, `modelar-dominio`, `revisar-seguridad` | ✅ |
| `construir-por-piezas` | Cada pieza construida con su prueba, explicada, revisada, verificada y subida con su commit | `probar-primero`, `revisar-cambios`, `revisar-seguridad`, `verificar-antes-de-terminar`, `traspasar-sesion` | ✅ |
| `luptecx-codigo` | Las convenciones de la empresa por capas: en `SKILL.md` lo común a todo proyecto (idioma, git, documentos, pruebas, fechas, datos y secretos); en `stack-python.md` lo del stack Python. Lo propio de un tipo de proyecto va en un plugin de tipo aparte (`extras/`). Es el eje «estándares» de `revisar-cambios`; lo que se pueda comprobar solo va a un hook o al CI | — | ✅ |
| `luptecx-entrega` | Manual del cliente en `docs/MANUAL.md` y en PDF, capacitación en vivo en la que cada persona practica sola, acta de entrega en Word contra la carátula del contrato, aviso de salida en vivo y Notion en Soporte | `luptecx-comunicacion-cliente`, `herramientas/md_a_word.py` | ✅ |
| `cierre-de-proyecto` | Auditoría y limpieza del repositorio entero, revisión completa y plan de producción con vuelta atrás | `revisar-cambios`, `revisar-seguridad`, `depurar`, `probar-primero`, `verificar-antes-de-terminar` | ✅ |

## El flujo

```
luptecx-nuevo-proyecto ──► planificar-desarrollo ──► construir-por-piezas (× N piezas)
                                                              │
                     cierre-de-proyecto ◄─────────────────────┘
                            │
                     luptecx-desplegar ──► luptecx-entrega ──► (pasa a Mantener)
```

Se entrega lo que ya funciona en producción: primero se limpia y audita el repositorio,
después se despliega y al final se entrega (decisión del 16/10/2026).

La especificación y el plan se hacen en una sola conversación; cada pieza se construye en
una sesión limpia (con `traspasar-sesion` si queda algo fuera de los documentos).
