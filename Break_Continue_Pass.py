#Break: Permite salir de un bucle cuando se cumple una condicion.

"""
for numero in range(1, 6):
    if numero == 3:
        break #Descanso o interrupcion en este punto
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")
"""

#Continue: Omite una parte del bucle cuando se cumple una condicion y
#continua con el resto.

"""
for numero in range(1, 6):
    if numero == 3:
        break #Descanso o interrupcion en este punto
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")
"""

# Pass: Permite continuar con una sentencia o funcion que ya no tiene
# o agun no tiene un bloque de codigo util

for numero in range(1, 6):
    if numero <=3:
        # Aqui no pasa nada y el bucle sigue trabajando
        pass
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")

def funcionSinImplementar():
    pass

