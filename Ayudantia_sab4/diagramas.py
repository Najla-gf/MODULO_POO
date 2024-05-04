class Animales():
    def __init__(self, descripcion, especie, hablar):
        #atributos de clase
        self.descripcion = descripcion
        self.especie = especie
        self.hablar = hablar
    
    #Métodos de la clase
    def tipoAnimal(self):
        print("Hola yo soy:", self.descripcion)
    
    def habla(self):
        print("Yo hago", self.hablar)
    
    def describir(self):
        print("Soy de la especie", self.especie)
    

#La clase perro hereda los atributos de la clase animales
class Perro(Animales):
    pass

class Abeja(Animales):
    def sonido(self, sonido):
        self.sonido = sonido
        print(self.sonido)

perro = Perro("Perro", "canino", "guau")
perro.tipoAnimal()
perro.habla()
perro.describir()

print("")
abeja = Abeja("Abeja", "Insecto", "bzzz")
abeja.tipoAnimal()
abeja.habla()
abeja.describir()
abeja.sonido("Bzzz")

#Los atributos de clase son privados porque se acceden mediante la clase o subclase
#en este caso animales.descipcion o perro.descripcion





