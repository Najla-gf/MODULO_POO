class Pelota():
    #atributos de Clase
    marca = "adidas" #<<<--- se puede volver a modificar más tarde, no es fijo.
    
    #Método Constructor (se recomienda definirlo bajo los atributos de clase)
    #NO debe tener retorno a menos que sea none
    """
    def __init__(self):
        print("Método constructor al crear el objeto")
        self.color = "blanco"
        self.tamano = 20
        self.material = "plastico"

    #instancia de clase    
pelota_futbol = Pelota()
print(pelota_futbol.color, pelota_futbol.tamano, pelota_futbol.material) #blanco 20 plastico """

#OTRA FORMA DE HACERLO
    def __init__(self,color: str, tamano= 20, material= "plastico"):
            print("Método constructor al crear el objeto")
            self.__color = color
            self.tamano = tamano
            self.material = material
            self.rebotes = 0 #Se puede asignar después
            self.marca = "Adidas"
            self.__password = "qwerty" #Atributo oculto
    #Metodo oculto
    def __getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color
    
    def setPassword(self,password):
        self.__password = password
    
    #Getter
    @property
    def color(self):
        return self.__color 
    
    #setter
    @color.setter
    def color(self,color: str):
        self.__color = color if color != "" else "Verde"
    
    #deleter
    @color.deleter
    def color(self):
        del self.__color

pelota_futbol = Pelota("Amarillo",16,"plastico")
#print(pelota_futbol.__color) #AttributeError: 'Pelota' object has no attribute '__color'
#print("getColor(): ",pelota_futbol.getColor()) #getColor():  Amarillo
print("Método getter: ", pelota_futbol.color) #Método getter:  Amarillo


print(pelota_futbol.color, pelota_futbol.tamano, pelota_futbol.material)
#Amarillo 16 plastico  

#pelota2 = Pelota() #TypeError: Pelota.__init__() missing 3 required positional arguments: 'color', 'tamano', and 'material'

pelota3 = Pelota("Rojo")
print(pelota3.color, pelota3.tamano, pelota3.material)
#Rojo 20 plastico

print(Pelota.marca, pelota_futbol.marca) #adidas Adidas