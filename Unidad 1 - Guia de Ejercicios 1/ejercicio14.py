#programa que lea un periodo de tiempo en segundos
# y muestre el numero de dias, horas, minutos y segundos
dias = 0
horas = 0
minuto = 0
segundos = 0
total = 0
dato_leido = input('Introduzca el número de segundos: ')
if dato_leido.isdigit():
    segundos = int(dato_leido)

    meses = segundos // 2592000
    segundos = segundos % 2592000
    dias = segundos // 86400
    segundos = segundos % 86400
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    print(f'{meses} meses, {dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos')


else:
    print('Este programa solo acepta números')
