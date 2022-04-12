#Empleando la estructura Repetir…Hasta que realice 
#un algoritmo que imprima el mensaje “HOLA" 
#de manera repetitiva. Para esto al usuario se le debe 
#preguntar si desea visualizar el mensaje nuevamente. 
#En caso de no responder afirmativamente salirse del 
#ciclo de saludo y enviar un mensaje que agradezca el 
#haber usado el programa.
continuar=1
while continuar==1:
    print("HOLA")
    continuar=int(input("¿Otro saludo? 1) Sí, 2) No:"))
print("Gracias por usar este programa")
