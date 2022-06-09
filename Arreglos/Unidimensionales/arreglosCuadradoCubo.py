#Realizar un programa que almacena 20 números en tres diferentes 
#arreglos, en el primero se almacena el número tal cual se tecleo,
#en el segundo se almacena el cuadrado de dicho número y en el tercero su cubo

listaNumero=[]
listaCuadrado=[]
listaCubo=[]

for i in range(0,19):
    print("Ingresa el número ",(i+1))
    num=int(input())
    listaNumero.append(num)
    listaCuadrado.append(num*num)
    listaCubo.append(num*num*num)

for i in range(0,len(listaNumero)):
    print("Número ingresado:",listaNumero[i])
    print("Número cuadrado:",listaCuadrado[i])
    print("Número cubo:",listaCubo[i])
    print("")