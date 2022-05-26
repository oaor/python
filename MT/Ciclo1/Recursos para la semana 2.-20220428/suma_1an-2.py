"""
Elaborar un algoritmo que calcule la suma de los números de 1 a n.
"""
# Definir clase
class sumarDigitos:

    # Definir armador
    def __init__(self, v1):
        self.a = v1  # Valor de n
        self.x = 0  # Valor de x

# Definir el método o funciones a usar en la clase
    def sumatoria(self):
        c = 1 # Variable contador

# Iniciamos el ciclo
        while c <= self.a:
            self.x += c
            c += 1
            print('el valor de la suma es: ',self.x)

        def mostrar(self):
            print(self.x)

a = int(input('Ingrese el número de veces que desea sumar N: '))

t = sumarDigitos(a)
t.sumatoria()
# t.mostrar()

# Borrar la variable
del t



