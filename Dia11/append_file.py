from datetime import datetime

try:
    now = datetime.now()
    print(now) #muestra la fecha y hora: 2024-04-22 12:36:15.313646
    print(now.strftime('%Y-%m-%d %H:%M:%S')) #2024-04-22 12:38:45
    
    edad = int(input("Ingrese su edad:\n"))
    
except Exception as e:
    #El a es el append y el + permite leer y escribir en el archivo
    with open("Dia11/logs/error.log", "a+") as log:
        log.seek(0) #Seek recibe como argumento la posición en BYTES, si es 0 es el inicio del doc
        #Es la cantidad de CARACTERES(bytes), no la lista. Ej: log.seek(2) = g
        print(log.read())
        now = datetime.now() 
        #se crea la variable now para después concatenar los errores en un mismo lugar
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(3) #'fdgdg'
        print(log.read(4)) #24-0
        print("*************")
        log.seek(3) 
        print(log.read(40)) #24-04-22 12:33:28] ERROR: invalid litera
        print("*************")
        log.seek(5) 
        print(log.read(55)) #-04-22 12:33:28] ERROR: invalid literal for int() with








