class Pizza():
    tamano = "Familiar"
    precio = 10000
    
    #paso2
    @staticmethod
    def validar(elemento,posibles_valores):
        for valor in posibles_valores:
            if valor == elemento:
                return True
        return False
        #return elemento in posibles_valores
        
    #paso3 
    def tomar_pedido(self):
        self.proteico = input(""" Ingrese un ingrediente proteico
            Vacuno\nPollo\nCarne Vegetal
        """ )
        self.vegetales = []
        self.vegetales.append(input(""" Ingrese un ingrediente proteico
                Vacuno\nPollo\nCarne Vegetal
        """))

        self.vegetal2 = input(""" Ingrese segundo ingrediente vegetal
            Tomate\nAceituna\nChampiñones                      
        """)
        
        self.masa = input(""" Ingrese tipo de masa
                          Tradicional\nDelgada                      
        """)
    
    #paso4 
    # #regresa True o False segun lo que ingresó el usuario
        self.es_pizza_valida = self.validar(self.proteico,lista_proteicos) and \
        self.validar(self.vegetales[0], lista_vegetales) and\
        self.validar(self.vegetal, lista_vegetales) and\
        self.validar(self.masa, lista_masa)
        #self.es_pizza_valida = True and True and True and True <<-- Esto es lo que estamos haciendo
    
    
    