
#Constructor clase personaje
class Personaje:
    def __init__(self, nombre, nivel=1, experiencia=0):
        self.__nombre = nombre
        self.__experiencia = experiencia
        self.__nivel = nivel
    
    #Definimos un método para retornar el estado del personaje como una cadena
    def __str__(self):
        return f"Nombre: {self.__nombre} Nivel: {self.__nivel} Experiencia: {self.__experiencia}"

    @property #Getter de la experiencia del personaje
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter #Se va acumulando exp y aumenta o disminuye segun las batallas
    def experiencia(self, value):
        self.__experiencia = value
    
    def aumentar_exp(self, cantidad):
        self.__experiencia += cantidad

    def disminuir_exp(self, cantidad):
        self.__experiencia -= cantidad

    @property #getter
    def nivel(self):
        return self.__nivel
    
    @nivel.setter #setter
    def nivel(self):
        if self.__experiencia >= 100:
            self.__nivel +=1
        elif self.__experiencia < 0:
            self.__nivel -=1
        



    def __lt__(self, otro_nivel):
        return self.nivel < otro_nivel

    def __gt__(self, otro_nivel):
        return self.nivel > otro_nivel

    def probabilidad_ganar(self, otro):
        if self < otro:
            return 0.33
        elif self > otro:
            return 0.66
        else:
            return 0.5

