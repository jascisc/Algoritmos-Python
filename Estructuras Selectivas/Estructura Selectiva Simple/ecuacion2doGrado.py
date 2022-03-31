#Realiza un algoritmo para resolver una ecuación de 
#segundo grado por la formula general.
a=float(input("Ingresa el valor de a:"))
b=float(input("Ingresa el valor de b:"))
c=float(input("Ingresa el valor de c:"))

raiz=(((b)**2)-(4*a*c))

if raiz<0:
    print("La ecuación no tiene solicion en los números reales")
elif raiz==0:
    x=((-b)/(2*a))
    print("La unica solución es x=",x)
else:
    x1=((-b)+(raiz**0.5))/(2*a)
    x2=((-b)-(raiz**0.5))/(2*a)
    print("Las soluciones son:")
    print("x1=",x1)
    print("x2=",x2)