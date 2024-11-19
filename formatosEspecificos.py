#formatos especificos = {: banderas} foramtea un valor en base a la bandera insertada

# (numero)f redondear a esa cantidad de decimales (punto fijo)
# (number) asignar y rellenar con ceros
# 03  asignar y rellenar con ceros esa cantidad de espacios
# < justificacion a la izquierda
# > justificacion a la derecha 
# ^ centrar 
# + para indicar un valor positivo
# = coloca el cartel en la posición más a la izquierda
# , separador de coma

precio1 = 3.991646
precio2 = -15.3465345
precio3 = 15

print(f"el precio del producto 1 es ${precio1:.3f}")
print(f"el precio del producto 2 es ${precio2:^3}")
print(f"el precio del producto 2 es ${precio2:<3}")
print(f"el precio del producto 2 es ${precio2:>3}")