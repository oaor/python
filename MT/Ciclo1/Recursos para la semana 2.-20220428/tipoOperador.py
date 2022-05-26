"""
Codigo que muestra el manejo de los operadores de asignación
"""
class tipoOperador:
# Aca se definen las variables o caracteristicas privadas de la clase
    def __init__(self, valor1, valor2):
        self.a = valor1
        self.b = valor2

    def igual(self):
        print('El valor de a es {} y el de b es {}'.format(a,b))

    def masigual(self):
        self.a += self.b # self.a = self.a + self.b
        print('El valor nuevo de a es igual a lo que tiene a = {}, mas b = {} total: {}'.format(a, b, self.a))
    
    def menosigual(self):
        c = self.a
        self.a -= self.b # self.a = self.a - self.b
        print('El valor nuevo de a es igual a lo que tiene a = {}, menos b = {} total: {}'.format(c, b, self.a))

    def porigual(self):
        c = self.a
        self.a *= self.b
        print('El valor nuevo de a es igual a lo que tiene a = {}, multiplicado por b = {} total: {}'.format(c, b, self.a))
    
    def divisionigual(self):
        c = self.a
        self.a /= self.b
        print('El valor nuevo de a es igual a lo que tiene a = {}, dividido entre b = {} total: {}'.format(c, b, self.a))

    def moduloigual(self):
        c = self.a
        self.a %= self.b
        print('El valor nuevo de a es igual a lo que tiene a = {}, módulo b = {} total: {}'.format(c, b, self.a))

    def divisionenteraigual(self):
        c = self.a
        self.a //= self.b
        print('El nuevo valor de a es igual a lo que tiene a = {}, division entera entre b = {} total: {}'.format(c, b, self.a))

a = 7
b = 2

# Operador igual (=)
op = tipoOperador(a, b)
op.igual()

# Operador mas igual (+=)
op.masigual()

# Operador menos igual (-=)
op.menosigual()

# Operador por igual (*=)
op.porigual()

# Operador division igual (/=)
op.divisionigual()

# Operador modulo igual (%=)
op.moduloigual()

#a = 7
#b = 2
# Operador division entera igual (//=)
op1 = tipoOperador(a,b)
op1.divisionenteraigual()

del op
del op1