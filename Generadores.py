#Generadores: Permiten extraer valores de una funcion y almacenarlo
#(de uno en uno) en objetos iterables (que se pueden recorrer),
#sin la necesidad de almacenar TODOS ALAS VEZ en la memoria RAM.

"""
def generaMultiplos7(limite):
    numero = 1
    listaNumeros = []

    while numero <= limite:
        listaNumeros.append(numero * 7)
        numero = numero + 1
    return listaNumeros #Retorna toda la lista creada

print(generaMultiplos7(10))
"""


def generadorMultiplo7(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7 #ceder. La instruccion "yiel" genera un objeto iterable.
        numero = numero + 1


obtieneMultiplos7 = generadorMultiplo7(10)

"""
#print(obtieneMultiplos7)
for n in obtieneMultiplos7:
    print(n)
"""

#next(): Retorna el siguiente elemento de un objeto iterable:

print(next(obtieneMultiplos7))
print("Aca hay 300 lineas de codigo...")
print(next(obtieneMultiplos7))
print("Aca hay 100 lineas de codigo...")
print(next(obtieneMultiplos7))

#Son mas eficientes que las funciones tradicionales.
#Mul utiles con listas de valores infinitos.
#Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspension)
