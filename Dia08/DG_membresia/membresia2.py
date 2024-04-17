from abc import ABC, abstractmethod

class TodasLasMembresias:
    def crear_membresia(self, tipo_membresia, correo_electronico, numero_tarjeta):
        # Crear membresía según el tipo especificado
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
        self.__correo_electronico = correo_electronico
        self.__numero_tarjeta = numero_tarjeta

    @abstractmethod
    def cancelar_suscripcion(self):
        pass

    @abstractmethod
    def cambiar_membresia(self, tipo_membresia):
        pass

    @property
    def correo_electronico(self):
        return self.__correo_electronico

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

class MembresiaGratis(Membresia):
    costo = 0
    dispositivos_maximos = 1

    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        todas_las_membresias = TodasLasMembresias()
        return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)

class MembresiaBasica(Membresia):
    costo = 3000
    dispositivos_maximos = 2

    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        todas_las_membresias = TodasLasMembresias()
        return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)

class MembresiaFamiliar(Membresia):
    costo = 5000
    dispositivos_maximos = 5

    def __init__(self, correo_electronico, numero_tarjeta):
        super().__init__(correo_electronico, numero_tarjeta)
        self.__dias_regalo = 7 if isinstance(self, MembresiaFamiliar) else 0
        self.__control_parental = False

    @property
    def dias_regalo(self):
        return self.__dias_regalo

    @property
    def control_parental(self):
        return self.__control_parental

    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        todas_las_membresias = TodasLasMembresias()
        return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)

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
    def dias_regalo(self):
        return self.__dias_regalo

    @property
    def contenido_sin_conexion(self):
        return self.__contenido_sin_conexion

    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        todas_las_membresias = TodasLasMembresias()
        return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)

    def incrementar_contenido_sin_conexion(self, cantidad):
        self.__contenido_sin_conexion += cantidad


class MembresiaPro(Membresia):
    costo = 7000
    dispositivos_maximos = 6

    def __init__(self, correo_electronico, numero_tarjeta):
        super().__init__(correo_electronico, numero_tarjeta)
        self.__dias_regalo = 15 if isinstance(self, MembresiaPro) else 0
        self.__control_parental = False

    @property
    def dias_regalo(self):
        return self.__dias_regalo

    @property
    def control_parental(self):
        return self.__control_parental

    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)

    def cambiar_membresia(self, tipo_membresia):
        todas_las_membresias = TodasLasMembresias()
        return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)

#################
#EJEMPLO DE USO

# Crear una membresía básica
membresia_actual = MembresiaBasica("correo@example.com", "1234567890")
print("Membresía actual: Básica")

# Cambiar a una membresía familiar
membresia_actual = membresia_actual.cambiar_membresia(2)
print("Cambiando a: Familiar")
print("Membresía actual: Familiar")

# Verificar días de regalo y control parental (solo disponible para membresía familiar)
if isinstance(membresia_actual, MembresiaFamiliar):
    print("Días de regalo:", membresia_actual.dias_regalo)
    print("Control parental:", membresia_actual.control_parental)

# Cambiar a una membresía sin conexión
membresia_actual = membresia_actual.cambiar_membresia(3)
print("Cambiando a: Sin Conexión")
print("Membresía actual: Sin Conexión")

# Incrementar el contenido sin conexión (solo disponible para membresía sin conexión)
if isinstance(membresia_actual, MembresiaSinConexion):
    membresia_actual.incrementar_contenido_sin_conexion(10)
    print("Contenido sin conexión:", membresia_actual.contenido_sin_conexion)

# Cambiar a una membresía pro
membresia_actual = membresia_actual.cambiar_membresia(4)
print("Cambiando a: Pro")
print("Membresía actual: Pro")

# Verificar días de regalo y control parental (solo disponible para membresía pro)
if isinstance(membresia_actual, MembresiaPro):
    print("Días de regalo:", membresia_actual.dias_regalo)
    print("Control parental:", membresia_actual.control_parental)

# Cancelar la suscripción
membresia_actual = membresia_actual.cancelar_suscripcion()
print("Cancelando suscripción")
print("Membresía actual: Gratis")

# Verificar los atributos de la membresía actual
print("Correo electrónico:", membresia_actual.correo_electronico)
print("Número de tarjeta:", membresia_actual.numero_tarjeta)
