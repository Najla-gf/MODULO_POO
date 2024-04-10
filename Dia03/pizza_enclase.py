from ingredientes_enclase import lista_proteicos, lista_vegetales, lista_masa

#Paso 1:
class Pizza: #No es necesario agregar paréntesis si es que está vacío
    precio = 10000 
    tamano = "Familiar"

    #Paso 2:
    @staticmethod
    def validar(elemento, posibles_valores):
        for valor in posibles_valores:
            if valor == elemento.lower(): #para que todo quede en minuscula en la validacion
                return True
        return False
    #return elemento in posibles_valores (otra forma más corta)
    
    #Paso 3:
    def tomar_pedido(self): #Aqui empezamos a hacer el pedido
        #Se agrega la variable directo para almacenar el ing
        self.proteico = input("Ingrese un ingrediente proteico Vacuno, Pollo o Carne Vegetal:\n")
        self.vegetales = [] #Lista vacía para agregar altiro los 2 vegetales
        self.vegetales.append(input("Ingrese el primer ingrediente vegetal Tomate, Aceituna o Champinones:\n"))
        self.vegetal = input("Ingrese el segundo ingrediente vegetal Tomate, Aceituna o Champinones:\n")
        self.masa = input("Ingrese tipo de masa Tradicional o Delgada:\n")
        
    #Paso 4:
        #regresa True o False segun lo que ingresó el usuario
        self.es_pizza_valida = self.validar(self.proteico,lista_proteicos) and \
            self.validar(self.vegetales[0], lista_vegetales) and\
            self.validar(self.vegetal, lista_vegetales) and\
            self.validar(self.masa, lista_masa)
        #self.es_pizza_valida = True and True and True and True <<-- Esto es lo que estamos haciendo
        
    #Paso 5:
        
        
        