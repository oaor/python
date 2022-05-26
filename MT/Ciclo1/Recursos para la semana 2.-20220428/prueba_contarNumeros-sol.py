"""
Elaborar un algoritmo que almacene en la variable a la cantidad de números pares y en b la
cantidad números impares que existan entre 1 y n.
"""
num = int(input("Ingrese un número: "))
a = 0 # Números Pares
b = 0 # Números Impares
c = 0

while c < num:
        if c % 2 == 0:
                a += 1
        else:
                b += 1
        c += 1



print("El número de pares es ",a)
print("El número de impares es ",b)