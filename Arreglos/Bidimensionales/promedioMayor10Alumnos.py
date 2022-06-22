#Se necesita un sistema que utiliza una matriz de 10 
#renglones y 3 columnas. En las dos primeras columnas 
#se colocan los promedios de los 10 alumnos de dos 
#grupos (A y B) y en la tercera columna se almacenará 
#el promedio más alto de cada posición.
n = 10
m = 3
matriz = []
for i in range(n):
    matriz.append([])
    cal1=0
    cal2=0
    for j in range(m):
        if(j==0):
            print("Ingresa calificación "+str(j+1)+ " del grupo "+str(i+1))
            cal1=int(input())
            matriz[i].append(cal1)
        if(j==1):
            print("Ingresa calificación "+str(j+1)+ " del grupo "+str(i+1))
            cal2=int(input())
            matriz[i].append(cal2)
        if(j==2):
            if(cal1>cal2):
                matriz[i].append(cal1)
            else:
                matriz[i].append(cal2)

print(matriz)
