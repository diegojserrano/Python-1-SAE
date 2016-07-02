n = int(input("Ingrese un número "))
cp = cn = 0
c = ac = 0
cpares = 0
paso_un_5 = False

while n != 0:

    if n > 0:
        cp += 1
    else:
        cn += 1
    ac += n
    c += 1
    if n % 2 == 0:
        cpares += 1
    if n == 5:
        paso_un_5 = True

    n = int(input("Ingrese un número "))

promedio = ac / c

print("Cantidad de positivos:",cp)
print("Cantidad de negativos:",cn)
print("Promedio",promedio)
print("Cantidad de pares:",cpares)
if paso_un_5:
    print("Se ingresó un 5 al menos una vez")
else:
    print("No se ingresó nunca el 5")
