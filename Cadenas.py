texto = "bienvemidos al canal de UskokruM2010"

print(texto)
print(texto.lower()) #es minuscula
print(texto.upper()) #es mayuscula
print(texto.title()) #Convierte una cadena a un formato de titulo
print(texto.find("al")) #Posicion donde encuentra la caxdena o porcio.
print(texto.count("e")) #cantidad de ocurrencias de una letra o porcion.

textoFinal = texto.replace("e", "3")
print(textoFinal)

valor = texto.isnumeric() #Arroja true o false dependiendo si es un numero
print(valor)

cadenaSeparada = texto.split(" ") #separar un valor 
print(cadenaSeparada)