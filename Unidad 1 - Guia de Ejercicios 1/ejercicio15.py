#crear programa que dado numero positivo vea los divisores que tiene

acumulador = 0

dato_leido = input('Introduce un numero: ')
if dato_leido.isdigit():
    numero = int(dato_leido)
    if numero > 0:
        for i in range(1,numero+1):
            if numero % i == 0:
                #numero = numero // 2
                acumulador = i 
                #if numero // numero:
                    #total = acumulador
                print(acumulador)
                
    else:
        print('El dato debe ser mayor a 0')
else:
    print('El dato es incorrecto')   


    # if numero == 1:
    #     print(f'El {numero} SI es potencia de 2')
        