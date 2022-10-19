from database import Conexiones


class Monopatin:
    def __init__(self,marca, precio= None, cant_disponibles = None):
        self.marca = marca
        self.precio = precio
        self.cant_disponibles = cant_disponibles

    def cargar_monopatin(self):
        conexion = Conexiones()
        conexion.iniciar()
        try:
            conexion.miCursor.execute("INSERT INTO MONOPATINES(marca,precio,cant_disponibles) VALUES('{}', '{}','{}')".format(self.marca, self.precio,self.cant_disponibles))
            conexion.miConexion.commit()
            print("Se cargo el monopatin exitosamente")
        except:
            print("No se pudo cargar el monopatin")
        finally:
            conexion.finalizar()

    
    def mostrarTabla(self):# revisar
        conexion = Conexiones()
        conexion.iniciar()
        try:
            conexion.miCursor.execute("SELECT * FROM MONOPATINES")
            print(conexion.miCursor.fetchall())
        except:
            print("No se puede mostrar la tabla")
        finally:
            conexion.finalizar()

    def cargarDisponibilidad(self):
        conexion = Conexiones()
        conexion.iniciar()
        try:
            conexion.miCursor.execute("UPDATE MONOPATINES SET cant_disponibles='{}' where marca='{}' ".format(self.marca, self.cant_disponibles))
            conexion.miConexion.commit()
            print("Se modifico la cantidad disponible")
        except:
            print("No se logro modificar la cantidad disponible")
        finally:
            conexion.finalizar()

def mostrarTabla():# revisar
    conexion = Conexiones()
    conexion.iniciar()
    try:
        conexion.miCursor.execute("SELECT * FROM MONOPATINES")
        print(conexion.miCursor.fetchall())
    except:
        print("No se puede mostrar la tabla")
    finally:
        conexion.finalizar()

def borrar_monopatin(id1):
    conexion = Conexiones()
    conexion.iniciar()
    try:
        conexion.miCursor.execute("DELETE FROM MONOPATINES WHERE ID='{}'".format(id1))
        conexion.miConexion.commit()
        print("El monopatin fue eliminado exitosamente")
    except:
        print("el monopatin no pudo ser eliminado")
    finally:
        conexion.finalizar()

def modificar_Monopatin(precio, id1):
    conexion = Conexiones()
    conexion.iniciar()
    try:
        conexion.miCursor.execute("UPDATE MONOPATINES SET precio='{}' where ID='{}' ".format(precio, id1))
        conexion.miConexion.commit()
        print("Se modifico el monopatin")
    except:
        print('Error al modificar el monopatin')
    finally:
        conexion.finalizar()  

