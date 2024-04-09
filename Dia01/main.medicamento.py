from medicamento import Medicamento

#instancia de la clase o creación de un objeto
paracetamol = Medicamento()
aspirina = Medicamento()
"""
print(paracetamol.descuento) #0.05
print(aspirina.descuento) #0.05

#Modificacion del estado de un objeto
paracetamol.descuento = "0.06" #Le asigno un nuevo valor
print(paracetamol.descuento) #0.06
print(aspirina.descuento) #0.05"""

Medicamento.descuento = 0.04
ibuprofeno = Medicamento()
print(ibuprofeno.descuento)

precio = int(input("Ingrese el precio a validar > "))
#llamado a un método estático
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es válido")
else:
    print("El precio ingresado NO es válido")

if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento:
    print("Todas las instancias (objetos), tienen los mismos valores de IVA y descuento")
    print("El valor del IVA es", Medicamento.IVA)
    print("El valor del descuento es", Medicamento.descuento)

ibuprofeno.modificar_atributo()
print(ibuprofeno.IVA) #0.19

