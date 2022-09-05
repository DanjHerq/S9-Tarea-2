class Personas:

    def __init__(self, apePat, apeMat, nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombre = nom

    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

    def datos(self):
        print(self.mostrarNombreCompleto())


class Estudiante(Personas):

    def __init__(self, apePat, apeMat, nom, pro):
        super().__init__(apePat, apeMat, nom)
        self.profesion = pro

    def datos(self):
        super().datos()
        print("Profesion: {0}".format(self.profesion))


estu1 = Estudiante("Henríquez", "Quiroz", "Daniel", "Ingenieria en Software")
per1 = Personas("Henríquez", "Quiroz", "Daniel")
print(estu1.mostrarNombreCompleto())
print(estu1.profesion)
estu1.datos()

print(isinstance(per1, Personas))
