#crear un programa que determine si el año es bisiesto o no

por_4 = 0
por_100 = 0
por_400 = 0

dato_leido = input('Introduzca un numero: ')
if dato_leido.isdigit():
    numero = int(dato_leido)
    
    if numero >0:
        if numero % 4 == 0 or numero % 100 == 0 or numero % 400 == 0:
            # por_4 = numero
            print('El año' ,numero, 'SI es bisiesto') #x4

            # if por_4 % 100 == 0:
            #     por_100 = por_4
            #     print('El año' ,numero, 'SI es bisiesto') # x100

            #     if por_100 % 400 == 0:
            #         por_400 = por_100
            #     print('El año' ,numero, 'SI es bisiesto') #x400
                
        else:
            print('El año',numero, 'NO es bisiesto')
else:
    print('El valor introducido no es correcto')

