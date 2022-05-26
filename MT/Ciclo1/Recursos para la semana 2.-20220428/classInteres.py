"""
Solución para: Suponga que un individuo desea invertir su capital en un banco y desea saber
cuanto dinero ganará después de un mes si el banco paga a razón de 15% efectivo anual.
"""

class interes:

    def __init__(self, valor1): # Función recibe los valores
        self.v1 = valor1

    def calcular(self):
        im = self.v1 * (0.15/12)
        self.tb = im + self.v1


    def mostrar(self):
        print(self.tb)

o = interes(1000)
o.calcular()
o.mostrar()