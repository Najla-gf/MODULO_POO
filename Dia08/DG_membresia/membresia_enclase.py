"""
Grupo 2:
Edinson Ahumada
Yanina Belmar
Najla Gatica
Livio Gutierrez
Manuel Ruiz
Pablo Hernández

"""

from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor #__ metodo privado, no se pueden sobreescribir
        self.__numero_tarjeta = numero_tarjeta #_ metodo oculto, se puede sobreescribir

    @property
    def correo_suscriptor(self): #Getter para el correo de la membresía
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self): #Getter para la tarjeta asociada a la membresía
        return self.__numero_tarjeta    

    @abstractmethod
    def cambiar_suscripcion(self, tipo_membresia):
        pass

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def _crear_nueva_membresia(self, tipo_membresia):
        if tipo_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)


class Gratis(Membresia):
    costo = 0
    dispositivos_maximos = 1
    
    def cambiar_suscripcion(self, tipo_membresia):
        return self._crear_nueva_membresia(tipo_membresia)

class Basica(Membresia):
    costo = 3000
    dispositivos_maximos = 2
    
    def cambiar_suscripcion(self, tipo_membresia):
        if tipo_membresia >= 2 and tipo_membresia <= 4:
            return self._crear_nueva_membresia(tipo_membresia)
        return self #si no selecciona ninguna, se mantiene en básica

class Familiar(Basica):
    costo = 5000
    dispositivos_maximos = 5
    dias_regalo = 7

    def cambiar_suscripcion(self, tipo_membresia):
        if tipo_membresia in [1,3,4]:
            return self._crear_nueva_membresia(tipo_membresia)
        return self 

    def control_parental(self):
        pass


class SinConexion(Basica):
    costo = 3500
    dispositivos_maximos = 2
    dias_regalo = 7
    
    def cambiar_suscripcion(self, tipo_membresia):
        if tipo_membresia in [1,2,4]:
            return self._crear_nueva_membresia(tipo_membresia)
        return self 

    def incrementar_contenido(self):
        pass


class Pro(Familiar, SinConexion):
    costo = 7000
    dispositivos_maximos = 6
    dias_regalo = 15

    def cambiar_suscripcion(self, tipo_nueva_membresia: int):
        nueva_membresia = self._crear_nueva_membresia(tipo_nueva_membresia)
        if isinstance(nueva_membresia, Pro):
            if isinstance(self, SinConexion):
                nueva_membresia.dias_regalo += 5  # Agregamos 5 días extra por el cambio de membresia
        return nueva_membresia
    
    def control_parental(self):
        pass
    
    def incrementar_contenido(self):
        pass



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


membresia = Gratis("correo@example.com", "1234567890123456")
nueva_membresia = membresia.cambiar_suscripcion(4)  # Cambiar a Pro
print(nueva_membresia.costo, nueva_membresia.dispositivos_maximos, nueva_membresia.dias_regalo) #7000 6 15