""" 
funcion OPEN 
file = open(ruta,argumento o modo de apertura) -> si no agregamos esto, x default ret

#metodo open retorna un archivo de tipo file
#si no se puede abrir se lanza una excepcion

"""
import os

try:
    log_file = open(os.path.abspath("logs/error.log"))
    print(log_file)
    print(type(log_file))
except FileNotFoundError as fnfe:
    print("Archivo o directorio no encontrado")
    print(fnfe)
    #[Errno 2] No such file or directory: 'C:\\DESAFÍO_LATAM\\0044-1\\MODULO4\\MODULO_POO\\logs\\error.log'
    #aqui esta dicicendo ke es solo lectura
    
#ARGUMENTO
log_file2 = open(os.path.abspath("dia11/html/index.html"),"r")
print(log_file2.read())
log_file2.close()
print("*****************READ**********************\n")
log_file3 = open(os.path.abspath("dia11/html/index.html"),"r")
print(log_file3.readline())#trabajar con un for para leer linea a linea
log_file3.close()
print("*****************READLINE**********************\n")
log_file4 = open(os.path.abspath("dia11/html/index.html"),"r")
print(log_file4.readlines())#retorna una lista de c/una de las lineas
log_file4.close()
print("*****************READLINES**********************\n")
print("")
print("*****************WITH**********************\n")
with open(os.path.abspath("dia11/html/index.html"),"r") as archivo:
    #print(archivo)#<_io.TextIOWrapper name='C:\\DESAFÍO_LATAM\\0044-1\\MODULO4\\MODULO_POO\\dia11\\html\\index.html' mode='r' encoding='cp1252'>
    for linea in archivo:
        print(linea.strip())

#ARGUMENTO w, SOLO ESCRITURA
#la ruta donde se creará el archivo, debe existir
#el w no crea rutas, ya debe ser existente. Si no esta creada la carpeta no funcionará
log_file5 = open(os.path.abspath("dia11/html/assets/css/style.css"),"w")
log_file5.write("/*esto es otro comentario*/")
log_file5.write("*{\n\tmargin: 0px\n}")
log_file5.close()

import time
try:
    print(time.time())
    print(round(time.time()))
    edad = int(input("Ingrese su edad:\n"))
    
except Exception as e:
    with open(f"dia11/logs/{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")
        
#condicional: para hacer uso de r+ siempre el archivo debe existir
#    with open(f"dia11/logs/{round(time.time())}.log", "r+") as log:



