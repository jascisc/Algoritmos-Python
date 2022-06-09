#Realizar un programa que utiliza 2 arreglos para almacenar
#20 números, en el primero se almacenan los números tal 
#y como son capturados y en el segundo se almacenan sus inversos (5, -5)


listaNumeros=[]
listaInverso=[]
num1=-1
for i in range(0,19):
    print("Ingresa el número ",(i+1))
    num=int(input())
    listaNumeros.append(num)
    listaInverso.append(((num)*(num1)))

for num in listaNumeros:
    print(num)

for num in listaInverso:
    print(num)