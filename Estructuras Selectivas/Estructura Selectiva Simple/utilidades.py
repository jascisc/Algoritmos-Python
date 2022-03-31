#Calcular la utilidad que un trabajador recibe 
#en el reparto anual de utilidades si a este se le
#asigna un porcentaje de su salario mensual 
#que depende de su antigüedad en la empresa 
#de acuerdo con la siguiente tabla:

#            Tiempo					       Utilidad
#	Menos de 1 año						5 % del salario
#	1 año o más y menos de 2 años		7% del salario
#	2 años o más y menos de 5 años		10% del salario
#   5 años o más y menos de 10 años		15% del salario
#   10 años o más					    20% del salario

tiempo=float(input("Ingresa tiempo trabajado (Solo años completos, 0 para quien no tiene un año cumplido):"))
salario=float(input("Ingresa tu salario:"))
if tiempo<1:
    print("Utilidades:",((salario*5)/100))
elif tiempo<2:
    print("Utilidades:",((salario*7)/100))
elif tiempo<5:
    print("Utilidades:",((salario*10)/100))
elif tiempo<10:
    print("Utilidades:",((salario*15)/100))
elif tiempo>=10:
    print("Utilidades:",((salario*20)/100))
