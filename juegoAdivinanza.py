import random

# numero_secreto = random.randint(1,21) # busca un nº entre 1 y 20
# adivinado = False
# intentos_max = 5
# intentos = 0

# print('Bienvenido a ADIVINÁ EL NÚMERO!')

# while not adivinado:
#     numero = input('Introducí un nº del 1 al 20:  ') 
#     numero_int = int(numero)
#     intentos += 1
#     if intentos == intentos_max:
#         print('te quedaste sin intentos')
#         break
#     if numero_int == numero_secreto:
#         adivinado = True
#         print('adivinasteeeee!!!!  FELICITACIONES 🎈🎈🎈🎈')
#     elif numero_int < numero_secreto:
#         print ('sssss...pista. Es un número más alto')
#     else:
#         print ('nono. Es un número más bajo')
        

# otra versión con mismo resultado

numero_secreto = random.randint(1,21) # busca un nº entre 1 y 20
adivinado = False
intentos_max = 5
intentos = 0

print('Bienvenido a ADIVINÁ EL NÚMERO!')

while not adivinado and intentos < intentos_max:
    numero = input('Introducí un nº del 1 al 20:  ') 
    numero_int = int(numero)
    if numero_int == numero_secreto:
        adivinado = True
        print('adivinasteeeee!!!!  FELICITACIONES 🎈🎈🎈🎈')
    elif numero_int < numero_secreto:
        print ('sssss...pista. Es un número más alto')
    else:
        print ('nono. Es un número más bajo')
    
    intentos += 1

if intentos == intentos_max:
    print('te quedaste sin intentos')