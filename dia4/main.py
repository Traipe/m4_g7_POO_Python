from pelota import Pelota

nueva_pelota= Pelota("Negro")
nueva_pelota.___password= "admin1234"#no hace nada
#print(nueva_pelota.__password)#AttributeError: 'Pelota' object has no attribute '__password'

nueva_pelota.setColor("Blanco")
print(nueva_pelota.color)#Blanco
#es decir, la asignacion de un metodo funciona

nueva_pelota.color = "Naranjo"
print(nueva_pelota.color)

nueva_pelota.color = ""
print(nueva_pelota.color)#Verde

print(nueva_pelota.marca)#Adidas

nueva_pelota.color
print(nueva_pelota.color)