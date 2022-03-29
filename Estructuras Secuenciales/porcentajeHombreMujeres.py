#Algoritmo para determinar el porcentaje de hombres y mujeres que hay en un grupo.
print("Cantidad de mujeres")
cMujeres=int(input())
print("Cantidad de hombres")
cHombres=int(input())

print("En total tenemos "+str(cMujeres+cHombres)+" personas")
print(str(((cMujeres/(cMujeres+cHombres))*100))+"% son mujeres y el "+str(100-((cMujeres/(cMujeres+cHombres))*100))+"% son hombres")
