from error import DimensionError#Importar la excepción DimensionError
class Foto():
    MAX = 2500 #Valor máximo permitido para el ancho y el alto

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property#metodo estatiko
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter #setter para el atributo ancho
    def ancho(self, ancho: int) -> None:
        """
        Args:
            ancho (int): Nuevo valor para el ancho.
        Raises:
            DimensionError: Si el nuevo valor de ancho es menor que 1 o mayor que el valor máximo permitido.
        """
        if ancho < 1 or ancho > self.MAX:
            raise DimensionError("Valor de ancho inválido", "Ancho", self.MAX)
        else:
            self.__ancho = ancho

    @property #metodo estatiko
    def alto(self) -> int:
        return self.__alto

    @alto.setter#setter para el atributo alto
    def alto(self, alto: int) -> None:
        """
        Args:
            alto (int): Nuevo valor para el alto.
        Raises:
            DimensionError: Si el nuevo valor de alto es menor que 1 o mayor que el valor máximo permitido.
        """
        if alto < 1 or alto > self.MAX:
            raise DimensionError("Valor de alto inválido", "Alto", self.MAX)
        else:
            self.__alto = alto
