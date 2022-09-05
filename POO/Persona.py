"""
¿En que consiste la Programacio Orientada a Objeto?
-En trasladar la naturaleza de los objetos de la vida real  a codigo
de programacion (en algun lenguaje de programacion, como Python).

Los objetos de la realidad tienen caracteristicas (atributos o propiedades)
y funcionalidades o cmportamientos (funciones o metodos).

Ventajas:
-Modularizacion (divisuion en pequeñas partes) de un programa completo.
-Codigo fuente muy reutilizable.
-Codigo fuente mas facil de incremetar en eel futuro y mantener.
-Si existe un fallo en una pequeña parte del codigo el programa completo
no debe fallar necesariamente. Ademas, es mas facil de corregir esos fallos.
-Encapsulamiento: Ocultamiento del funcionamiento interno de un objeto.
"""


class Persona():
    # Propiedades, caracteristicas o atributos:
    apellido = ""
    nombre = ""
    edad = 0
    despierta = False

    #Funcionalidades:
    def despertar(self):
        #self: Parametro que hace referencia a la instacia perteneciente a la clase.
        self.despierta = True
        print("Buen dia.")


persona1 = Persona()
persona1.apellido = "Garcia Sanchez"
print(persona1.apellido)
persona1.despertar()
print(persona1.despierta)

persona2 = Persona()
persona2.apellido = "Pardo Sanchez"
print(persona2.apellido)
#persona2.despertar()
print(persona2.despierta)