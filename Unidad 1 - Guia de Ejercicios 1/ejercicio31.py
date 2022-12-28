

for i in range(1,1000):
    suma_cubos = 0

    for digito in str(i): #el doble for recorre cada uno de los digitos...
        cubo_digito = int(digito) ** 3
        suma_cubos += cubo_digito
    
    if suma_cubos == i:
        print(i)

