class ClaseA():

    def __init__(self, par1, par2):
        self.parametro1 = par1
        self.parametro2 = par2


class ClaseB():

    def __init__(self, par3, par4, par5):
        self.parametros3 = par3
        self.parametros4 = par4
        self.parametros5 = par5


class Clasex(ClaseA, ClaseB):
    pass

cX1=Clasex(15, 21)