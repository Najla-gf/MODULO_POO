"""
    Najla Gatica
    Lolett Llanquinao
    Jimena Traipe
"""

from pizza import Pizza

# Paso 5a: Mostrar los valores de los atributos de clase
print(Pizza.tamano, Pizza.tipos_masa)

# Paso 5b: Verificar si "salsa de tomate" está presente en la lista
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Paso 5c: Crear una instancia de la clase Pizza y llamar al método del requerimiento 3
pizza = Pizza()
pizza.realizar_pedido()
print("")

# Paso 5d: Mostrar en pantalla los ingredientes y el tipo de masa
print(pizza.ingrediente_prot, pizza.ingrediente_veg1, pizza.ingrediente_veg2, pizza.tipo_masa)

# Paso 5e: Mostrar si la clase Pizza es una pizza válida o no
print(pizza, pizza.es_valida) #<pizza.Pizza object at 0x000002239B1EA030> True

