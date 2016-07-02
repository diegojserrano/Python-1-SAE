lista1 = [3,8,5,2,8,6]
lista2 = [3,8,10]

for buscado in lista2:
    existe = False
    for x in lista1:
        if x == buscado:
            existe = True

    if existe == True:
        print(buscado, "Existe")
    else:
        print(buscado, "No existe")

