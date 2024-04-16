class Padre():
    #atributo de clase
    color = "verde"
    #constructor
    def __init__(self, tamano: int):
        #atributos de instancia
        self.__tamano = tamano #atributo oculto/privado
        
    #métodos estáticos
    
    
    #método de instancia
    def cambia_color(self, color: str):
        if color != "":
            self.color = color
    
    #sobrecarga del método base (estamos reescribiendo)
    def __str__(self):
        return f"El color es: {self.color}, y de tamaño {self.__tamano}"
    
    #getter y stetter
    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self, tamano: int):
        if tamano > 0:
            self.__tamano = tamano
        else:
            self.__tamano = 0

#HERENCIA ---> Hereda TODO y cada uno de los hijos puede tener sus propios metodos y atributoss
class Hija(Padre):
    peso = 100

class Hijo(Padre):
    deuda = 120

class Nieto(Hija):
    pañal = "XL"

#instancia de la clase hija (creando un objeto)
hijita = Hija(100)
print(f"El color de la clase hija es: {hijita.color}")
#El color de la clase hija es: verde

regalon = Nieto(50)

