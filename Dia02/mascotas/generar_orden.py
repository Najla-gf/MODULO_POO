# archivo generar_orden.py
from orden_compra import OrdenCompra

#crear objeto de tipo OrdenCompra, y llamar al método nueva_orden
oc = OrdenCompra()
oc.nueva_orden()

#solicitar al usuario el valor para el identificador
oc.identificador = int(input("Ingrese identificador de la OC:\n"))

#total de productos y monto
oc.total_productos = int(input("Ingrese total de productos:\n"))
#oc.monto = int(input("Ingrese monto:\n"))

monto = int(input("Ingrese monto:\n"))
oc.asigna_monto(monto)
print(oc.codigo_descuento)

"""#Determinar si se aplica codigo de descuento. EL programa lo detecta según lo que usuario ingresó
if oc.monto > 20000:
    oc.codigo_descuento = "20PORCIENTO"
elif oc.monto > 10000:
    oc.codigo_descuento = "10PORCIENTO"""
