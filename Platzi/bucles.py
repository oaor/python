"""
Imprimir todas las potencias de 2 hasta llegar al número 1000

contador = 0
print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))
"""

def potencia(numero):
    
    potencia = 1

    while (potencia <= 10):
        
        result = numero ** potencia
        print('Potencia de {} elevado a la {} es {}'.format(numero, potencia, result))
        potencia += 1
        
# ESta es la primera función que se debe desarrrollar

def run():
    numero = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
    potencia(numero)

# ESto siempre debemos realizarlo para que corra la función run que hemos escrito

if __name__ == "__main__":
    run()