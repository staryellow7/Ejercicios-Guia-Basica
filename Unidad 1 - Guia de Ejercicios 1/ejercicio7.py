#crear programa que verifique si un numero en potencia de 2 es o no potencia de 2
#todos los numeros en potencia de 2 son pares y divisibles entre 2

continuar = 's'
while continuar == 's':
    dato_leido = input('Ingrese numero: ')
    if dato_leido.isdigit():
        numero = int(dato_leido)
        
        if numero > 0:
            while numero % 2 == 0:
                numero = numero // 2

            if numero == 1:
                print(f'El {dato_leido} SI es potencia de 2')
                
            else:
                print(f'El {dato_leido} NO es potencia de 2')
                    

        else:
            print('El numero debe ser mayor a 0')

    else:
        print('El dato introducido no es un numero')
    continuar = input('¿Desea continuar con el programa? s/n: ')