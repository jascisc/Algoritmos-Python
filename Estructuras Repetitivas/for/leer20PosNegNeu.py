#Leer 20 números e imprimir cuantos son  
#positivos, cuantos negativos y cuantos neutros.

pos=0
neg=0
neu=0
for i in range(1,21):
    print("Ingresa el número ",i)
    num=int(input())
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        neu+=1

print("Positivos:",pos," Negativos:",neg," Neutros:",neu)