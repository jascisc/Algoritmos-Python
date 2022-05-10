#Empleando la estructura while realice un algoritmo 
#para calcular el factorial de un número.(FOR)

from math import factorial


numero=int(input("Ingresa un número:"))
factorial=1
for i in range(1,(numero+1)):
    factorial*=i
print("Factorial",factorial)
