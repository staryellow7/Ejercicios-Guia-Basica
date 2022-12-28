#correo electronico

arroba = '@'
punto = '.'
dato_leido = input('Escribe un correo electronico valido: ')
usuario, dominio = dato_leido.split(arroba)
dominio_nom, extension_dominio = dominio.split(punto)
# print(dato_leido,usuario,dominio)
# print(dominio_nom,extension_dominio)

if usuario[0].isalpha():
    if usuario[1:].isalnum():
        #print(usuario,'usuario valido')
        #print('El Correo Electronico es Valido')
        pass

    if dominio[0].isalpha():
        if dominio[1:].isalnum():
            print(dominio,'dominio valido')

        if len(extension_dominio) >=2 and len(extension_dominio) <=4:
            if extension_dominio[0].isalpha():
                if extension_dominio[1:].isalnum():
                    #print(extension_dominio,'signo valido')
                    print('El Correo Electronico es Valido')
            else:
                print(extension_dominio,'Dato Invalido. La extension de dominio no debe empezar con numero.')
        else:
            print('La extension de dominio debe ser entre 2 y 4')
    else:
        print(dominio_nom,'Dato Invalido. El nombre de dominio no debe empezar con numero.')
        
else:
    print(usuario,'Dato invalido, el usuario no debe empezar con un numero')

# for pos in dato_leido:
#     for pos2 in numero:
#         if pos == pos2:
#             contador = contador + 1

# if contador == 0:
#     acumulador = dato_leido
#     if arroba in acumulador:
#     #acumulador = acumulador + dato_leido
#         print(acumulador)

# if contador >1 and dato_leido[len(numero):]:
#     acumulador = dato_leido
#     if arroba in acumulador:
#         print(acumulador)

# elif contador >1 and dato_leido[:len(numero)]:
#     # acumulador = dato_leido
#     # if arroba in acumulador:
#     print('novalido')

    