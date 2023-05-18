import csv
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
  
  

def mostrarMenu():
  print("""
        1.Consultar Cantidad de millas
        2.Acumular millas
        3.Canjear millas
  """)


if __name__=='__main__':
    listaViajeros=[]
    viajeros=[]
    print(listaViajeros)
    archivo=open('viajerosFrecuentes.csv')
    reader=csv.reader(archivo, delimiter=';')
    for fila in reader:
      print(fila)
      viajero=ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
      listaViajeros.append(viajero)
    print(listaViajeros)
    num_viajero1=(input("ingrese un numero de viajero frecuente:"))
    mostrarMenu()
    opc=int(input(""))
    while opc!=0:
      match opc:
        case 1:
          i=0
          encontrado=False
          while(i<len(listaViajeros) and (not encontrado)):
              if listaViajeros[i].get_numero() == num_viajero1 :
                encontrado= True
              i=i+1
          if encontrado:
            print(f"Usted tiene acumuladas {listaViajeros[i-1].cantidadTotaldeMillas()} millas") 
          else:
            print("numero de viajero frecuente no encontrado")
          break          
        case 2:
          i=0
          encontrado=False
          while(i<len(listaViajeros) and (not encontrado)):
              if listaViajeros[i].get_numero() == num_viajero1 :
                encontrado= True
              i=i+1
          if encontrado:
            millas_recorridas=int(input("Ingrese cantidad de millas a agregar:"))
            listaViajeros[i-1].acumularMillas(millas_recorridas)
            print(f"Usted acumuló {millas_recorridas}en total tiene {listaViajeros[i-1].cantidadTotaldeMillas()} millas") 
          else:
            print("numero de viajero frecuente no encontrado")
          break
        case 3:
          i=0
          encontrado=False
          while(i<len(listaViajeros) and (not encontrado)):
              if listaViajeros[i].get_numero() == num_viajero1 :
                encontrado= True
              i=i+1
          if encontrado:
            millas_Acanjear=int(input("Ingrese cantidad de millas a canjear:"))
            listaViajeros[i-1].canjearMillas(millas_Acanjear)
            if millas_Acanjear < listaViajeros[i].get_millas():
              print("canje exitoso")
              #print(f"usted canjeó{millas_Acanjear}millas, su nuevo valor de millas acumuladas es{listaViajeros[i-1].canjearMillas()}millas")#
          else:
            print("numero de viajero frecuente no encontrado")
          break
        
  
   






