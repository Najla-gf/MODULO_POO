class Ram():
    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.byte = 32

class DiscoDuro():
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tipo = "SSD"

class Teclado():
    def __init__(self, idioma: str, cant_teclas: int):
        self.idioma = idioma
        self.cant_teclas = cant_teclas

class Mouse():
    def __init__(self, tipo: str, conectividad: str):
        self.tipo = tipo
        self.conectividad = conectividad

class Computador:
    def __init__(self, teclado: Teclado, mouse: Mouse):
        #componentes y perifericos
        #Composición es el proceso de hacer una instancia dentro de otra clase
        self.ram = Ram(1500)
        #atributo de instancia de tipo objeto dentro del computador
        self.disco_duro = DiscoDuro(1024)
        
        self.teclado = teclado #agregación
        self.mouse = mouse#agregación

#AGREGACION:
#Instancia de clase que se toma como atributo
teclado = Teclado("latino", 120)
mouse = Mouse("Gamer", "bluetooth")

computador_gamer = Computador(teclado,mouse)

print(computador_gamer.ram.velocidad) #1500
print(computador_gamer.teclado.cant_teclas) #120

