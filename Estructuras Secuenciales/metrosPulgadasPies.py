#algoritmo para convertir una distancia en metros a pies y pulgadas.
pies=3.28084 #Un metro equivale a 3.28084 pies
pulgadas=39.3701 #Un metro equivale a 39.3701 pulgadas
print("Ingresa la cantidad de metros")
metros=int(input())

print(str(metros)+" metro(s) son "+str(metros*pies)+" pies y "+str(metros*pulgadas)+" pulgadas")
