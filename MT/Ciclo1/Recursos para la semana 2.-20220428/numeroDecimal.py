"""
    Impresión números decimales, The math.pi constant returns the value of PI: 3.141592653589793.
"""
# importar la librería matemática
import math

class Decimal:

    def numerodecimal(self):
        print ("Impresión de (cantidad) números decimales, valor de PI...: {:.1f}".format(math.pi))

# Creación de objetos
qw = Decimal()
qw.numerodecimal()