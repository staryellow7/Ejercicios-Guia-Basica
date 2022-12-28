#programa que lea e imprima por pantalla el num de digitos
#de un numero sea positivo o negativo
#checar comprobaciones
#todos los contadores o almacenadors deben inicializarse en el
#bucle para que se reinicie y no se almacenen
#contador = 0
auxnum = 0
signo = '-'
continuar = 's'

while continuar == 's':
    contador = 0

    dato_leido = input('Escribe un numero: ')
    dato_leido = dato_leido.strip(signo)
        
    if dato_leido.isdigit():
        numero = int(dato_leido)
        auxnum = numero
        
        while numero > 0:
            numero = numero // 10
            contador = contador + 1
        print(f'El numero {auxnum} tiene {contador} digitos') 
        continuar = input('Desea continuar con el programa s/n: ')   

    else:
        print('El programa solo acepta números: ')

