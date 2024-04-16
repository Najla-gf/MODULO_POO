from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre #Devuelve el nombre de la tienda

    @property
    def costo_delivery(self):
        return self.__costo_delivery #Devuelve el costo de delivery de la tienda

    def __str__(self):
        return f"Nombre de la tienda: {self.__nombre}, Costo de delivery: {self.__costo_delivery}"

#Método para ingresar un nuevo producto a la tienda
    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod == producto: #si el producto ya existe en la lista
                prod += producto.stock  #se incrementa el stock del producto con sobrecarga
                return
        self.__productos.append(producto)  #Agrega un nuevo producto a la lista

#Método para listar los productos de la tienda
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

#Método para realizar la venta de un producto
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                #isinstance: verifica si un objeto pertenece a una de las clases especificadas
                if isinstance(self, (Farmacia, Supermercado)):
                    if isinstance(self, Farmacia) and cantidad > 3:
                        print("No se puede solicitar más de 3 unidades por producto.")
                        return
                    cantidad_vendida = min(producto.stock, cantidad)
                    producto -= cantidad_vendida  #se resta el stock del producto vendido con sobrecarga
                    print(f"Venta realizada: {cantidad_vendida} unidades de {nombre_producto}")
                else:  #restaurante
                    pass  #no es necesario hacer validaciones ni modificar el stock para un restaurante
                return
        print("Producto no encontrado en la tienda.")

    def __eq__(self, otra):
        #Método de igualdad para comparar dos tiendas por su nombre
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

#Mensaje de envío gratis para productos sobre 15mil
    def listar_productos(self):
        lista_productos = ""
        for producto in self._Tienda__productos:  # Accedemos a productos con el nombre de la variable de clase original
            stock_info = ""
            if producto.precio > 15000:
                stock_info = ", Envío gratis al solicitar este producto\n"
            lista_productos += f"Nombre: {producto.nombre}, Precio: {producto.precio}" + stock_info
        return lista_productos
    
    """def listar_productos(self):
        return ''.join([f"Nombre: {producto.nombre}, Precio: {producto.precio}" + (", Envío gratis al solicitar este producto\n" if producto.precio > 15000 else "") 
                        for producto in self._Tienda__productos])"""