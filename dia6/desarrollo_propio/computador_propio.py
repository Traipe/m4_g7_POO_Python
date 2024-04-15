class Computador:
    def __init__(self, ram, disco_duro, monitor, mouse, teclado):
        # Inicializamos los componentes del computador
        self.ram = ram
        self.disco_duro = disco_duro
        self.monitor = monitor
        self.mouse = mouse
        self.teclado = teclado

class Ram:
    def __init__(self, capacidad):
        # Inicializamos la capacidad de la RAM
        self.capacidad = capacidad

class DiscoDuro:
    def __init__(self, capacidad):
        # Inicializamos la capacidad del disco duro
        self.capacidad = capacidad

class Monitor:
    def __init__(self, tamano):
        # Inicializamos el tamaño del monitor
        self.tamano = tamano

class Mouse:
    def __init__(self):
        pass  # No se necesita inicialización específica para el mouse

class Teclado:
    def __init__(self):
        pass  # No se necesita inicialización específica para el teclado

# Creación de los objetos para las clases Ram, DiscoDuro, Monitor, Mouse y Teclado
ram = Ram(capacidad=8)  # Creamos una RAM de 8 GB
disco_duro = DiscoDuro(capacidad=512)  # Creamos un disco duro de 512 GB
monitor = Monitor(tamano=24)  # Creamos un monitor de 24 pulgadas
mouse = Mouse()  # Creamos un mouse
teclado = Teclado()  # Creamos un teclado

# Creación del objeto Computador y asociación con los objetos de sus componentes
computador = Computador(ram=ram, disco_duro=disco_duro, monitor=monitor, mouse=mouse, teclado=teclado)

# Mensaje indicando que el programa se ha ejecutado correctamente
print("El programa se ha ejecutado correctamente.")
