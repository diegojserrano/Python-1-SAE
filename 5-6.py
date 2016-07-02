conjunto1 = {3,8,5,2,8,6}
conjunto2 = {3,8,10}
interseccion = set()

for buscado in conjunto2:
    if buscado in conjunto1:
        interseccion.add(buscado)

print (interseccion)