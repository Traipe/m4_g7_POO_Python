#Clase Base para Excepciones
class Error(Exception):
    pass

#Excepción para errores relacionados con el formato de hora
class HoraError(Error):
    pass

#Excepción para errores relacionados con la longitud de texto
class LargoTextoError(Error):
    #Constructor de la clase LargoTextoError.
    def __init__(self, mensaje: str, texto: str = None, largo: int = None) -> None:
        self.mensaje = mensaje
        ##Acorta el texto si es k supera los 50 caracteres para evitar mensajes demasiado largos
        self.texto = (f"{texto[:50]}..." if texto is not None and len(texto) > 50 else texto)
        self.largo = largo

    #Método para obtener una representación en forma de cadena del objeto.
    def __str__(self) -> str:
        if self.texto is None and self.largo is None:
            # Si no se proporciona texto ni longitud, se usa el método __str__ de la clase base
            return super().__str__()
        else:
            ret = f"{self.mensaje}."#Construye el mensaje de error básico
            if self.texto is not None:
                ret += f" Texto ingresado: {self.texto}."#Agrega el texto si está presente
            if self.largo is not None:
                ret += f" Máximo {self.largo} caracteres permitidos."#Agrega la longitud máxima si está presente
            return ret