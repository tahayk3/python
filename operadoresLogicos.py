#Operadores logicos = evaluan multiples condiciones (or, and, not)
    #or = una de las condiciones debe ser True
    #and ambas condiciones deben ser True
    #not = invierte una condicion

temp = 25 
is_raining = False
if temp > 40 or temp < 0 or is_raining:
    print("El evento ha sido cancelado debito a las temperaturas extremas")
else:
    print("El evento sigue en marcha")