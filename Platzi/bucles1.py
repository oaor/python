# Vamos a desarrollar un código para usar la función while
# usando el ejemplo de la potencia



# Defino la función run
def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))
        contador += 1
        potencia_2 = 2**contador

# ESto siempre debemos realizarlo para que corra la función run que hemos escrito

if __name__ == "__main__":
    run()