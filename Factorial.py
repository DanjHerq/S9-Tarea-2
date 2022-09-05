#Factorial: Es el producto de todos los numeros positivos enteros comprendidos entre 1 y un

#Factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
#Factorial de 4 : 1 * 2 * 3 * 4 = 24

numero = int(input("Ingrese un numero: "))

factorial = 1
for n in range (1, (numero + 1)):
    factorial = factorial * n

print("El factorial de {0} es: {1}".format(numero, factorial))
