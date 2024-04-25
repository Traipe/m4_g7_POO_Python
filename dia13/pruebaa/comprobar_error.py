from datetime import datetime  #Importa el módulo datetime para manejar fechas y horas
from error import LargoExcedidoError, SubTipoInvalidoError  #Importa las clases de error personalizadas desde error.py

def manejar_excepciones():
    try:
        nombre_campaña = "Campaña de marketing " * 30  #Simula un nombre de campaña demasiado largo
        if len(nombre_campaña) > 200:
            raise LargoExcedidoError("El nombre de la campaña es demasiado largo")  #Lanza una excepción si el nombre de la campaña es demasiado largo

    except LargoExcedidoError as e:  #Captura la excepción de nombre de campaña demasiado largo
        ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #Obtiene la fecha y hora actual
        with open("dia13/pruebaa/errores.log", "a+", encoding="utf-8") as archivo:  #Abre el archivo de registro de errores en modo de añadir al final del archivo
            archivo.write(f"[{ahora}] LargoExcedidoError: {e.mensaje}\n")  #Escribe el mensaje de la excepción junto con la fecha y la hora en el archivo de registro de errores

    try:
        sub_tipo_invalido = "invalido"  # Simula un subtipo de anuncio inválido
        if sub_tipo_invalido not in ("instream", "outstream"):  # Verifica si el subtipo de anuncio es válido
            raise SubTipoInvalidoError("Subtipo de anuncio inválido", sub_tipo_invalido)  # Lanza una excepción si el subtipo de anuncio es inválido

    except SubTipoInvalidoError as e:  #Captura la excepción de subtipo de anuncio inválido
        ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #Obtiene la fecha y hora actual
        with open("dia13/pruebaa/errores.log", "a+", encoding="utf-8") as archivo:  #Abre el archivo de registro de errores en modo de añadir al final del archivo
            archivo.write(f"[{ahora}] SubTipoInvalidoError: {e.mensaje}, Subtipo: {e.subtipo}\n")  #Escribe el mensaje de la excepción junto con la fecha y la hora en el archivo de registro de errores

if __name__ == "__main__":
    manejar_excepciones()  #llama a la función manejar_excepciones cuando se ejecuta el script
