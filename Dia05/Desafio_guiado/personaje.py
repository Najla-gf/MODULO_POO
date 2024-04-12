#Constructor clase personaje
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self._nivel = 1
        self._experiencia = 0

    @property #getter del nivel del personaje
    def nivel(self):
        return self._nivel

    @property #Getter de la experiencia del personaje
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, value):
        self._experiencia = value
    
    def aumentar_exp(self, cantidad):
        self.experiencia += cantidad

    def disminuir_exp(self, cantidad):
        self.experiencia -= cantidad

""" def __lt__(self, otro_nivel):
        return self.nivel < otro_nivel

    def __gt__(self, otro_nivel):
        return self.nivel > otro_nivel

    def __eq__(self, otro_nivel):
        return self.nivel == otro_nivel

    def probabilidad_ganar(self, nivel_orco):
        if self < nivel_orco:
            return 0.33
        elif self > nivel_orco:
            return 0.66
        else:
            return 0.5
"""
