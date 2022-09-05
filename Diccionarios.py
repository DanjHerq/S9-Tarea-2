# Diccionarios: Son estructuras de datos que nos permiten almacenar distintos
#valores.

#Es que los datos se almacenan asociados a una clave unica, tenemos una relacion
#clave:valor

#Los elementos almacenados estan en desorden, el orden es diferente ala forma
#de almacenamiento

miDiccionario = {"España": "Madrid", "Ecuador": "Quito", "Alemania": "Berlin"}
print(miDiccionario["Ecuador"])
print(miDiccionario)

miDiccionario["Venezuela"] = "Caracas"
print(miDiccionario)

miDiccionario["España"] = "Barcelona"
print(miDiccionario)

del miDiccionario["España"] #eliminar elememento
print(miDiccionario)

dic2={"Pardo": "Evelyn", 24: True, "Sueldo": 150.80}
print(dic2[24])

llaves=("España", "Fracia", "Inglaterra")
dicPaises ={llaves[0]: "Madrid", llaves[1]: "Paris", llaves[2]: "Londres"}
print(dicPaises)

datosPersonales={"Ape": "Garcia", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
print(datosPersonales)
print(datosPersonales["Anios"])

print(datosPersonales.get('Apel', "Evelyn"))

print(datosPersonales.keys())
#valores=list(datosPersonales.values())
valores=tuple(datosPersonales.values())
print(valores)