 #crear programa que lea una frase lea una frase y escriba 
 # el numero de vocales que tiene

vocales = 'aeiou'
palabra = ''
contador = 0

dato_leido = input('Escriba una palabra: ')
palabra = str(dato_leido)

if palabra.isdigit():
    numero = int(palabra)
    print('El programa no acepta numeros, solo palabras')

elif isinstance(palabra,str):
    for letra in palabra: #se recorre los elementos en de la variable
        for vocal in vocales:
            if letra == vocal:
                contador = contador + 1
    print(f'La frase {palabra} tiene {contador} vocales')

# elif palabra.isdigit():
#     numero = int(palabra)
# print('El programa no acepta numeros, solo palabras')