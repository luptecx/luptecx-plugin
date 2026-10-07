# Producción y vuelta atrás

Antes de dar un proyecto por cerrado tiene que poder responderse, sin improvisar: **¿qué
hacemos si la próxima versión sale mal?** Todo despliegue tiene que ser reversible,
observable y, si es grande, gradual. Para el detalle de despliegue por etapas, umbrales y
monitoreo, la skill `shipping-and-launch` (si está instalada) es el complemento.

## Lista previa a producción

Marca cada punto ✅ (comprobado), ⚠️ (parcial, explica) o ❌ (falta). Salta lo que no
aplique al tipo de proyecto y dilo («sin interfaz web: no aplica»).

**Código**
- La suite pasa en local y en el CI, sobre el mismo motor de base de datos que producción.
- Sin secretos ni datos reales en el repositorio.
- Sin restos de depuración ni TODOs que deban resolverse antes.
- Dependencias auditadas y fijadas.

**Configuración**
- Todas las variables de producción documentadas (archivo de ejemplo al día) y
  guardadas en un gestor de secretos, no en chats ni documentos.
- El arranque valida la configuración y se niega a seguir si falta algo obligatorio.

**Base de datos**
- Migraciones al día, y cada una con su `downgrade` probado o su vuelta atrás escrita.
- Respaldo automático y una restauración probada al menos una vez.

**Operación**
- Endpoint o comando de salud.
- Logs accesibles y sin datos sensibles.
- Alguien recibe un aviso si el servicio cae o un job programado no corre.

**Versiones**
- Cada versión desplegada tiene etiqueta (`vX.Y.Z`) y entrada en el CHANGELOG: es lo que
  dice a qué volver.
- El despliegue se hace por un solo camino documentado (un script o el CI), nunca a mano.

## Plan de vuelta atrás

Escríbelo para el proyecto concreto, con los comandos reales, y déjalo en la documentación
(README, CLAUDE.md o `docs/`). Si ya existe, compruébalo contra el código actual.

```markdown
## Vuelta atrás

### Cuándo
- <Señales concretas: el health check falla, errores nuevos en los logs, un cliente
  reporta X, un job no corrió.>

### Código
1. Identificar la versión anterior: `git tag --sort=-creatordate | head`
2. <Comando real para desplegar esa versión, o para revertir el commit y desplegar.>
3. Verificar: <health check, prueba manual del flujo crítico, logs.>
Tiempo estimado: <minutos>

### Base de datos
- Si la versión trajo migración: <comando de downgrade> o restaurar el respaldo tomado
  justo antes del despliegue (<dónde está y cómo se restaura>).
- Datos creados por la versión nueva: <se conservan / cómo se limpian>.
Tiempo estimado: <minutos>

### Configuración y servicios externos
- <Variables, plantillas, webhooks, banderas de función que hay que devolver a su valor
  anterior, y dónde se cambian.>

### Avisar
- <A quién y por dónde.>
```

## Para la propia limpieza

La limpieza también tiene su vuelta atrás, y es más sencilla: la etiqueta
`cierre-antes-AAAA-MM-DD` creada en la fase 0 y un commit por categoría. Para deshacer
una categoría: `git revert <commit>`. Para deshacer todo: revertir los commits de la
sesión en orden inverso. No se usa `reset --hard` sobre una rama ya subida.
