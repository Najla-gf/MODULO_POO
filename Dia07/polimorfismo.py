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
    #POLIMORFISMO: cambio en el comportamiento del método segun como estaba escrito en el padre
    def cambia_color(self, color: str):
        self.color = color

class Hijo(Padre):
    deuda = 120
    
    def __init__(self, tamano: int, saldo=0):
        super().__init__(tamano) #llamado al constructor padre
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo

class Nieto(Hija):
    pañal = "XL"

#instancia de la clase hija (creando un objeto)
hijita = Hija(100)
hijita.cambia_color("")

print(f"El color de la clase hija es: {hijita.color}")
#El color de la clase hija es: 

regalon = Nieto(50)

#Llamado al método del padre a través de la hija
super(type(hijita),hijita).cambia_color("gris")
print(f"el color de la clase hija es {hijita.color}")
#el color de la clase hija es gris

#Instancia de la clase HIJO
hijito = Hijo(10,1200)
print(hijito.tamano, hijito.saldo, hijito.deuda) #10 1200 120