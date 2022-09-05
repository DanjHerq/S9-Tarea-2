# AND: Equivalente a "Y si ademas..."
# OR:"O sino..."
# not -> negacion

distancia = 1200
numeroHermanos = 3
salarioPadres = 1500

tieneBeneficio = False

if (distancia > 100 and numeroHermanos > 2) or salarioPadres < 2000:
    tieneBeneficio = True

print(not tieneBeneficio)

if (5 > 3) and (8 < 15):
    print("Verdad")
else:
    print("Es mentira...")