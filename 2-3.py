a = int(input("Ingrese un numero"))
b = int(input("Ingrese un numero"))
c = int(input("Ingrese un numero"))

if a > b and a > c:
    mayor = a
elif b > c:
    mayor = b
else:
    mayor = c

print("El mayor es:", mayor)