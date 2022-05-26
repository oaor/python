"""
Codigo que calcula la suma de los digitos que conforman un número de dos cifras
"""
class sumaDigitos:
# Aca se definen las variables o caracteristicas privadas de la clase
    def __init__(self,valor1):
        self.v1 = valor1
        self.s = 0

# Definicion de los metodos o funciones 
    def calcular(self):
        self.c = self.v1 // 10
        self.r = self.v1 % 10
        self.s = self.c + self.r
    
    def mostrar(self):
        print ("La suma de los digitos es:" + str(self.s))

# Creacion de objetos o instancias de la clase
# w = sumaDigitos(35) # Creación de objeto con envío de dato fijo

a = input() # Creación de objeto con envío de dato digitado desde el teclado
a = int(a)
w = sumaDigitos(a)

w.calcular()
w.mostrar()

# Borrado de objetos o instancias una vez usadas
del w