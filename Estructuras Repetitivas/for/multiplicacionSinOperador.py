#Dados 2 números determinar la multiplicación de ellos, 
#sin usar el operador de multiplicación.(FOR)

n1=int(input("Ingresa el Número 1:"))
n2=int(input("Ingresa el Número 2:"))
multiplicacion=0
for i in range(0,n2):
    multiplicacion+=n1
print("La multiplicación es:",multiplicacion)