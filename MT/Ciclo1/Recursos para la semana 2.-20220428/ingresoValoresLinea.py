class ingresoValores:

    # Definición de variables o atributos a usar en la clase
    def __init__(self, valor1, valor2, valor3):
        self.a = valor1
        self.b = valor2
        self.c = valor3
        self.r = 0

# Definición de métodos o funciones a usar en la clase    
    def sumar(self):
        self.r = self.a + self.b + self.c
    
    def mostrar(self):
        print('El resultado de a + b + c, es : {}'.format(self.r))

# a, b, c = [int(a) for a in input("Digite los tres valores para a, b y c, separado por espacios: ").split()]
# a, b, c = map(int,input().split())

a, b, c = input().split(" ") # el separador entre valores es una coma
a = int(a)
b = int(b)
c = int(c)

uno = ingresoValores(a, b, c)
uno.sumar()
uno.mostrar()