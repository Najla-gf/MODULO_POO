class Madre():
    def __init__(self, color: str):
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

class Padre():
    def __init__(self, tamano: int):
        self.__tamano = tamano

    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano

class Hija(Madre, Padre):
    pass

#objeto
princesa = Hija("Azul")
princesa.tamano = 80
print(princesa.tamano) #80