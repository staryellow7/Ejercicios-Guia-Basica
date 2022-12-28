#crear programa que determine si un numero es primo o no
#validar datos
#si el numero es menor a 2 NO ES PRIMO
dato_leido = input('Introduce un numero: ')
if dato_leido.isdigit():
    numero = int(dato_leido)
    es_primo = True

    if numero > 0:

        if numero < 2:
            es_primo = False
        
        else:
            es_primo == es_primo
            for i in range(2,numero):
                if numero % i == 0:
                    es_primo = False
                    break
                
        if es_primo:
            print(f'{numero} es un numero primo')
        else:
            print(f'{numero} no es primo')    
    else:
        print('El numero debe ser mayor a 0')

else:
    print('El programa no acepta letras')