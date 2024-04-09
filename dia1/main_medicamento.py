from medicamento import Medicamento

#INSTANCIA DE LA CLASE O CREACION DE UN OBJ
paracetamol = Medicamento()
aspirina = Medicamento() #aki creamos otro obj ke pertenece a la clase

print(paracetamol.descuento)#0.05
print(aspirina.descuento)#0.05

#Modificacion del estado de un objeto
paracetamol.descuento = 0.06

print(paracetamol.descuento)#0.06
print(aspirina.descuento)

Medicamento.descuento = 0.04
ibuprofeno = Medicamento()
print(ibuprofeno.descuento)

precio = int(input("Ingrese el precio a validar >"))
#llamado a un método estático
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es válido")
else:
    print("El precio ingresado NO es válido")
    
print(paracetamol.descuento,aspirina.descuento)#0.04 0.04 
    
if paracetamol.IVA == aspirina.IVA  and paracetamol.descuento == aspirina.descuento:
    print("Todas las instancias(objetos), tienen los mismos valores IVA y descuento")
    print("El valor del IVA es", Medicamento.IVA)
    print("El valor de descuento es", Medicamento.descuento)

Medicamento.IVA = 0.19
#ibuprofeno.modificar_atributo()
print(ibuprofeno.IVA)#0.19
print(aspirina.IVA)#0.19
print("")
print(paracetamol.descuento,aspirina.descuento,ibuprofeno.descuento)#0.06 0.04 0.04