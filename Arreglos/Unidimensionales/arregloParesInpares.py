#Realizar un programa que capture 20 números y después 
#de capturarlos que haga la revisión de estos para 
#indicarnos cuantos son pares y cuántos son impares

listaNumeros=[]
for i in range(0,5):
    print("Ingresa el número ",(i+1))
    num=int(input())
    listaNumeros.append(num)

pares=0
inpares=0
for num in listaNumeros:
    if num%2==0:
        pares+=1
    else:
        inpares+=1

print("Pares:",pares," Inpares:",inpares)