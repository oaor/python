"""
Elaborar un algoritmo que almacene en la variable a la cantidad de números pares y en b la
cantidad números impares que existan entre 1 y n.
"""
x = int(input("Ingrese un número: "))
a = 0
b = 0
c = 0
while c <= x-1:
        x % 2 == 0
        c += 1
        a += 1
else:
        b += 1
        c += 1

print("El número de pares es ",a," y el número de impares es ",b)