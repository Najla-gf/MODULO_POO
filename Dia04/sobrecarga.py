class Auto():
    def __init__(self, color:str = "blanco"):
        self.__color = color

    def __str__(self): #str convierte un objeto en una cadena de caracteres
        return f"Metodo sobrecargado, color: {self.__color}"
    
nissan = Auto()
print(nissan) #<__main__.Auto object at 0x000002AAE6CE9DC0>
#Metodo sobrecargado blanco

toyota = Auto("Negro")
print(toyota) #Metodo sobrecargado, color: Negro










