from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    def __str__(self):
        return f"Nombre de la tienda: {self.__nombre}, Costo de delivery: {self.__costo_delivery}"

    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod == producto:
                prod += producto.stock  # Aplicando sobrecarga del operador __add__
                return
        self.__productos.append(producto)

    def listar_productos(self):
        lista_productos = ""
        for producto in self.__productos:
            stock_info = ""
            if self.tipo == "Restaurante" or self.tipo == "Farmacia":
                stock_info = ""
            elif self.tipo == "Supermercado" and producto.stock < 10:
                stock_info = f", Pocos productos disponibles: {producto.stock}\n"
            #elif self.tipo == "Farmacia":
                #stock_info = ", Envío gratis al solicitar este producto" if producto.precio > 15000 else ""
            else:
                stock_info = f", Stock: {producto.stock}\n"
            lista_productos += f"Nombre: {producto.nombre}, Precio: {producto.precio}" + stock_info
        return lista_productos

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if isinstance(self, (Farmacia, Supermercado)):
                    if isinstance(self, Farmacia) and cantidad > 3:
                        print("No se puede solicitar más de 3 unidades por producto en una venta de una farmacia.")
                        return
                    cantidad_vendida = min(producto.stock, cantidad)
                    producto -= cantidad_vendida  # Aplicando sobrecarga del operador __sub__
                    print(f"Venta realizada: {cantidad_vendida} unidades de {nombre_producto}")
                else:  # Restaurante
                    pass  # No es necesario hacer validaciones ni modificar el stock para un restaurante
                return
        print("Producto no encontrado en la tienda.")

    def __eq__(self, otra):
        return self.__nombre == otra.__nombre


class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
        self.tipo = "Restaurante"

    # Imprimir mensaje de venta en supermercado
    def realizar_venta(self, nombre_producto, cantidad):
        print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")


class Supermercado(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
        self.tipo = "Supermercado"


class Farmacia(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
        self.tipo = "Farmacia"

def listar_productos(self):
        lista_productos = ""
        for producto in self._Tienda__productos:  # Accedemos a productos con el nombre de la variable de clase original
            stock_info = ""
            if producto.precio > 15000:
                stock_info = ", Envío gratis al solicitar este producto\n"
            lista_productos += f"Nombre: {producto.nombre}, Precio: {producto.precio}" + stock_info
        return lista_productos