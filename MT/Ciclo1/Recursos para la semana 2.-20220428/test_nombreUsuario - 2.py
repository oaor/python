"""
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes criterios de
aceptación:
● El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
● El nombre de usuario debe ser alfanumérico.
● Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos
6 caracteres".
● Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de
12 caracteres".
● Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede
contener solo letras y números".
● Nombre de usuario válido, retorna True
"""
# Definir la clase
class username:
    # Definir variables
    def __init__(self, name, namel):
        self.n = name
        self.nl = namel
    #    namel = len(nikname)
    #   name = nikname.isalnum()
        user = True

    def nickname(self):
        nikname = input('Ingresa un nombre de usuario: ')
        self.nl = len(nikname)
        self.n = nikname.isalnum()
        while user == False:
            
            if self.n == False:
                print('El nombre de usuario debe ser alfanumérico.')
            if self.nl <= 6:
                print('El nombre de usuario debe contener al menos 6 caracteres')
            if self.nl >= 12:
                    print('El nombre de usuario debe contener menos de 12 caracteres')
            else:
                user = True
        print('Nombre de usuario correcto')
    # Definir mostrar
    def mostrar(nickname):
        print(nickname)
