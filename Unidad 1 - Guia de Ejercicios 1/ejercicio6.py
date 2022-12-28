#del ejercicio 4 hacer lo mismo pero sumando todos los elementos salidos
resultado = 0
sumatoria = 0
continuar = 's'

while continuar == 's':
    dato_leido = input('Ingrese numero: ')
    if dato_leido.isdigit():
        numero = int(dato_leido)

        if numero >= 1:  
            for i in range(numero):
                resultado = 2 ** i        
                sumatoria = sumatoria + resultado
                #print(i, resultado, sumatoria)
                print(sumatoria)
            
        else:
            print('El numero debe ser mayor a 0')

    else:
        print('El dato introducido no es un numero')
    continuar = input('¿Desea continuar con el programa? s/n: ')