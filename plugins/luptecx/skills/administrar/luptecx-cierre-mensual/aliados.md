# Aliados y comisiones

Se lee al crear los pagos esperados y en el paso 1 del cierre. Un **aliado** es una empresa o
persona externa con la que LUPTECX comparte ingresos: vende un servicio suyo a nuestros
clientes, o nos trae clientes. No es socio: lo que se le paga es un gasto, y la utilidad que
se reparte 50/50 es lo que queda después.

## Dónde están los acuerdos

Los acuerdos son de la empresa y **no se escriben en el plugin** (su repositorio es
público): viven en la base **Aliados** de Notion, dentro de Finanzas, con su identificador en
la página «Mapa de Notion para Claude» de Recursos (búscala por ese nombre con el conector de Notion). Cada fila es un acuerdo:

| Campo | Qué dice |
|---|---|
| Acuerdo, Aliado, Caso | Con quién y en qué caso: «Le vendemos su servicio» o «Nos trae un cliente» |
| Aliado: % del onboarding, Aliado: % de cada mes | Lo que gana el aliado; LUPTECX gana el resto |
| Onboarding usual | Cuánto del pago inicial suele ser la parte del aliado; se confirma con cada cliente |
| Límite, Desde, Estado | Hasta cuándo se paga, desde cuándo y si sigue Vigente |
| Clientes | Los clientes del CRM a los que aplica el acuerdo |
| Notas | Lo que no cabe en los campos (cifras de un cliente, excepciones) |

Un acuerdo nuevo o un cambio de porcentajes se escribe en esa base y en el Registro de
decisiones, con su fecha. Un cambio no toca los meses ya cerrados.

## Qué cliente tiene un acuerdo

El campo **Clientes** de la base Aliados. Si un cliente no aparece en ningún acuerdo y el
usuario dice que tiene uno, se agrega ahí. Para la parte del aliado hace falta además
**cuánto del cobro le corresponde** (por ejemplo, qué parte es publicidad): sale de la
carátula, de la propuesta o de las Notas del acuerdo; si no, se pregunta y se anota en las
Notas.

## Cómo se registra

La comisión se debe **cuando el cliente paga**, no antes: un pago del cliente En Mora no
genera comisión hasta que entra. Si el pago inicial se paga por partes (por ejemplo, la
mitad al empezar y la mitad al salir en vivo), se pregunta en qué cuota se le paga al
aliado su parte del onboarding, y se anota en la ficha del cliente en el CRM.

| Caso | Ingreso (Client Payments) | Gasto (Business Expenses) |
|---|---|---|
| El cliente nos paga todo, publicidad incluida | El pago completo, como siempre | «Publicidad <mes> · <cliente>» por la parte del aliado, Categoria «Aliados», Clientes = el cliente |
| El cliente le paga la publicidad directo al aliado | Solo nuestra parte, Name «Comisión publicidad <mes> · <cliente>», Categoria «Comisión aliado», cuando el aliado la transfiera | — |
| El aliado nos trajo al cliente | El pago del cliente completo, como siempre | «Comisión <Pago inicial / Mensualidad> <mes> · <cliente>» por su parte, Categoria «Aliados», Clientes = el cliente |

Cada gasto al aliado lleva **Pagado por** (quien le transfirió) y se enlaza al Cierre Mensual
del mes en que se le pagó; mientras no se le pague, queda Planeado y sin enlazar. Si una
categoría no existe en la base, se crea con ese nombre exacto.

**Al revisar** (paso 3), se dice en una línea lo que se llevó cada aliado en el mes y lo
que se le debe todavía.
