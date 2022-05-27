# Ejercicio propio de números primos
# numero = int(input('Ingresa un número: '))

# def numero_primo(numero):
numero = int(input('Ingresa un número: '))
if numero > 1:
    for i in range (2, numero):
        # cont = 0
        if numero % i == 0:
            break
    if (i + 1) == numero:
        print('El {}  es un número primo '.format(numero))
    else:
        print('El {} No es un número primo '.format(numero))




