from abc import ABC, abstractmethod

class Membresia(ABC):
    #Clase abstracta que define la estructura base de todas las membresías.
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        
        #Constructor de la clase Membresia.
        """Parámetros:
        - correo_suscriptor: (str) Correo electrónico del suscriptor.
        - numero_tarjeta: (str) Número de tarjeta del suscriptor.
        """
        self.__correo_suscriptor = correo_suscriptor  # Encapsulamiento del correo del suscriptor
        self.__numero_tarjeta = numero_tarjeta  # Encapsulamiento del número de tarjeta
        
    @abstractmethod
    def cambiar_suscripcion(self, tipo_membresia: int):#Metodo abstracto para cambiar el tipo de membresia

        """
        Parámetros:
        - tipo_membresia: (int) Identificador del tipo de membresía a cambiar.      
        Retorna:
        - Membresia: Nueva instancia de membresía.
        """
        pass

    @abstractmethod
    def cancelar_suscripcion(self):#Método abstracto para cancelar la membresía.
        """
        Retorna:
        - Membresia: Nueva instancia de membresía (Gratis).
        """
        pass

class Gratis(Membresia):#Clase que representa la membresía gratuita.

    #Cambia la suscripción a otra membresía segun el tipo especificado.
    def cambiar_suscripcion(self, tipo_membresia: int) -> Membresia:
        """
        Parámetros:
        - tipo_membresia: (int) Tipo de membresía al que se desea cambiar.

        Retorna:
        - Membresia: Instancia de la nueva membresía.
        """
        return MembresiaFactory.crear_membresia(tipo_membresia, self._Membresia__correo_suscriptor, self._Membresia__numero_tarjeta)

    #Método para cancelar la membresía gratuita.
    def cancelar_suscripcion(self):
        """
        Retorna:
        - Membresia: Nueva instancia de membresía (Gratis).
        """
        return Gratis(self._Membresia__correo_suscriptor, self._Membresia__numero_tarjeta)

class Basica(Membresia):#Clase que representa la membresia basica.
        
    #Constructor de la clase Basica
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Parámetros:
        - correo_suscriptor: (str) Correo electrónico del suscriptor.
        - numero_tarjeta: (str) Número de tarjeta del suscriptor.
        """
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 3000  # Costo de la membresia basica
        self.max_dispositivos = 2  # Máximo de dispositivos permitidos

    def cambiar_suscripcion(self, tipo_membresia: int) -> Membresia:#Cambia la suscripción a otra membresía según el tipo especificado.
        """
        Parámetros:
        - tipo_membresia: (int) Tipo de membresía al que se desea cambiar.

        Retorna:
        - Membresia: Instancia de la nueva membresía.
        """
        return MembresiaFactory.crear_membresia(tipo_membresia, self._Membresia__correo_suscriptor, self._Membresia__numero_tarjeta)

    def cancelar_suscripcion(self):#Método para cancelar la membresía básica.
        """
        Retorna:
        - Membresia: Nueva instancia de membresía (Gratis).
        """
        return Gratis(self._Membresia__correo_suscriptor, self._Membresia__numero_tarjeta)

class Familiar(Basica):#Clase que representa la membresía familiar.
    #Constructor de la clase Familiar.
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Parámetros:
        - correo_suscriptor: (str) Correo electrónico del suscriptor.
        - numero_tarjeta: (str) Número de tarjeta del suscriptor.
        """
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 5000  # Costo de la membresía familiar
        self.max_dispositivos = 5  # Máximo de dispositivos permitidos
        self.dias_regalo = 7  # Días de regalo al crear la membresía
        self.control_parental = None  # Estado del control parental

    def cambiar_suscripcion(self, tipo_membresia: int):#Método para cambiar la membresía familiar por otra.
        """
        Parámetros:
        - tipo_membresia: (int) Identificador del tipo de membresía a cambiar.

        Retorna:
        - Membresia: Nueva instancia de membresía.
        """
        if tipo_membresia == 1 or tipo_membresia == 3 or tipo_membresia == 4:
            return MembresiaFactory.crear_membresia(tipo_membresia, self._Membresia__correo_suscriptor, self._Membresia__numero_tarjeta)
        else:
            print("Tipo de membresía no válido.")
            return self

    def modificar_control_parental(self, nuevo_estado):#Método para modificar el control parental.
        """
        Parámetros:
        - nuevo_estado: (str) Nuevo estado del control parental.
        """
        self.control_parental = nuevo_estado

