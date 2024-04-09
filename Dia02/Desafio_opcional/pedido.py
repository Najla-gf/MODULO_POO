"""
    Najla Gatica
    Lolett Llanquinao
    Jimena Traipe
"""

from te import Te 

#Solicitar al usuario ingresar los datos para generar un pedido de té
sabor = int(input("Ingrese el número correspondiente al sabor (1: Té negro, 2: Té verde, 3: Agua de hierbas):"))
#Validar que el sabor ingresado esté dentro de las opciones válidas
while sabor not in [1, 2, 3]:
    sabor = int(input("Por favor ingrese un valor válido (1, 2 o 3): "))

formato = int(input("Ingrese el formato deseado (300 para 300 gr, 500 para 500 gr):"))
#Validar que el formato ingresado esté dentro de las opciones válidas
while formato not in [300, 500]:
    formato = int(input("Por favor ingrese un valor válido (300 o 500): "))

#Obtener tiempo de preparacion y recomendacion segun el sabor ingresado por usuario
tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor)

#Crear una instancia de la clase Te
te = Te()

#Obtener el precio según el formato ingresado por el usuario
precio = Te.obtener_precio_segun_formato(formato)
print("")
#mostrar en pantalla el detalle de toda la informacion del te ordenado
print("Detalle del pedido:")
print("Sabor del té:")
if sabor == 1:
    print("Té negro")
elif sabor == 2:
    print("Té verde")
elif sabor == 3:
    print("Agua de hierbas")

print("Formato:", formato, "gr")
print("Precio: $", precio)
print("")
print("Recomendación:" ,recomendacion)
print("Tiempo de preparación:", tiempo, "minutos")

