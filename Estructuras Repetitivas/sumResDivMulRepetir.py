#Algoritmo que contenga un menú con las siguientes opciones:
#MENU DE OPCIONES
#    1. Suma
#    2. Resta
#    3. Multiplicación
#    4. División
#    5. SALIR DEL SISTEMA
#ELIJA OPCION:
#Al presionar del 1 al 5 se deberá ejecutar la opción correspondiente. 
#Mientras no se presiona la opción 5, si elegimos del 1 al 4 se ejecutará 
#la opción correspondiente sin parar el programa. Hasta que 
#presione la opción 5 se deberá terminar de ejecutar el programa. 
#Cualquier otra opción se deberá indicar como OPCION NO VALIDA.
opcion=1
while opcion<5:
    print("MENU DE OPCIONES")
    print("     1. Suma")
    print("     2. Resta")
    print("     3. Multiplicación")
    print("     4. División")
    print("     5. SALIR DEL SISTEMA")
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
    elif opcion==5:
        print("Gracias por usar el programa")
    else:
        opcion=1
        print("OPCION NO VALIDA EN EL SISTEMA")