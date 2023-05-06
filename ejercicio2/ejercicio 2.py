import csv
class ViajeroFrecuente:
  __num_viajero= 0
  __dni=""
  __nombre= ""
  __apellido= ""
  __millas_acum= 0
  #constructor
  def __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
    self.__num_viajero= num_viajero
    self.__dni= dni
    self.__nombre= nombre
    self.__apellido= apellido
    self.__millas_acum= millas_acum
    # item b) cantidad de millas
  def cantidadTotaldeMillas(self,millas_acum):
     millasacum=self.__millas_acum
     return (millasacum)
    # item c) acumularMillas
  def acumularMillas(self,millas_recorridas):
    return (self.__millas_acum+self.__millas_recorridas)
    # item d) Canjear millas
  def canjearMillas(self,millas_Acanjear):
    if millas_Acanjear <= self.__millas_acum  :
         print("canje exitoso",{self.__millas_acum-self.__millas_Acanjear})
    else: return("Error en canje,su numero de millas acumuladas no es suficiente para realizar la operacion",{self.__millas_acum})
def mostrarMenu():
	print("""
        1.Consultar Cantidad de millas
        2.Acumular millas
        3.Canjear millas
  """) 
def crearviajero(num_viajero=0, dni="", nombre="", apellido="", millas_acum=""):
    num_viajero1=num_viajero
    dni1=dni
    nombre1=nombre
    apellido1= apellido
    millas_acum1= millas_acum
    return ViajeroFrecuente(num_viajero, dni, nombre, apellido, millas_acum)


if __name__=='__main__':
    archivo= open('viajerosFrecuentes.csv')
    reader=csv.reader(archivo,delimiter=";")
    listaViajeros=archivo
    crearviajero()
    for fila in reader:
        lineaCompleta=fila
        print(lineaCompleta)
    num_viajero1=int(input("ingrese un numero de viajero frecuente:"))
    num_viajero1=crearviajero()
    n=ViajeroFrecuente(num_viajero1,dni1,nombre1,apellido1,millas_acum1)
    mostrarMenu()
    opc=int(input(""))
    while opc!=0:
      match opc:
        case 1:
          print(f"Usted tiene acumuladas{viajero11.cantidadTotaldeMillas()} millas")
   





