"""
 Cálculo de un numero si es multiplo de cinco o no 
"""
class Calculo:
# Caraceristicas, atributos o propiedades  

# Definicion de méNtodos o funciones
    def __init__(self, valor1): # Función recibe los valores
        self.v1 = valor1
    
    def evaluar(self):
        r = self.v1 % 5
        if r == 0:
            self.b = 1
        else:
            self.b = 0
    
    def mostrar(self):
        print(self.b)


# Ingreso de datos o captura desde el teclado
a = input()
a = int(a)

# Creación de objetos
op = Calculo(a)
op.evaluar()
op.mostrar()