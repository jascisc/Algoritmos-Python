#Se necesita de un sistema que utiliza un arreglo 
#de 5 renglones y cuatro columnas, para almacenar 
#los 3 parciales y su promedio de 5 alumnos
n = 5
m = 4
matriz = []
for i in range(n):
    matriz.append([])
    calTotal=0
    for j in range(m):
        if(j<3):
            print("Ingresa calificación "+str(j+1)+ " del alumno "+str(i+1))
            cal=int(input())
            calTotal+=cal
            matriz[i].append(cal)
        if(j==3):
            matriz[i].append(calTotal/3)

print(matriz)