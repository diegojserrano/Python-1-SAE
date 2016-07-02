
#Carga de la lista
listaNumeros = []
n = int(input("Ingrese un número "))

while n != 0:
    listaNumeros.append(n)
    n = int(input("Ingrese un número "))

print(listaNumeros)

#Conteo de positivos y negativos
c_positivos = c_negativos = 0
for numero in listaNumeros:
    if numero > 0:
        c_positivos += 1
    else:
        c_negativos += 1

#Conteo de pares
c_pares = 0
for numero in listaNumeros:
    if numero % 2 == 0:
        c_pares += 1

#Promedio
ac = 0
for numero in listaNumeros:
    ac += numero

promedio = ac / len(listaNumeros)

#Busqueda del 5
#Variante 1
paso_un_5 = False
for numero in listaNumeros:
    if numero == 5:
        paso_un_5 = True
#Variante 2
if listaNumeros.count(5) > 0:
    paso_un_5 = True
#Variante 3
    paso_un_5 = 5 in listaNumeros


#Resultados
print("Cantidad de positivos:",c_positivos)
print("Cantidad de negativos:",c_negativos)
print("Promedio:",promedio)
print("Cantidad de pares:",c_pares)
if paso_un_5:
    print("SÍ se ingresó un 5")
else:
    print("NO se ingresó un 5")
