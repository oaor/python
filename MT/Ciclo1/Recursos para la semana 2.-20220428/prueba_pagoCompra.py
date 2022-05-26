"""
En una tienda de descuento se efectúa una promoción en la cual se hace un descuento sobre el
valor de la compra total según el color de la bolita que el cliente saque al pagar en caja. Si la bolita
es de color blanco no se le hará descuento alguno, si es verde se le hará un 10% de descuento, si
es amarilla un 25%, si es azul un 50% y si es roja un 100%. Determinar la cantidad final que el
cliente deberá pagar por su compra. se sabe que solo hay bolitas de los colores mencionados.
"""

# Crear la clase
class totalpago:
    # Definir variables de la clase
    def __init__(self, v1, v2):
        self.a = v1 # valor de la compra
        self.b = v2 # color de la bolita

# Definir el método o funciones a usar en la clase
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
Crear los objetos
"""

a = int(input("Ingres el valor de la compra: $"))
b = input("INGRESE, Blanco, Verde, Azul, Amarillo o Rojo: ")
a = int(a)

t = totalpago(a,b)
t.descuento()
t.mostrar()

# Borrar la variable
del t
