#Ayudantía sobre POO
#Ejercicio de fábrica de celulares

class Fabrica():
    pass

print(type(Fabrica()))
#con type vemos el tipo al que pertenece el objeto

#Instanciar es crear el objeto y mandar a llamar
celular = Fabrica()
cargador = Fabrica()
audifonos = Fabrica()

print(type(celular))
############################################
def saludo(nombre):
        print("Hola, " + nombre)
    
saludo("Mundo")
#Aquí se imprime la función + el parámetro que le estoy entregando "mundo".
#Hola, Mundo
############################################

class Persona():
    #Atributos: caracteristicas
    nombre = "Najla"
    apellido = "Gatica"
    sexo = "Femenino"
    edad = "31"
    
    #Método: le orotgamos una acción
    def hablar(self,mensaje):
        return mensaje
    
#Vamos a crear el objeto
persona = Persona()
print(persona.hablar("Hola, yo soy"), "{} mi apellido es {}, tengo {} años y soy del sexo {}"
    .format(persona.nombre, persona.apellido, persona.edad, persona.sexo))
#Hola, yo soy Najla mi apellido es Gatica, tengo 31 años y soy del sexo Femenino

print(f"{persona.nombre} mi apellido es {persona.apellido}, tengo {persona.edad} y soy del género {persona.sexo}")


