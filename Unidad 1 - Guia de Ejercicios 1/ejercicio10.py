#programa que lea un numero e invierta sus digitos
#no se leen letras

# num = 73
# auxnum = num % 10
# print(auxnum)
resultado = 0

dato_leido = input('Introduce un número: ')
if dato_leido.isdigit():
    numero = int(dato_leido)

    while numero >0:
        resultado = resultado * 10 + numero % 10
        numero = numero // 10
    print(f'El numero con las cifras invertidas de {dato_leido} es {resultado}')

    #forma simplificada pero NO correcta
    # for i in range(len(dato_leido)-1,-1,-1):
    #     print(dato_leido[i], end="",)

else:
    print('El dato introducido no es correcto')



