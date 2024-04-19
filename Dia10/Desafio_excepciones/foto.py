""" 
Integrantes:
-Najla Gtica
-Yanina Belmar
-Edinson Ahumada
-Pablo Hernández
-Manuel Ruiz
-Livio Gutierrez
"""

from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho > self.MAX or ancho < 1:
            raise DimensionError("Ancho invalido", ancho ,self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto > self.MAX or alto < 1:
            raise DimensionError("Alto invalido", alto ,self.MAX)
        self.__alto = alto

if __name__ == "__main__":
    try:#Error: Ancho invalido, La dimension ingresada es: 3000, el maximo permitido es: 2500
        foto = Foto(ancho=500, alto=500, ruta="foto.jpeg")
        print(f"Foto con dimensiones {foto.ancho} x {foto.alto}")
        foto.ancho = 3000
        foto.alto = 0
    except DimensionError as e:
        print(f"Error: {e}")
    
    try:#Error: Alto invalido, La dimension ingresada es: -5, el maximo permitido es: 2500
        foto = Foto(ancho=500, alto=500, ruta="foto.jpeg")
        print(f"Foto con dimensiones {foto.ancho} x {foto.alto}")
        foto.ancho = 500
        foto.alto = -5
    except DimensionError as e:
        print(f"Error: {e}")
    
    try:#Error: ('Ancho invalido', 0, 2500)
        foto = Foto(ancho=500, alto=500, ruta="foto.jpeg")
        print(f"Foto con dimensiones {foto.ancho} x {foto.alto}")
        foto.ancho = 0
        foto.alto = 0
    except DimensionError as e:
        print(f"Error: {e}")
    
    try:#Error: Ancho invalido, La dimension ingresada es: -3000, el maximo permitido es: 2500
        foto = Foto(ancho=500, alto=500, ruta="foto.jpeg")
        print(f"Foto con dimensiones {foto.ancho} x {foto.alto}")
        foto.ancho = -3000
        foto.alto = 9000
    except DimensionError as e:
        print(f"Error: {e}")