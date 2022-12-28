#programa palindronoma

espacio = " "
palabra_inversa = ""
palabra_noinversa = ""

dato_leido = input('Introduzca una frase: ')
dato_leido = dato_leido.lower()
nuevo_dato = dato_leido.replace(espacio,'')
#print(nuevo_dato)

for i in range(len(nuevo_dato)-1,-1,-1):
    palabra_inversa = nuevo_dato[i]
    palabra_inversa = palabra_inversa.lower()
    print(palabra_inversa, end="")
print()
    
for i in range(len(nuevo_dato)):
    palabra_noinversa = nuevo_dato[i]
    palabra_noinversa = palabra_noinversa.lower()
    print(palabra_noinversa, end="")
print()
if palabra_inversa == palabra_noinversa:
    print('La frase es PALÍNDROME')
else:
    print('La frase NO es Palíndrome')
 

