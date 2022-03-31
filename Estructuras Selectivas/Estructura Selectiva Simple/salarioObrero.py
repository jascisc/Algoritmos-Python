#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
#   • Si trabaja 40 horas o menos se le paga $16 por hora
#   • Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
print("Ingresa las horas trabajadas")
hTrabajadas=float(input())
salario=0
if hTrabajadas>40:
    salario+=(40*16)
    hExtra=hTrabajadas-40
    salario+=(hExtra*20)
else:
    salario=(hTrabajadas*16)

print("El salario es:$"+str(salario))