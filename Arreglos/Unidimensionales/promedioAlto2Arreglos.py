#Realizar un programa que utilice 3 arreglos, en los dos 
#primeros se colocan los promedios de dos grupos de 5 
#alumnos cada uno y el tercer arreglo almacenará el promedio 
#más alto de cada posición. Imprimir los promedios más altos.
arreglo1=[]
arreglo2=[]
arreglo3=[]
aux=0
while aux<5:
    print("Promedio ",(aux+1)," grupo 1")
    num=int(input())
    arreglo1.append(num)
    print("Promedio ",(aux+1)," grupo 2")
    num=int(input())
    arreglo2.append(num)
    aux+=1

aux=0

while aux<5:
    if arreglo1[aux]>arreglo2[aux]:
        arreglo3.append(arreglo1[aux])
    else:
        arreglo3.append(arreglo2[aux])
    aux+=1

for i,mayor in enumerate(arreglo3):
    print("Promedio más alto", i,"=", mayor)