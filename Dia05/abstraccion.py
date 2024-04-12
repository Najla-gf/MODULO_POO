"""
ABSTRACCION: 
Una clase es abstracta si tiene al menos un método abstracto

Método abstracto: 
Son aquellos que tienen solo la definición del método y deben tener el decorador @abstractmethod

Para poder crear una clase abstracta y un método abstracto importamos:

from abc import ABC, abstractmethod



"""
from abc import ABC, abstractmethod

class Pelota(ABC):#clase abstracta

    #definicion del metodo abstracto
    @abstractmethod
    def rebotar(self, altura: int):
        pass


## creando una subclase: una clase que nace a partir de otra clase
class PelotaDeJuguete(Pelota):
    def __init__(self):
        self.color = "Blanco"

    #obligacion de implementar el método abstracto
    def rebotar (self, altura: int):
        pass
    
    def imprimir (self):
        print("método de la subclase")

#creacion de objeto
pelotita = PelotaDeJuguete()
#TypeError: Can't instantiate abstract class PelotaDeJuguete without an implementation for abstract method 'rebotar'
print(pelotita.rebotar(20))

