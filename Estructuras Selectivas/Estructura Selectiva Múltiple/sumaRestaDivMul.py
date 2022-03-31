#Algoritmo que contenga un menú con las siguientes opciones:
#MENU DE OPCIONES
#    1. Suma
#    2. Resta
#    3. Multiplicación
#    4. División
#ELIJA OPCION:
#Al presionar del 1 al 4 se deberá ejecutar la opción correspondiente. 
# Si se teclea otra opción se debe mandar el mensaje “OPCION NO VALIDA EN EL SISTEMA”.

print("MENU DE OPCIONES")
print("     1. Suma")
print("     2. Resta")
print("     3. Multiplicación")
print("     4. División")
opcion=int(input("ELIJA OPCION:"))
if opcion==1:
    n1=float(input("Ingresa número 1:"))
    n2=float(input("Ingresa número 2:"))
    print("Suma:",str(n1+n2))
elif opcion==2:
    n1=float(input("Ingresa número 1:"))
    n2=float(input("Ingresa número 2:"))
    print("Resta:",str(n1-n2))
elif opcion==3:
    n1=float(input("Ingresa número 1:"))
    n2=float(input("Ingresa número 2:"))
    print("Multiplicación:",str(n1*n2))
elif opcion==4:
    n1=float(input("Ingresa número 1:"))
    n2=float(input("Ingresa número 2:"))
    print("División:",str(n1/n2))
else:
    print("OPCION NO VALIDA EN EL SISTEMA")
