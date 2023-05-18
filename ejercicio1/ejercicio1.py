import csv,re
from email import email

def crearCuenta(correos="",contraseña=""):
	    datos=correos.split("@")
	    dom=datos[1].split(".")
	    return email(datos[0],dom[0],dom[1],contraseña)
        
    
if __name__=="__main__":
    nombre=input("Ingrese su nombre:")
    mail=input("Ingrese su email:")
    print(f"estimado {nombre} te enviaremos tus mensajes a la direccion de correo {mail}")
    email.__contraseña=input("ingrese su contraseña actual:")
    nueva=input("ingrese la nueva contraseña:")
    print(f"su nueva contraseña es:"+email.modificarContraseña(email,nueva))
    cuenta2=input("ingrese su mail:")
    datos=cuenta2.split("@")
    dominio=datos[1].split(".")
    email.__idCuenta=datos[0]
    email.__dominio=dominio[0]
    email.__tipoDominio=dominio[0]
    print(f"idCuenta: "+email.__idCuenta+  " - dominio:"+email.__dominio+  " - tipoDominio:"+email.__tipoDominio)
    archivo = open('lista.csv')
    reader = csv.reader(archivo,delimiter=';')
    correos=[]
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    for fila in reader:
        if re.search(email_regex,fila[0]):
            print(f"correo electronico valido: {fila[0]}")
            correos.append(crearCuenta(fila[0]))
        else:
            print(f"cuenta no valida: {fila[0]}")

    

    
  

