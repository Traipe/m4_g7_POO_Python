import random #para generar números aleatorios
from personaje import Personaje#Importamos la clase Personaje del módulo personaje

# Definimos una clase llamada Juego
class Juego:
    # Definimos un método estático llamado jugar
    @staticmethod
    def jugar():
        print("Bienvenido a Gran Fantasia!")#mensaje de bienvenida
        # Pedimos al usuario el nombre de su personaje
        nombre_personaje = input("Por favor indique nombre de su personaje:\n")
        # Creamos un nuevo objeto Personaje con el nombre dado
        jugador = Personaje(nombre_personaje)
        print(jugador.obtener_estado())#estado actual del personaje del jugador
        
        # Creamos un nuevo objeto Personaje llamado "Orco"
        orco = Personaje("Orco")
        # Calculamos la probabilidad de que el jugador gane contra el orco
        probabilidad_ganar = jugador.probabilidad_ganar(orco)

        # Mostramos el diálogo de enfrentamiento y obtenemos la elección del jugador
        opcion = jugador.enfrentamiento_dialogo(probabilidad_ganar)

        # Continuamos el juego hasta que el jugador elija huir
        while opcion == 1:
            resultado_ataque = "Gana" if random.uniform(0, 1) <= probabilidad_ganar else "Pierde"
            if resultado_ataque == "Gana":
                print("Le has ganado al orco, felicidades!")
                print("¡Recibirás 50 puntos de experiencia!")
                jugador.asignar_experiencia(50)
                orco.asignar_experiencia(-30)
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                print("¡Has perdido 30 puntos de experiencia!")
                jugador.asignar_experiencia(-30)
                orco.asignar_experiencia(50)
            # Imprimimos el estado actual de ambos personajes    
            print(jugador.obtener_estado())
            # Recalculamos la probabilidad de ganar
            print(orco.obtener_estado())
            probabilidad_ganar = jugador.probabilidad_ganar(orco)
            # Mostramos el diálogo de enfrentamiento nuevamente y obtenemos la nueva elección del jugador
            opcion = jugador.enfrentamiento_dialogo(probabilidad_ganar)
        
        # Si el jugador elige huir, imprimimos un mensaje de despedida
        print("¡Has huido! El orco ha quedado atras.")

# Iniciamos del juego
Juego.jugar()
