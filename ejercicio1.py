import csv
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
        
    
if __name__=="__main__":
    #nombre=input("Ingrese su nombre:")
    #mail=input("Ingrese su email:")
   # print(f"estimado{nombre} te enviaremos tus mensajes a la direccion de correo {mail}")#
    #email.__contraseña=input("ingrese su contraseña actual:")
    #nueva=input("ingrese la nueva contraseña:")
    #print(f"su nueva contraseña es:"+email.modificarContraseña(email,nueva))
    """cuenta2=input("ingrese su mail:")
    datos=cuenta2.split("@")
    dominio=datos[1].split(".")
    email.__idCuenta=datos[0]
    email.__dominio=dominio[0]
    email.__tipoDominio=dominio[0]
    print(f"idCuenta: "+email.__idCuenta+  " - dominio:"+email.__dominio+  " - tipoDominio:"+email.__tipoDominio)"""
    archivo = open('lista.csv')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        lineacompleta=fila
        print(lineacompleta)
  

