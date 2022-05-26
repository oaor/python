"""
Cálculo resoluciom enunciado primero
"""

# Definición de la clase
class hacerOperacion:
    # Definición de variables o atributos a usar en la clase
    def __init__(self, v1, v2):
        self.a = v1 # Primer operando
        self.b = v2 # Segundo operando

    # Definición de métodos o funciones a usar en la clase    
    def comparar(self):
        if self.a == self.b:
            print("Los valores son iguales")
            self.c = self.a * self.b
        elif self.a > self.b:
            print("El valor de a es el mayor")
            self.c = self.a - self.b
        else:
            self.c = self.a + self.b
            print("El valor de b es el mayor: "+str(self.c))
    
    def mostrar(self):
        print (self.c)

"""
Inicio, creación de objeto(s) o instancias de la  clase y desde allí se manipulan los
métodos o funciones creadas en la clase
"""  
a = hacerOperacion(5,9)
a.comparar()
a.mostrar()

# Borrado de objeto(s) o instancias
del a