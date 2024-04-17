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


class Membresia:
    def __init__(self, correo_electronico, numero_tarjeta):
        self.correo_electronico = correo_electronico
        self.numero_tarjeta = numero_tarjeta

    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_electronico, self.numero_tarjeta)


class MembresiaGratis(Membresia):
    costo = 0
    dispositivos_maximos = 1

    def cambiar_membresia(self, tipo_membresia):
            if 1 <= tipo_membresia <= 4:
                todas_las_membresias = TodasLasMembresias()
                return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
            else:
                return self


class MembresiaBasica(Membresia):
    costo = 3000
    dispositivos_maximos = 2

    def cambiar_membresia(self, tipo_membresia):
            if 2 <= tipo_membresia <= 4:
                todas_las_membresias = TodasLasMembresias()
                return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
            else:
                return self


class MembresiaFamiliar(Membresia, MembresiaBasica):
    costo = 5000
    dispositivos_maximos = 5

    def __init__(self, correo_electronico, numero_tarjeta):
        super().__init__(correo_electronico, numero_tarjeta)
        self.dias_regalo = 7
        self.control_parental = False

    def cambiar_membresia(self, tipo_membresia):
        if tipo_membresia in [1,3,4]:
            todas_las_membresias = TodasLasMembresias()
            return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
        else:
            return self

    def modificar_control_parental(self, activado):
            self.control_parental = activado


class MembresiaSinConexion(Membresia, MembresiaBasica):
    costo = 3500
    dispositivos_maximos = 2

    def __init__(self, correo_electronico, numero_tarjeta):
        super().__init__(correo_electronico, numero_tarjeta)
        self.dias_regalo = 7
        self.contenido_sin_conexion = 0
    
    def cambiar_membresia(self, tipo_membresia):
        if tipo_membresia in [1, 2, 4]:
            todas_las_membresias = TodasLasMembresias()
            return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
        else:
            return self
    
    def incrementar_contenido_sin_conexion(self, cantidad):
        self.contenido_sin_conexion += cantidad


class MembresiaPro(Membresia, MembresiaBasica):
    costo = 7000
    dispositivos_maximos = 6

    def __init__(self, correo_electronico, numero_tarjeta):
        super().__init__(correo_electronico, numero_tarjeta)
        self.dias_regalo = 15

    def cambiar_membresia(self, tipo_membresia):
        if 1 <= tipo_membresia <= 3:
            todas_las_membresias = TodasLasMembresias()
            return todas_las_membresias.crear_membresia(tipo_membresia, self.correo_electronico, self.numero_tarjeta)
        else:
            return self

    def modificar_control_parental(self, activado):
        self.control_parental = activado

    def incrementar_contenido_sin_conexion(self, cantidad):
        self.contenido_sin_conexion += cantidad


if __name__ == "__main__":
    correo_electronico = "usuario@correo.com"
    numero_tarjeta = "1234-5678-9012-3456"
    membresia_actual = MembresiaPro(correo_electronico, numero_tarjeta)
    nueva_membresia = membresia_actual.cambiar_membresia(3)  # Cambiar a membresía sin conexión
    print(type(nueva_membresia))