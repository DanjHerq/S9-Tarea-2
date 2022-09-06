#Polimorfismo (poli => muchas / morfos: formas)

class Estudiante():

    def describir(self):
        print("Soy un buen estudiante.")


class Docente():

    def describir(self):
        print("Me dedico a enseñar cursos.")


class Trabajador():

    def describir(self):
        print("Trabajo dentro de una gran empresa.")


def describirPersonas(persona):
    persona.describir()


# doc1 = Trabajador()
# describirPersonas(doc1)
# doc2 = Docente()
# describirPersonas(doc2)
# doc3 = Estudiante()
# describirPersonas(doc3)