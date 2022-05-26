"""
    Codigo muestra la multiplicacion en sumas sucesivas

"""
class calculeMultiplicacion:

    def __init__(self, valor1, valor2):
        self.a = valor1
        self.b = valor2
        self.s = 0 # Esta variable se usará para calcular la sumatoria
        self.c = 1 # Esta variable se usará para contar las veces a sumar

    def sumar(self):
        while self.c <= self.b:
            self.s += self.a # Equivalente -> self.s = self.s + self.b ====> s =  s + a
            self.c += 1

    def mostrar(self):
        # print('El valor de la multiplicacion en sumas es {}'.format(self.s))
        print(self.s)


a = int(input("Ingrese un número: ")) # lee el dato a
b = int(input("Ingrese un número: ")) 

m = calculeMultiplicacion(a, b)
m.sumar()
m.mostrar()

del m