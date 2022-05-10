#Suponga que se tiene un conjunto de calificaciones de un
#grupo de 40 alumnos. Realizar un algoritmo para mostrar
#la calificación más alta y la calificación mas baja de
#todo el grupo
menor=10
mayor=0
for i in range(1,41):
    print("Ingresa la calificación",i)
    num=int(input())
    if mayor<num:
        mayor=num
    if menor>num:
        menor=num

print("Mayor=",mayor," Menor=",menor)

