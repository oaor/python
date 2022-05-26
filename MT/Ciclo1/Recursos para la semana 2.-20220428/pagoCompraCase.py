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
        match self.b:
            case 'Blanco':
                self.pago = self.a * 1
            case 'Verde':
                self.pago = self.a * 0.9
            case 'Amarillo':
                self.pago = self.a * 0.75
            case 'Azul':
                self.pago = self.a * 0.5
            case 'Roja':
                self.pago = self.a * 0

    def mostrar(self):
        print(self.pago)

"""
Inicio, creación de objeto(s) o instancias de la  clase y desde allí se manipulan los
métodos o funciones creadas en la clase
"""  
a = input() # Valor de la compra
b = input() # Color de la bolita
a = int(a)

l = totalpago(a,b)
l.descuento()
l.mostrar()

# Borrado de objeto(s) o instancias
del l