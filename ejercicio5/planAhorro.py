class PlanAhorro:
    __codigp = ''
    __modelo_auto = ''
    __version = ''
    __costo = ''
    __cuotas = 60
    __CantCuotasMin = 10
    def __init__(self, codigo, modelo_auto, version, costo):
        self.__codigo = int(codigo)
        self.__modelo_auto = modelo_auto
        self.__version = version
        self.__costo = float(costo)
    def __str__ (self):
        return "%s %s %s" %(self.__codigo,self.__modelo_auto,self.__version)
    def getValor(self):
        return (self.__costo)
    def getCuotas(self):
        return(self.__cuotas)
    def getCod(self):
        return(self.__codigo)
    def getModelo(self):
        return(self.__modelo_auto)
    def actualizaValor(self,costo):
        self.__costo = costo
    @classmethod
    def getCantCuotas(cls):
        return (cls.__CantCuotasMin)
    @classmethod
    def getCuotas(cls):
        return (cls.__cuotas)
    @classmethod
    def modificaCantCuotas(cls,CuotasLicitas):
        cls.__CantCuotasMin = CuotasLicitas