""" 
Adivinar el número que escojamos, si el número ingresado es menor al escogido, la máquina va a decir que el
número es muy pequeño, si es mayor al escogido la máquina dirá que es demasiado grande
"""

n = 55
cont = 1

while  True:
    numero = int(input('Ingresa un número entre 1 y 100: '))
    if numero > n:
        print("Elige un numero mas pequeño que {}".format(numero))
    elif numero < n:
        print("Elige un numero mas grande que {}".format(numero))
    
    if numero == n:
        print('Lo lograste en  {} veces'.format(cont))
        break
    cont += 1

