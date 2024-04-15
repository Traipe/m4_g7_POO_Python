class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(stock, 0)  

    def __str__(self):
        return f"Nombre: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__stock}"

    def __add__(self, cantidad):
        self.__stock += cantidad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = max(nuevo_stock, 0)  
