#Realizar un programa que solicite al usuario una matriz 
#cuadrada (una matriz cuadrada es aquella que tiene el 
#mismo número de filas y columnas) e imprima la diagonal de esta.
m=int(input("Ingrese el tamaños de la matriz: "))

matriz = []
matrizDiagonal = []
for i in range(m):
    matriz.append([])
    for j in range(m):
        matriz[i].append(int(input("Ingrese el valor de la matriz en la posición "+ str(i) + "," + str(j) + ": ")))
for i in range(m):
    matrizDiagonal.append([])
    for j in range(m):
        if i==j:
            matrizDiagonal[i].append(matriz[i][j])
        else:
            matrizDiagonal[i].append(0)
for ma in matrizDiagonal:
    print(ma)