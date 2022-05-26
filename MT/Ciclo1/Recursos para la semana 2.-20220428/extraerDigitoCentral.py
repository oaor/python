"""
    Codigo que ejecuta la extracción del digito de la mitad dada una cifra de cinco digitos,
    además muestra el manejo de los operadores de asignación.
"""
class extraerDigito:

    def __init__(self, valor1):
        self.a = valor1
        
    def extraer(self):
        contador = 1
        v = 10000
        while contador <= 3:
            self.datoCociente = self.a // v
            datoResiduo = self.a % v
            v //= 10
            self.a = datoResiduo
            contador += 1
                
    def mostrar(self):
        print('El valor extraido es = {}'.format(self.datoCociente))

numero = int(input("Ingrese un número: "))

n = extraerDigito(numero)
n.extraer()
n.mostrar()

# Borrado de objetos o instancias una vez usadas
del n