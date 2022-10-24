from os import sep
from database import Conexiones

# Funciones de tabla
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
        conexion.miCursor.execute(
            "DELETE FROM MONOPATINES WHERE ID='{}'".format(id1))
        conexion.miConexion.commit()
        separador()
        print("El monopatin fue eliminado exitosamente")
        separador()
    except:
        separador()
        print("El monopatin no pudo ser eliminado")
        separador()
    finally:
        conexion.finalizar()


def modificar_Monopatin(precio, id1):
    conexion = Conexiones()
    conexion.iniciar()
    try:
        conexion.miCursor.execute(
            "UPDATE MONOPATINES SET precio='{}' where ID='{}' ".format(precio, id1))
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


#Funciones esteticas

def separador():
    print("---------------------------------")


def mensajeError(tipoError):
    if tipoError == 1 :
        separador()
        print("Valor invalido ingrese un numero")
        separador()
    elif tipoError == 2:
            separador()
            print("Ingreso un tipo de caracter no valido.")
            separador()
    elif tipoError == 3:
            separador()
            print("Formato invalido, ingrese la fecha de forma correcta.")
            separador()
