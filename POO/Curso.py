class Curso():
    """
    nombre = "Matematica"
    creditos = 5
    profesion = "Ingenieria Civil"
    """

    #Estado inicila del objeto
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial" #Propiedad encapsualda.

    def mostrarDatos (self):
        dat = "Nombre: {0} / Creditos: {1} / Modo de imparticion: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docenteAsignado  =self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asiganado.")
        else:
            print("No es necesario asignar un docente.")

    def __verificarDocente(self):
        #print("Verificando si existe docente asignado...")
        if self.__imparticion =="Presencial":
            return True
        else:
            return False

    #toString()
    def __str__(self):
        texto = "Nombre: {0} - Creditos: {1}"
        return texto.format(self.nombre, self.creditos)



# curso1 = Curso("Matematica",5,"Ingenieria Civil")
# print(curso1)
# curso1.mostrarDatos()


#curso2 = Curso("Lenguaje",4,"Ingenieria Civil")
#print(curso2.nombre)