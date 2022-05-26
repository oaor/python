"""
Haciendo una función que detecte si una palabra es palíndromo o no
Ej: Ana, 1991, 2002, Luz azul, etc.
"""
# Lo tercer que debemos hacer es definir la variable palindromo
def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

# Lo segundo es definir la función run()
def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


# Se crea primero esta función y vamos hacia arriba
if __name__ == "__main__":
    run()