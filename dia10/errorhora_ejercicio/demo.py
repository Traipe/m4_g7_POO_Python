from error import HoraError, LargoTextoError  # Importar las clases de errores
from reunion import Reunion  # Importar la clase Reunion
import re  # Importar el módulo de expresiones regulares

titulo = None  # Variable para almacenar el título de la reunión
hora = None  # Variable para almacenar la hora de la reunión
time_re = "^(?:(?:([01]?\\d|2[0-3]):)?([0-5]?\\d):)?([0-5]?\\d)$"  # Expresión regular para validar el formato de la hora

while True:  # Iniciar un ciclo while infinito
    try:  # Bloque try para manejar excepciones
        if titulo is None or len(titulo) > 150:  # Validar título
            titulo = input("\nIngrese titulo de la reunion (Maximo 150 caracteres):\n")  # Solicitar título
            if len(titulo) > 150:  # Si el título excede el máximo permitido
                raise LargoTextoError(  # Lanzar excepción de LargoTextoError
                    "Titulo de la reunion excede maximo de caracteres", titulo, 150)  # Mensaje de error

        if hora is None or re.search(time_re, hora) is None:  # Validar hora
            hora = input("\nIngrese hora de la reunion (Formato: HH:MM:SS):\n")  # Solicitar hora
            if re.search(time_re, hora) is None:  # Si la hora no tiene el formato correcto
                raise HoraError("Formato de Hora debe ser HH:MM:SS.")  # Lanzar excepción de HoraError

        r = Reunion(titulo, hora)  # Crear instancia de Reunion con los datos ingresados
        print("\nReunion creada correctamente.")  # Imprimir mensaje de éxito
        break  # Salir del ciclo while
    except Exception as e:  # Manejar excepciones de cualquier tipo
        print(f"\n{e}\n")  # Imprimir la instancia de la excepción
        continue  # Continuar con la siguiente iteración del ciclo
