import json

# Paso 1: Definir la clase Producto
class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

#paso2: Crear una lista vacía para almacenar las instancias de Producto
instancias = []

#paso3: Abrir el archivo de texto que contiene los productos en modo lectura
with open("productos.txt") as productos:
    #paso4: Leer la primera línea del archivo
    linea = productos.readline()
    
    #paso5: Iniciar un ciclo while que se ejecutará mientras haya líneas en el archivo
    while linea:
        #paso6: Convertir la línea en un diccionario usando JSON
        producto = json.loads(linea)
        
        #paso7: Crear una instancia de Producto y añadirla a la lista de instancias
        instancias.append(Producto(producto["nombre"], producto["precio"]))
        
        #paso8: Leer la siguiente línea del archivo
        linea = productos.readline()
