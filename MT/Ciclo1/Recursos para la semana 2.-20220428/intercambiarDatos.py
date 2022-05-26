"""
Codigo que calcula el cambio de datos entre variables

"""
class Cambiar:
# Aca se definen las variables o caracteristicas o atributos de la clase
    def __init__(self,a, b):
        self.v1 = a
        self.v2 = b

# Definicion de los metodos o funciones 
    def cambiar(self):
        print ("El valor de a original..:" + str(self.v1))
        print ("El valor de b original..:" + str(self.v2))
        self.v1 = self.v1 - self.v2
        self.v2 = self.v2 + self.v1
        self.v1 = self.v2 - self.v1

    def mostrar(self):
        print ("El valor ahora de a.....:" + str(self.v1))
        print ("El valor ahora de b.....:" + str(self.v2))

# Creacion de objetos o instancias de la clase
t = Cambiar(3,5)
t.cambiar()
t.mostrar()

# Borrado de objetos o instancias una vez usadas
del t