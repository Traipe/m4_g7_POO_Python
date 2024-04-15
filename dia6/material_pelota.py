#EJEMPLO PDF clases
class Material:
    def __init__(self, nombre: str, duracion: str, textura: str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota:
    def __init__(self, tamanio: int, color: str, material: Material):
        self.tamanio = tamanio
        self.color = color
        # La pelota tiene un material
        self.material = material

# Creamos una instancia de la clase Material
m = Material("Plástico", "Corta", "Lisa")

# Creamos una instancia de la clase Pelota, pasando la instancia de Material como argumento
p = Pelota(16, "Amarillo", m)

# Salida: <class '__main__.Material'> (Muestra el tipo de objeto del atributo 'material' de la pelota)
print(type(p.material))

# Salida: Plástico (Muestra el nombre del material de la pelota)
print(p.material.nombre)
