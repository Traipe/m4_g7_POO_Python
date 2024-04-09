from te import Te 

#crear dos instancias de la clase Te
te_1 = Te()
te_2 = Te()

#mostrar x pantalla el valor de cada tipo de dato almacenado
print("Tipo de te_1:", type(te_1))
print("Tipo de te_2:", type(te_2))

#verificar si ambos tipos almacenados son iguales 
if type(te_1) == type(te_2):
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")