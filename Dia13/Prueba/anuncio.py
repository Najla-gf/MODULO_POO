from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1  # Se establece el ancho, que sea al menos 1
        self.__alto = alto if alto > 0 else 1  # Se establece el alto, que sea al menos 1
        self.__url_archivo = url_archivo  # Se establece la URL del archivo del anuncio
        self.__url_clic = url_clic  # Se establece la URL de clic del anuncio
        self.__sub_tipo = sub_tipo  # Se establece el subtipo del anuncio

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1 

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo  # Se actualiza la URL del archivo del anuncio

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic  # Se actualiza la URL de clic del anuncio

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if sub_tipo not in self.get_subtipos():  # Se verifica si el subtipo es válido para esta instancia
            raise SubTipoInvalidoError("No es un subtipo permitido para esta instancia", sub_tipo)
        self.__sub_tipo = sub_tipo  # Se actualiza el subtipo

    @staticmethod
    @abstractmethod
    def get_subtipos():
        pass

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @staticmethod
    def mostrar_formatos():
        print("FORMATO VIDEO:")
        print("==========")
        for subtipo in Video.get_subtipos():  # Se muestra los subtipos asociados a los videos
            print(f"- {subtipo}")

        print("FORMATO DISPLAY:")
        print("==========")
        for subtipo in Display.get_subtipos():  # Se muestra los subtipos asociados a los anuncios display
            print(f"- {subtipo}")

        print("FORMATO SOCIAL:")
        print("==========")
        for subtipo in Social.get_subtipos():  # Se muestra los subtipos asociados a los anuncios sociales
            print(f"- {subtipo}")

class Video(Anuncio):
    FORMATO = "VIDEO"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(0, 0, url_archivo, url_clic, sub_tipo)
        self.__ancho = 1
        self.__alto = 1
        self.__duracion = duracion if duracion > 0 else 5  # Duración del video

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5  # Se actualiza la duración del video

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, value):
        self.__ancho = value

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, value):
        self.__alto = value

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
        
    @staticmethod
    def get_subtipos():
        return Video.SUB_TIPOS

class Display(Anuncio):
    FORMATO = "DISPLAY"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
        
    @staticmethod
    def get_subtipos():
        return Display.SUB_TIPOS

class Social(Anuncio):
    FORMATO = "SOCIAL"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
        
    @staticmethod
    def get_subtipos():
        return Social.SUB_TIPOS

#Anuncio.mostrar_formatos()
if __name__ == "__main__":
    pelicula = Video("","","",0)
    pelicula.ancho = 100
    print(pelicula.ancho)
