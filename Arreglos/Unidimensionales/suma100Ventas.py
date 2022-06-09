#Un supermercado necesita un sistema en donde almacenar 
#sus ingresos, los cuales son la sumatoria de todas las 
#ventas realizadas a los clientes (100 clientes).
ventas=[]
for i in range(0,99):
    print("Ingreso ",(i+1))
    ventas.append(input())

suma=0
for ven in ventas:
    suma+=float(ven)

print("Los ingresos son =",suma)