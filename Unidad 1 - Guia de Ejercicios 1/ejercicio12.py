#programa que lea un periodo de tiempo:
# dias. horas. minutos. segundos
#y muestre  los segundos totales de ese periodo de tiempo indicado

segundos = 0
continuar = 's'
while continuar == 's':

    dato_dias = input('Introduzca el numero de días: ')
    if dato_dias.isdigit():
        num_dias = int(dato_dias)
        segundos = num_dias * 24 * 60 * 60

    else:
        print('ERROR! El dato es Incorrecto 🚫')
        

    dato_horas = input('Introduce el numero de horas: ')
    if dato_horas.isdigit():
        num_horas = int(dato_horas)
        segundos = segundos + num_horas * 60 * 60

    else:
        print('ERROR! El dato es Incorrecto 🚫')
            

    dato_minutos = input('Introduzca el numero de minutos: ')
    if dato_minutos.isdigit():
        num_min = int(dato_minutos)
        segundos = segundos + num_min * 60
    
    else:
        print('ERROR! El dato es Incorrecto 🚫')
        
    
    dato_seg = input('Introduzca el numero de segundos: ')
    if dato_seg.isdigit():
        num_seg = int(dato_seg)
        segundos = segundos + num_seg
        print('El numero total de segundos es:', segundos)
        
        continuar = input('¿Desea volver a intentarlo? s/n: ')


