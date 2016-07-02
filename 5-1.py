lista1 = [3,8,5,2,8,6]

buscado = int(input("Ingrese el número a buscar"))

existe = False
for x in lista1:
    if x == buscado:
        existe = True

if existe == True:
    print("Existe")
else:
    print("No existe")

