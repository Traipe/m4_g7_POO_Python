class Pelota():
    #atributos de Clase
    marca = "adidas"
    
    #Metodo Constructor
    def __init__(self,color: str, tamano = 20, material = "plastico"):
        print("Metodo constructor al crear el objeto")
        self.tamano = tamano
        self.material = material
        self.rebotes = 0  
        self.__color = color #ocultando el atributo
        self.marca = "Adidas"
        self.__password = "qwerty"
        
    #metodo oculto    
    def __getColor(self):
        return self.__color 
    
    def setColor(self,color):
        self.__color = color
        
    def setPassword(self,password):
        self.__password = password
    
    #getter
    @property #el decorador nos deja tratar el metodo "color" como atributo
    #nos da acceso al atributo oculto
    def color(self):
        return self.__color
    
    #setter
    @color.setter
    def color(self,color: str):
        self.__color = color if color != "" else "Verde"
    
    #deleter
    @color.deleter
    def color(self):
        del self.__color   
        
pelota_futbol = Pelota("Amarillo",16,"plastico")
#print(pelota_futbol.__color)
#print("getColor()",pelota_futbol.getColor())
print("metodo getter", pelota_futbol.color)#SIN PARENTESIS


print(pelota_futbol.tamano,pelota_futbol.material)


#pelota2 = Pelota()#TypeError: Pelota.__init__() missing 1 required positional argument: 'color'

pelota3 = Pelota("Rojo")
print(pelota3.color,pelota3.tamano,pelota3.material)
pelota3.rebotes = 10

#pelota4 = Pelota()#TypeError: Pelota.__init__() missing 1 required positional argument: 'color'

print(Pelota.marca, pelota_futbol.marca)