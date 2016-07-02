c = 0
ac = 0
mayor = menor = 0
nombre_mayor = nombre_menor= ""
for i in range(5):
    print("Articulo",i+1)
    nombre = input("Ingrese el nombre ")
    precio = int(input("Ingrese el precio "))

    if precio < 50:
        c += 1
    ac += precio
    if precio > mayor:
        mayor = precio
        nombre_mayor = nombre

    if precio < menor or i == 0:
        menor = precio
        nombre_menor = nombre

promedio = ac / 5

print("El promedio de precios es:",promedio)
print("Hay",c,"artículos con precio inferior a $50")
print("El artículo más caro es:", nombre_mayor)
print("El artículo más barato es:", nombre_menor)
