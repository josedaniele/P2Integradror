from os import sep
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
            conexion.miCursor.execute("INSERT INTO MONOPATINES(marca,precio,cant_disponibles) VALUES('{}', '{}','{}')".format(self.marca, self.precio, self.cant_disponibles))
            conexion.miConexion.commit()
            separador()
            print("Se cargo el monopatin exitosamente")
            separador()
        except IntegrityError:
            separador()
            print("La marca que ingreso ya se encuentra en la base de datos")
            separador()
        except:
            print("No se logro cargar el monopatin")
        finally:
            conexion.finalizar()

    def cargarDisponibilidad(self):
        conexion = Conexiones()
        conexion.iniciar()
        try:
            conexion.miCursor.execute("UPDATE MONOPATINES SET cant_disponibles='{}' where marca='{}' ".format(self.cant_disponibles, self.marca))
            conexion.miConexion.commit()
            #DETECTA LA CANTIDAD DE CAMBIOS Y EN CASO DE NO ENCONTRAR CAMBIOS SE INTUYE QUE NO EXISTE EL MONOPATIN
            total_changes= conexion.miConexion.total_changes
            if total_changes == 0:
                separador()
                print("No se encontro el monopatin")
                separador()
            else:
                separador()
                print("La cantidad disponible fue modificada exitosamente")
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
            conexion.miCursor.execute("INSERT INTO MONOPATINES2(modelo,marca,potencia,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}', '{}','{}')".format(self.modelo, self.marca, self.potencia, self.precio, self.color, self.fecha_ultimo_precio))
            conexion.miConexion.commit()
            separador()
            print("Se cargo el monopatin exitosamente")
            separador()
        except:
            separador()
            print("No se logro cargar el monopatin")
            separador()
        finally:
            conexion.finalizar()
    