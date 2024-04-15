from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    @property
    def productos(self):
        return self.__productos

    def __str__(self):
        productos_str = ", ".join([f"{producto.nombre} ({producto.stock} disponibles)" for producto in self.__productos])
        return f"Nombre de la tienda: {self.__nombre}, Costo de delivery: {self.__costo_delivery}, Productos: {productos_str}"

    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod.nombre == producto.nombre:  
                prod += producto.stock  
                return
        self.__productos.append(producto)

    def listar_productos(self):
        if not self.__productos:  
            return "No hay productos disponibles en esta tienda."
        
        lista_productos = ""
        for producto in self.__productos:
            nombre = producto.nombre
            precio = producto.precio
            stock = producto.stock
            lista_productos += f"Nombre: {nombre}, Precio: {precio}, Stock: {stock}\n"
        return lista_productos

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad  
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                    return  
                else:
                    print("No hay suficiente stock para realizar la venta.")
                return
        print("Producto no encontrado en la tienda.")


class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        lista_productos = ""
        for producto in self.productos:
            nombre = producto.nombre
            precio = producto.precio
            lista_productos += f"Nombre: {nombre}, Precio: {precio}\n"
        return lista_productos

    def realizar_venta(self, nombre_producto, cantidad):
        print("No se puede realizar venta en un restaurante.")


class Supermercado(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)


class Farmacia(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if cantidad > 3:
                    print("No se puede solicitar una cantidad superior a 3 en una farmacia.")
                    return
                elif cantidad > producto.stock:
                    print("Solo se venderá la cantidad disponible.")
                    cantidad = producto.stock
                super().realizar_venta(nombre_producto, cantidad)
                return
        print("Producto no encontrado en la tienda.")
