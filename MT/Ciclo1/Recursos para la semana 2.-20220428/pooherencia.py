# -*- coding: utf-8 -*-
"""pooHerencia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VncHyg1cJ1OOR7MTE5F_QXGVzv6n1wVp
"""

"""
  Manejo de la herencia en la POO
"""
##################
# Clase padre
##################
class Vehiculo:
    
    def __init__(self, marca, color, placa, modelo):
        self.marca = marca
        self.color = color
        self.placa = placa
        self.modelo = modelo
    
    # Acá se definen los métodos o funciones de la clase
    def acelerar(self):
        print(f"Soy {self.marca}, estoy acelerando!!")
    
    def frenar(self):
        print(f"Soy {self.marca}, estoy frenando!!")
    
    def voltear(self, direccion):
        print(f"Soy {self.marca}, estoy volteando a la {direccion}")
    
    def __str__(self):
        """Este método nos servirá para ver una representación en cadena del objeto"""
        return self.marca

####################################
# clase que hereda de la clase padre
####################################
class Carro (Vehiculo):
    numero_llantas = 4

    def tocar_claxon(self):
        print(f"Soy {self.marca}, y estoy tocando el claxon!!")

####################################
# clase que hereda de la clase padre
####################################
class Motocicleta (Vehiculo): 
    numero_llantas = 2

    def encender_con_patada(self):
        print(f"Soy {self.marca} y estoy encendiendo con patada!!")

####################################
# clase que hereda de la clase padre
####################################
class Avion (Vehiculo):
    numero_llantas = 32
    
    def sacar_llantas(self):
        print(f"Soy {self.marca} y estoy sacando las llantas!!")
    
    def aterrizar(self):
        print(f"Soy {self.marca} y estoy aterrizando!!")

class CocheVolador(Avion):
    numeroHelices = 4

#####################################################################
# Creamos Objetos Carro
obj_mazda = Carro('Mazda 6', 'Rojo', 'RED126', '2020')
obj_renault = Carro('Renault Logan', 'Negro', 'FRE009', '2021')
obj_audi = Carro('Audi Q3', 'Blanco', 'DPK312', '2016')

# Creamos Objetos Motocicleta
obj_honda = Motocicleta('Honda CB 500', 'Negro', 'XDR321', '2018')
obj_yamaha = Motocicleta('Yamaha R10', 'Azul', 'GTR576', '2016')
obj_suzuky = Motocicleta('Suzuky VStrom 650', 'Gris', 'RET841', '2020')

# Creamos Objeto Avion
obj_jet = Avion('Jet Privado', 'Blanco', 'G-DER4', '2014')

######################################################################
# Ejecución de los métodos definidos para las clases
######################################################################

# El Mazda 6, va a voltear a la izquierda
obj_mazda.voltear('izquierda')

# El Audi Q3, va a voltear a la derecha
obj_audi.voltear('derecha')

# El Renault Logan va a acelerar y tocar el claxon
obj_renault.acelerar()
obj_renault.tocar_claxon()

# --------------------------------------------------------------------
# La Honda va a encender con patada.
obj_honda.encender_con_patada()

# La Honda, va a voltear a la izquierda
obj_honda.voltear('izquierda')

# La Yamaha, va a voltear a la derecha
obj_yamaha.voltear('derecha')

# La Suzuky va a frenar
obj_suzuky.frenar()

# --------------------------------------------------------------------
# El Jet acelera
obj_jet.acelerar()

# El Jet voltea a la derecha
obj_jet.voltear('derecha')

# El Jet saca las llantas
obj_jet.sacar_llantas()

# Y aterriza.
obj_jet.aterrizar()