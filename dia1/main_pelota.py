#import pelota
from pelota import Pelota

#INSTANCIAR O CREAR OBJETO
#pelota_de_andy = pelota.Pelota()
pelota_de_andy = Pelota()

print(pelota_de_andy)#<pelota.Pelota object at 0x000002738B6F5A00>
print(type(pelota_de_andy))#<class 'pelota.Pelota'>
print(pelota_de_andy.forma)#redondeada
print(pelota_de_andy.material)# arroja linea vacia

pelota_de_andy.material = "Goma"
print(pelota_de_andy.material)#Goma

pelota_tenis = Pelota()
print(pelota_tenis.material)# arroja linea vacia
pelota_tenis.material = "Caucho"
print("material pelota tenis",pelota_tenis.material)#Caucho
print("")
print(pelota_tenis.posiciones)#[3, 0, 2, 1, 0]
#hasta aqui mantiene su valor inicial

#Metodos estaticos
#no se necesita crear un objeto para invocar al metodo
#se agrega la clase + . + metodo
print(Pelota.crear_rebote)#<function Pelota.crear_rebote at 0x0000016C4206DB20>
print(Pelota.crear_rebote())#[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

#modificando el valor del atributo x medio de la clase
Pelota.posiciones = [2,4,6]#modifico directamente el atributo
#clase.atributo = [cambio de valor]
Pelota.imprimir_posiciones()
print(Pelota.posiciones)#[2, 4, 6]
print("")

pelota_basketball = Pelota()
print(pelota_basketball.posiciones)#[2, 4, 6]

#METODOS NO ESTATICOS
pelota_basketball.rebotar()
print(pelota_basketball.posiciones)#[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
#este cambio es sólo para él, realziado a través de un método

pelota_pinpong = Pelota()
print(pelota_pinpong.posiciones)#[2, 4, 6]
#porque no se hizo la modificacion mediante el metodo rebotar

pelota_rugby = Pelota()
print(pelota_rugby.posiciones)#[2, 4, 6]

##aca cambie los nombres:  futbol =>basketball y basket =>pinpong

#Los metodos no estaticos permiten crear atributos(variables)
# de tipo "atributo de instancia"
pelota_pinpong.nuevo_atributo()
print(pelota_pinpong.color)#blanco
print(pelota_rugby.color)#AttributeError: 'Pelota' object has no attribute 'color'