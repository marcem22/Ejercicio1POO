from planAhorro import PlanAhorro
import csv
class ManejadorPlan:
    def __init__(self):
        self.__lista = []
    def agregarPlan(self,unPlan):
        self.__lista.append(unPlan)
    def testPlan(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            codigo = int(fila[0])
            modelo_auto = fila[1]
            version = fila[2]
            costo= float(fila[3])
            unPlan = PlanAhorro(codigo,modelo_auto,version,costo)
            self.agregarPlan(unPlan)
        archivo.close
        return
    def modificaValor(self):
        i = 0
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            importe = float(input('Ingrese nuevo valor: '))
            self.__lista[i].actualizaValor(costo)
        return
    def obtenerCuota(self,i):
        cuotas = self.__lista[i].getCuotas()
        valor = self.__lista[i].getValor()
        return ((valor/cuotas)+valor * 0.10)
    def mostrarPlanes(self,costo):
        i = 0
        for i in range(len(self.__lista)):
            if(costo > self.obtenerCuota(i)):
                print(self.__lista[i])
            else:
                print(f"El modelo{self.__lista[i]} no se ajusta al monto del que dispone el cliente.")
        return
    def obtenerCuotaLicita(self,i):
        cuota = self.obtenerCuota(i)
        cuotasLicitas = PlanAhorro.getCantCuotas() 
        return (cuota * cuotasLicitas)
    def mostrarMontos(self):
        i = 0
        for i in range(len(self.__lista)):
            print("Vehiculo:", self.__lista[i].getModelo())
            print("Monto: $", self.obtenerCuotaLicita(i))
        return
    def cambiarCuotas(self,codigo,cant):
        i = 0
        b = None
        while not b and i in range(len(self.__lista)):
            if(codigo == self.__lista[i].getCod()):
                self.__lista[i].modificaCantCuotas(cant)
                b = True
                print("Se modificaron las cuotas.")
            i+=1
        return