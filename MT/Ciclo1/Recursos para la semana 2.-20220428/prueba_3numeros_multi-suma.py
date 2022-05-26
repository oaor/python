"""
Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo, debe imprimir
el producto de los tres y si no lo es, imprimirá la suma.
"""
a = int(input('Ingresea el primer número: '))
b = int(input('Ingresea el segundo número: '))
c = int(input('Ingresea el tercer número: '))

if (a < 0):
  operacion = a * b * c
  print('a es negativo y la multiplicaciones es: ',operacion)
else:
  operacion = a + b + c
  print('a es positivo y la suma es: ',operacion)

# Borrar variables
del a
del b
del c
