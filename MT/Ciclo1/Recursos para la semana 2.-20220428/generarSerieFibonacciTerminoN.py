"""
Codigo que genera la serie de fibonaci hasta el número término n
"""
class fibonacci:

    # Aca se definen las variables o caracteristicas que deban ser inicializadas por la clase
    def __init__(self):
        self.a = 0
        self.b = 1
            
    # Definición de métodos o funciones a usar en la clase    
    def generar(self, termino):
        ct = 1 # Contador de términos de la serie
        while ct <= termino:
            print (self.a, end=' ')
            c = self.a + self.b
            self.a = self.b
            self.b = c
            ct += 1
        print('\n')

"""
Inicio, creación de objeto(s) o instancias de la  clase y desde allí se manipulan los
métodos o funciones creadas en la clase
"""
y = fibonacci()
y.generar(10) # Se genera la serie hasta el término dado

# Borrado de objeto(s) o instancias
del y