# Aliados y comisiones

Se lee al crear los pagos esperados y en el paso 1 del cierre. Un **aliado** es una empresa o
persona externa con la que LUPTECX comparte ingresos: vende un servicio suyo a nuestros
clientes, o nos trae clientes. No es socio: lo que se le paga es un gasto, y la utilidad que
se reparte 50/50 es lo que queda después.

## Acuerdos vigentes

| Aliado | Qué hace | Lo que gana LUPTECX | Lo que gana el aliado | Desde |
|---|---|---|---|---|
| Steven (publicidad) | Maneja la publicidad que pagan algunos de nuestros clientes | 40 % del onboarding de la publicidad (el primer mes) y 20 % de cada mes siguiente | El resto: 60 % del onboarding y 80 % de cada mes siguiente | 21/10/2026 |
| Steven, como vendedor | Nos trae un cliente que compra un producto de LUPTECX | El resto: 60 % del pago inicial y 80 % de cada mensualidad | 40 % del pago inicial y 20 % de cada mensualidad | 21/10/2026 |

Los porcentajes **no tienen límite de tiempo**: se pagan mientras el cliente pague.

Un acuerdo nuevo o un cambio de porcentajes se anota aquí y en el Registro de decisiones de
Notion, con su fecha. Un cambio no toca los meses ya cerrados.

## Qué cliente tiene un acuerdo

Lo dice el CRM de Notion: en la ficha del cliente, **cuál aliado** y **por qué** (le vendemos
su publicidad, o él nos trajo al cliente). Si el CRM no lo dice, se le pregunta al usuario
una vez por cliente y se anota en el CRM. Para la publicidad hace falta además **cuánto del
cobro es publicidad**: sale de la carátula o de la propuesta; si no lo dice, se pregunta. Lo
usual es que **$1.000.000 del pago inicial** sea el onboarding de la publicidad (Steven
$600.000, LUPTECX $400.000), pero se confirma con cada cliente.

## Cómo se registra

La comisión se debe **cuando el cliente paga**, no antes: un pago del cliente En Mora no
genera comisión hasta que entra.

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
