# Convertir monedas usando menú y utilizando una función conversor
def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuántos pesos " + tipo_pesos + " tienes? $")
    pesos = float(pesos)
    dolar = pesos / valor_dolar
    dolar = round(dolar,2)
    dolares = str(dolar)
    print("Tienes $ "+ dolares + " dolares USD")

menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Colombianos
2-Pesos Argenitnos
3-Pesos Mexicanos

Elige una opción: 

"""
print(menu)
opcion = input('>> ')

if opcion == "1":
    conversor("colombianos",3978.92)
elif opcion == "2":
    conversor("argentinos",119.06)
elif opcion == "3":
    conversor("colombianos",19.83)
else:
    print("Por favor ingresa una opción correcta por favor")



