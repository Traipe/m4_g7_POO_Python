class Madre():
    def __init__(self, color: str,**parametros):
        super().__init__(**parametros)#obligatorio
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

class Padre():
    def __init__(self, tamanio: int,**parametros):
        super().__init__(**parametros)#obligatorio
        self.__tamanio = tamanio

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        self.__tamanio = tamanio

class Hija(Madre,Padre):#si tenemos mismo atributo, se modifica el 1ro de la izq SIEMPRE
    """ sobreescritura de los constructores"""
    #def __init__(self, color: str, tamanio: int ):
    #    Madre.__init__(self,color)
    #    Padre.__init__(self,tamanio)
    
    def __init__(self, deuda = 0, **parametros ):
        super().__init__(**parametros)
        
        #atributo de instancia propio de Hija
        self.deuda = deuda


#objeto
#princesa = Hija("Azul",80)
princesa = Hija(deuda = 350, color = "Azul", tamanio = 80)

print(princesa.tamanio, princesa.color, princesa.deuda)

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"princesa es una instancia de Hija: {isinstance(princesa,Hija)}")#True
print(f"princesa es una instancia de Madre: {isinstance(princesa,Madre)}")#True
print(f"princesa es una instancia de Padre: {isinstance(princesa,Padre)}")#True
print(f"hijita es una instancia de Nieto: {isinstance(princesa,Padre)}")#True

#print(f"princesa es una instancia de Hija: {isinstance(princesa,Hijo)}")#NameError: name 'Hijo' is not defined. Did you mean: 'Hija'?