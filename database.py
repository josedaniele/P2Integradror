import sqlite3

tabla = "CREATE TABLE IF NOT EXISTS MONOPATIN (ID INTEGER PRIMARY KEY, MARCA VARCHAR (20) UNIQUE, PRECIO FLOAT NOT NULL, CANTIDAD_DISPONIBLE INTEGER NOT NULL)"
agregar_mono = "INSERT INTO MONOPATIN(marca,precio,cant_disponible) VALUES('{}', '{}','{}','{}')"
tabla_completa= "SELECT * FROM MONOPATIN"
borrar = "DELETE FROM MONOPATIN WHERE id= ?"
updt_precio = "UPDATE MONOPATIN SET precio =? WHERE id = ?"

def conectar():
    return sqlite3.connect("Datos_Monopatin.db")
   

def crear_tabla(conexion):
    with conexion:
        conexion.miCursor.execute(tabla)
   

def insert_monopatin(conexion,marca,precio,cant_disponible):
    with conexion:
        conexion.miCursor.execute(agregar_mono,(marca, precio, cant_disponible))

def mostrar_tabla(conexion):
    with conexion:
        return conexion.execute(tabla_completa).fetchall()

def eliminar_monopatin(conexion, id):
    with conexion:
        conexion.execute(borrar, (id))

def modificar_precio(conexion, precio, id):
    with conexion:
        conexion.execute(updt_precio,(precio,id))