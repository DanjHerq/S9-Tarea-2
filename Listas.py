#Listas: Son estructuras de datos que permiten alamacenar distintos valores
#(equivalentes a los arrays en otros lenguajes de programacion)

#son estructuras dinamicas, pueden MUTAR.

listas1 = ["Oscar", 25, 98.3, True, "Flavio", 56.3]
print(listas1) #lista completa
print(listas1[:])
print(listas1[2]) #de la lista solo los numeros
print(listas1[-1])

print(listas1[0:3])
print(listas1[:2])
print(listas1[3:])

listas1.append("UskokruM2010")
print(listas1)

listas1.insert(4, "Ecuador")
print(listas1)

listas1.extend(["Jessenia",110, False])
print(listas1)

print(listas1.index("Flavio"))

listas1.remove(56.3)
print(listas1)

listas1.pop()
print(listas1)

lista2 = ["Guayaquil", "Andrea"]
lista3=listas1+lista2
print(lista3)

print(lista2 * 4)

print("UskokruM2010" in listas1)