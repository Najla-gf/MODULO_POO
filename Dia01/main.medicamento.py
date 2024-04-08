from medicamento import Medicamento

#instancia de la clase o creación de un objeto
paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento) #0.05
print(aspirina.descuento) #0.05

paracetamol.descuento = "0.06" #Le asigno un nuevo valor
print(paracetamol.descuento) #0.06
print(aspirina.descuento) #0.05