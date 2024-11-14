#validate user input exercie

# 1. username is no more than 12 characteres 
# 2. username must not contain spaces
# 3. username must not cotain digits

username = input("Ingresa un nombre de usuario: ")

spaces = username.isalpha()

if len(username) > 12:
    print("La longitud no debe sobrepasar los 12 caracteres")
elif username.count(" ") !=0:
    print("The username cannot contain spaces")
elif username.isalpha() == False:
    print("The username cannot contain digits")
else:
    print("Usuario aceptado")

