#from foto import Foto

#instancia de Foto con dimensiones inválidas
try:
    foto_invalida = Foto(0, 2000, "ruta_de_la_foto.jpg")  # Intenta establecer un ancho inválido
except Exception as e:
    print("Se lanzó una excepción al intentar establecer un ancho inválido:", e)

try:
    foto_invalida = Foto(3000, 500, "ruta_de_la_foto.jpg")  # Intenta establecer un alto inválido
except Exception as e:
    print("Se lanzó una excepción al intentar establecer un alto inválido:", e)
