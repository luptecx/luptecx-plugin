# Finanzas en Notion

Se lee en los pasos 1 a 5. Notion ya calcula la utilidad, la parte de cada socio y la
liquidación 50/50 con fórmulas: **la skill no calcula, registra y revisa**.

Los identificadores de cada base están en la página «Mapa de Notion para Claude» de
Recursos (búscala por ese nombre con el conector de Notion), no aquí: el repositorio del
plugin es público. Los acuerdos con aliados, en la base Aliados ([aliados.md](aliados.md)).

| Base | Para qué | Campos que se usan |
|---|---|---|
| Cierre Mensual | Un registro por mes | Mes (título, «Octubre 2026»), Periodo, Estado (Abierto, Por cuadrar, Cerrado), Ingresos, Gastos, Aportes y Retiros, Cuadrado, Fecha de cuadre, Comprobante, Notas. Fórmulas: Utilidad, Utilidad por socio (50%), Liquidación socios, Monto a transferir |
| Client Payments | Ingresos | Name, Clientes, Fecha, Cantidad, Categoria (Pago Inicial, Mensualidad, Consultoria, Comisión aliado), Estado (Pendiente, Realizado, En Mora), Recibido por (Camilo, Felipe, Cuenta empresa), Cuenta, Cierre Mensual |
| Business Expenses | Gastos | Name, Fecha, Cantidad, Categoria (entre otras, Aliados: lo que se le paga a un aliado), Tipo de gasto (Suscripción mensual, Suscripción anual, Pago único), Status (Planeado, Pagado, No realizado), Pagado por, Clientes, Cuenta, Cierre Mensual |
| Aportes y Retiros de Socios | Plata que un socio mete o saca; no es ingreso ni gasto | Movimiento, Socio, Tipo (Aporte, Retiro de utilidades), Cantidad, Fecha, Comprobante, Cierre Mensual |
| Payment Accounts | Las cuentas donde entra y sale la plata | Name, saldos |
| Clientes (CRM) y Proyectos | Quién paga mensualidad (ver `construir/luptecx-nuevo-proyecto/notion.md`) | Proyectos en Fase Soporte |

**Lo enlazado cuenta.** Los totales del cierre suman todo lo que esté enlazado, sin mirar
el estado: un pago Pendiente o En Mora se deja **sin enlazar** hasta que entre, y un gasto
Planeado o No realizado no se enlaza.

**Cómo liquida Notion:** a cada socio le suma lo que pagó de gastos y lo que aportó, y le
resta lo que recibió de clientes y lo que retiró. La mitad de la diferencia entre los dos
es lo que uno le transfiere al otro. Por eso cada movimiento tiene que decir **quién** lo
recibió o lo pagó.

Los movimientos de los extractos son datos financieros de los socios: se usan para cruzar
y no se copian a Notion, al repositorio ni a ningún archivo que se quede.
