cant1 = int(input("Ingrese la cantidad del articulo 1"))
precio1 = float(input("Ingrese el precio unitario del articulo 1"))
cant2 = int(input("Ingrese la cantidad del articulo 2"))
precio2 = float(input("Ingrese el precio unitario del articulo 2"))
cant3 = int(input("Ingrese la cantidad del articulo 3"))
precio3 = float(input("Ingrese el precio unitario del articulo 3"))

subtotal1 = cant1 * precio1
subtotal2 = cant2 * precio2
subtotal3 = cant3 * precio3

total = subtotal1 + subtotal2 + subtotal3
descuento = total * 0.15
total_a_pagar = total - descuento

print("Subtotal articulo 1:", subtotal1)
print("Subtotal articulo 2:", subtotal2)
print("Subtotal articulo 3:", subtotal3)
print("Total de la factura:", total)
print("Descuento por pago de contado: {0:b}".format(descuento))
print("Total a pagar",total_a_pagar)









