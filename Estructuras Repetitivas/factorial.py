#Empleando la estructura while realice un algoritmo 
#para calcular el factorial de un número.
factorial=1
num=int(input("Ingresa un número:"))
while num>0:
    factorial*=num
    num-=1
print(factorial)