"""
Elaborar un algoritmo que calcule la suma de los números de 1 a n.
"""
class calculoSumatoria:
    # Definir métodos de calculoSumatoria
    def __init__(self,n): # Es la función que recibe el valor de n
        self.a = n # Límite de la sumatoria
        self.s = 0 # Variable acumuladora

    def sumatoria(self):
        c = 1 # Variable contador
        while c <= self.a:
          self.s += c
          c += 1 # c = c + 1

    def mostrar(self):
      print(self.s)

ty = calculoSumatoria(10)
ty.sumatoria()
ty.mostrar()
