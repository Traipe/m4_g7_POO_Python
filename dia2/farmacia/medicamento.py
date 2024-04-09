class Medicamento():
    #atributos de la clase 
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    #los metodos estaticos no pueden modificar los atributos
    @staticmethod
    def modificar_atributo():
        #la clase esta modificando
        Medicamento.IVA = 0.19
        
    def asigna_precio(self, precio_entregado: int):
        es_valido = self.validar_mayor_a_cero(precio_entregado)#validar si el precio entregado es valido
        #if, se podria reemplazar por self.validar_mayor ...
        if es_valido:
            self.precio = precio_entregado  
        else:
            print(f"El precio {precio_entregado}, no es un valor valido")
