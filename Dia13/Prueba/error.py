class Error(Exception):
    """Clase base para excepciones personalizadas."""
    pass

class SubTipoInvalidoError(Error):
    """Excepción lanzada cuando se proporciona un subtipo no válido."""
    def __init__(self, mensaje, subtipo):
        self.mensaje = mensaje
        self.subtipo = subtipo

class LargoExcedidoError(Error):
    """Excepción lanzada cuando se excede el límite de caracteres."""
    def __init__(self, mensaje):
        self.mensaje = mensaje

