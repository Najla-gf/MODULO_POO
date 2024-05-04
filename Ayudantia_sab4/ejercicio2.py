class Persona():
    nombre = False
    
    def __init__(self):
        print("Hemos creado el objeto Persona")
    
    def datos(self):
        self.nombre = True

#creamos el objeto para poder usar la función
persona = Persona()
print(persona.nombre) #False pq llamados al atributo

persona.datos()
print(persona.nombre) #True pq llamamos a la función
########################################################

class Persona2():
    nombre = ""
    apellido = ""
    
    def __init__(self, nombrePersona, apellidoPersona):
        self.nombre = nombrePersona
        self.apellido = apellidoPersona
        print(f"Hemos creado nuestro objeto persona y se llama {self.nombre} {self.apellido}")
        
        
persona = Persona2("Najla", "Gatica")

        
        
        