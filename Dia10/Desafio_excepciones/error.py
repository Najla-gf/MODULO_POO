class  DimensionError(Exception):
    def __init__(self, mensaje, dimension, maximo):
        self.mensaje= mensaje
        self.dimension= dimension
        self.maximo= maximo
    
    def __str__(self):
        
        if self.dimension and self.maximo: 
            return f"{self.mensaje}, La dimension ingresada es: {self.dimension}, el maximo permitido es: {self.maximo}"
        return super().__str__()