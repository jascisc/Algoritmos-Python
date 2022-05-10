#Se necesita un sistema que despliega una tabla 
#de multiplicar de un número dado por el usuario de n a 10.

numero=int(input("Ingresa un número:"))
for i in range(1, 11):
    print(i,"x",numero,"=",i*numero)