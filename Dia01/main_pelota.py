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

pelota_de_andy.material = "Plastico"
print(pelota_de_andy.material) #Plastico
