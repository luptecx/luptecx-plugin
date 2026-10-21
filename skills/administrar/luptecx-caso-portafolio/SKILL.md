---
name: luptecx-caso-portafolio
description: Convertir un proyecto entregado de LUPTECX en material de venta. Úsala cuando el usuario diga «hagamos el caso de <cliente>», «actualiza el Portafolio», «un post de LinkedIn sobre <proyecto>», «necesito un caso de éxito para la propuesta», o cuando `luptecx-entrega` o un buen reporte mensual lo propongan.
---

# Caso de portafolio

Cada proyecto entregado es la mejor prueba para el próximo cliente. Esta skill deja tres
piezas, siempre las mismas: **la ficha del Portafolio** al día, **un caso de una página**
en PDF y **el borrador del post de LinkedIn**. Lo técnico (instalación, código) no va aquí:
va en el README del repositorio.

Claude redacta; el cliente aprueba lo que habla de él y el socio publica.

## 1. La ficha del Portafolio

Apenas se entrega el proyecto, sin esperar resultados. En la ficha del producto
(Portafolio en Notion; la nota de la ficha dice qué va):

- **Status** = Vendida y el cliente en **Clientes Usando**.
- **Description**, **Industria**, **Stack** y **Tiempo de implementación** con lo que de
  verdad se construyó y lo que tardó (del acta de entrega).
- Si los precios de la propuesta aceptada no coinciden con los de la ficha, se pregunta
  cuál vale: la ficha es de donde salen las próximas propuestas.

**Terminado cuando:** la ficha refleja lo entregado.

## 2. ¿Hay caso?

El caso necesita resultados medidos. Pasa estos filtros antes de escribir una línea:

| Filtro | Cumple si |
|---|---|
| En producción | El sistema lleva funcionando al menos un mes, con al menos un reporte mensual |
| Cifra de antes | El diagnóstico tiene la cifra del problema, dicha por el cliente |
| Cifra de después | El reporte mensual tiene la misma cifra medida, con su fuente |
| Permiso | La carátula del contrato dice si autoriza mencionarlo. Sin autorización: versión anónima |

Si no pasa, se dice qué falta y cuándo podría haberlo. No se escribe un caso con cifras
estimadas como si fueran medidas.

**Terminado cuando:** pasa los filtros, o sabes qué falta.

## 3. La lista de pruebas

Antes de redactar, una fila por cada afirmación que va a hacer el caso:

| Afirmación | Fuente | Cuándo |
|---|---|---|
| «Contestaban la mitad de los mensajes de la noche» | Diagnóstico, Reuniones 28/09 | Antes |
| «El asistente atendió 1.180 conversaciones en octubre» | Reporte de octubre, panel de la plataforma | Después |

Lo que no tiene fuente no entra. Las citas del cliente van **tal cual las dijo**, de un
mensaje o de la reunión; no se inventan ni se «mejoran».

**Terminado cuando:** cada afirmación tiene su fila.

## 4. El caso y el post

**Versión anónima** (sin autorización): «una ferretería en Bogotá»; sin nombre, logo,
ciudad pequeña o cifra que lo delate (si el volumen lo identifica, se usa el porcentaje);
sin citas.

- **El caso:** `datos.json` con un valor por cada `{{campo}}` de
  [plantilla-caso.md](plantilla-caso.md). El titular dice el resultado («Una ferretería
  dejó de perder los mensajes de la noche»); `resultado` lleva la tabla antes y después y,
  si hay permiso, la cita. `limitaciones` dice con honestidad lo que el sistema todavía no
  hace: es lo que hace creíble el resto.

  ```powershell
  uv run --script <plugin>\herramientas\md_a_word.py --pdf --datos <carpeta>\datos.json `
    --salida "<carpeta>\Caso <producto> <fecha>.docx" <carpeta de esta skill>\plantilla-caso.md
  ```

- **El post:** sigue [linkedin.md](linkedin.md). Desde el perfil del socio que lo va a
  publicar, en primera persona.

**Terminado cuando:** el PDF y el borrador del post están listos.

## 5. Aprobación y publicación

1. **El cliente ve el texto antes de publicarlo**, también en la versión anónima:
   `luptecx:luptecx-comunicacion-cliente`, «Aprobación de un caso», con el PDF y el post.
   Se publica solo con su sí, y con sus cambios.
2. El socio publica en LinkedIn (el enlace, en el primer comentario) y la página de
   LUPTECX lo comparte.
3. **Notion:** el PDF del caso en la ficha del Portafolio (Thumbnail o un archivo en la
   página), para usarlo en las propuestas.

## Al terminar

```
Caso: <producto> · <cliente o «anónimo»>
Ficha: al día (Vendida, Clientes Usando)
Caso: <PDF> · Post: borrador para <socio>
Pruebas: <n afirmaciones con fuente>
Aprobación del cliente: <pendiente / aprobado el …>
```
