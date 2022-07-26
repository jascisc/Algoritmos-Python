#Realizar un programa que solicite las 
#calificaciones de un grupo de m estudiantes 
#de n materias. Se deberá obtener el promedio 
#por alumno, materia y promedio grupal

m=int(input("Ingrese el número de alumnos: "))
n=int(input("Ingrese el número de materias: "))

matrizCal= []
matrizAlu = []
matrizMat = []
matrizMat1 = []
sumaTotal=0

for i in range(m):
    matrizCal.append([])
    for j in range(n):
        matrizCal[i].append(int(input("Ingrese la calificación "+ str(j+1) + " del estudiante " + str(i+1) + ": ")))
for cal in matrizCal:
    suma=0
    for c in cal:
        suma+=c
    promedio=suma/len(cal)
    matrizAlu.append(promedio)
print("El promedio de cada alumno es: ")
for p in matrizAlu:
    print(p)


for i in range(n):
    columna = [fila[i] for fila in matrizCal]
    matrizMat.append(columna)
for mat in matrizMat:
    suma=0
    for c in mat:
        suma+=c
        sumaTotal+=c
    promedio=suma/len(mat)
    matrizMat1.append(promedio)

print("El promedio de cada materia es: ")
for mat in matrizMat1:
    print(mat)

print("El promedio grupal es: " + str(sumaTotal/(n*m)))