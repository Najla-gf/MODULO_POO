"""class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

import json
instancias = []

with open("Dia11/Ejercicio_producto/productos.txt") as productos:
    linea = productos.readline()
    while linea:
        producto = json.loads(linea)
        
        instancias.append(Producto(producto.get("nombre"), 
                                producto.get("precio"))
                        ) 
        linea = productos.readline()"""
        

import json
from datetime import datetime

# Abre el archivo de productos en modo lectura
with open("Dia11/Ejercicio_producto/productos.txt", "r") as productos:
    try:
        linea = productos.readline()  # Lee la primera línea del archivo
        while linea:  # Mientras haya líneas en el archivo
            try:
                # Intenta cargar la línea como un objeto JSON
                producto = json.loads(linea)
                
                # Procesa el producto y realiza alguna operación
                # Por ejemplo, crear una instancia de Producto
                # instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
                
            except Exception as e:
                # Si ocurre una excepción, registra el error en el archivo de registro
                with open("Dia11/Ejercicio_producto/error.log", "a+") as log:
                    now = datetime.now()
                    log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
                
            finally:
                linea = productos.readline()  # Lee la siguiente línea del archivo

    except Exception as e:
        # Si ocurre una excepción al abrir o leer el archivo principal, registra el error en el archivo de registro
        with open("Dia11/Ejercicio_producto/error.log", "a+") as log:
            now = datetime.now()
            log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")



