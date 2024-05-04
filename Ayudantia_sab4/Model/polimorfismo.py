#POLIFORMISMO

class Animales():
    def __init__(self, nombre, mensaje):
        self.nombre = nombre
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)


class Perro(Animales):
    def hablar(self):
        #print("Yo hago guau")
        pass

class Pez(Animales):
    def hablar(self):
        #print("Yo no hablo")
        pass

perro = Perro("Firulais", "Guau guau guau!!")
perro.hablar()

lista_animales = [Perro("Cachupin", "AUUUUUU!!"), Pez("Nemo", "glup glup")]
for animal in lista_animales:
    animal.hablar()
#Se sobrescribe el método como lo habiamos definido antes 
#y no con los valores que le entregamos en la lista
    print(animal.nombre)
    print(animal.mensaje)
    print(f"Nombre: {animal.nombre}, Mensaje: {animal.mensaje}")
    #Con esto imprime el mensaje de la lista





