# dado un numero decimal sea positivo o negativo obtener solo la parte decimal e imprimir
# por pantalla
# verficicar numero

# numero = -100.25
# auxnum = numero *-1
# auxnum1 = auxnum % 1
# print('La parte decimal de', numero, 'es', auxnum1)
# auxnum = 
continuar = 's'
while continuar == 's':
    dato_leido = input('Introduce un número decimal: ')
    #numero = float(dato_leido)

    if dato_leido.isdigit():
        print('Debes introducir un numero mayor a 0 con punto flotante')
    
    else:
        numero = float(dato_leido) 
        if isinstance(numero,float):
            #print('dato valido')
            if numero < 0: #numero negativo
                auxnum = numero
                auxnum1 = auxnum * -1 #convierte a positivo
                #print(auxnum,'numero_negativo')
                auxnum2 = auxnum1 % 1
                print('La parte decimal del numero es: {:.2f}'.format(auxnum2))

            elif numero > 0: #numero positivo
                auxnum3 = numero *1
                auxnum4 = auxnum3 % 1
                print('La parte decimal del numero es: {:.2f}'.format(auxnum4))    
                
    continuar = input('¿Deseas volver a intentarlo? s/n: ')




# if numero.isdigit():
#     print('dato invalido')
# else:
#     print(numero)


# else:   
#     try:
#         decimal = float(dato_leido)
#         print(decimal)

#     except AttributeError:
#         print('datoinvalido1')

