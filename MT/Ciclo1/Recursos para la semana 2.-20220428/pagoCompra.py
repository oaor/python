"""
Cálculo resoluciom enunciado segundo
"""

# Definición de la clase
class totalpago:
    # Definición de variables o atributos a usar en la clase
    def __init__(self, v1, v2):
        self.a = v1 # Valor de la compra
        self.b = v2 # Color de la bolita

# Definición de métodos o funciones a usar en la clase    
    def descuento(self):
        if self.b == "Blanco":
            self.pago = self.a * 1
        elif self.b == "Verde":
            self.pago = self.a * 0.9
        elif self.b == "Amarillo":
            self.pago = self.a * 0.75
        elif self.b == "Azul":
            self.pago = self.a * 0.5
        else:
            self.pago = self.a * 0
    
    def mostrar(self):
        print(self.pago)

"""
Inicio, creación de objeto(s) o instancias de la  clase y desde allí se manipulan los
métodos e instancias creadas en la clase
"""  
a = input() # Valor de la compra
b = input() # Color de la bolita
a = int(a)

l = totalpago(a,b)
l.descuento()
l.mostrar()

# Borrado de objeto(s) o instancias
del l