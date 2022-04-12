#Dado un número n determinar si es un número perfecto
numero=int(input("Ingresa un número:"))
aux=2
suma=1
while aux<(numero/2)+1:
    if (numero%aux)==0:
        suma+=aux
    aux+=1
if suma==numero:
    print("El número es perfecto")
else:
    print("El número no es perfecto")