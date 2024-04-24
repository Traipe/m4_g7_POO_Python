from error import HoraError, LargoTextoError  # Importar las clases de errores
from reunion import Reunion  # Importar la clase Reunion
import re  # Importar el módulo de expresiones regulares

# Expresión regular para validar el formato de la hora
time_re = "^(?:(?:([01]?\\d|2[0-3]):)?([0-5]?\\d):)?([0-5]?\\d)$"

while True:  # Iniciar un ciclo while infinito
    try:  # Bloque try para manejar excepciones
        titulo = input("\nIngrese titulo de la reunion (Maximo 150 caracteres):\n")  # Solicitar título
        if len(titulo) > 150:  # Si el título excede el máximo permitido
            raise LargoTextoError(  # Lanzar excepción de LargoTextoError
                "Titulo de la reunion excede maximo de caracteres", titulo, 150)  # Mensaje de error

        hora = input("\nIngrese hora de la reunion (Formato: HH:MM:SS):\n")  # Solicitar hora
        if re.search(time_re, hora) is None:  # Si la hora no tiene el formato correcto
            raise HoraError("Formato de Hora debe ser HH:MM:SS.")  # Lanzar excepción de HoraError

        fecha = input("\nIngrese fecha de la reunion (Formato: DD/MM/AAAA):\n")  # Solicitar fecha
        if not re.match(r'^([0-3]?\d\/{1})([01]?\d\/{1})([12]{1}\d{3}?)$', fecha):
            raise ValueError("El formato de la fecha no es válido. Debe ser DD/MM/AAAA.")

        r = Reunion(titulo, hora, fecha)  # Crear instancia de Reunion con los datos ingresados
        print("\nReunion creada correctamente.")  # Imprimir mensaje de éxito
        break  # Salir del ciclo while
    except Exception as e:  # Manejar excepciones de cualquier tipo
        print(f"\n{e}\n")  # Imprimir la instancia de la excepción
        continue  # Continuar con la siguiente iteración del ciclo
