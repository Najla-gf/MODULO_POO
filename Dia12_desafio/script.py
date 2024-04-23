from usuario import Usuario
from datetime import datetime
import json

#Funciones para escribir errores en un archivo de registro
def escribir_error(err):
    now = datetime.now() #Fecha y hora actual
    with open("Dia12_desafio/error.log", 'a+') as log: #Se abre el archivo en modo append+
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {err}\n")
        print(err) #Se imprime el error en la consola
        log.close()

#Función para cargar usuarios de un archivo de texto
def cargar_usuarios(archivo):
    lista_usuarios = [] #lista que almacena los usuarios
    numero_linea = 1 #Variable para leer el num de linea
    with open(archivo, 'r') as file:
        for linea in file: #Se itera cada linea del archivo
            try:
                datos_usuario = json.loads(linea.strip()) #le quita espacios y saltos de linea que pueda tener
                #objeto de Usuario con los datos cargados
                usuario = Usuario(datos_usuario['nombre'], 
                                datos_usuario['apellido'], 
                                datos_usuario['email'], 
                                datos_usuario['genero'])
                lista_usuarios.append(usuario) #se agrega a la lista
            #Captura cualquier excepción que ocurra durante la ejecución
            except Exception as e:
                escribir_error(f"ERROR en la linea {numero_linea}: {e}")
            numero_linea += 1 #Se agrega una linea más
    return lista_usuarios #Devuelve la lista de usuarios cargados

#carga los usuarios del archivo
usuarios = cargar_usuarios('Dia12_desafio/usuarios.txt')
for usuario in usuarios: #Itera cada uno y entrega los datos solicitados
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


