from sqlite3 import IntegrityError
from database import Conexiones
from funciones import separador
# Clase Monopatin
class Monopatin:
    # Constructor
    def __init__(self, marca, precio=None, cant_disponibles=None):
        self.marca = marca
        self.precio = precio
        self.cant_disponibles = cant_disponibles
    # Metodos de instancia

    def cargar_monopatin(self):
        conexion = Conexiones()
        conexion.iniciar()
        try:
            conexion.miCursor.execute("INSERT INTO MONOPATINES(marca,precio,cant_disponibles) VALUES('{}', '{}','{}')".format(
                self.marca, self.precio, self.cant_disponibles))
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
            conexion.miCursor.execute("UPDATE MONOPATINES SET cant_disponibles='{}' where marca='{}' ".format(
                self.cant_disponibles, self.marca))
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


class Monopatin2(Monopatin):
    def __init__(self, modelo, marca, potencia, color, precio, fecha_ultimo_precio):
        super().__init__(marca, precio)
        self.modelo = modelo
        self.potencia = potencia
        self.color = color
        self.fecha_ultimo_precio = fecha_ultimo_precio

    def cargar_monopatin2(self):
        conexion = Conexiones()
        conexion.iniciar()
        try:
            conexion.miCursor.execute("INSERT INTO MONOPATINES2(modelo,marca,potencia,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}', '{}','{}')".format(
                self.modelo, self.marca, self.potencia, self.precio, self.color, self.fecha_ultimo_precio))
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
