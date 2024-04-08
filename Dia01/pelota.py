#Se recomienda trabajar la clase en un archivo separado
#La clase se define con mayúscula inicial
class Pelota():
    #atributo
    forma = "redondeada"
    material = ""
    posiciones = [3,0,2,1,0]
    
    #Método estático:
    @staticmethod
    def crear_rebote():
        return [5,0,4,0,3,0,2,0,1,0]
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote() #llamando a un metodo estatico
        print(Pelota.posiciones) #imprime el valor del atributo
    
    #Método no estático o de instancia, siempre va con self
    def rebotar(self):
        self.posiciones = self.crear_rebote()
    
    def nuevo_atributo(self):
        self.color = "blanco"





