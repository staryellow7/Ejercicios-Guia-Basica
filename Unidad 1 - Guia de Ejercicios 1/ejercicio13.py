# ejercicio 12 pero con formato de entrada será: dd:hh:mm:ss

continuar = 's'
while continuar == 's':
    dato_leido = input('Introduzca el período de tiempo a convertir: dd:hh:mm:ss ')
    f_dias = dato_leido.index(':') #buscando el signo
    f_horas = dato_leido.index(':',f_dias +1)
    f_min = dato_leido.index(':',f_horas +1)

    dias = int(dato_leido[:f_dias]) #slice
    horas = int(dato_leido[f_dias +1:f_horas])
    minutos = int(dato_leido[f_horas +1:f_min])
    segundos = int(dato_leido[f_min +1:])

    total_segundos = dias *24 *60 *60 + horas *3600 + minutos *60 + segundos
    print('El total de segundos del período indicado es:', total_segundos)
    continuar = input('¿Deseas reproducir el programa de nuevo? s/n: ')