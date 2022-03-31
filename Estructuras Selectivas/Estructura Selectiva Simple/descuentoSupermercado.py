#Se necesita un sistema para un supermercado, 
#en el cual si el monto de la compra del cliente 
#es mayor de $5000 se le hará un descuento del 30%, 
#si es menor o igual a $5000 pero mayor que $3000 
#será del 20%, si no rebasa los $3000 pero si los 
#$1000 la rebaja efectiva es del 10% y en caso de 
#que no rebase los $1000 no tendrá beneficio.

monto=float(input("Ingresa el monto:"))

if monto<=1000:
    print("Debes pagar:",monto)
elif monto <=3000:
    descuento=(monto*10)/100
    print("Debes pagar:",monto-descuento)
elif monto<=5000:
    descuento=(monto*20)/100
    print("Debes pagar:",monto-descuento)
else:
    descuento=(monto*30)/100
    print("Debes pagar:",monto-descuento)