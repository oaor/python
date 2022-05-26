"""
Elaborar un algoritmo que lea dos números enteros y los almacene en las variables a y b. El
algoritmo debe determinar si uno es múltiplo del otro, en cuyo caso se debe escribir ‘s’. Se deberá
escribir ‘n’ en caso contrario.
"""
a = int(input('Ingresea el primer número: '))
b = int(input('Ingresea el segundo número: '))

if (a % b == 0):
    print('si es múltiplo')
else:
    print('no es múltiplo')