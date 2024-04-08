#INSTANCIAR o CREAR UN OBJETO

#import pelota
#pelota_de_andy = pelota.Pelota() #llamamos al archivo y a la función dentro de este

#Otra forma:
from pelota import Pelota
pelota_de_andy = Pelota()

print(pelota_de_andy) #<pelota.Pelota object at 0x0000020E15FE9F40>
print(type(pelota_de_andy)) #<class 'pelota.Pelota'>
print(pelota_de_andy.forma) #redondeada
print(pelota_de_andy.material)

#Modificamos el material de la pelota
pelota_de_andy.material = "Plastico"
print(pelota_de_andy.material) #Plastico

pelota_tenis = Pelota()
print(pelota_tenis.material) #No se imprime nada
pelota_tenis.material = "Caucho"
print(pelota_tenis.material) #Caucho
print(pelota_tenis.posiciones) #[3, 0, 2, 1, 0]
print("")

#Métodos estáticos: no necesitan la creación de un objeto
print(Pelota.crear_rebote) #<function Pelota.crear_rebote at 0x0000012E325ED3A0>  
print(Pelota.crear_rebote()) #[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

Pelota.imprimir_posiciones() #[3, 0, 2, 1, 0]

#Modificando el valor del atributo mediante la clase
Pelota.posiciones = [2,4,6]
print(Pelota.posiciones) #[2, 4, 6]

pelota_futbol = Pelota()
print(pelota_futbol.posiciones) #[2, 4, 6]
print("")

#Método no estático
pelota_futbol.rebotar()
print(pelota_futbol.posiciones) #[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

pelota_basket = Pelota()
print(pelota_basket.posiciones) #[2, 4, 6]
#Método no estático, permiten crear atributos (variables)
#de tipo "atributo de instancia"
pelota_basket.nuevo_atributo()
print(pelota_basket.color) #blanco
print(pelota_futbol.color) #AttributeError: 'Pelota' object has no attribute 'color' 

