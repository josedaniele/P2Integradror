import database

class Monopatin():
    def __init__(self, marca, precio, cantidad):
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad
    def cargarDatos(self, marca, precio, cant_disponible, conexion):
       
        database.insert_monopatin(conexion, marca, precio, cant_disponible)

    def mostrarDatos(self):
        print(f"{self.marca} {self.precio} {self.cantidad}")


'''def cargarDatos():
    Valido = True
    marca: str = input("Ingrese la marca ").upper()
    while Valido == True:
        try:
            precio = float(input("Ingrese el precio "))
            Valido = False
        except ValueError:
            print("Precio no valido introduzca un numero")
    Valido = True
    while Valido == True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible "))
            Valido = False
        except ValueError:
            print("Cantidad no valido introduzca un numero")'''



