from medicamento import Medicamento

#paso1: crear una instancia
medicamento_nuevo = Medicamento()

#paso2: solicitud de ingreso de datos
precio = int(input("Ingrese el precio del medicamento > "))

#paso3: pasar al metodo de instancia el valor capturado 
medicamento_nuevo.asigna_precio(precio)

print(f"el precio es: ${medicamento_nuevo.precio}.-")
print(f"el descuento es: {medicamento_nuevo.descuento}%")

#NO SE PUEDE LLAMAR A UN METODO NO ESTATICO DESDE UNA CLASE
Medicamento.asigna_precio(1000)
#TypeError: Medicamento.asigna_precio() missing 1 required positional argument: 'precio_entregado'
