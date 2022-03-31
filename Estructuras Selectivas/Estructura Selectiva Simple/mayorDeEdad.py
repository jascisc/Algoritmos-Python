#Algoritmo para decir si una persona es MAYOR DE EDAD 
#en base a su edad. El usuario introduce su edad y si 
#es mayor o igual a 18 años decirlo al usuario. 
# Al final mandar un mensaje de agradecimiento 
# por usar el sistema.

print("Ingresa tu edad")
edad=int(input())
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("Gracias por usar el programa")