"""
Codigo que genera la serie de fibonaci hasta el número n
"""
class fibonacci:

    # Aca se definen las variables o caracteristicas que deban ser inicializadas por la clase
    def __init__(self):
        self.a = 0
        self.b = 1
    
    # Definición de métodos o funciones a usar en la clase    
    def generar(self, numero):
        while self.a < numero:
            print (self.a, end=' ')
            c = self.a + self.b
            self.a = self.b
            self.b = c
        print('\n')

"""
Inicio, creación de objeto(s) o instancias de la  clase y desde allí se manipulan los
métodos o funciones creadas en la clase
"""
y = fibonacci()
y.generar(1000) # Se genera la serie hasta el número dado (rango)

# Borrado de objeto(s) o instancias
del y