from medicamento import Medicamento

#paso1: crear una instancia
medicamento_nuevo = Medicamento()

#paso2: solicitud de ingreso de datos
precio = int(input("Ingrese el precio del medicamento > "))

#paso3: pasar al metodo de instancia el valor capturado 
medicamento_nuevo.asigna_precio(precio)
medicamento_nuevo.precio
