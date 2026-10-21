---
name: luptecx-cierre-mensual
description: Llevar las cuentas del mes de LUPTECX y cuadrar a los socios. Úsala al empezar el mes («registra los pagos esperados del mes», «qué nos tienen que pagar este mes») y al cerrarlo («cerremos el mes», «el cierre de octubre», «cuánto le transfiero a Felipe / a Camilo», «cuadremos las cuentas»), o cuando haya que anotar un pago de un cliente, un gasto, un aporte o retiro de un socio, o lo que se le paga o nos paga un aliado (comisiones, publicidad).
---

# Cierre mensual

Notion ya calcula la utilidad y la liquidación 50/50 entre los socios; esta skill hace que
**todo esté registrado, enlazado y cuadrado** antes de confiar en esas cifras. Es una
cadena en orden: registrar → cuadrar → revisar → liquidar → cerrar. Ningún paso empieza con
algo abierto del anterior, salvo que los dos socios decidan seguir.

Las bases, sus campos y cómo liquida Notion están en [notion-finanzas.md](notion-finanzas.md);
los acuerdos con aliados y cómo se registran sus comisiones, en [aliados.md](aliados.md).

**Claude registra y revisa; no mueve plata.** Las transferencias las hacen los socios.

## Al empezar el mes: los pagos esperados

En los primeros días del mes, por cada proyecto en **Fase Soporte**:

1. El valor de la mensualidad y su fecha de pago salen de la carátula del contrato. Si no
   hay contrato en el formato nuevo, se le pregunta al usuario, una vez por cliente.
2. Se crea en Client Payments un pago **Pendiente**: Name «Mensualidad <mes> · <cliente>»,
   Clientes, Fecha (la de vencimiento), Cantidad, Categoria = Mensualidad, **sin enlazar**
   al Cierre Mensual: el total de ingresos del cierre suma todo lo enlazado, esté pagado o
   no.
3. Lo mismo con un **Pago Inicial** que vence este mes (implementación, según la carátula).
4. Si el cliente tiene un acuerdo con un aliado ([aliados.md](aliados.md)), su comisión del
   mes se crea como gasto **Planeado** y sin enlazar, con el valor que dice el acuerdo.
5. Si el Cierre Mensual del mes no existe, se crea en Abierto.

Cuando un pago llega: Estado = Realizado, **Recibido por**, Cuenta, la fecha en que entró y
**se enlaza** al Cierre Mensual del mes en que entró la plata. Si pasa la fecha y no llegó,
el cobro lo hace `luptecx:luptecx-comunicacion-cliente` («Cobro»).

**Terminado cuando:** cada cliente con mensualidad tiene su pago esperado del mes.

## Al cerrar el mes

En los primeros 5 días hábiles del mes siguiente, junto con los reportes mensuales.

### 1. Registrar lo que falta

Revisa el mes en las cuatro bases (filtro por Mes) y que cada movimiento esté enlazado a
su Cierre Mensual:

- **Ingresos:** cada pago esperado está Realizado (con quién lo recibió) y enlazado, o pasa
  a **En Mora** y sigue sin enlazar hasta que entre. Un pago que llegó sin esperarse
  (consultoría, otro cliente) se crea y se enlaza.
- **Gastos:** cada suscripción mensual que se pagó el mes anterior tiene su gasto este mes
  (Status Pagado, Pagado por). Una suscripción que falta se pregunta: ¿se canceló o no se
  anotó?
- **Aliados:** por cada pago de un cliente con acuerdo que entró este mes, la parte del
  aliado está registrada como dice [aliados.md](aliados.md): pagada y enlazada, o Planeada
  y sin enlazar si todavía no se le transfirió.
- **Aportes y retiros:** los que dicen los socios.

**Terminado cuando:** no queda un movimiento del mes sin quién, sin cantidad o sin enlazar.

### 2. Cuadrar contra los extractos

Pide los extractos del mes de cada cuenta que se usa (de la empresa y de cada socio, solo
los movimientos de LUPTECX), en PDF o CSV. Cruza movimiento por movimiento con lo
registrado, por fecha y valor, y clasifica cada diferencia:

| Tipo | Ejemplo | Qué se hace |
|---|---|---|
| De tiempo | Pagó el 31 y entró el 1 | Se anota en el mes en que entró la plata, con una nota |
| Ajuste | Comisión del banco, 4×1000, un gasto duplicado | Se propone el registro o la corrección; el usuario aprueba cada uno |
| Por investigar | Un movimiento que nadie reconoce | Se pregunta. **Sin explicar, el mes no se cierra** |

Nunca borres un registro que parece duplicado sin mostrar los dos y tener un sí. Si no hay
extractos, se dice en el cierre: «cuadrado solo contra Notion».

**Terminado cuando:** cada diferencia está registrada, explicada o decidida por los socios.

### 3. Revisar las cifras

Lee del Cierre Mensual: Total Ingresos, Total Gastos, Utilidad, Utilidad por socio y
Liquidación socios. Compara con el mes anterior y explica en una línea cualquier cambio
grande («entró el pago inicial de un cliente nuevo»; «se pagó el dominio anual»). Lo que no se
explica se revisa antes de seguir. Si hubo aliados, una línea con lo que se llevó cada uno
y lo que se le debe.

**Terminado cuando:** las cifras se explican.

### 4. Liquidar

La fórmula **Liquidación socios** dice quién le transfiere a quién y cuánto («⏳ Pendiente:
Felipe → Camilo $350.000»). Dale a los socios esa línea y el detalle (qué recibió y qué
pagó cada uno). La transferencia la hace el socio; después:

- **Cuadrado** marcado, **Fecha de cuadre** y el comprobante en **Comprobante**.
- Si la liquidación dice «Nada que cuadrar», no hay transferencia.

**Terminado cuando:** la liquidación dice «✅ Cuadrado» o «✅ Nada que cuadrar».

### 5. Cerrar

Estado = **Cerrado**, y en **Notas**, en dos o tres líneas: cómo se cuadró (con extractos o
solo contra Notion), lo que quedó en mora y cualquier decisión tomada. Un mes Cerrado no se
modifica: una corrección posterior entra en el mes en curso, con una nota.

## Al terminar

```
Cierre <mes>: Ingresos $… · Gastos $… · Utilidad $… ($… por socio)
Cuadrado contra: <extractos de … / solo Notion> · Diferencias: <n resueltas>
En mora: <cliente y valor, o ninguno>
Aliados: <aliado $… pagado · $… por pagar, o ninguno>
Liquidación: <quién → quién $… · hecha el … / nada que cuadrar>
Estado: Cerrado
```
