"""
Codigo que determina que tipo de triángulo es dados tres lados
"""
class tipoTriangulo:
# Aca se definen las variables o caracteristicas privadas de la clase

# Aca se definen las variables o caracteristicas que deban ser inicializadas por la clase
    def __init__(self, lado1, lado2, lado3):
        self.l1 = lado1 # Valor del lado 1
        self.l2 = lado2 # Valor del lado 2
        self.l3 = lado3 # Valor del lado 3

    def evaluar(self):
        if (self.l1 == self.l2 and self.l2 == self.l3):
            print ("El triángulo es equilatero")
        elif (self.l1 == self.l2 or self.l2 == self.l3 or self.l1 == self.l3): # (sino si....)
            print ("El triángulo es isósceles")
        else:
            print ("El triángulo es escaleno")

# Creacion de objetos o instancias de la clase
w = tipoTriangulo(7,6,9)
w.evaluar()

# Borrado de objetos o instancias una vez usadas
del w