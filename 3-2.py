print("Generador de secuencias enteras")
inicio = int(input("Ingrese el inicio:"))
fin = int(input("Ingrese el final:"))
incremento = int(input("Ingrese el incremento:"))

for i in range(inicio, fin, incremento):
    print(i)