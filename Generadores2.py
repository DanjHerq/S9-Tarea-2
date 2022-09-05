# Cuando inidicamos un * adelante del parametros de una funcion,
# estamos indicado que se va a recibir un numero indeterminado
# de parametros. Ademas, esos parametross se recibieran en forma de tupla.

"""
def devuelveLenguaje(*lenguajes):
    for leng in lenguajes:
        yield leng
"""

def devuelveLenguaje(*lenguajes):
    for leng in lenguajes:
          yield from leng

lenguajesObtenidos = devuelveLenguaje("Python", "Java", "PHP", "Ruby", "JavaScript")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))