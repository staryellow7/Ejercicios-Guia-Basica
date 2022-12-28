#crea un programa que pida un rango de numeros y muestre los numeros primos

dato_leido = input('Introduce un numero inicial: ')
dato_leido2 = input('Introduce un numero final: ')
if dato_leido.isdigit() and dato_leido2:
    numero,numero2 = int(dato_leido), int(dato_leido2)

    if numero > 0 and numero2 >0:
        for rango in range(numero,numero2+1):
            es_primo = True

            for divisor in range(2,rango):
                if rango % divisor == 0:
                    es_primo = False
                    break
                
            if es_primo:
                print(f'{rango}')
        # else:
        #     print(f'{numero} no es primo')    

    else:
        print('El numero debe ser mayor a 0')
else:
    print('El programa no acepta letras')