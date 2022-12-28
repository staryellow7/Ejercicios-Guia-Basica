#conversor de unidades de longitud
#se lea un numero decimal, unidad inicial(km,hm,dam,m...), unidad de destino
# se validan las entradas: NO LETRAS, numero MAYOR A 0

# valor_inicial = 'km,hm,dam,m,dm,cm,mm'
# valor_final = 'km,hm,dam,m,dm,cm,mm'
auxnum = float(0)

dato_leido = input('Introduzca un numero: ')
if dato_leido.isdigit() or float(dato_leido):
    numero = float(dato_leido)

    if numero > 0:
        valor_inicial = input('Elige una medida: Km Hm Dam M Dm Cm Mm: ')
        valor_final = input('Elige la medida de destino: Km Hm Dam M Dm Cm Mm: ')

                    ###### convetir km a :
        if valor_inicial == 'km':
            if valor_final == 'km':
                print(f'No existe conversion, el {numero} es igual')

            if valor_final == 'hm':
                auxnum = numero * 10
                print(f'{numero} km son {auxnum} hm')
            
            if valor_final == 'dam':
                auxnum = numero * 100
                print(f'{numero} km son {auxnum} dam')

            if valor_final == 'm':
                auxnum = numero * 1000
                print(f'{numero} km son {auxnum} m')

            if valor_final == 'dm':
                auxnum = numero * 10000
                print(f'{numero} km son {auxnum} dm')
            
            if valor_final == 'cm':
                auxnum = numero * 100000
                print(f'{numero} km son {auxnum} cm')
            
            if valor_final == 'mm':
                auxnum = numero * 1000000
                print(f'{numero} km son {auxnum} mm')


                ###### convetir hm a :
        if valor_inicial == 'hm':
            if valor_final == 'hm':
                print(f'No existe conversion, el {numero} es igual')

            if valor_final == 'km':
                auxnum = numero / 10
                print(f'{numero} hm son {auxnum} km')
            
            if valor_final == 'dam':
                auxnum = numero * 10
                print(f'{numero} hm son {auxnum} dam')

            if valor_final == 'm':
                auxnum = numero * 100
                print(f'{numero} hm son {auxnum} m')

            if valor_final == 'dm':
                auxnum = numero * 1000
                print(f'{numero} hm son {auxnum} dm')
            
            if valor_final == 'cm':
                auxnum = numero * 10000
                print(f'{numero} hm son {auxnum} cm')
            
            if valor_final == 'mm':
                auxnum = numero * 100000
                print(f'{numero} hm son {auxnum} cm')
            
                   ###### convetir dam a :
        if valor_inicial == 'dam':
            if valor_final == 'dam':
                print(f'No existe conversion, el {numero} es igual')

            if valor_final == 'km':
                auxnum = numero / 100
                print(f'{numero} dam son {auxnum} km')
            
            if valor_final == 'hm':
                auxnum = numero / 10
                print(f'{numero} dam son {auxnum} hm')

            if valor_final == 'm':
                auxnum = numero * 10
                print(f'{numero} dam son {auxnum} m')

            if valor_final == 'dm':
                auxnum = numero * 100
                print(f'{numero} dam son {auxnum} dm')
            
            if valor_final == 'cm':
                auxnum = numero * 1000
                print(f'{numero} dam son {auxnum} cm')
            
            if valor_final == 'mm':
                auxnum = numero * 10000
                print(f'{numero} dam son {auxnum} mm')

        ###### convetir metros a :
        if valor_inicial == 'm':
            if valor_final == 'm':
                print(f'No existe conversion, el {numero} es igual')

            if valor_final == 'km':
                auxnum = numero / 1000
                print(f'{numero} m son {auxnum} km')
            
            if valor_final == 'hm':
                auxnum = numero / 100
                print(f'{numero} m son {auxnum} hm')

            if valor_final == 'dam':
                auxnum = numero / 10
                print(f'{numero} m son {auxnum} dam')

            if valor_final == 'dm':
                auxnum = numero * 10
                print(f'{numero} m son {auxnum} dm')
            
            if valor_final == 'cm':
                auxnum = numero * 100
                print(f'{numero} m son {auxnum} cm')
            
            if valor_final == 'mm':
                auxnum = numero * 1000
                print(f'{numero} m son {auxnum} cm')
        
         ###### convetir dm a :
        if valor_inicial == 'dm':
            if valor_final == 'dm':
                print(f'No existe conversion, el {numero} es igual')

            if valor_final == 'km':
                auxnum = numero / 10000
                print(f'{numero} dm son {auxnum} km')
            
            if valor_final == 'hm':
                auxnum = numero / 1000
                print(f'{numero} dm son {auxnum} hm')

            if valor_final == 'dam':
                auxnum = numero / 100
                print(f'{numero} dm son {auxnum} dam')

            if valor_final == 'm':
                auxnum = numero / 10
                print(f'{numero} dm son {auxnum} m')
            
            if valor_final == 'cm':
                auxnum = numero * 10
                print(f'{numero} dm son {auxnum} cm')
            
            if valor_final == 'mm':
                auxnum = numero * 100
                print(f'{numero} dm son {auxnum} cm')
        
        ###### convetir centimetros a :
        if valor_inicial == 'cm':
            if valor_final == 'cm':
                print(f'No existe conversion, el {numero} es igual')

            if valor_final == 'km':
                auxnum = numero / 100000
                print(f'{numero} cm son {auxnum} km')
            
            if valor_final == 'hm':
                auxnum = numero / 10000
                print(f'{numero} cm son {auxnum} hm')

            if valor_final == 'dam':
                auxnum = numero / 1000
                print(f'{numero} cm son {auxnum} dam')

            if valor_final == 'm':
                auxnum = numero / 100
                print(f'{numero} cm son {auxnum} m')
            
            if valor_final == 'dm': ####
                auxnum = numero / 10
                print(f'{numero} cm son {auxnum} dm')
            
            if valor_final == 'mm':
                auxnum = numero * 10
                print(f'{numero} cm son {auxnum} mm')
        
        ###### convetir milimetros a :
        if valor_inicial == 'mm':
            if valor_final == 'mm':
                print(f'No existe conversion, el {numero} es igual')

            if valor_final == 'km':
                auxnum = numero / 1000000
                print(f'{numero} mm son {auxnum} km')
            
            if valor_final == 'hm':
                auxnum = numero / 100000
                print(f'{numero} mm son {auxnum} hm')

            if valor_final == 'dam':
                auxnum = numero / 10000
                print(f'{numero} mm son {auxnum} dam')

            if valor_final == 'm':
                auxnum = numero / 1000
                print(f'{numero} mm son {auxnum} m')
            
            if valor_final == 'dm': 
                auxnum = numero / 100
                print(f'{numero} mm son {auxnum} dm')
            
            if valor_final == 'cm':
                auxnum = numero / 10 
                print(f'{numero} mm son {auxnum} cm')

    else:
        print('El numero debe ser mayor a 0')
else:
    print('El valor introducido es incorrecto')