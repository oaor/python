"""
Codigo que calcula el armado de una cifra
"""
class sumaDigitos:
    # Aca se definen las variables o caracteristicas privadas de la clase
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
# Definicion de los metodos o funciones 

    def armadoCifra(self):
        x = self.a*100 + self.b*10 + self.c
        print ("La cifra armada es: " + str(x))

# Creacion de objetos o instancias de la clase
q = sumaDigitos(8,5,3)
q.armadoCifra()

# Borrado de objetos o instancias una vez usadas
del q