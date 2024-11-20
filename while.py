#while loop = ejecuta algun codigo hasta que alguna condicion cambie de valor 

#nombre = ""
#while nombre == "":
#    print("Ingrese un nombre valido")
#    nombre = input("Ingrese su nombre")
#else:
#    print("Nombre ingresado :D")

number = int(input("Ingrese un numero entre 1 y 10: "))

while number < 1 or number >10:
    print("error")
    number = int(input("Ingrese un numero entre 1 y 10: "))

print("Numero ingresado correctamente")


