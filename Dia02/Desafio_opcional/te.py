class Te():
    """
    Clase que representa un tipo de té.

    Atributos:
    precio_300gr (int): Precio del té por 300 gramos.
    precio_500gr (int): Precio del té por 500 gramos.

    Métodos estáticos:
    obtener_tiempo_recomendacion(sabor): Devuelve el tiempo de preparación y recomendación según el sabor del té.
    obtener_precio_segun_formato(formato): Devuelve el precio del té según el formato de envasado (300 gramos o 500 gramos).
    """

    #Atributos de la clase
    precio_300gr = 3000
    precio_500gr = 5000
    
    #Método estático para obtener tiempo de prep y recomendacion segun sabor
    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        if sabor == 1:
            return 3, "al desayuno"
        elif sabor == 2:
            return 5, "al medio dia"
        elif sabor == 3: 
            return 6, "en la tarde"
        
    #Método estático para obtener precio segun el formato
    @staticmethod
    def obtener_precio_segun_formato(formato):
        if formato == 300:
            return Te.precio_300gr
        elif formato == 500:
            return Te.precio_500gr
