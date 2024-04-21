from foto import Foto  # Importar la clase Foto del archivo foto.py

# Crear una instancia de Foto con dimensiones válidas
foto_valida = Foto(100, 150, "ruta_de_la_foto.jpg")

# Imprimir los atributos de la instancia para verificar que se hayan establecido correctamente
print("Ancho de la foto válida:", foto_valida.ancho)
print("Alto de la foto válida:", foto_valida.alto)
