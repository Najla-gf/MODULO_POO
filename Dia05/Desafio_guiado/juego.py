from personaje import Personaje
import random

class Juego:
    def __init__(self):
        pass

    def jugar(self):
        print("¡Bienvenido a Gran Fantasia!")
        nombre_personaje = input("Por favor, indica el nombre de tu personaje: > ")

        # Crear al jugador
        jugador = Personaje(nombre_personaje)
        print("\nEstado del jugador:")
        print(f"Nombre: {jugador.nombre}")
        print(f"Nivel: {jugador.nivel}")
        print(f"Experiencia: {jugador.experiencia}")

        # Crear un personaje orco
        orco = Personaje("Orco")
        print("\nEstado del Orco:")
        print(f"Nombre: {orco.nombre}")
        print(f"Nivel: {orco.nivel}")
        print(f"Experiencia: {orco.experiencia}")

        # Calcular la probabilidad de ganar del jugador contra el orco
        probabilidad_ganar = int(jugador._nivel * 50)
        print("")
        print(f"Con el nivel actual, {jugador.nombre} tiene un {probabilidad_ganar}% de probabilidad de ganarle al Orco.")

        # Enfrentamiento con el orco y elección del jugador
        opcion = None
        while opcion not in ["1", "2"]:
            opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")

            if opcion == "1":
                if random.random() < probabilidad_ganar / 100:
                    print("¡Le has ganado al orco, felicidades!")
                    jugador.aumentar_exp(50)
                    print("¡Recibirás 50 puntos de experiencia!")
                else:
                    print("¡Oh no!, has sido derrotado por el orco.")
                    jugador.disminuir_exp(30)
                    print("Perdiste 30 puntos de experiencia.")
            elif opcion == "2":
                print("Has huido de la batalla.")
            else:
                print("Opción inválida.")


if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
