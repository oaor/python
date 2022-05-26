"""
Determinar si un año es bisiesto o no. Si el año es bisiesto se debe asignar en la variable a el valor
‘s’ de lo contrario ‘n’. Un año es bisiesto si es divisible por 4 y no es divisible por 100, excepto los
los años múltiplos de 400.
"""
# Determinar la clase
class bisiestoYear:
   a = "n" # Variable definida
   
# Defino las variables de la clase
   def __init__(self,year):
        self.y = year # Año variable a evaluar
        
# Definir métodos o funciones a usar en la clase
   def evaluar(self):
        if ((self.y % 4) == 0 and (self.y % 100) != 0 or (self.y % 400) == 0):
            self.a = "s"

# Definir mostrar
def mostrar(self):
    print(self.a)

# Definir objetos o instancias de la clase
year = int(input("Ingresa un año: "))

w = bisiestoYear(year)
w.evaluar()
w.mostrar()

# Borrar la variable
del w