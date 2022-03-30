#algoritmo para dada una cantidad en pesos, 
#obtener la equivalencia en dólares, 
# asumiendo que la unidad cambiaria es un 
# dato desconocido.
print("Ingresa el precio del dólar")
pDolar=float(input())
print("Ingresa la cantidad de pesos a convertir")
cPesos=float(input())
print(str(cPesos)+" pesos son "+str((pDolar*cPesos))+" dólares")