class DimensionError(Exception):#Excepción para errores relacionados con las dimensiones de la foto
    #Constructor de la clase DimensionError.
    def __init__(self, mensaje: str, dimension: str = None, maximo: int = None) -> None:
        """
        Args:
            mensaje (str): Mensaje descriptivo del error.
            dimension (str, optional): Dimensión de la foto afectada (ancho o alto). Por defecto es None.
            maximo (int, optional): Valor máximo permitido para la dimensión. Por defecto es None.
        """
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    #Método para obtener una representación en forma de cadena del objeto.
    def __str__(self) -> str:
        """
        Returns:
            str: Cadena que representa el objeto DimensionError.
        """
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            ret = f"{self.mensaje}."
            if self.dimension is not None:
                ret += f" Dimensión: {self.dimension}."
            if self.maximo is not None:
                ret += f" Máximo permitido: {self.maximo}."
            return ret
