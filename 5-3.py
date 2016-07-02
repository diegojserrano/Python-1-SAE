lista1 = [3,8,5,2,8,6]
lista2 = [3,8,10]
interseccion = []

for buscado in lista2:
    existe = False
    for x in lista1:
        if x == buscado:
            existe = True

    if existe:
        interseccion.append(buscado)

print("Cantidad de repetidos",len(interseccion))
print("Lista de repetidos",interseccion)
