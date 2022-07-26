#Realizar un programa que sume dos matrices A y B. 
#El usuario tendrá la libertad de decir de cuantas 
#filas y columnas deben de ser recordando que ambas 
#deben de ser de la misma dimensión

m=int(input("Ingrese el número de filas de las matrices: "))
n=int(input("Ingrese el número de columnas de las matrices: "))

matrizA = []
matrizB = []
matrizC = []
for i in range(m):
    matrizA.append([])
    for j in range(n):
        matrizA[i].append(int(input("Ingrese el valor de la matriz A en la posición "+ str(i) + "," + str(j) + ": ")))
for i in range(m):
    matrizB.append([])
    for j in range(n):
        matrizB[i].append(int(input("Ingrese el valor de la matriz B en la posición "+ str(i) + "," + str(j) + ": ")))
for i in range(m):
    matrizC.append([])
    for j in range(n):
        matrizC[i].append(matrizA[i][j]+matrizB[i][j])

for mc in matrizC:
    print(mc)