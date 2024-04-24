"""Paso 5
En un archivo demo.py, importar las clases HoraError, LargoTextoError y Reunion.
Importar también el módulo re, y definir las variables titulo y hora asignando None.
Definir también una variable time_re con el valor indicado."""

from error import HoraError, LargoTextoError
from reunion import Reunion
import re

titulo = None
hora = None
time_re = "^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"

"""Paso 6
Iniciar un ciclo while infinito y dentro de este crear un bloque try/except. La cláusula
except debe manejar todas las excepciones de tipo Exception. En ella, mostrar la
instancia de la excepción y agregar la instrucción continue. Agregar también una
cláusula else, y en ella agregar la instrucción break."""

while True:
    try:
        """Paso 7
        Luego, dentro de la cláusula try, solicitar el título, en caso de que este no tenga valor
        o su largo supere 150. Luego de ser ingresado, en caso de que su largo sea superior
        a 150, lanzar una excepción de tipo LargoTextoError."""
        if titulo is None or len(titulo) > 150:
            titulo = input("\nIngrese título de la reunión" " (Máximo 150 caracteres):\n")
            if len(titulo) > 150:
                raise LargoTextoError("Título de la reunión excede máximo de caracteres", titulo, 150)
        
        """Paso 8
        A continuación, también dentro de la cláusula try, solicitar la hora, en caso de que no
        tenga valor o no tenga el formato permitido. Luego de ser ingresada, en caso de que
        no tenga el formato solicitado, lanzar una excepción de tipo HoraError.
        """
        if hora is None or re.search(time_re, hora) is None:
            hora = input("\nIngrese hora de la reunión" " (Formato: HH:MM:SS):\n")
            if re.search(time_re, hora) is None:
                raise HoraError("Formato de Hora debe ser HH:MM:SS.")

    except Exception as e:
        print(f"\n{e}\n")
        continue
    else:
        break

"""Paso 9
A continuación del ciclo while, crear una instancia de Reunion con el título y la hora
ingresados."""

r = Reunion(titulo, hora)
print("\nReunión creada correctamente.")