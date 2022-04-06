#Un supermercado realiza una tómbola con todos los clientes,
#  si son hombres tienen que sacar de una canasta una bolita la 
# cual tiene un número grabado y si son mujeres lo mismo pero de 
# otra canasta, los premios se dan bajo la siguiente tabla:
#       HOMBRES                  MUJERES
#   Bolita    Premio        Bolita    Premio
#     1    Desodorante         1      Loción
#     2 SixPack de Cerveza     2      Bikini
#     3      Boxer             3   Crema p/la cara
#     4     Rasuradora         4      Plancha
#     5     Sudadera           5   Barniz de uñas

genero=int(input("Eres hombre(1) o mujer:(2)"))
if genero==1:
    bolita=int(input("Selecciona una bolita de 1 al 5:"))
    if bolita>0 and bolita<6:
        if bolita==1:
            print("Ganaste un desodorante")
        if bolita==2:
            print("Ganaste un SixPack de Cerveza")
        if bolita==3:
            print("Ganaste un Boxer")
        if bolita==4:
            print("Ganaste un Rasuradora")
        if bolita==5:
            print("Ganaste un Sudadera")
    else:
        print("Opción invalida, oportunidad perdida")
elif genero==2:
    bolita=int(input("Selecciona una bolita de 1 al 5:"))
    if bolita>0 and bolita<6:
        if bolita==1:
            print("Ganaste un Loción")
        if bolita==2:
            print("Ganaste un Bikini")
        if bolita==3:
            print("Ganaste un Crema p/la cara")
        if bolita==4:
            print("Ganaste un Plancha")
        if bolita==5:
            print("Ganaste un Barniz de uñas")
    else:
        print("Opción invalida, oportunidad perdida")
else:
    print("Opción invalida, oportunidad perdida")