# Convertir monedas usando menú

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
    pesos = input("Cuántos pesos colombianos tienes? $")
    pesos = float(pesos)
    valor_dolar = 3978.92
    dolar = pesos / valor_dolar
    dolar = round(dolar,2)
    dolares = str(dolar)
    print("Tienes $ "+ dolares + " dolares USD")
elif opcion == "2":
    pesos = input("Cuántos pesos argentinos tienes? $")
    pesos = float(pesos)
    valor_dolar = 119.06
    dolar = pesos / valor_dolar
    dolar = round(dolar,2)
    dolares = str(dolar)
    print("Tienes $ "+ dolares + " dolares USD")
elif opcion == "3":
    pesos = input("Cuántos pesos mexicanos tienes? $")
    pesos = float(pesos)
    valor_dolar = 19.83
    dolar = pesos / valor_dolar
    dolar = round(dolar,2)
    dolares = str(dolar)
    print("Tienes $ "+ dolares + " dolares USD")
else:
    print("Por favor ingresa una opción correcta por favor")

# Eliminar variables
del opcion
del pesos
del valro_dolar
del dolar
del dolares
