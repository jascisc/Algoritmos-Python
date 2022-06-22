#Realizar un programa que tabule los valores de la 
#función f(x,y)=x^2-y^2+10 para los siguientes intervalos :
#Para x: [0,7] es decir 0,1,2,…,6,7
#Para y: [0,6] es decir 0,1,2,…,5,6
n = 42
m = 3
x=1
y=1
matriz = []
for i in range(n):
    matriz.append([])
    resultado=0
    for j in range(m):
        # print("Ingresa calificación "+str(j+1)+ " del alumno "+str(i+1))
        resultado=(i**2)-(j**2)+10
        matriz[i].append(j)

print(matriz)