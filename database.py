import sqlite3

class Conexiones:
    
    def iniciar(self):
        self.miConexion = sqlite3.connect("MONOPATINES.db")
        self.miCursor = self.miConexion.cursor()
        
    def finalizar(self):
        self.miConexion.close()   


def crearTabla():
    conexion = Conexiones()
    conexion.iniciar()
    conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATINES")
    conexion.miCursor.execute("CREATE TABLE MONOPATINES (ID INTEGER PRIMARY KEY , marca  VARCHAR(30) ,precio FLOAT NOT NULL, cant_disponibles INTEGER NOT NULL,UNIQUE(marca))")    
    conexion.miConexion.commit()       
    conexion.finalizar()