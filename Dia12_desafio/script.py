from usuario import Usuario
from datetime import datetime
import json

#Fecha y hora actual
now = datetime.now()
print(now)

#Abrimos el archivo
with open("Dia12_desafio/usuarios.txt", 'r') as archivo:
    #Creamos la lista de usuarios
    lista_usuarios = []
    
    #Iteramos cada linea y obtenemos el numero de linea
    for num_linea, linea in enumerate(archivo, start=1):
        
        try:
            #Se carga la info del usuario desde la línea
            datos_usuarios = json.loads(linea)
            
            #Se crea la instancia de Usuario
            usuario = Usuario(datos_usuarios['nombre'],
                            datos_usuarios['apellido'],
                            datos_usuarios['email'],
                            datos_usuarios['genero'])
            lista_usuarios.append(datos_usuarios) #se agregan los datos a la lista

        except Exception as e:
            print(f"ERROR:", e) #Si hay un error, se imprime
                
            #El error se guarda en el registro de errores
            with open("Dia12_desafio/error.log", 'a+') as log: 
                #El error se guarda con fecha, hora, num de linea y el error
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR en la linea {num_linea}: {e}\n")


