#Realizar un programa que tabule los valores de la 
#función f(x,y)=x^2-y^2+10 para los siguientes intervalos :
#Para x: [0,3] es decir 0,1,2,3
#Para y: [0,2] es decir 0,1,2
n = 3
m = 4
x=-1
y=0
matriz = []
for i in range(m):
    matriz.append([])
    x+=1
    y=0
    for j in range(n):
        resultado=(x**2)-(y**2)+10
        matriz[i].append([x,y,resultado])
        y=y+1
for mat in matriz:
    print(mat)