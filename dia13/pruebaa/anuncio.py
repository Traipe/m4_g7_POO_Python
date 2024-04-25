from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

#Constructor clase Anuncio
class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        self.__duracion = 5

    #getter para alto 
    @property
    def alto(self):
        return self.__alto

    #setter para alto
    @alto.setter
    def alto(self, value):
        self.__alto = value if value > 0 else 1 #nuevo valor para alto del anuncio

    #getter para sub_tipo
    @property
    def sub_tipo(self):
        return self.__sub_tipo

    #setter para sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, value):
        if value not in ("instream", "outstream"):
            raise SubTipoInvalidoError("Subtipo de anuncio inválido", value)
        self.__sub_tipo = value #nuevo valor para subtipo del anuncio

    #getter para duracion
    @property
    def duracion(self):
        return self.__duracion

    #setter para duracion
    @duracion.setter
    def duracion(self, value):
        self.__duracion = value if value > 0 else 5 #nueva duracion del anuncio

    #comprime el anuncio con metodo abst
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    #redimensiona el anuncio con metodo abst
    @abstractmethod
    def redimensionar_anuncio(self):
        pass
    
    #metodo statico para mostrar formatos de anuncios dispo
    @staticmethod
    def mostrar_formatos():
        print("FORMATO:")
        print("==========")


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    #metodo de compresion de anuncio de video
    def comprimir_anuncio(self):
        print("COMPRESION DE VIDEO NO IMPLEMENTADA AUN")

    #metodo de redimensionar el anuncio de video
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AUN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    #meotodo para comprimir anuncio display
    def comprimir_anuncio(self):
        print("COMPRESION DE ANUNCIOS DISPLAY NO IMPLEMENTADA AUN")

    #metodo de redimension de anuncio display
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AUN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    #metodo de comprimir anuncio para Social
    def comprimir_anuncio(self):
        print("COMPRESION DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AUN")

    #metodo para redimensionar anuncio Social
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AUN")
