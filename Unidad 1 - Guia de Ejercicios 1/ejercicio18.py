#programa que cuente cada una de vocales que hay en la palabra

vocales = 'aeiou'
palabra = ''
cuent_a = 0
cuent_e = 0
cuent_i = 0
cuent_o = 0
cuent_u = 0

dato_leido = input('Escriba una palabra: ')
palabra = str(dato_leido)

if palabra.isdigit():
    numero = int(palabra)
    print('El programa no acepta numeros, solo palabras')

elif isinstance(palabra,str):
    for letra in palabra: #se recorre los elementos en de la variable
        for vocal in vocales:
            if letra == vocal and vocal == 'a':
                cuent_a = cuent_a + 1
            if letra == vocal and vocal == 'e':
                cuent_e = cuent_e + 1
            if letra == vocal and vocal == 'i':
                cuent_i = cuent_i + 1
            if letra == vocal and vocal == 'o':
                cuent_o = cuent_o + 1
            if letra == vocal and vocal == 'u':
                cuent_u = cuent_u +1

    print(f'{cuent_a} a')
    print(f'{cuent_e} e')
    print(f'{cuent_i} i')
    print(f'{cuent_o} o')
    print(f'{cuent_u} u')
