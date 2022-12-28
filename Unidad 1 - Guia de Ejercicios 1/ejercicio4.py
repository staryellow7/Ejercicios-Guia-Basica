#escribir programa que dado un numero (validado) muestre si es o no fibonacci

continuar = 's'
while continuar == 's':
    dato_leido = input('Introduce un numero: ')
    if dato_leido.isdigit():
        numero = int(dato_leido)
        auxnum = 0
        num1 = 0
        num2 = 1
        if numero >1:
            while num1 < numero and num2 < numero:
                num3 = num1
                num1 = num2
                num2 = num3 + num2
                auxnum = num2  

            if auxnum == numero:
                print(f'El número {numero} SI es un numero Fibonacci')

            else:
                print(f'El número {numero} NO es un numero Fibonacci')
            continuar = input('Desea continuar con el programa: s/n ') 

        else:
            print('El numero debe ser mayor a 1')  
    else:
        print('El dato introducido es incorrecto')
      


