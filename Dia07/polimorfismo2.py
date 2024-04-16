class Madre():
    def __init__(self, color: str, **parametros):
        super().__init__(**parametros)
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

class Padre():
    def __init__(self, tamano: int, **parametros):
        super().__init__(**parametros)
        self.__tamano = tamano

    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano

class Hija(Madre,Padre):
    """ sobreescritura de los constructores"""
    #def __init__(self, color: str, tamano: int ):
    #    Madre.__init__(self,color)
    #    Padre.__init__(self,tamano)
    def __init__(self, deuda = 0, **parametros ):
        super().__init__(**parametros)
        
        #atributo de instancia propio de Hija
        self.deuda = deuda
        
        


#objeto
#princesa = Hija("Azul",80)
princesa = Hija(color = "Azul", tamano = 80, deuda=350)
print(princesa.tamano, princesa.color, princesa.deuda) #80 Azul 350

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"princesa es intancia de Hija: {isinstance(princesa,Hija)}") #True
print(f"princesa es intancia de Padre: {isinstance(princesa,Padre)}") #True
print(f"princesa es intancia de Madre: {isinstance(princesa,Madre)}") #True


