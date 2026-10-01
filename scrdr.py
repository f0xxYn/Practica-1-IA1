
#**Single-Classification Ripple-Down Rules**#

#Clasificacion: 
#Condicion: Conjunto pares clave-valor
#Excepcion: Puntero
#Else:

class scrdr:
    def __init__(self):
        self.__clasi = ""
        self.__cond = set()
        self.__exc = None
        self.__else = None

    #to_string
    def __str__(self):
        print("")

    def set_clasi(self, clasi):
        self.__clasi = clasi

    def set_cond(self, cond):
        self.__cond = cond

    def set_exc(self, exc):
        self.__exc = exc

    def set_else(self, els):
        self.__els = els

    def get_clasi(self):
        return self.__clasi

    def get_cond(self):
        return self.__cond

    def get_exc(self):
        return self.__exc

    def get_else(self): 
        return self.__else

