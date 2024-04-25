class Error(Exception):#clase base para las excepciones
    pass

#se levanta cuando se excede el limite de longitud
class LargoExcedidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        
#funciona cuando se proporciona un subtipo de anuncio invalido
class SubTipoInvalidoError(Error):
    def __init__(self, mensaje, subtipo):
        self.mensaje = mensaje
        self.subtipo = subtipo
