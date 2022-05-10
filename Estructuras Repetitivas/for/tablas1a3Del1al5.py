#Se necesita un sistema que despliega las tablas de 
#multiplicar del uno al tres (cada tabla del 1 al 5).

for i in range(1,4):
    print("Tabla del ",i)
    for j in range(1,6):
        print(i,"x",j,"=",i*j)