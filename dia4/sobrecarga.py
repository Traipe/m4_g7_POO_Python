class Auto():
    def __init__(self,color: str = "blanco"): 
        self.__color=color
    
    def __str__(self): 
        return f"Metodo sobre cargado {self.__color}"#Metodo sobre cargado blanco
        
nissan = Auto()
print(nissan)#<__main__.Auto object at 0x000002A28DBC5EB0>
#con metodo str
#Metodo sobre cargado

toyota = Auto("Negro")
print(toyota)#Metodo sobre cargado Negro