#escribir programa fibonacci que dado un numero muestre la posicion
#que llegue al numero fibonacci en consecuccion

continuar = 's'
while continuar == 's':
    num1 = 0 #las variables a usar deben estar dentro del while
    num2 = 1 #si no se acumularan junto con la anterior operacion
    num3 = 0
    dato_leido = input('Introduzca un numero: ')
    if dato_leido.isdigit():
        num = int(dato_leido)
        print(0)
        
        for i in range(num):
            num1 = num2
            num2 = num3
            num3 = num1 + num2
            print(num3)
        continuar = input('¿Desea continuar con el programa? s/n: ')     
    else:
        print('El programa solo acepta numeros positivos')



    