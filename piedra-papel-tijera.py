nombre1 = input('Nombre jugador 1 ').lower()
nombre2 = input('Nombre jugador 2 ').lower()


jugador1 = input(f'{nombre1.title()}. ¿Qué elegís? ¿piedra, papel o tijera? ')
jugador2 = input(f'{nombre2.title()}. ¿Qué elegís? ¿piedra, papel o tijera? ')

if jugador1 == jugador2:
    print('Empate')
elif (jugador1 == 'piedra' and jugador2 == 'tijera') or (jugador1 == 'papel' and jugador2 == 'priedra') or (jugador1 == 'tijera' and jugador2 == 'papel'):
    print(f'{nombre1.title()} GANASTEEEEE!!!')
else:
    print(f'ganaste {nombre2.title()}!!!')