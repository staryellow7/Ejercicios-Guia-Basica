#programa que pide 2 palabras y diga cual es la mas larga
#y muestre el trozo de string en que se diferencia

contador = 0
contador2 = 0

primer_palabra = input('Introduzca una palabra: ')
segunda_palabra = input('Introduzca una segunda: ')

for num in range(len(primer_palabra)):
    contador = contador +1

for nletra in range(len(segunda_palabra)):
    contador2 = contador2 +1

print(f'{primer_palabra} tiene {contador}')
print(f'{segunda_palabra} tiene {contador2}')

if len(primer_palabra) == len(segunda_palabra):
    print(f'por tanto {primer_palabra} y {segunda_palabra} tienen la misma longitud')

elif len(primer_palabra) > len(segunda_palabra):
    diferencia = primer_palabra [len (segunda_palabra) - len (primer_palabra):]
    print(f'por tanto {primer_palabra} es mas larga')

    print(f'El string en el que difieren es: {diferencia}')

else:
    diferencia = segunda_palabra [len (primer_palabra) - len (segunda_palabra):]
    print(f'por tanto {segunda_palabra} es mas larga')

    print(f'El string en el que difieren es: {diferencia}')
