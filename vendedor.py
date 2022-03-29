#Un vendedor recibe un sueldo base más un 10% 
#extra por comisión de sus ventas, el vendedor 
#desea saber cuánto dinero obtendrá por concepto 
#de comisiones por las ventas que realiza
#en el mes y el total que recibirá en el mes 
#tomando en cuenta su sueldo base y comisiones.

print("Ingresa sueldo base")
sueldo=int(input())
print("Número de ventas")
nVentas=int(input())
tVentas=0

for iterable in range(0,nVentas):
    print('Ingresa la venta '+str(iterable+1))
    tVentas+=int(input())

print("Tús comisiones son: "+str((10/100)*tVentas))
print("Total a recibir (Sueldo + comisión) "+str((sueldo)+((10/100)*tVentas)))

