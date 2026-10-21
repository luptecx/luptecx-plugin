# Finanzas en Notion

Se lee en los pasos 1 a 5. Notion ya calcula la utilidad, la parte de cada socio y la
liquidación 50/50 con fórmulas: **la skill no calcula, registra y revisa**.

| Base | Origen de datos (`data_source_id`) | Para qué | Campos que se usan |
|---|---|---|---|
| Cierre Mensual | `3e31aff9-02bf-813a-9303-000b54638c99` | Un registro por mes | Mes (título, «Octubre 2026»), Periodo, Estado (Abierto, Por cuadrar, Cerrado), Ingresos, Gastos, Aportes y Retiros, Cuadrado, Fecha de cuadre, Comprobante, Notas. Fórmulas: Utilidad, Utilidad por socio (50%), Liquidación socios, Monto a transferir |
| Client Payments | `2f01aff9-02bf-8163-8f24-000b16544ccd` | Ingresos | Name, Clientes, Fecha, Cantidad, Categoria (Pago Inicial, Mensualidad, Consultoria, Comisión aliado), Estado (Pendiente, Realizado, En Mora), Recibido por (Camilo, Felipe, Cuenta empresa), Cuenta, Cierre Mensual |
| Business Expenses | `2f01aff9-02bf-8128-9300-000b2c55f35a` | Gastos | Name, Fecha, Cantidad, Categoria (entre otras, Aliados: lo que se le paga a un aliado), Tipo de gasto (Suscripción mensual, Suscripción anual, Pago único), Status (Planeado, Pagado, No realizado), Pagado por, Clientes, Cuenta, Cierre Mensual |
| Aportes y Retiros de Socios | `3ef1aff9-02bf-81a3-baca-000b786d578e` | Plata que un socio mete o saca; no es ingreso ni gasto | Movimiento, Socio, Tipo (Aporte, Retiro de utilidades), Cantidad, Fecha, Comprobante, Cierre Mensual |
| Payment Accounts | `2f01aff9-02bf-81f5-9a53-000bc95cbd6e` | Las cuentas donde entra y sale la plata | Name, saldos |
| Clientes (CRM) y Proyectos | Ver `construir/luptecx-nuevo-proyecto/notion.md` | Quién paga mensualidad | Proyectos en Fase Soporte |

**Lo enlazado cuenta.** Los totales del cierre suman todo lo que esté enlazado, sin mirar
el estado: un pago Pendiente o En Mora se deja **sin enlazar** hasta que entre, y un gasto
Planeado o No realizado no se enlaza.

**Cómo liquida Notion:** a cada socio le suma lo que pagó de gastos y lo que aportó, y le
resta lo que recibió de clientes y lo que retiró. La mitad de la diferencia entre los dos
es lo que uno le transfiere al otro. Por eso cada movimiento tiene que decir **quién** lo
recibió o lo pagó.

Los movimientos de los extractos son datos financieros de los socios: se usan para cruzar
y no se copian a Notion, al repositorio ni a ningún archivo que se quede.
