---
name: verificar-antes-de-terminar
description: Evidencia antes de afirmar. Úsala justo antes de decir que algo está listo, arreglado, terminado o que pasa; antes de un commit, un push, un despliegue o de marcar una tarea como hecha; y antes de pasar a la siguiente pieza o tarea.
---

# Verificar antes de terminar

**Ley de hierro: ninguna afirmación de éxito sin evidencia fresca.** Si no corriste el
comando que lo prueba *en este mensaje*, no puedes decir que pasa.

## La compuerta

Antes de afirmar cualquier estado o mostrar satisfacción:

1. **Identifica** qué comando prueba la afirmación.
2. **Córrelo** completo y fresco, no un resultado anterior.
3. **Lee** la salida entera: código de salida, número de fallos, advertencias.
4. **Compara:** ¿la salida confirma la afirmación?
   - No → di el estado real, con la evidencia.
   - Sí → afírmalo, **con** la evidencia (el comando y la línea que lo prueba).

Saltarse un paso no es verificar: es suponer.

## Qué prueba cada afirmación

| Afirmación | Evidencia que sí sirve | No basta |
|---|---|---|
| «Las pruebas pasan» | La salida de la suite completa: 0 fallos | Una corrida anterior, «debería pasar» |
| «El error quedó arreglado» | El lazo de `luptecx:depurar` con el síntoma original, en verde | «Cambié el código» |
| «La prueba de regresión sirve» | Rojo-verde comprobado: quitar el arreglo → falla; restaurarlo → pasa | Que pase una vez |
| «El CI está en verde» | `gh run list --branch main --limit 1` con el estado del commit que subiste | Que el hook local pasó |
| «Hay migración» | El archivo en `migraciones/` y `alembic upgrade head` corriendo sobre una base de prueba | Que cambió `app/modelos.py` |
| «Cumple lo pedido» | Releer la especificación o la pieza y marcar cada criterio, uno por uno | Que las pruebas pasan |
| «El subagente terminó» | El `git diff` con los cambios que dice que hizo | Su informe de éxito |

## La definición de terminado

Cuando la afirmación es «terminé» (una pieza, una corrección, una funcionalidad), además de
la compuerta revisa la **definición de terminado** de LUPTECX. Si el `CLAUDE.md` del
proyecto le suma algo (en «Lo propio de este proyecto»), se revisa también:

- [ ] Hay una prueba que fallaba antes del cambio y ahora pasa.
- [ ] La suite pasa en local y el CI está en verde (o, si aún no se subió, queda dicho que
      falta comprobar el CI).
- [ ] Si cambió la base de datos, hay migración.
- [ ] Si cambió el comportamiento, están al día la especificación, el CHANGELOG y, si
      aplica, el manual del cliente.
- [ ] Si apareció un término nuevo o una decisión de diseño, están en `docs/GLOSARIO.md` o
      en `docs/decisiones/`.
- [ ] Ningún secreto ni dato real de clientes en el repositorio (`git diff` revisado).
- [ ] La tarea de Notion tiene el enlace al commit.

Cada casilla se marca con su evidencia, no de memoria. La que no se pueda comprobar se
dice tal cual: «falta: el CI, porque todavía no se hizo push».

## Señales de que vas a afirmar sin evidencia

- «Debería», «seguramente», «parece que».
- Celebrar antes de verificar: «¡Listo!», «¡Perfecto!».
- Ir a hacer commit, push o desplegar sin haber corrido nada en este mensaje.
- Confiar en el informe de un subagente o en una verificación parcial.
- «Solo esta vez», o el cansancio.
