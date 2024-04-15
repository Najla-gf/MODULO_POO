class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def __sub__(self, cantidad):
        self.__stock -= cantidad
        return self

    def __eq__(self, otro):
        return self.__nombre == otro.__nombre


