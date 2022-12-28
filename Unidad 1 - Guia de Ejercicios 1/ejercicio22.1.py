#crear otro programa adivina el numero

import random
continuar = 's'

while continuar == 's':
    x = random.randint(1,25)
    print(x)
    contador = 0

    while contador < 10:
        dato_leido = input('Introduce un numero para adivinar el numero: ')
        if dato_leido.isdigit():
            numero = int(dato_leido)
            contador = contador + 1
        else:
            print('dato no reconocido')

        if numero == x:
            print('Adivinaste el numero en el intento',contador)
            break
    else:
        print('No adivinaste el numero, este era:', x)
    continuar = input('Volver a jugar? s/n: ')


