#leer un numero mayor o igual a 0
#mostrar por pantalla el resultado de calcular el factorial del numero
#no se permiten letras 

auxnum = 1
dato_leido = input('Introduzca un número: ')
if dato_leido.isdigit():
    numero = int(dato_leido)

    if numero == 0:
        print(1)

    else: 
        if numero >= 1:
        #operacion facotrial
            for i in range(numero,1,-1): 
                #print(i)
                auxnum = auxnum * i #30
            print(auxnum)
        else:
            print('El numero debe ser mayor a 0')

else:
    print('El dato introducido no es un número')