class Madre:
    def __init__(self, hija: 'Hija'):
        # Asignar la instancia de la clase hija como un atributo de instancia de la clase madre
        self.hija = hija

class Hija:
    def __init__(self, nombre: str):
        self.nombre = nombre

# Primero creamos una instancia de la clase hija
hija1 = Hija(nombre="Juana")

# Luego utilizamos esta instancia como argumento para crear la instancia de la clase madre
madre1 = Madre(hija=hija1)

# Podemos acceder a los atributos de la instancia hija a través de la instancia madre
print("El nombre de la hija es: \n",madre1.hija.nombre)  # Esto imprimirá "María"
