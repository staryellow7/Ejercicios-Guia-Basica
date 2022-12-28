#crear programa qur lea un numero positivo y muestre la secuencia de Collatz

dato_leido = input('Introduce un numero: ')
if dato_leido.isdigit():
    numero = int(dato_leido)

    if numero > 0:
        while numero != 1:
            if numero % 2 == 0:
                numero = numero // 2
                print(numero)
            if numero % 2 == 1:
                #print(numero)
                if numero == 1:
                    break
                else:
                    numero = numero * 3 + 1
                    print(numero)

else:
    print('El dato es incorrecto')