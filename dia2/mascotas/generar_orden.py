#paso2
from orden_compra import OrdenCompra

#paso3
oc = OrdenCompra()
oc.nueva_orden()

#paso4
oc.identificador = int(input("Ingrese identificador de la OC:\n"))

#paso5
oc.total_productos = int(input("Ingrese total de productos:\n"))
oc.monto = int(input("Ingrese monto:\n"))

#paso6
if oc.monto > 20000:
    oc.codigo_descuento = "20PORCIENTO"
elif oc.monto > 10000:
    oc.codigo_descuento = "10PORCIENTO"

