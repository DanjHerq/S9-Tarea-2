class Cuenta():

    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    #Getters (metodo GET)
    def get_Saldo(self):
        return self.__saldo

    def get_Propietario(self):
        return self.__propietario

    def get_Moneda(self):
        return self.__moneda

    # Setters (metodo SET)
    def set_Moneda(self, moneda):
        self.__moneda = moneda


# cuenta1 = Cuenta("Oscar Garcia", 15000, "Soles")
# print(cuenta1.get_Saldo())
# print(cuenta1.get_Moneda())
# cuenta1.set_Moneda("Dolares")
# print(cuenta1.get_Moneda())