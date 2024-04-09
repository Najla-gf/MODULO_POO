from te import Te 

#Crear dos instancias de la clase Te
te_1 = Te()
te_2 = Te()

#Mostrar el valor de cada tipo de dato almacenado
print("Tipo de te 1:", type(te_1))
print("Tipo de te 2:", type(te_2))

#Verificar si ambos tipos almacenados son iguales 
if type(te_1) == type(te_2):
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
