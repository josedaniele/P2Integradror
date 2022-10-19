import sqlite3

class Conexiones:
    
    def iniciar(self):
        self.miConexion = sqlite3.connect("MONOPATINES.db")
        self.miCursor = self.miConexion.cursor()
        
    def finalizar(self):
        self.miConexion.close()   

#Primer Tabla
def crearTabla():
    conexion = Conexiones()
    conexion.iniciar()
    conexion.miCursor.execute("CREATE TABLE IF NOT EXISTS MONOPATINES (ID INTEGER PRIMARY KEY , marca  VARCHAR(30) ,precio FLOAT NOT NULL, cant_disponibles INTEGER NOT NULL,UNIQUE(marca))")    
    conexion.miConexion.commit()       
    conexion.finalizar()

#Segunda Tabla
def crearTabla2():
    conexion = Conexiones()
    conexion.iniciar()
    conexion.miCursor.execute("CREATE TABLE IF NOT EXISTS MONOPATINES2 (ID_mono INTEGER PRIMARY KEY ,modelo VARCHAR(30), marca VARCHAR(30), potencia VARCHAR(30), precio INTEGER, color VARCHAR(30), fechaUltimoPrecio DATETIME)")    
    conexion.miConexion.commit()       
    conexion.finalizar()