from sqlite3 import IntegrityError
from database import Conexiones

#Clase Monopatin
class Monopatin:
    #Constructor
    def __init__(self,marca, precio= None, cant_disponibles = None):
        self.marca = marca
        self.precio = precio
        self.cant_disponibles = cant_disponibles
    #Metodos de instancia
    def cargar_monopatin(self):
        conexion = Conexiones()
        conexion.iniciar()
        try:
            conexion.miCursor.execute("INSERT INTO MONOPATINES(marca,precio,cant_disponibles) VALUES('{}', '{}','{}')".format(self.marca, self.precio,self.cant_disponibles))
            conexion.miConexion.commit()
            separador()
            print("Se cargo el monopatin exitosamente")
            separador()
        except IntegrityError:
            separador()
            print("La marca que ingreso ya se encuentra en la base de datos")
            separador()
        finally:
            conexion.finalizar()


    def cargarDisponibilidad(self):
        conexion = Conexiones()
        conexion.iniciar()
        try:
            conexion.miCursor.execute("UPDATE MONOPATINES SET cant_disponibles='{}' where marca='{}' ".format(self.cant_disponibles,self.marca))
            conexion.miConexion.commit()
            separador()
            print("Se modifico la cantidad disponible")
            separador()
        except:
            separador()
            print("No se logro modificar la cantidad disponible")
            separador()
        finally:
            conexion.finalizar()

#Funciones
def mostrarTabla():
    conexion = Conexiones()
    conexion.iniciar()
    try:
        conexion.miCursor.execute("SELECT * FROM MONOPATINES ORDER BY marca")
        print(conexion.miCursor.fetchall())
       
    except:
        separador()
        print("No se puede mostrar la tabla")
        separador()
    finally:
        conexion.finalizar()

def borrar_monopatin(id1):
    conexion = Conexiones()
    conexion.iniciar()
    try:
        conexion.miCursor.execute("DELETE FROM MONOPATINES WHERE ID='{}'".format(id1))
        conexion.miConexion.commit()
        separador()
        print("El monopatin fue eliminado exitosamente")
        separador()
    except:
        separador()
        print("el monopatin no pudo ser eliminado")
        separador()
    finally:
        conexion.finalizar()

def modificar_Monopatin(precio, id1):
    conexion = Conexiones()
    conexion.iniciar()
    try:
        conexion.miCursor.execute("UPDATE MONOPATINES SET precio='{}' where ID='{}' ".format(precio, id1))
        conexion.miConexion.commit()
        separador()
        print("Se modifico el monopatin")
        separador()
    except:
        separador()
        print('Error al modificar el monopatin')
        separador()
    finally:
        conexion.finalizar()  

def separador():
    print("---------------------------------")




