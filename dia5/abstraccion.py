""" 
ABSTRACCION:
Una clase es abstracta, si tiene a lo menos un metodo abstracto
Metodo Abstracto: son aquellos que tienen solo la deficion de metodo
ademas debe tener el decorador @abstractmethod

para poder crear una clase abstracta i un metodo abstracto importamos:

from abc import ABC, abstractmethod

"""

from abc import ABC, abstractmethod

class Pelota(ABC):#clase abstracta

    #definicion del metodo abstracto
    @abstractmethod
    def rebotar(self, altura: int):
        pass


## creando una subclase: una clase que nace a partir de otra clase
class PelotaDeJuguete(Pelota):
    def __init__(self):
        self.color = "Blanco"

    #obligacion de implementar metodo abstracto
    def rebotar(self, altura: int):
        pass
    
    def imprimir(self):
        print("metodo de la subclase")
    
#creacion de objeto
pelotita = PelotaDeJuguete()
#TypeError: Can't instantiate abstract class PelotaDeJuguete without an implementation for abstract method 'rebotar'
print(pelotita.rebotar(20))#None
