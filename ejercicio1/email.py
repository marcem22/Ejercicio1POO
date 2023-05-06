class email():
    __idCuenta=""
    __dominio=""
    __tipoDominio=""
    __contraseña=""
    def __init__(self,idCuenta,dominio,tipoDominio,contraseña):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__tipoDominio= tipoDominio
        self.__contraseña=contraseña
    def retornaEmail(self):
        return self.__idCuenta+"@" +self.__dominio+'.'+self.__tipoDominio
    def getDominio(self):
        return self.__dominio
    def modificarContraseña(self,contraseña):
        self.__contraseña=contraseña
        return self.__contraseña
