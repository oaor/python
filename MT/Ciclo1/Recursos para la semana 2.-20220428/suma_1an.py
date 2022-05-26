"""
Elaborar un algoritmo que calcule la suma de los números de 1 a n.
"""
n = input('Ingrese el número de veces que desea sumar N: ')
n = int(n)
x = 0
suma = 0

# Iniciamos el ciclo
while x < n + 1:
    suma = suma + x
    x += 1

print('el valor de la suma es: ',suma)
