"""
Ejercicio para hallar el mayor valor entre a y b
"""
# Definición de la clase
class hallarMayor():

    # Definición de métodos a usar para la clase
    def __init__(self, valor1, valor2): # Constructor de la clase -inicializa variables-
        self.a = valor1
        self.b = valor2
    
    # Métodos o funciones para la clase
    def comparar(self): # Función o métodos a usar en la clase
        if self.a > self.b:
            print(self.a)
        else:
            print(self.b)

# Lectura de variables desde el teclado
a, b = input().split(",") # el separador entre valores es una coma
a = int(a)
b = int(b)

# Creacción de objeto(s) de la clase y manejo de los métodos o funciones desde el objeto creado
qw = hallarMayor(a,b)
qw.comparar()

# Borrado del objeto una vez usado
del qw