class Personaje:
    # Definimos el método constructor
    def __init__(self, nombre):
        # Inicializa los atributos del personaje
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    # Definimos un método para retornar el estado del personaje como una cadena
    def obtener_estado(self):
        # Retorna una cadena con el estado del personaje
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    # Definimos un método para asignar experiencia al personaje
    def asignar_experiencia(self, experiencia):
        # Actualiza la experiencia y nivel del personaje según la experiencia recibida
        suma_temporal = self.experiencia + experiencia
        while suma_temporal >= 100:
            self.nivel += 1
            suma_temporal -= 100
        if suma_temporal < 0:
            if self.nivel == 1:
                print("Juego perdido")
                suma_temporal = 0
                return
            else:
                self.nivel -= 1
                suma_temporal = 100 + suma_temporal
        self.experiencia = suma_temporal

    # Definimos un método de comparación para "menor que"
    def __lt__(self, other):
        # Método de comparación para "menor que"
        return self.nivel < other.nivel

    # Definimos un método de comparación para "mayor que"
    def __gt__(self, other):
        # Método de comparación para "mayor que"
        return self.nivel > other.nivel

    # Definimos un método para calcular la probabilidad de ganar contra otro personaje
    def probabilidad_ganar(self, other):
        # Calcula la probabilidad de ganar contra otro personaje
        return 0.33 if self < other else (0.66 if self > other else 0.5)

    # Definimos un método estático para mostrar un diálogo de enfrentamiento y retornar la opción elegida por el jugador
    @staticmethod
    def enfrentamiento_dialogo(probabilidad):
        # Muestra un diálogo de enfrentamiento y retorna la opción elegida por el jugador
        print(f"¡Oh no!, ¡Ha aparecido un Orco!\nCon tu nivel actual, tienes {probabilidad * 100}%  de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Huir")
        opcion = int(input())
        return opcion
