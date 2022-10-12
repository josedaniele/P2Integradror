import sqlite3

conexion = sqlite3.connect("baseDatos.db")
try:
    conexion.execute("""create table articulos (
                              id_mono integer primary key autoincrement,
                              modelo text,
                              marca text,
                              potencia real,
                              color text
                              fechaUltimoPrecio datetime
                              precio real
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe") 