class SinConexion(Basica):#Clase que representa la membresía sin conexión.

    #Constructor de la clase SinConexion.
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Parámetros:
        - correo_suscriptor: (str) Correo electrónico del suscriptor.
        - numero_tarjeta: (str) Número de tarjeta del suscriptor.
        """
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 3500  # Costo de la membresía sin conexión
        self.max_dispositivos = 2  # Máximo de dispositivos permitidos
        self.dias_regalo = 7  # Días de regalo al crear la membresía
        self.max_contenido_sin_conexion = None  # Máximo de contenido sin conexión

    def cambiar_suscripcion(self, tipo_membresia: int):#metodo para cambiar la membresía sin conexión por otra.
        """
        Parámetros:
        - tipo_membresia: (int) Identificador del tipo de membresía a cambiar.

        Retorna:
        - Membresia: Nueva instancia de membresía.
        """
        if tipo_membresia == 1 or tipo_membresia == 2 or tipo_membresia == 4:
            return MembresiaFactory.crear_membresia(tipo_membresia, self._Membresia__correo_suscriptor, self._Membresia__numero_tarjeta)
        else:
            print("Tipo de membresía no válido.")
            return self

    def incrementar_contenido_sin_conexion(self, cantidad):#metodo para incrementar la cantidad máxima de contenido sin conexión.
        """      
        Parámetros:
        - cantidad: (int) Cantidad a incrementar.
        """
        if self.max_contenido_sin_conexion is not None:
            self.max_contenido_sin_conexion += cantidad
        else:
            self.max_contenido_sin_conexion = cantidad

class Pro(Familiar, SinConexion):#Clase que representa la membresía Pro.

    #constructor de la clase Pro.
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Parámetros:
        - correo_suscriptor: (str) Correo electrónico del suscriptor.
        - numero_tarjeta: (str) Número de tarjeta del suscriptor.
        """
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 7000  # Costo de la membresía Pro
        self.max_dispositivos = 6  # Máximo de dispositivos permitidos
        self.dias_regalo = 15  # Días de regalo al crear la membresía

    def cambiar_suscripcion(self, tipo_membresia: int):#metodo para cambiar la membresía Pro por otra.
        """
        Parámetros:
        - tipo_membresia: (int) Identificador del tipo de membresía a cambiar.

        Retorna:
        - Membresia: Nueva instancia de membresía.
        """
        if tipo_membresia >= 1 and tipo_membresia <= 3:
            return MembresiaFactory.crear_membresia(tipo_membresia, self._Membresia__correo_suscriptor, self._Membresia__numero_tarjeta)
        else:
            print("Tipo de membresía no válido.")
            return self

# Factory para crear instancias de membresías
class MembresiaFactory:

    #Método estático para crear una membresía según el tipo especificado.
    @staticmethod
    def crear_membresia(tipo_membresia: int, correo_suscriptor: str, numero_tarjeta: str):
        """
        Parámetros:
        - tipo_membresia: (int) Identificador del tipo de membresía a crear.
        - correo_suscriptor: (str) Correo electrónico del suscriptor.
        - numero_tarjeta: (str) Número de tarjeta del suscriptor.

        Retorna:
        - Membresia: Nueva instancia de membresía.
        """
        if tipo_membresia == 1:
            return Basica(correo_suscriptor, numero_tarjeta)
        elif tipo_membresia == 2:
            return Familiar(correo_suscriptor, numero_tarjeta)
        elif tipo_membresia == 3:
            return SinConexion(correo_suscriptor, numero_tarjeta)
        elif tipo_membresia == 4:
            return Pro(correo_suscriptor, numero_tarjeta)
        else:
            print("Tipo de membresía no válido.")
            return None

# Pruebas
g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))
