lista1 = [3,8,5,2,8,6]
lista2 = [3,8,10]
diferencia = []

for buscado in lista1:
    existe = False
    for x in lista2:
        if x == buscado:
            existe = True

    if not existe:
        diferencia.append(buscado)

print("Números en la segunda lista no existentes en la primera")
print("Cantidad",len(diferencia))
print("Lista",diferencia)
