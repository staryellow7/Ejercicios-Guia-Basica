#crear programa que genere un numero entre 1y10
#luego de 5 opciones para adivinarlo
#si se adivina  debe mostrarse el numero y en cuantos intentos se realizo
#si no se adivino sale un msj que no se adivino y del numero

import random

continuar = 's'
while continuar == 's':
    x = random.randint(1,10) #se guarda en una variable el numero aleatorio
    print(x)
    contador = 0

    while contador < 5:
        dato_leido = input('Introduzca numero del intento:')
        if dato_leido.isdigit():
            numero = int(dato_leido)
            contador = contador + 1 #incremento hasta 5
        else:
            print('Dato invalido')

        if numero == x: #si numero añadido es igual a la variable numero random
            print(f'adivinaste el numero en el intento {contador}')
            break

    else:
        print(f'No adivinaste el numero, este era el {x}')
    continuar = input('Volver a jugar? s/n: ')




