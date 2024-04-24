"""En un archivo error.py, definir clase Error, que deriva de Exception, sin
implementación. En el mismo archivo, definir a continuación la clase HoraError, que
deriva de Error, sin implementación."""
class Error(Exception):
    """Clase Base Excepciones"""
    pass
class HoraError(Error):
    pass

    """Paso 2
    En el mismo archivo, definir la clase LargoTextoError; Sobreescriba el constructor,
    admitiendo los parámetros mensaje, texto (opcional) y largo (opcional), los cuales
    debe asignar a atributos de instancia. En el caso del texto, acortar en caso de que
    supere los 50 caracteres."""
class LargoTextoError(Error):
    def __init__(self, mensaje: str, texto: str = None, largo: int = None) -> None:
        self.mensaje = mensaje
        self.texto = (f"{texto[:50]}..."if texto is not None
    and len(texto) > 50 else texto)
        self.largo = largo

    """Paso 3
    En el mismo archivo, sobrecargue el método __str__. En caso de que no se haya
    ingresado texto ni largo, retornar el método de la clase padre. En caso contrario,
    según los valores ingresados, construir mensaje de retorno."""
    def __str__(self) -> str:
        if self.texto is None and self.largo is None:
            return super().__str__()
        else:
            ret = f"{self.mensaje}."
        if self.texto != None:
            ret += f" Texto ingresado: {self.texto}."
        if self.largo != None:
            ret += f" Máximo {self.largo} caracteres permitidos."
        return ret