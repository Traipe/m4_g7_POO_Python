from datetime import date

#constructor de campania
class Campania:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        self.nombre = nombre #nombre campaña
        self.fecha_inicio = fecha_inicio #fecha start
        self.fecha_termino = fecha_termino #fecha end
        self.anuncios = [self.instancia_de_anuncios(dicc) for dicc in anuncios] #lista de anuncios de la campaña

    #metodo creacion de instancias de anuncios a partir de un dicc
    def instancia_de_anuncios(self, anuncio: dict):
        pass #Aki debería ir la implementacion del metodo, por ahora es un marcador de posicion.

    #metodo para representar en cadena de la campaña
    def __str__(self):
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {', '.join([f'{len(self.anuncios)} {tipo}' for tipo in ('Video', 'Display', 'Social')])}"
