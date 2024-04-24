# Define la clase base Monitor
class Monitor:
    def __init__(self, marca, pulgadas, resolucion):
        # Inicializa los atributos comunes a todos los monitores
        self.marca = marca
        self.pulgadas = pulgadas
        self.resolucion = resolucion

# Define la clase LED que hereda de Monitor
class LED(Monitor):
    def __init__(self, marca, pulgadas, resolucion, tipo_led):
        # Llama al constructor de la clase base Monitor
        super().__init__(marca, pulgadas, resolucion)
        # Inicializa el atributo específico de LED
        self.tipo_led = tipo_led

# Define la clase Televisor que hereda de Monitor
class Televisor(Monitor):
    def __init__(self, marca, pulgadas, resolucion):
        # Llama al constructor de la clase base Monitor
        super().__init__(marca, pulgadas, resolucion)
        # Inicializa el atributo de funciones como una lista vacía
        self.funciones = []

# Creamos una instancia de Televisor y añadimos una función
tv = Televisor("LG", 32, "1920x1080")
tv.funciones.append("Smart TV")

# Imprimimos la marca, pulgadas, resolución y funciones del televisor
print("Marca:", tv.marca)
print("Pulgadas:", tv.pulgadas)
print("Resolución:", tv.resolucion)
print("Funciones:", tv.funciones)
