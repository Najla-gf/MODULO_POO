from medicamento import Medicamento

#Paso 1: crear instancia
medicamento_nuevo = Medicamento()

#paso 2: solicitud de ingreso de datos
precio = int(input("Ingrese el precio de medicamento >"))

#paso 3: pasar al método de instancia el valor capturado
medicamento_nuevo.asigna_precio(precio)

print(f"El precio es: {medicamento_nuevo.precio}")
print(f"El descuento es: {medicamento_nuevo.descuento}")