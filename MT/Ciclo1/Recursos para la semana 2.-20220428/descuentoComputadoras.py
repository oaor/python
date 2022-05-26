"""
En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del
número de computadoras que compre. Si las computadoras son menos de cinco se les dará un
10% de descuento sobre el total de la compra; si el número de computadoras es mayor o igual a
cinco pero menos de diez se le otorga un 20% de descuento; y si son 10 o más se les da un 40% de
descuento. El precio de cada computadora es de $3.500.000
"""

# Definir la clase
class totalDescuento:
    # Definir variables de la clase
    def __init__(self, v1):
        self.a = v1 # Número de computadores
    
# Definir el método de la funcion
    def descuento(self):
        if self.a < 5:
            self.pago = self.a * (0.9 * 3500000)
            print("El número de computadores es: "+str(self.a) +" el valor a pagar es: $"+str(self.pago))
        elif 10 > self.a >= 5:
            self.pago = self.a * (0.8 * 3500000)
            print("El número de computadores es: "+str(self.a) +" el valor a pagar es: $"+str(self.pago))
        else:
            self.a >= 10
            self.pago = self.a * (0.6 * 3500000)
            print("El número de computadores es: "+str(self.a) +" el valor a pagar es: $"+str(self.pago))
    
    def mostrar(self):
        print(self.pago)

"""
Definir los objetos y los métodos
"""
a = input("Número de computadores: ")
a = int(a)

l = totalDescuento(a)
l.descuento()
l.mostrar()

# Borrado de objeto(s) o instancias
del l