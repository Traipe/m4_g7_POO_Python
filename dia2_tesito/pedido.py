""" 
Najla Gatica
Lolett Llanquinao
Jimena Traipe

"""

from te import Te 
#solicitar al usuario ingresar los datos para generar un pedido de té
#Solicitar al usuario ingresar el sabor
sabor = int(input("Ingrese el número correspondiente al sabor (1: Té negro, 2: Té verde, 3: Agua de hierbas):"))
#Validar que el sabor ingresado esté dentro de las opciones válidas
while sabor not in [1, 2, 3]:
    sabor = int(input("Ingrese el número correspondiente al sabor (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))

formato = int(input("Ingrese el formato deseado (300 para 300 gr, 500 para 500 gr):"))
#Validar que el formato ingresado esté dentro de las opciones válidas
while formato not in [300, 500]:
    formato = int(input("Ingrese el formato deseado (300 para 300 gr, 500 para 500 gr): "))
    
#obtener tiempo de preparacion i recomendacion segun el sabor ingresado x usuario
tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor)

#Crear una instancia de la clase Te
te = Te()

#Obtener el precio según el formato ingresado por el usuario
precio = Te.obtener_precio_segun_formato(formato)
print("")
#mostrar en pantalla el detalle de toda la informacion del te ordenado
print("detalle del pedido:\n")
print("sabor del té:")
if sabor ==1:
    print("Té negro")
elif sabor == 2:
    print("Té verde")
elif sabor == 3:
    print("Agua de hierbas")

print("Formato:", formato, "gr")
print("Precio: $", precio)
print("")
print("Recomendación:", recomendacion)
print("Tiempo de preparación:", tiempo, "minutos")

