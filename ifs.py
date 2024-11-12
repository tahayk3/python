# los ifs son condicionales que permiten ejecutar o no cierto bloque de codigo, en el caso de que la condicion en el if se cumpla

money = float(input("Ingresa una cantidad"))

if money >= 9000:
    print("La transferencia supera el monto limite permitido")
elif money <9000 and money >0:
    print("Transferencia valida")
else:
    print("ingrese un dato valido")