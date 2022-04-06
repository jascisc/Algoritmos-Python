#Algoritmo que contenga un menú con las siguientes opciones:
#MENU DE OPCIONES DECALCULO DE VOLUMENES
#     1. Volumen de cilindro circular de radio r y altura inclinada l
#     2. Volumen de cono circular recto de radio r y altura h
#     3. Volumen de casquete esférico
#     4. Volumen de tronco de cono circular recto de radios a,b y altura h
#ELIJA OPCION:
#Al presionar del 1 al 4 se deberá ejecutar la opción correspondiente. 
#Si se teclea otra opción se debe mandar el mensaje “OPCION NO VALIDA EN EL SISTEMA”
pi=3.1416


print("MENU DE OPCIONES DECALCULO DE VOLUMENES")
print("     1. Volumen de cilindro circular de radio r y altura l")
print("     2. Volumen de cono circular recto de radio r y altura h")
print("     3. Volumen de casquete esférico")
print("     4. Volumen de tronco de cono circular recto de radios a,b y altura h")
opcion=int(input("ELIJA OPCION:"))
if opcion==1:
    r=float(input("r:"))
    h=float(input("h:"))
    print("El volumen del cilindro es:", ((pi*(r**2))*h))
elif opcion==2:
    r=float(input("r:"))
    h=float(input("h:"))
    print("El volumen del cono es:", ((1/3)*((pi*(r**2))*h)))
elif opcion==3:
    h=float(input("h:"))
    print("Ingresa R o r")
    print("     1. R:")
    print("     2. r:")
    optR=int(input(""))
    if optR==1:
        R=float(input("R:"))
        print("El volumen del casquete circular es:", (pi*(h**2))*((3*R)-h)/(3))
    elif optR==2:
        r=float(input("r:"))
        print("El volumen del casquete circular es:", (pi*h)*((3*(r**2))+(h**2))/(6))
    else:
        print("Opción invalida")
elif opcion==4:
    R=float(input("R:"))
    r=float(input("r:"))
    h=float(input("h:"))
    #g=(((h**2)+((R-r)**2))**0.5)
    print("El volumen del cono truncado es:",((pi*h)*((R**2)+(r**2)+(R*r)))/3)
else:
    print("OPCION NO VALIDA EN EL SISTEMA")
