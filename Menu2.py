import os
from Curso.Paquete1.funcionCadena import contraLetras
from Curso.Paquete1.funcionesNumericas import *
from Curso.funciones import *
from Curso.Modulos.funcionesMatematicas import *
from Curso.POO.Persona import Persona
from Curso.POO.Curso import Curso
from Curso.POO.Cuenta import Cuenta
from Curso.POO.Herencia import Personas, Estudiante
from Curso.POO.HerenciaMultiple import ClaseA, ClaseB, Clasex
from Curso.POO.Polimorfismo import Estudiante, Docente, Trabajador
from Curso.POO.RelacionesClases import Pais, Ciudad, Urbanizacion



class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo = titulo
        self.opciones = opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1...{}]: ".format(len(self.opciones)))
        return opc

opc=""
while opc != "34":
    os.system("cls")
    men = Menu("Menu Operaciones", ["1) Hola Mundo", "2) Variables", "3) Conversiones", "4) Números y Operaciones Matemáticas ", "5) Concatenación", "6) Funciones de Cadena", "7) Tuplas", "8) Listas", "9) Diccionarios", "10) Lectura de Datos", "11) Estructura Condicional", "12) Funciones", "13) Operadores Lógicos", "14) Operadores Ternarios", "15) Funcion Range", "16) Bucle For", "17) If con Tuplas y Listas", "18) Factorial de un Número", "19) Bucle While", "20) Sentencia Break, Continue y Pass", "21) Generadores", "22) Generadores 2", "23) Excepciones", "24) Sentencia Raise", "25) Módulos", "26) Paquetes", "27) POO", "28) Curso y __str__", "29) Método Accesores", "30) Herencia, Sobreescritura de Método y Principio de Sustitución", "31) Herencia Múltiple", "32) Polimorfismo", "33) Relaciones entre Clases", "34) Salir"])
    opc = men.menu()
    if opc == "1":
        opc = ()
        print("Lectura")
        print("Hola Mundo")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "2":
        opc2 = ()
        print("Variables")
        print("Daniel Henríquez")
        print("27")
        print("True")
        print("3008.95")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "3":
        opc3 = ()
        print("Conversiones")
        numero1 = "35"
        numero2 = "18"
        print("numero1 + numero2")
        num1 = int(numero1)
        num2 = int(numero2)
        print(num1 + num2)
        sueldo = 1200.43
        sueldoEntero = int(sueldo)
        print(sueldoEntero)
        valor = "4500.89"
        valorDecimal = float(valor)
        print(valorDecimal * 3)
        edad = 100
        print(len(str(edad)))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "4":
        opc4 = ()
        print("Números y Operaciones")
        num1 = 20
        num2 = 4
        print("Suma:", (num1 + num2))
        print("Resta:", (num1 - num2))
        print("Multiplicacion:", (num1 * num2))
        print("Division:", (num1 / num2))
        print("Division Exacta:", (num1 // num2))
        print("Potencia:", (num1 ** num2))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "5":
        opc5 = ()
        print("Concatenación")
        texto1 = "Hola"
        texto2 = "Mundo"
        textoFinal = texto1 + " " + texto2
        print(textoFinal)
        print("El saludo es: %s %s " % (texto1, texto2))
        saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
        print(saludoFinal)
        saludoFinal2 = "Saludo: {x} {y}".format(x=texto1, y=texto2)
        print(saludoFinal2)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "6":
        opc6 = ()
        print("Funciones de Cadena")
        texto = "bienvenidos al canal de DanjHerq"
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())
        print(texto.find("al"))
        print(texto.count("e"))
        textoFinal = texto.replace("e", "3")
        print(textoFinal)
        valor = texto.isnumeric()
        print(valor)
        cadenaSeparada = texto.split(" ")
        print(cadenaSeparada)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "7":
        opc7 = ()
        print("Tuplas")
        tupla = (1, 2, 3)
        print(tupla)
        tupla2 = (7, "Daniel", True, 450.1, 16 + 7j, "Felicidades", False)
        print(tupla2)
        tupla3 = (9, 3, (4, 5, 6))
        print(tupla3)
        print(tupla2[1])
        print(tupla2[-1])
        print(tupla2[0:4])
        print(tupla2[-2])
        a, b, c = tupla
        print(a)
        print(b)
        print(c)
        tuplaFinal = tupla + tupla3
        print(tuplaFinal)
        print(tuplaFinal.count(21))
        print(tuplaFinal.index(3))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "8":
        opc8 = ()
        print("Listas")
        listas1 = ["Daniel", 25, 98.3, True, "Quiroz", 56.3]
        print(listas1)  # lista completa
        print(listas1[:])
        print(listas1[2])  # de la lista solo los numeros
        print(listas1[-1])
        print(listas1[0:3])
        print(listas1[:2])
        print(listas1[3:])
        listas1.append("Jesús")
        print(listas1)
        listas1.insert(4, "Ecuador")
        print(listas1)
        listas1.extend(["Jessenia", 110, False])
        print(listas1)
        print(listas1.index("Quiroz"))
        listas1.remove(56.3)
        print(listas1)
        listas1.pop()
        print(listas1)
        lista2 = ["Guayaquil", "Andrea"]
        lista3 = listas1 + lista2
        print(lista3)
        print(lista2 * 4)
        print("Jesús" in listas1)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "9":
        opc9 = ()
        print("Diccionario")
        miDiccionario = {"España": "Madrid", "Ecuador": "Quito", "Alemania": "Berlin"}
        print(miDiccionario["Ecuador"])
        print(miDiccionario)
        miDiccionario["Venezuela"] = "Caracas"
        print(miDiccionario)
        miDiccionario["España"] = "Barcelona"
        print(miDiccionario)
        del miDiccionario["España"]
        print(miDiccionario)
        dic2 = {"Pardo": "Evelyn", 24: True, "Sueldo": 150.80}
        print(dic2[24])
        llaves = ("España", "Fracia", "Inglaterra")
        dicPaises = {llaves[0]: "Madrid", llaves[1]: "Paris", llaves[2]: "Londres"}
        print(dicPaises)
        datosPersonales = {"Ape": "Garcia", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
        print(datosPersonales)
        print(datosPersonales["Anios"])
        print(datosPersonales.get('Apel', "Evelyn"))
        print(datosPersonales.keys())
        valores = tuple(datosPersonales.values())
        print(valores)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "10":
        opc10 = ()
        print("Lectura de Datos")
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingrese su sueldo: "))
        print("Hola," + nombre)
        edadFutura = edad + 20
        print("Tu edad es", edad)
        print("Tu edad (Dentro de 20 años) sera:", edadFutura)
        print("Tu sueldo es:", sueldo)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "11":
        opc11 = ()
        print("Estructura Condicional")
        edad = int(input("Ingrese su edad: "))
        if edad >= 18:
            print("Eres mayor de edad.")
        elif edad == 18:
            print("Tienes 18 años")
        else:
            print("No eres mayor de edad.")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "12":
        opc12 = ()
        print("Funciones")
        print(saludar())
        evaluarSueldoMinimo(900)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "13":
        opc13 = ()
        print("Operadores Lógicos")
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
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "14":
        opc14 = ()
        print("Operadores Ternarios")
        sexos = ("Hombre", "Mujer")

        posicion = True
        sexo = sexos[posicion]
        print(sexo)
        sexo = sexos[not posicion]
        print(sexo)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "15":
        opc15 = ()
        print("Función Range")
        numeros = range(5)

        print(numeros[1])

        numeros1 = range(4, 10)
        print(numeros1[5])

        numeros2 = range(10, 100, 8)
        print(numeros2[9])
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "16":
        opc16 = ()
        print("Bucle For")
        for i in range(1, 13):
            print(" {0} x {1} es: {2}".format(1, 1, (i * i)))
        for nom in ["Karen", "Oscar", "Hector", "Leonardo"]:
            print("Cantidad de letras de (0) es: (1)".format(nom, len(nom)))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "17":
        opc17 = ()
        print("If, Else y Elif")
        print("--Cursos--")
        print("Matematica - Biologia - Lenguaje - Ciencias")

        curso = input("Ingreso al curso deseado: ")

        if curso in ("Matematica", "Biologia", "Lenguaje", "Ciencias"):
            print("Curso [0] seleccionado.".format(curso))
        else:
            print("No existe ese curso...")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "18":
        opc18 = ()
        print("Factorial")
        numero = int(input("Ingrese un numero: "))

        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n

        print("El factorial de {0} es: {1}".format(numero, factorial))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "19":
        opc19 = ()
        print("While")
        inicio = 2

        while inicio <= 100:
            print("Numero par: {0}".format(inicio))
            inicio += 2

        print("Hemos terminado el bucle while.")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "20":
        opc20 = ()
        print("Sentencias Break")
        for numero in range(1, 6):
            if numero <= 3:
                pass
            print("El numero es: {0}".format(numero))

        print("Bucle terminado.")
        def funcionSinImplementar():
            pass
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "21":
        opc21 = ()
        print("Generadores")
        def generadorMultiplo7(limite):
            numero = 1

            while numero <= limite:
                yield numero * 7
                numero = numero + 1

        obtieneMultiplos7 = generadorMultiplo7(10)
        print(next(obtieneMultiplos7))
        print("Aca hay 300 lineas de codigo...")
        print(next(obtieneMultiplos7))
        print("Aca hay 100 lineas de codigo...")
        print(next(obtieneMultiplos7))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "22":
        opc22 = ()
        print("Generadores 2")
        def devuelveLenguaje(*lenguajes):
            for leng in lenguajes:
                yield from leng
        lenguajesObtenidos = devuelveLenguaje("Python", "Java", "PHP", "Ruby", "JavaScript")

        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "23":
        opc23 = ()
        print("Excepciones")
        numero1 = 20
        numero2 = 0
        print("La division de {0} entre {1} es:{2}".format(numero1, numero2, (numero1 / numero2)))
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
            print("Error en  el programa...")
        finally:
            print("Yo siempre aparezco")

        print("Aqui termina mi programa")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "24":
        opc24 = ()
        print("Raise")
        def evaluarNota(nota):
            if nota < 0:
                raise ValueError("Valor incorrecto...")
                # raise ZeroDivisionError("Este mensaje es personalizado.")
            elif nota >= 16:
                print("Excelente")
            elif nota >= 11:
                print("Aprobado")
            else:
                print("Desaprobado")
        evaluarNota(8)
        print("Este es el fin de mi programa")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "25":
        opc25 = ()
        print("Módulos")
        print(Sumar(5, 6))
        print(Multiplicar(5, 6))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "26":
        opc26 = ()
        print("Paquete")
        print(multiplicar(85, 6))
        print(contraLetras("Jessenia"))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "27":
        opc27 = ()
        print("POO")
        def despertar(self):
            self.despierta = True
            print("Buen dia.")
        per = Persona()
        per.despertar()
        per.apellido = "Henríquez Quiroz"
        print(per.apellido)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "28":
        opc28 = ()
        print("Curso")
        curso = Curso("Física", 7, "Ingenieria Eléctrica")
        print(curso)
        curso.mostrarDatos()
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "29":
        opc29 = ()
        print("Método Accesores")
        cuenta = Cuenta
        cuenta1 = Cuenta("Daniel Henríquez", 15000, "Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dolares")
        print(cuenta1.get_Moneda())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "30":
        opc30 = ()
        print("Herencia, Sobreescritura y Sustitución")
        estu1 = Estudiante("Henríquez", "Quiroz", "Daniel", "Ingenieria en Software")
        per1 = Personas("Henríquez", "Quiroz", "Daniel")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)
        estu1.datos()
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "31":
        opc31 = ()
        print("Herencia Multiple")
        cX1=Clasex(15, 21)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "32":
        opc32 = ()
        print("Polimorfismo")
        def describirPersonas(persona):
            persona.describir()
        doc1 = Trabajador()
        describirPersonas(doc1)
        doc2 = Docente()
        describirPersonas(doc2)
        doc3 = Estudiante()
        describirPersonas(doc3)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "33":
        opc33 = ()
        print("Relaciones entre Clases")
        pais1 = Pais("Ecuador", "Guillermo Lasso")
        print(pais1)
        ciudad1 = Ciudad("Guayaquil", 2698000, pais1)
        print(ciudad1)
        urba1 = Urbanizacion("Guasmo Central", ciudad1)
        print(urba1)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "34":
            print("Gracias por usar el sistema ")
    else:
            print("Opcion no valida")

print("Lo esperamos en una proxima ocasion")


