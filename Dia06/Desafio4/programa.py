"""
    Najla Gatica
    Lolett Llanquinao
    Jimena Traipe
"""


from tienda import Tienda, Restaurante, Supermercado, Farmacia
from producto import Producto

def crear_tienda():
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ").lower()
    
    if tipo_tienda == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo_tienda == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo_tienda == "farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None

def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    return Producto(nombre, precio, stock)

def main():
    tienda = crear_tienda()
    if tienda is None:
        return

    # Solicitar ingresar productos hasta que el usuario indique lo contrario
    while True:
        respuesta = input("¿Desea ingresar un producto? (s/n): ").lower()
        if respuesta == "s":
            producto = ingresar_producto()
            tienda.ingresar_producto(producto)
            print("Producto ingresado exitosamente.")
        elif respuesta == "n":
            break
        else:
            print("Respuesta no válida. Por favor, ingrese 's' para sí o 'n' para no.")

    # Presentar opciones al usuario
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Listar productos existentes")
        print("2. Realizar una venta")
        print("3. Salir del programa")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            print("\nProductos existentes:")
            print(tienda.listar_productos())

        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto que desea vender: ")
            cantidad = int(input("Ingrese la cantidad que desea vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)

        elif opcion == "3":
            print("¡Adiós! Muchas gracias por su preferencia")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 3.")

if __name__ == "__main__":
    main()
