from datetime import datetime
from campana import Campana
from error import LargoExcedidoError, SubTipoInvalidoError


def manejar_excepciones():
    try:
        # Crear una instancia de Campana con un anuncio de tipo Video
        campana = Campana("Campaña de Ejemplo", datetime.now(), datetime.now(), [{"tipo": "Video", "url_archivo": "video.mp4", "url_clic": "enlace.com", "sub_tipo": "instream", "duracion": 10}])
        print(campana)

        # Solicitar un nuevo nombre para la campaña
        nuevo_nombre = input("Ingrese el nuevo nombre para la campaña: ") * 50  # Simula un nombre de campaña demasiado largo
        campana.nombre = nuevo_nombre

        # Solicitar un nuevo sub_tipo para el anuncio de Video
        nuevo_sub_tipo = input("Ingrese el nuevo subtipo para el anuncio de Video: ")
        if nuevo_sub_tipo not in ("instream", "outstream"):  # Verifica si el subtipo de anuncio es válido
            raise SubTipoInvalidoError("Subtipo de anuncio invalido", nuevo_sub_tipo)

    except (LargoExcedidoError, SubTipoInvalidoError) as error:
        now = datetime.now()
        with open("Dia13/Prueba/error.log", "a+") as archivo:
            archivo.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error}\n")


if __name__ == "__main__":  # Verifica si este es el archivo principal que se está ejecutando
    manejar_excepciones()