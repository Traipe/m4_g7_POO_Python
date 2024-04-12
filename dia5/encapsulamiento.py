class Auto:
    __color = "Blanco" #definimos un atrubuto de clase
    
    def __cambiar_color(self, color):
        print("Nuevo color", color)#Nuevo color Negro
        self.__color = color
    
    #este es un metodo publico, para usarlo necesito la instancia
    def imprimir_estado(self,nuevo_color):
        print(self.__color)#llamado al atributo
        self.__cambiar_color(nuevo_color)
        print(self.color)#llamado al getter

#getter -> obtener un valor
    @property
    def color(self):
        return self.__color#self va a ser la instancia
    
nissan = Auto()
print(nissan._Auto__color)
print("")
#print(nissan.__color)#AttributeError: 'Auto' object has no attribute '__color'
#print(Auto.__color)#AttributeError: type object 'Auto' has no attribute '__color'

#nissan.cambiar_color("Negro")
#AttributeError: 'Auto' object has no attribute 'cambiar_color'

#nissan.imprimir_estado()#Blanco
nissan.imprimir_estado("Negro")
print("")
print(nissan.color)#llamado al metodo getter
print(nissan._Auto__color)