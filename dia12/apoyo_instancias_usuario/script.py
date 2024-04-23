import json #se importa JSON para manejo de datos en formato JSON
from datetime import datetime #se importa datetime para ocupar fechas y horas
from usuario import Usuario #para poder crear instancias de Usuario, s importa la clase Usuario de modulo usuario

instancias = []

#Abre el archivo usuarios.txt en modo lectura
with open("dia12/apoyo_instancias_usuario/usuarios.txt") as usuarios:
    #Lee cada línea del archivo
    for num_linea, linea in enumerate(usuarios, start=1):#bukle for itera sobre cada línea del usuarios.txt;
        #las enumera empezando desde el 1 (enumerate y start)
        try:
            #cadena JSON se está convirtiendo en un objeto = dicc{}
            usuario = json.loads(linea)#parseando una cadena JSON con loads
            
            #Crea una instancia de Usuario y la agrega a la lista de instancias
            instancias.append(Usuario(usuario["nombre"], usuario["apellido"], usuario["email"], usuario["genero"]))
        except Exception as e:
            #Si ocurre una excepcion, registra el error en el archivo de registro
            now = datetime.now()#fecha y hora actual rai nou
            with open("dia12/apoyo_instancias_usuario/error.log", "a") as log:#open el archivo de registro en modo de adjuntar con append
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Error en línea {num_linea}: {e}\n")#msje: error + arch registro + tiempo + num linea
                print(f"Este es el ERROR registrados en el archivo, modifiquelo en brevedad:\n{e}")
                
"""
# Muestra las instancias creadas correctamente
print("Instancias creadas correctamente:")
for instancia in instancias:
    print(instancia.__dict__)
"""

""" 
Este es el ERROR registrados en el archivo, modifiquelo en brevedad:
Expecting ',' delimiter: line 2 column 1 (char 99)
Este es el ERROR registrados en el archivo, modifiquelo en brevedad:
Expecting property name enclosed in double quotes: line 1 column 40 (char 39)
Este es el ERROR registrados en el archivo, modifiquelo en brevedad:
Expecting value: line 1 column 88 (char 87)
"""