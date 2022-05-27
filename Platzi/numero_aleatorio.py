""" 
Adivinar el número aleatorio, si el número ingresado es menor al escogido, la máquina va a decir que el
número es muy pequeño, si es mayor al escogido la máquina dirá que es demasiado grande
"""
import random

def run():
    num_aleatorio  = random.randint(1, 100)
    cont = 1

    while  True:
        numero = int(input('Ingresa un número entre 1 y 100: '))
        if numero > num_aleatorio:
            print("Elige un numero mas pequeño que {}".format(numero))
        elif numero < num_aleatorio:
            print("Elige un numero mas grande que {}".format(numero))
        
        if numero == num_aleatorio:
            print('Lo lograste en  {} veces'.format(cont))
            break
        cont += 1


if __name__ == '__main__':
    run()