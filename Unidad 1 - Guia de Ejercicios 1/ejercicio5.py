#programa que lea un numero mayor o igual a 1
# mostrar por pantalla la potencia de 2 de un numero dado
#verificar entrada no se aceptan letras
auxnum = 0
resultado = 0
continuar = 's'

while continuar == 's':
    dato_leido = input('Escribe un numero: ')
    if dato_leido.isdigit():
        numero = int(dato_leido)
        if numero >=1:
            for i in range(numero):
                auxnum = auxnum + 1
                resultado = 2 ** i
                #print(i, auxnum, resultado)
                print(resultado)
        else:
            print('El numero debe ser mayor a 0')
    else:
        print('El dato es incorrecto')
    continuar = input('¿Desea continuar con el programa? s/n: ')