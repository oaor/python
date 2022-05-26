"""
Codigo que determina si un año es bisiesto o no
"""

class evaluarYear:
# Aca se definen las variables o caracteristicas privadas de la clase que se inicializan
    a = 'no es bisiesto' # Variable que guartda si el año es bisiesto o no

# Aca se definen las variables o caracteristicas que deban ser inicializadas por la clase (constructor)
    def __init__(self,year):
        self.y = year # Valor del año a evaluar

    def evaluar(self):
        if ((self.y % 4) == 0 and (self.y % 100) != 0 or (self.y % 400) == 0):
            self.a = 'si es bisiesto'
        
    def mostrar(self):
        print (self.a)

# Creacion de objetos o instancias de la clase
year = int(input("Ingresa un año: "))

w = evaluarYear(year)
w.evaluar()
w.mostrar()

# Borrado de objetos o instancias una vez usadas
del w