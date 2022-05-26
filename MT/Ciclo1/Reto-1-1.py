"""
RETO 1: hacer una calculadora
que le facilitará llevar al tendero la cuenta de una compra.
"""

subtotal = 0
sub = 0
iterador = True

while iterador == True:
        prod = input("Ingrese el valor unitario del producto: ")
        prod = int(prod)
        iva = input("¿El producto tiene IVA? ")
        iva = str(iva.lower())

        if iva == 's':
            print('IVA incluído')
            ivas = 1.19
        else:
            print('PRODUCTO SIN IVA')
            ivas = 1

        cant = input('Cantidad de Productos? ')
        cant = int(cant)   
         
        sub = (prod * ivas) * cant
        subtotal = sub + subtotal
        printsubt = print(f"SUBTOTAL: {subtotal}")

        faltan = input('Faltan productos por cobrar? ')
        faltan = str(faltan.lower())
       
        if faltan == 's':
            iterador = True
        else:
            print(f"TOTAL A COBRAR: {subtotal}")
            iterador = False



