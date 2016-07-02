filas = 8

print("Figura 1")
for i in range(filas):
    for j in range(filas+1):
        print("*", end=" ")
    print()


print("Figura 2")
for i in range(1,filas+1):
    for j in range(i):
        print("*", end=" ")
    print()

print("Figura 3")
for i in range(filas):
    for j in range(i,filas):
        print("*", end=" ")
    print()


print("Figura 4")
for i in range(filas):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i,filas):
        print("*", end=" ")
    print()

print("Figura 5")
for i in range(filas):
    for j in range(i,filas):
        print(" ", end=" ")
    for j in range(i*2+1):
        print("*", end=" ")
    print()


