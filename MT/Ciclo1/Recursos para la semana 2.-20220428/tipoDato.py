"""
Codigo que muestra que tipo de datos tiene una variable
"""
class tipoDato:
# Aca se definen las variables o caracteristicas privadas de la clase
    def __init__(self):
        self.td = tipoDato

# Definicion de los metodos o funciones         
    def mostrar(self):
        print(type(self.td))

# Creacion de objetos o instancias de la clase
t = tipoDato()

# la variable dato contiene un entero
dato = 10
t.td = dato
t.mostrar()

# la variable dato contiene una cadena de caracteres
dato = "Universidad"
t.td = dato
t.mostrar()

# la variable dato contiene un número decimal (flotante)
dato = 10.5
t.td = dato
t.mostrar()

# la variable dato contiene un booleano
dato = False
t.td = dato
t.mostrar()

# la variable dato contiene un número complejo
dato = 2+3j
t.td = dato
t.mostrar()

# la variable dato contiene una lista
dato = [1, 2.2, 'python']
t.td = dato
t.mostrar()

# la variable dato contiene una tupla
dato = (5,'program', 1+3j)
t.td = dato
t.mostrar()

# la variable dato contiene un diccionario
dato = {5,2,3,1,4}
t.td = dato
t.mostrar()

dato = {"Llave1":0,'Llave2': 2}
t.td = dato
t.mostrar()

# Borrado de objetos o instancias una vez usadas
del t