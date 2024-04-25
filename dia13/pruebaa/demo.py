from datetime import datetime #Importa el módulo datetime para manejar fechas y horas
from error import LargoExcedidoError, SubTipoInvalidoError #Importa las clases de error personalizadas desde error.py

def manejar_excepciones():
    try:
        nombre_campaña = "Campaña de marketing " * 30
        if len(nombre_campaña) > 200:
            raise LargoExcedidoError("El nombre de la campaña es demasiado largo")

    except LargoExcedidoError as e:
        #obtiene fecha y hora actual
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #abre el archivo de registro de errores, creandolo dentro de la carpeta
        with open("dia13/pruebaa/errores.log", "a+", encoding="utf-8") as file:
            file.write(f"[{now}] LargoExcedidoError: {e.mensaje}\n")#mensaje de excepcion con fecha y hora actual

    try:
        sub_tipo_invalido = "invalido"
        if sub_tipo_invalido not in ("instream", "outstream"):
            raise SubTipoInvalidoError("Subtipo de anuncio inválido", sub_tipo_invalido)

    except SubTipoInvalidoError as e:
        #obtiene fecha y hora actual
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #abre el archivo de registro de errores, creandolo dentro de la carpeta
        with open("dia13/pruebaa/errores.log", "a+", encoding="utf-8") as file:
            file.write(f"[{now}] SubTipoInvalidoError: {e.mensaje}, Subtipo: {e.subtipo}\n")#mensaje de excepcion con fecha y hora actual

if __name__ == "__main__":
    manejar_excepciones()
