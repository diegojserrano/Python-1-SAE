
#Carga de la lista
def cargar(lista):
    n = int(input("Ingrese un número "))

    while n != 0:
        lista.append(n)
        n = int(input("Ingrese un número "))


#Conteo de positivos y negativos
def contar_positivos_negativos(lista):
    c_positivos = c_negativos = 0
    for numero in lista:
        if numero > 0:
            c_positivos += 1
        else:
            c_negativos += 1
    return c_positivos, c_negativos


#Conteo de pares
def contar_pares(lista):
    c_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            c_pares += 1
    return c_pares


#Promedio
def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    ac = 0
    for numero in lista:
        ac += numero

    promedio = ac / len(lista)
    return promedio

#Busqueda del 5
#Variante 1
def existe_5 (lista):
    paso_un_5 = False
    for numero in listaNumeros:
        if numero == 5:
            paso_un_5 = True
    return paso_un_5


listaNumeros = []

cargar(listaNumeros)
cantidad_pares = contar_pares(listaNumeros)
promedio = calcular_promedio(listaNumeros)
paso_5 = existe_5(listaNumeros)
cantidad_positivos, cantidad_negativos = contar_positivos_negativos()

#Resultados
print("Cantidad de positivos:",cantidad_positivos)
print("Cantidad de negativos:",cantidad_negativos)
print("Promedio:",promedio)
print("Cantidad de pares:",cantidad_pares)
if paso_5:
    print("SÍ se ingresó un 5")
else:
    print("NO se ingresó un 5")
