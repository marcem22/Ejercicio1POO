class ViajeroFrecuente:
  __num_viajero= 0
  __dni=""
  __nombre= ""
  __apellido= ""
  __millas_acum= ""
  #constructor
  def __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
    self.__num_viajero= num_viajero
    self.__dni= dni
    self.__nombre= nombre
    self.__apellido= apellido
    self.__millas_acum= millas_acum
  def __str__(self)-> str:
    return f"{self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum}"
  def __repr__(self) -> str :
    return f"{self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum}"
  def get_numero(self):
    return self.__num_viajero
    # item b) cantidad de millas
  def cantidadTotaldeMillas(self):
    return self.__millas_acum
    # item c) acumularMillas
  def acumularMillas(self,millas_recorridas):
    self.__millas_acum=millas_recorridas+int(self.__millas_acum)
    return (self.__millas_acum)
    # item d) Canjear millas
  def canjearMillas(self,millas_Acanjear):
    self.__millas_acum= int(self.__millas_acum)- int(millas_Acanjear)
    return(self.__millas_acum)
  def get_millas(self):
    return int(self.__millas_acum)