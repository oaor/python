"""
Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los
reste y si no que los sume.
"""
# Definir la clase
class hacerOperacion:
    # Definir los atributos
    def __init__ (self, v1, v2):
        self.a = v1
        self.b = v2
    
    # Definir métodos o funciones a usar en la clase
    def comparar(self):
        if self.a == self.b:
            print("Los valores a y b son iguales")
            self.c = self.a * self.b
        elif self.a > self.b:
            print("El valor de a es mayor que b")
            self.c = self.a - self.b
        else:
            self.c = self.a + self.b
            print("El valor de b es el mayor: "+str(self.c))
    
    def mostrar(self):
        print(self.c)

"""
Inicio o crreación de objetos o instancfias de la clase y desde allí se manipulan los métodos o funciones crados en la clase
"""

a = hacerOperacion(7,5)
a.comparar()
a.mostrar()

# Borrar todo de los objetos y las variables
del a
