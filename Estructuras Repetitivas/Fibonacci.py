#Encontrar los primeros n elementos de la serie Fibonacci
n=int(input("Ingresa n:"))
a=0
b=1
aux=0
while aux<n:
    print((aux+1),".-",a)
    c=a+b 
    a=b
    b=c
    aux+=1