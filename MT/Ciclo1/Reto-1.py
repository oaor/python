"""
RETO 1: hacer una calculadora
que le facilitará llevar al tendero la cuenta de una compra.
"""


cp = 1
i = 0
subtotal = 0
sub = 0


while i < cp:
        prod = input("Ingrese el valor unitario del producto: ")
        prod = int(prod)
        iva = input("¿El producto tiene IVA? ")
        iva = iva.lower()

        if iva == 'S' or iva == 's':
            print('IVA incluído')
            ivas = 1+ 0.19
        else:
            print('PRODUCTO SIN IVA')
            ivas = 1

        cant = input('Cantidad de Productos? ')
        cant = int(cant)   
         
        sub = (prod * ivas) * cant
        subtotal = sub + subtotal
        printsubt = print(f"SUBTOTAL: {subtotal}")

        faltan = input('Faltan productos por cobrar? ')
       
        if faltan == 'S' or faltan == 's':
            cp += 1
            i += 1
        else:
            break


t = print(f"TOTAL A COBRAR: {subtotal}")
