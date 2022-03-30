#algoritmo para evaluar con cualquier 
# valor de x la siguiente función matemática:
#Y=5x^5-4x^4+3x^3-2x^2+6x-12

print("Ingresa el valor de x")
x=float(input())
y=(5*(x**5)-(4*(x**4))+(3*(x**3))-(2*(x**2))+(6*(x))-12)
print("Y="+str(y)+" cuando x="+str(x))