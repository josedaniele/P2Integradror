from database import Conexiones, conexion 
from datetime import datetime

# Funciones de tabla
def mostrarTabla():
    conexion.iniciar()
    try:
        conexion.miCursor.execute("SELECT * FROM MONOPATINES ORDER BY marca")
        print(conexion.miCursor.fetchall())

    except:
        separador()
        print("No se puede mostrar la tabla.")
        separador()
    finally:
        conexion.finalizar()


def borrar_monopatin(id1):
    conexion.iniciar()
    try:
        conexion.miCursor.execute("DELETE FROM MONOPATINES WHERE ID='{}'".format(id1))
        conexion.miConexion.commit()
        #DETECTA LA CANTIDAD DE CAMBIOS Y EN CASO DE NO ENCONTRAR CAMBIOS SE INTUYE QUE NO EXISTE EL MONOPATIN
        total_changes= conexion.miConexion.total_changes
        if total_changes == 0:
            separador()
            print("No se encontro el monopatin.")
            separador()
        else:
            separador()
            print("El monopatin fue eliminado exitosamente.")
            separador()
    except:
        separador()
        print("El monopatin no pudo ser eliminado.")
        separador()
    finally:
        conexion.finalizar()


def modificar_Monopatin(precio, id1):
    conexion.iniciar()
    try:
        conexion.miCursor.execute("UPDATE MONOPATINES SET precio='{}' where ID='{}' ".format(precio, id1))
        conexion.miConexion.commit()
        #DETECTA LA CANTIDAD DE CAMBIOS Y EN CASO DE NO ENCONTRAR CAMBIOS SE INTUYE QUE NO EXISTE EL MONOPATIN
        total_changes= conexion.miConexion.total_changes
        if total_changes == 0:
            separador()
            print("No se encontro el monopatin.")
            separador()
        else:
            separador()
            print("El monopatin fue modificado exitosamente.")
            separador()
    except:
        separador()
        print('Error al modificar el monopatin.')
        separador()
    finally:
        conexion.finalizar()

def actualizar_precios():
        #cargamos en el historial antes de actualizar
        conexion.iniciar()
        try:
            conexion.miCursor.execute("INSERT INTO HISTORICO_PRECIO(modelo,marca,potencia,precio,color,fechaPreciosViejos) SELECT modelo,marca,potencia,precio,color,fechaUltimoPrecio FROM MONOPATINES2 ")
            conexion.miConexion.commit()
        except:
            separador()
            print("No se pudieron guardar los precios viejos.")
            separador()
        finally:
            conexion.finalizar()
         

        conexion.iniciar()
        try:
            fechaActual= datetime.now()
            conexion.miCursor.execute("UPDATE MONOPATINES2 SET precio = round((precio * 1.23),2), fechaUltimoPrecio = '{}'".format(fechaActual))
            conexion.miConexion.commit()
            separador()
            print("El precio de los monopatines sufrio un aumento del 23% por el aumento del dolar.")
            separador()
        except:
            separador()
            print("El precio del monopatin no pudo ser aumentado.")
            separador()
        finally:
            conexion.finalizar()

def mostrar_tabla_segunFecha(fecha1):
    conexion.iniciar()
    try:
        conexion.miCursor.execute("SELECT * FROM HISTORICO_PRECIO WHERE fechaPreciosViejos <='{}' ORDER BY fechaPreciosViejos" .format(fecha1))
        print(conexion.miCursor.fetchall())

    except:
        separador()
        print("No se puede mostrar la tabla segun la fecha.")
        separador()
    finally:
        conexion.finalizar()
#Funciones esteticas

def separador():
    print("---------------------------------")


def mensajeError(tipoError):
# error tipo 1 numero
# error tipo 2 caracter
# error tipo 3 fecha
    if tipoError == 1 :
        separador()
        print("Valor invalido ingrese un numero.")
        separador()
    elif tipoError == 2:
            separador()
            print("Ingreso un tipo de caracter no valido.")
            separador()
    elif tipoError == 3:
            separador()
            print("Formato invalido, ingrese la fecha de forma correcta.")
            separador()
