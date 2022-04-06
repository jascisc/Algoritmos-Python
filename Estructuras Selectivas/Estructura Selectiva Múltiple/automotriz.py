# Una empresa automotriz necesita un sistema para seleccionar 
# el tipo de carro (auto, camioneta o vagoneta) lo cual debe de aparecer 
# en un menú, y el color (negro, blanco o rojo) en otro menú. 
# Al final se necesita que despliegue la selección realizada.
# NOTA: Debe de anidarse una estructura de selección múltiple dentro de otra.
print("Opciones disponibles")
print("  1. Auto")
print("  2. Camioneta")
print("  3. Vagoneta")
opcion=int(input("Ingresa tu selección:"))
if opcion==1:
    print("Colores disponibles")
    print("  1. Negro")
    print("  2. Blanco")
    print("  3. Rojo")
    color=int(input("Ingresa tu selección:"))
    if color==1:
        print("Seleccionaste Auto color Negro")
    elif color==2:
        print("Seleccionaste Auto color Blanco")
    elif color==3:
        print("Seleccionaste Auto color Rojo")
    else:
        print("Opción no valida")
elif opcion==2:
    print("Colores disponibles")
    print("  1. Negro")
    print("  2. Blanco")
    print("  3. Rojo")
    color=int(input("Ingresa tu selección:"))
    if color==1:
        print("Seleccionaste Camioneta color Negro")
    elif color==2:
        print("Seleccionaste Camioneta color Blanco")
    elif color==3:
        print("Seleccionaste Camioneta color Rojo")
    else:
        print("Opción no valida")
elif opcion==3:
    print("Colores disponibles")
    print("  1. Negro")
    print("  2. Blanco")
    print("  3. Rojo")
    color=int(input("Ingresa tu selección:"))
    if color==1:
        print("Seleccionaste Vagoneta color Negro")
    elif color==2:
        print("Seleccionaste Vagoneta color Blanco")
    elif color==3:
        print("Seleccionaste Vagoneta color Rojo")
    else:
        print("Opción no valida")
else:
    print("Opción no valida")