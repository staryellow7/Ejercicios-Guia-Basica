# crear programa que lea un numero positivo
# muestre el numero magico

resultado = 0
dato_leido = input('Introduce un numero: ')
if dato_leido.isdigit():
    numero = int(dato_leido)

    if numero > 0:
        auxnum = numero
        while numero != 1:
            if numero % 2 == 0:
                numero = numero // 2
                print(numero)
                resultado = resultado + numero
            if numero % 2 == 1:
                if numero == 1:
                    #resultado = resultado + numero
                    if resultado == auxnum:
                        print(f'{auxnum} es numero mágico')
                    else:
                         print(f'{auxnum} NO es numero mágico')   
                else:
                    numero = numero // 3 * 2
                    resultado = resultado + numero
                    print(numero)
                



    else:
        print('El numero debe ser mayor a 0')

else:
    print('El dato leido no es un numero')