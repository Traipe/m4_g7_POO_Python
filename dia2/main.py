from pelota import Pelota

#creacion de objeto o instancia de la clase
pelota_multicolor = Pelota() #aki le asigno clase Pelota
#i se transforma en un objeto

#print(pelota_multicolor.color)#AttributeError: 'Pelota' object has no attribute 'color'
#va a existir cuando llame al metodo que lo crea
#pelota_multicolor.lee_color()#AttributeError: 'Pelota' object has no attribute 'color'


pelota_multicolor.asigna_color("kelu")
#aki re100 estamos definiendo i creando el atributo
print(pelota_multicolor.color)#kelu
#ahora existe, ahora fue creado
pelota_multicolor.lee_color()#El color de esta pelota es kelu
#
pelota_multicolor.asigna_color("karu")#El color de esta pelota es karu

#el valor se lo va a asignar a una variable i luego llamar al lee_color
# i ese va a buscar el atributo
pelota_multicolor.lee_color_local_y_atributo("chodz")#El color chodz NO es el color de ESTA pelota

pelota_curi = Pelota()
pelota_curi.lee_color_local_y_atributo("curi")#AttributeError: 'Pelota' object has no attribute 'color'

