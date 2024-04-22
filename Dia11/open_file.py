"""
funcion OPEN
file = open(ruta, argumento o modo de apertura)

"""

import os
try:
    log_file = open(os.path.abspath("Dia11/logs/error.log"))
    print(log_file) 
    #FileNotFoundError: [Errno 2] No such file or directory: 'C:\\0044-1\\MODULO_POO\\logs\\error.log'
    print(type(log_file))
    #<_io.TextIOWrapper name='C:\\0044-1\\MODULO_POO\\Dia11\\logs\\error.log' mode='r' encoding='cp1252'>
    
except FileNotFoundError as fnfe:
    print("Archivo no encontrado")
    #Archivo no encontrado
    print(fnfe)
    #<class '_io.TextIOWrapper'>

#ARGUMENTO
print("---------------READ---------------\n")
log_file2 = open(os.path.abspath("Dia11/html/index.html"), "r")
print(log_file2.read()) #lee TODO el documento
log_file2.close()
print("---------------READ LINE-------------\n")
log_file3 = open(os.path.abspath("Dia11/html/index.html"), "r")
print(log_file3.readline()) #Lee solo la primera linea: <!DOCTYPE html>
log_file3.close()
print("---------------READ LINES-------------\n")
log_file4 = open(os.path.abspath("Dia11/html/index.html"), "r")
print(log_file4.readlines()) #Retorna una lista con cada una de las lineas del doc
log_file4.close()
print("--------------WITH--------------\n")
with open(os.path.abspath("Dia11/html/index.html"), "r") as archivo:
    """print(archivo)""" #tipo de archivo: <_io.TextIOWrapper name='C:\\0044-1\\MODULO_POO\\Dia11\\html\\index.html' mode='r' encoding='cp1252'>
    for linea in archivo:
        #print(linea): Entrega todo el documento con un espacio entre cada linea
        print(linea.strip()) 
        #entrega el documento sin espaciados adicionales


#ARGUMENTO w, SOLO LECTURA
#La ruta donde se creará el archivo DEBE existir! pq el w NO crea la ruta
log_file5 = open(os.path.abspath("Dia11/html/assets/css/style.css"), "w")
log_file5.write("/*Esto es un comentario*/\n")
log_file5.write("*{\n\tmargin: 0px\n}")
#El w siempre agrega la información hacia el lado, así q se recomiendo agregar un \n
log_file5.close()

import time
try:
    print(time.time()) #Muestra la hora en segundos y milisegundos
    #1713802950.5118089
    print(round(time.time())) #Aproxima los decimales
    #1713802951
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open(f"dia11/logs/{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")
        
#Para hacer uso del r+, el archivo debe existir antes pq no lo crea
#with open(f"dia11/logs/{round(time.time())}.log", "r+") as log:
