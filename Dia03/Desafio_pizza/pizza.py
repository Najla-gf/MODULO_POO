
from ingredientes import ingredientes_prot, ingredientes_veg, tipos_masa

class Pizza():
    # atributos de clase
    ingredientes_prot = ["pollo", "vacuno", "carne vegetal"]  # Lista de ingredientes proteicos posibles
    ingredientes_veg = ["tomate", "aceitunas", "champinones"]  # Lista de ingredientes vegetales posibles
    tipos_masa = ["tradicional", "delgada"]  # Lista de tipos de masa posibles
    precio_fijo = 10000  #Precio fijo de 10mil
    tamano = "Familiar"

# Método estático para validar un elemento en una lista de casos posibles
    @staticmethod
    def validar_elemento(elemento, lista_posibles):
        return elemento in lista_posibles

    # Realizar un pedido
    def realizar_pedido(self):
        # Solicitar al usuario los ingredientes proteico, vegetales y el tipo de masa
        self.ingrediente_prot = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ").lower()
        self.ingrediente_veg1 = input("Ingrese el primer ingrediente vegetal (tomate, aceitunas, champinones): ").lower()
        self.ingrediente_veg2 = input("Ingrese el segundo ingrediente vegetal (tomate, aceitunas, champinones): ").lower()
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional, delgada): ").lower()

        # Validar los ingredientes y el tipo de masa
        if (self.validar_elemento(self.ingrediente_prot, self.ingredientes_prot) and
            self.validar_elemento(self.ingrediente_veg1, self.ingredientes_veg) and
            self.validar_elemento(self.ingrediente_veg2, self.ingredientes_veg) and
            self.validar_elemento(self.tipo_masa, self.tipos_masa)):
            self.es_valida = True
            print("")
            print("¡¡¡Pedido realizado con éxito!!!")
            print("")
            # Mostrar el pedido realizado
            print(f"Ingrediente proteico: {self.ingrediente_prot}")
            print(f"Primer ingrediente vegetal: {self.ingrediente_veg1}")
            print(f"Segundo ingrediente vegetal: {self.ingrediente_veg2}")
            print(f"Tipo de masa: {self.tipo_masa}")
            print(f"Precio: {self.precio_fijo}")
            print(f"Tamaño: {self.tamano}")
        else:
            self.es_valida = False
            print("Error: Ingredientes o tipo de masa no válidos.")

