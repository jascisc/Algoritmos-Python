#Dados 2 números determinar la multiplicación de ellos, 
#sin usar el operador de multiplicación.

n1=int(input("Ingresa el Número 1:"))
n2=int(input("Ingresa el Número 2:"))
multiplicacion=0
aux=0
while aux<n1:
    multiplicacion+=n2
    aux+=1
print("La multiplicación es:",multiplicacion)