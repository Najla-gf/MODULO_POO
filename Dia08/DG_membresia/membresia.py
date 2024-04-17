from abc import ABC, abstractmethod

class TodasLasMembresias:
    def crear_membresia(self, tipo_membresia, correo_electronico, numero_tarjeta):
        if tipo_membresia == 1:
            return MembresiaBasica(correo_electronico, numero_tarjeta)
        elif tipo_membresia == 2:
            return MembresiaFamiliar(correo_electronico, numero_tarjeta)
        elif tipo_membresia == 3:
            return MembresiaSinConexion(correo_electronico, numero_tarjeta)
        elif tipo_membresia == 4:
            return MembresiaPro(correo_electronico, numero_tarjeta)
        else:
            return MembresiaGratis(correo_electronico, numero_tarjeta)


class Membresia(ABC):
    def __init__(self, correo_electronico, numero_tarjeta):
        # Atributos de instancia privados
        self.__correo_electronico = correo_electronico
        self.__numero_tarjeta = numero_tarjeta

    @abstractmethod
    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    @abstractmethod
    def cambiar_membresia(self, tipo_membresia):
        pass

    @property
    def correo_electronico(self): #Getter para el correo de la membresía
        return self.__correo_electronico

    @property
    def numero_tarjeta(self): #Getter para la tarjeta asociada a la membresía
        return self.__numero_tarjeta

class MembresiaGratis(Membresia):
    costo = 0
    dispositivos_maximos = 1

    def cancelar_suscripcion(self): #Cancelar suscripción a la membresía gratuita
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        if tipo_membresia >= 1 and tipo_membresia <= 4: #Verificar si la membresia está dentro del rango válido (1 a 4)
            todas_las_membresias = TodasLasMembresias() #Si está, instanciar TodasLasMembresias
            #Retorna la nueva membresia
            return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
        else: #Si el rango no es válido, se mantiene la actual
            return self

class MembresiaBasica(Membresia):
    costo = 3000
    dispositivos_maximos = 2

    def cancelar_suscripcion(self): #Cancelar suscripción a la membresía básica
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        if tipo_membresia >= 2 and tipo_membresia <= 4:
            todas_las_membresias = TodasLasMembresias()
            return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
        else:
            return self

class MembresiaFamiliar(Membresia):
    costo = 5000
    dispositivos_maximos = 5

    def __init__(self, correo_electronico, numero_tarjeta):
        #Llama al constructor de la clase base (Membresia) para inicializar los atributos de instancia
        super().__init__(correo_electronico, numero_tarjeta)
        #Si la instancia es MembresiaFamiliar asignar 7 días de regalo, si no = 0
        self.__dias_regalo = 7 if isinstance(self, MembresiaFamiliar) else 0
        self.__control_parental = True

    @property
    def dias_regalo(self):#Getter para días de regalo
        return self.__dias_regalo

    @property
    def control_parental(self): #Getter para estado del control parental
        return self.__control_parental

    def cancelar_suscripcion(self):#Cancelar suscripción a la membresía familiar
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        if tipo_membresia in [1,3,4]:
            todas_las_membresias = TodasLasMembresias()
            return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
        else:
            return self

    def modificar_control_parental(self, activado):
        self.__control_parental = activado


class MembresiaSinConexion(Membresia):
    costo = 3500
    dispositivos_maximos = 2

    def __init__(self, correo_electronico, numero_tarjeta):
        super().__init__(correo_electronico, numero_tarjeta)
        self.__dias_regalo = 7 if isinstance(self, MembresiaSinConexion) else 0
        self.__contenido_sin_conexion = 0

    @property
    def dias_regalo(self):#Getter para días de regalo
        return self.__dias_regalo

    @property
    def contenido_sin_conexion(self): #Getter para contenido sin conexión
        return self.__contenido_sin_conexion

    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        if tipo_membresia in [1, 2, 4]:
            todas_las_membresias = TodasLasMembresias()
            return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
        else:
            return self

    def incrementar_contenido_sin_conexion(self, cantidad):
        self.__contenido_sin_conexion += cantidad


class MembresiaPro(Membresia):
    costo = 7000
    dispositivos_maximos = 6

    def __init__(self, correo_electronico, numero_tarjeta):
        super().__init__(correo_electronico, numero_tarjeta)
        self.__dias_regalo = 15 if isinstance(self, MembresiaPro) else 0
        self.__control_parental = True

    @property
    def dias_regalo(self):#Getter para días de regalo
        return self.__dias_regalo

    @property
    def control_parental(self):#Getter para estado del control parental
        return self.__control_parental

    def cancelar_suscripcion(self): #Cancelar suscripción a la membresía Pro
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        if 1 <= tipo_membresia <= 3:
            todas_las_membresias = TodasLasMembresias()
            return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
        else:
            return self

##########################################################################
################PRUEBA DE CODIGO##########################################
# Crear una membresía básica
membresia_inicial = MembresiaGratis("ejemplo@correo.com", "123456789")
print("Membresía actual:", membresia_inicial.__class__.__name__)  # Imprime el tipo de membresía inicial
print()

membresia_actual = MembresiaBasica("ejemplo@gmail.com", "123456789")
print("Membresía actual:", membresia_actual.__class__.__name__)  # Imprime el tipo de membresía actual
print("Correo electrónico:", membresia_actual.correo_electronico)
print("Número de tarjeta:", membresia_actual.numero_tarjeta)
print("Costo:", membresia_actual.costo)
print("Dispositivos máximos:", membresia_actual.dispositivos_maximos)
print()

# Cambiar a una membresía familiar
membresia_actual = membresia_actual.cambiar_membresia(2)
print("Membresía actual:", membresia_actual.__class__.__name__)  # Imprime el tipo de membresía actual
print("Correo electrónico:", membresia_actual.correo_electronico)
print("Número de tarjeta:", membresia_actual.numero_tarjeta)
print("Costo:", membresia_actual.costo)
print("Días de regalo:", membresia_actual.dias_regalo)
print("Dispositivos máximos:", membresia_actual.dispositivos_maximos)

# Modificar control parental en membresía familiar
membresia_actual.modificar_control_parental(True)
print("Control parental activado:", membresia_actual.control_parental)
print()

# Cambiar a una membresía sin conexión
membresia_actual = membresia_actual.cambiar_membresia(3)
print("Membresía actual:", membresia_actual.__class__.__name__)  # Imprime el tipo de membresía actual
print("Correo electrónico:", membresia_actual.correo_electronico)
print("Número de tarjeta:", membresia_actual.numero_tarjeta)
print("Costo:", membresia_actual.costo)
print("Días de regalo:", membresia_actual.dias_regalo)
print("Dispositivos máximos:", membresia_actual.dispositivos_maximos)
print("Contenido sin conexión:", membresia_actual.contenido_sin_conexion)

# Incrementar contenido sin conexión
membresia_actual.incrementar_contenido_sin_conexion(10)
print("Contenido sin conexión después de incrementar:", membresia_actual.contenido_sin_conexion)
print()

# Cambiar a una membresía pro
membresia_actual = membresia_actual.cambiar_membresia(4)
print("Membresía actual:", membresia_actual.__class__.__name__)  # Imprime el tipo de membresía actual
print("Correo electrónico:", membresia_actual.correo_electronico)
print("Número de tarjeta:", membresia_actual.numero_tarjeta)
print("Costo:", membresia_actual.costo)
print("Días de regalo:", membresia_actual.dias_regalo)
print("Dispositivos máximos:", membresia_actual.dispositivos_maximos)
print("Control parental activado:", membresia_actual.control_parental)

