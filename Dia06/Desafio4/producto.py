class Producto:
    #Iniciamos la clase Producto con atributos de nombre, precio y stock
    def __init__(self, nombre, precio, stock=0): #Stock es 0 por default
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        

    @property
    #Método getter para acceder al nombre del producto
    def nombre(self):
        return self.__nombre

    @property
    #Método getter para acceder al precio del producto
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        #Método getter para acceder al stock del producto
        return self.__stock

    def __add__(self, cantidad):
        #Método de sobrecarga del operador de suma para aumentar el stock del producto
        self.__stock += cantidad
        return self

    def __sub__(self, cantidad):
        #Método de sobrecarga del operador de resta para modificar el stock del producto
        self.__stock -= cantidad
        return self #Entrega el producto actualizado

    def __eq__(self, otro):
        #Método de sobrecarga del operador de igualdad para comparar dos productos por su nombre
        #True si los nombres de los productos coinciden, False si no.
        return self.__nombre == otro.__nombre


