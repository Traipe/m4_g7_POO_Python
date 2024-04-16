class Padre():
    #atributo de clase
    color = "verde"
    #constructor
    def __init__(self, tamanio: int):
        #atributos de instancia
        self.__tamanio = tamanio #atributo oculto/privado

    #metodos estaticos

    #metodos de instancia
    def cambia_color(self, color: str):
        if color != "":
            self.color = color    
    
    #sobrecarga
    def __str__(self):
        return f"El color es {self.color}, y de tamanio {self.__tamanio}"

    #getter - setters
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        if tamanio > 0:
            self.__tamanio = tamanio
        else:
            self.__tamanio = 0

#HERENCIA -> hereda TODO, y cada uno de los hijos puede tener sus propios metodos y atributos
#forma1
class Hija(Padre):
    peso = 100
    #polimorfismo: cambio en el comportamiento del metodo
    def cambia_color(self, color: str):
        #if color != "":
        self.color = color
#forma2
class Hijo(Padre):
    deuda = 120
    #sobreescrir el constructor
    def __init__(self, tamanio: int, saldo = 0):
        super().__init__(tamanio)#llamado al constructor del Padre
        self.__saldo =  saldo

    @property
    def saldo(self):
        return self.__saldo

class Nieto(Hija):
    pañal = "XL"

#instancia de la clase hija (creando un objeto)
hijita = Hija(100)#forma3 -> hereda al Nieto

hijita.cambia_color("")

print(f"el color de la clase hija es {hijita.color}")

#forma3 -> hereda de la Hija
regalon = Nieto(50)
#Llamado al metodo del padre a traves de la hija
super(type(hijita),hijita).cambia_color("gris")
print(f"el color de la clase hija es {hijita.color}")

#instancia de la clase HIJO
hijito = Hijo(10,1200)
print(hijito.tamanio,hijito.saldo,hijito.deuda)