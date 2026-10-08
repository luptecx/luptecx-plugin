# Construir

De la propuesta aceptada al proyecto entregado y en mantenimiento.

| Skill | Qué produce siempre igual | Usa | Estado | Prioridad |
|---|---|---|---|---|
| `luptecx-nuevo-proyecto` | Arranque: proyecto en Notion con sus tareas, repositorio desde `luptecx-plantilla` con los hooks activados y la lista de accesos que hay que pedirle al cliente; luego llama a `planificar-desarrollo` con la propuesta | `planificar-desarrollo` | Pendiente | 1 |
| `planificar-desarrollo` | `docs/ESPECIFICACION.md`, `docs/ARQUITECTURA.md` con sus costuras y el plan de piezas, glosario y decisiones | `entrevistar`, `modelar-dominio` | ✅ | — |
| `construir-por-piezas` | Cada pieza construida con su prueba, explicada, revisada, verificada y subida con su commit | `probar-primero`, `revisar-cambios`, `verificar-antes-de-terminar` | ✅ | — |
| `luptecx-codigo` | Las convenciones de la empresa: idioma, estructura de carpetas, tipos de commit, flujo de push, pruebas y las invariantes de todo bot de WhatsApp. Es el eje «estándares» de `revisar-cambios`; lo que se pueda comprobar solo va a un hook o al CI | — | ✅ | — |
| `luptecx-entrega` | Manual de uso en lenguaje del cliente, acta de entrega, guía de capacitación y mensaje de bienvenida | `luptecx-comunicacion-cliente` | Pendiente | 3 |
| `cierre-de-proyecto` | Auditoría y limpieza del repositorio entero, revisión completa y plan de producción con vuelta atrás | `revisar-cambios`, `depurar`, `probar-primero`, `verificar-antes-de-terminar` | ✅ | — |

## El flujo

```
luptecx-nuevo-proyecto ──► planificar-desarrollo ──► construir-por-piezas (× N piezas)
                                                              │
                                     luptecx-entrega ◄────────┘
                                            │
                                     cierre-de-proyecto ──► (pasa a Mantener)
```

`planificar-desarrollo` y `construir-por-piezas` reemplazan a `desarrollo-riguroso`
(retirada el 07/10/2026). La especificación y el plan se hacen en una sola conversación;
cada pieza se construye en una sesión limpia.
