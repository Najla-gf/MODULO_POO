"""
Grupo 2:
Najla Gatica
Livio Gutierrez
Pablo Hernández
Manuel Ruiz

"""



from personaje import Personaje
import random

class Juego:
    def __init__(self, jugador: Personaje, orco: Personaje):
        self.jugador = jugador
        self.orco = orco

    def jugar(self):
        vidas = 4
        while vidas > 0:
            # Calcular la probabilidad de ganar del jugador contra el orco
            probabilidad_ganar = int(self.jugador.nivel * 50)
            print("")
            print("¡Ha aparecido un Orco!")
            print(f"Con el nivel actual, tienes una {probabilidad_ganar}% de probabilidad de ganarle al Orco.")

            # Enfrentamiento con el orco y elección del jugador
            opcion = None
            while opcion not in ["1", "2"]:
                opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")

                if opcion == "1":
                    if random.random() < probabilidad_ganar / 100:
                        print("¡Le has ganado al orco, felicidades!")
                        self.jugador.aumentar_exp(50)
                        print("¡Recibirás 50 puntos de experiencia!")
                    else:
                        print("¡Oh no!, has sido derrotado por el orco.")
                        self.jugador.disminuir_exp(30)
                        vidas -=1
                        print(f"Perdiste 30 puntos de experiencia. Perdiste una vida. Vidas: {vidas}") 
                elif opcion == "2":
                    print("Has huido de la batalla.")
                else:
                    print("Opción inválida.")
                
                #Estado de los jugadores
                print(self.jugador)
                print(self.orco)



if __name__ == "__main__":
    
    print("¡Bienvenido a Gran Fantasia!")
    nombre_personaje = input("Por favor, indica el nombre de tu personaje: > ")
    
    jugador = Personaje(nombre_personaje,1)
    print(jugador)

    orco = Personaje("Orco",1)
    print(orco)
    
    juego = Juego(jugador,orco)
    juego.jugar()
