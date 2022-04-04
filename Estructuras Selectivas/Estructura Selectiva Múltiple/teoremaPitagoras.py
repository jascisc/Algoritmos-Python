#Algoritmo que contenga un menú con las siguientes opciones:
#MENU DE OPCIONES DEL TEOREMA DE PITAGORAS
#    1. Obtener Hipotenusa
#    2. Obtener Cateto Opuesto
#    3. Obtener Cateto Adyacente
#ELIJA OPCION:
#Al presionar del 1 al 3 se deberá ejecutar la opción correspondiente. 
#Si se teclea otra opción se debe mandar el mensaje 
#“OPCION NO VALIDA EN EL SISTEMA”. Las tres opciones 
#se basan en la fórmula del Teorema de Pitágoras, 
#donde se tendrá que introducir al programa el despeje correspondiente.

print("MENU DE OPCIONES DEL TEOREMA DE PITAGORAS")
print("  1. Obtener Hipotenusa")
print("  2. Obtener Cateto Opuesto")
print("  3. Obtener Cateto Adyacente")
opcion=int(input("ELIJA OPCION:"))
if opcion==1:
    co=int(input("Ingresa cateto opuesto:"))
    ca=int(input("Ingresa cateto adyacente:"))
    print("La hipotenusa es:",((((co)**2)+((ca)**2))**.5))
elif opcion==2:
    h=int(input("Ingresa hipotenusa:"))
    ca=int(input("Ingresa cateto adyacente:"))
    print("El cateto opuesto es:",((((h)**2)-((ca)**2))**.5))
elif opcion==3:
    h=int(input("Ingresa hipotenusa:"))
    co=int(input("Ingresa cateto opuesto:"))
    print("El cateto adyacente es:",((((h)**2)-((co)**2))**.5))
else:
    print("OPCION NO VALIDA EN EL SISTEMA")