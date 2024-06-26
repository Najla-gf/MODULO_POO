from anuncio import Video, Display, Social
from datetime import date
from error import LargoExcedidoError

class Campana:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios_info: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.__crear_anuncio(info) for info in anuncios_info] # Crea los anuncios a partir de la información proporcionada

    def __crear_anuncio(self, info: dict):
        # Método privado para crear un anuncio a partir de la información proporcionada
        tipo_anuncio = info.get("tipo", "") # Obtiene el tipo de anuncio del diccionario de información
        # Crea las instancias de video, display y social
        if tipo_anuncio == "Video":
            return Video(info.get("url_archivo", ""), info.get("url_clic", ""), info.get("sub_tipo", ""), info.get("duracion", 0))
        elif tipo_anuncio == "Display":
            return Display(info.get("url_archivo", ""), info.get("url_clic", ""), info.get("sub_tipo", ""))
        elif tipo_anuncio == "Social":
            return Social(info.get("url_archivo", ""), info.get("url_clic", ""), info.get("sub_tipo", ""))

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre de la campania excede los 250 caracteres")
        self.__nombre = nombre

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        # Método especial para representar la información de la campaña como cadena de texto
        conteo_anuncios = {'Video': 0, 'Display': 0, 'Social': 0}
        for anuncio in self.anuncios:
            tipo = anuncio.__class__.__name__ # Obtiene el nombre de la clase del anuncio
            conteo_anuncios[tipo] += 1 # Incrementa el contador para el tipo de anuncio
        # Retorna una cadena de texto con el nombre de la campaña y la cantidad de anuncios por tipo
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {conteo_anuncios['Video']} Video, {conteo_anuncios['Display']} Display, {conteo_anuncios['Social']} Social"

