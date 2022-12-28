#escribir programa fibonacci que dado un numero muestre la posicion
#que llegue al numero fibonacci en consecuccion

continuar = 's'
while continuar == 's':
    num1 = 0
    num2 = 1
    num3 = 0
    sumatorio = 0
    dato_leido = input('Introduzca un numero: ')
    if dato_leido.isdigit():
        num = int(dato_leido)
        #print(0)
        if num >0:
            for i in range(num):
                num1 = num2
                num2 = num3
                num3 = num1 + num2
                #print(num3)
                sumatorio += num3
            print(sumatorio)
            continuar = input('¿Desea continuar con el programa: s/n ')    
        else:
            print('El numero debe ser mayor a 0')

    else:
        print('El programa solo acepta numeros positivos')

    
