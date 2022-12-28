#escribir programa que lea num positivo y mostrar por pantalla los 20 primeros
#multiplos del numero
#verificar dato leido correcto
# numero mayor o igual a 0
#y la salida debe ser tabulada en 4 filas de 5 multiplos c/d una
auxnum = 0
dato_leido = input('introduzca un número: ')
if dato_leido.isdigit():
    numero = int(dato_leido)

    for i in range(1,21):
        auxnum = numero * i
        print(f'{auxnum:5d}', end=' ')
        if i % 5 == 0:
            print()
else:
    print('Dato incorrecto')
