import json
from datetime import datetime
from usuario import Usuario

instancias = []

# Abre el archivo usuarios.txt en modo lectura
with open("dia12/apoyo_instancias_usuario/usuarios.txt") as usuarios:
    # Lee cada línea del archivo
    for num_linea, linea in enumerate(usuarios, start=1):
        try:
            # Intenta cargar la línea como un objeto JSON
            usuario = json.loads(linea)
            
            # Crea una instancia de Usuario y la agrega a la lista de instancias
            instancias.append(Usuario(usuario["nombre"], usuario["apellido"], usuario["email"], usuario["genero"]))
        except Exception as e:
                        # Si ocurre una excepcion, registra el error en el archivo de registro
            now = datetime.now()
            with open("dia12/apoyo_instancias_usuario/error.log", "a") as log:
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Error en línea {num_linea}: {e}\n")
                print(f"Este es el ERROR registrados en el archivo, modifiquelo en brevedad:\n{e}")
                
"""
# Muestra las instancias creadas correctamente
print("Instancias creadas correctamente:")
for instancia in instancias:
    print(instancia.__dict__)
"""