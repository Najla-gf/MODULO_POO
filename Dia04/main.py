from pelota import Pelota

nueva_pelota = Pelota("Negro")

#Si se llama al atributo password sin el property se muestra tal cual
# print(nueva_pelota.password) #qwerty

#Pero si usamos property lo protegemos y nos impide acceder a él
# print(nueva_pelota.__password) #AttributeError: 'Pelota' object has no attribute '__password'

#Mientras yo no cree el getter en pelota.py, el script NO mostrará el atributo.

#Método
nueva_pelota.setColor("Blanco")
print(nueva_pelota.color) #Blanco

#Setter
nueva_pelota.color = ""
print(nueva_pelota.color) #Naranjo

#Deleter
nueva_pelota.color
print("Borrando",nueva_pelota.color) #Borrando Verde