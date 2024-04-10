from pizza_enclase import Pizza

#5a: Atributos de la clase importada
#print(Pizza.precio, Pizza.tamano) <<<---- Mediocre y feo XD
print(f"Las pizzas son de tamaño {Pizza.tamano} y su valor es de ${Pizza.precio}.-")

#5b: Validar si la salsa de tomate está en la lista
print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))
#True

#5c: Crear una instancia y llamar al metodo para ejecutar el script
pizza = Pizza()
pizza.tomar_pedido() #no se agrega nada más pq el self está implícito

#5d: ejecutar el script y ver si la pizza es valida
if pizza.es_pizza_valida:
    print(f"Ingrediente proteico: {pizza.proteico}")
    print(f"Ingrediente vegetal: {pizza.vegetales[0]} - {pizza.vegetal}")
    print(f"La masa seleccionada es: {pizza.masa}")
else:
    print("La pizza no es valida")

#5e: Ver si la clase pizza es una pizza valida o no sin crea instancia
print(Pizza.es_pizza_valida)
#AttributeError: type object 'Pizza' has no attribute 'es_pizza_valida'