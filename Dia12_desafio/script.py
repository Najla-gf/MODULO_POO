from usuario import Usuario
from datetime import datetime
import json

def escribir_error(err):
    now = datetime.now()
    with open("Dia12_desafio/error.log", 'a+') as log: 
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {err}\n")
        print(err)
        log.close()

def cargar_usuarios(archivo):
    lista_usuarios = []
    numero_linea = 1
    with open(archivo, 'r') as file:
        for linea in file:
            try:
                datos_usuario = json.loads(linea.strip()) #le quita espacios y saltos de linea que pueda tener
                usuario = Usuario(datos_usuario['nombre'], 
                                datos_usuario['apellido'], 
                                datos_usuario['email'], 
                                datos_usuario['genero'])
                lista_usuarios.append(usuario)
            except Exception as e:
                escribir_error(f"ERROR en la linea {numero_linea}: {e}")
            numero_linea += 1 #se agrega una linea más
    return lista_usuarios

usuarios = cargar_usuarios('Dia12_desafio/usuarios.txt')
for usuario in usuarios:
    print(f'{usuario.nombre} {usuario.apellidos} - {usuario.email}')



"""#Fecha y hora actual
now = datetime.now()
print(now)

#Abrimos el archivo
with open("Dia12_desafio/usuarios.txt", 'r') as archivo:
    #Creamos la lista de usuarios
    lista_usuarios = []
    
    #Iteramos cada linea y obtenemos el numero de linea
    for numero_linea, linea in enumerate(archivo):
        
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
            #El error se guarda en el registro de errores
            with open("Dia12_desafio/error.log", 'a+') as log: 
                #El error se guarda con fecha, hora, num de linea y el error
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR en la linea {numero_linea}: {e}\n")
                print(f"ERROR:", e) #Si hay un error, se imprime"""


