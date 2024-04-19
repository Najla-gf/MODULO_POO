#Excepcion = error DURANTE la ejecución del programa, ej: division por 0
#se ejecuta la división pero el resultado es un error
#La diferencia entre un while condicionado y un try/except es que en while podemos controlar antes el ingreso del dato, 
#en try/except la verificacion se hace durante la operación

"""class MisExcepciones(Exception):
    
    def imprimir_promedio(self, dividendo, divisor):
        promedio = 100/0
        print(f"El promedio es: {promedio}") #ZeroDivisionError: division by zero

calculo_promedio = MisExcepciones()
calculo_promedio.imprimir_promedio(100,0)"""

class Error(Exception):
    pass

class DivisorError(Error):
    def __init__(self, mensaje, divisor):
        self.divisor = divisor
        self.mensaje = mensaje


class MisExcepciones(Exception):
    
    def imprimir_promedio(self, dividendo, divisor):
        try:
            promedio = dividendo/divisor
            print(f"El promedio es: {promedio}")
        except ZeroDivisionError:
            print("ERROR: El divisor no puede ser un cero")
        
        #captura genérica de una excepción
        except Exception as error:
            print("ERROR: Se ha producido un error:", error) #Se ha producido un error: division by zero
        finally:
            print("El método se ha ejecutado\n")

calculo_promedio = MisExcepciones()
valido = True

while valido:
    try:
        dividendo = int(input("Ingrese el numero dividendo > "))
        valido = False
        #divisor = int(input("Ingrese el numero divisor > "))
        #calculo_promedio.imprimir_promedio(dividendo, divisor)
    except ValueError:
        print("Error en el ingreso de datos")
valido = True

while valido:
    try:
        divisor = int(input("Ingrese el numero divisor > "))
        if divisor == 0:
            raise DivisorError("Divisor no puede ser cero",divisor)
        valido = False
    except DivisorError as de:
        print("Divisor no puede ser cero", de)
    
    except ValueError:
        print("Error en el ingreso del divisor")

calculo_promedio.imprimir_promedio(dividendo, divisor)    
print("Gracias por participar en clases")

