from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @abstractmethod
    def cancelar_suscripcion(self):
        pass

    @abstractmethod
    def cambiar_suscripcion(self, tipo_membresia):
        pass

class Gratis(Membresia):
    def cancelar_suscripcion(self):
        return Gratis(super().__correo_suscriptor, super().__numero_tarjeta)

    def cambiar_suscripcion(self, tipo_membresia):
        if tipo_membresia == 1:
            return Basica(super().__correo_suscriptor, super().__numero_tarjeta)
        elif tipo_membresia == 2:
            return Familiar(super().__correo_suscriptor, super().__numero_tarjeta)
        elif tipo_membresia == 3:
            return SinConexion(super().__correo_suscriptor, super().__numero_tarjeta)
        elif tipo_membresia == 4:
            return Pro(super().__correo_suscriptor, super().__numero_tarjeta)
        else:
            return Gratis(super().__correo_suscriptor, super().__numero_tarjeta)

class Basica(Membresia):
    def cancelar_suscripcion(self):
        return Gratis(super().__correo_suscriptor, super().__numero_tarjeta)

    def cambiar_suscripcion(self, tipo_membresia):
        if tipo_membresia >= 2 and tipo_membresia <= 4:
            if tipo_membresia == 2:
                return Familiar(super().__correo_suscriptor, super().__numero_tarjeta)
            elif tipo_membresia == 3:
                return SinConexion(super().__correo_suscriptor, super().__numero_tarjeta)
            elif tipo_membresia == 4:
                return Pro(super().__correo_suscriptor, super().__numero_tarjeta)
        else:
            return self

class Familiar(Basica):
    def cancelar_suscripcion(self):
        return Gratis(super().__correo_suscriptor, super().__numero_tarjeta)

    def cambiar_suscripcion(self, tipo_membresia):
        if tipo_membresia in [1, 3, 4]:
            return super().cambiar_suscripcion(tipo_membresia)
        else:
            return self

class SinConexion(Basica):
    costo = 3500

    def cancelar_suscripcion(self):
        return Gratis(super().__correo_suscriptor, super().__numero_tarjeta)

    def cambiar_suscripcion(self, tipo_membresia):
        if tipo_membresia in [1, 2, 4]:
            return super().cambiar_suscripcion(tipo_membresia)
        else:
            return self

class Pro(Familiar, SinConexion):
    def cancelar_suscripcion(self):
        return Gratis(super().__correo_suscriptor, super().__numero_tarjeta)

    def cambiar_suscripcion(self, tipo_membresia):
        if tipo_membresia in [1, 2, 3]:
            return super().cambiar_suscripcion(tipo_membresia)
        else:
            return self


g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))