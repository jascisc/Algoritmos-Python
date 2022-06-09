#Realizar un programa que almacene los primeros 20 
#números primos recordando que un número primo es 
#aquel que es divisible entre si mismo y la unidad.

primos=[]
ba=True
n=0
con=2
while ba:
    x=0
    for i in range(2,con):
        if(con%i==0):
            x+=1
    if(x==0):
        primos.append(con)
        n+=1
    con+=1
    if(n>19):
        ba=False

for i in range(0,len(primos)):
    print(str(i+1)+":"+str(primos[i]))