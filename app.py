from database import crearTabla
from funciones import Monopatin, modificar_Monopatin, borrar_monopatin, mostrarTabla, separador

def menuPrincipal():
    print("\nBienvenido al sistema de cargas de Monopatines")
    while True:
        print(
            "1.Cargar Monopatin\n"
            "2.Modificar precio de un monopatin\n"
            "3.Borrar Monopatin\n"
            "4.Cargar Disponibilidad\n"
            "5.Mostrar Tabla\n"
            "0.Salir del Menu\n"
        )
        try :
            opcion =int(input("Ingrese un numero en base a las opciones: \n"))
            if opcion == 1:
                cargar_datos(opcion)
                monopatin1 = Monopatin(marca1, precio1, cant_ingresada)
                monopatin1.cargar_monopatin()

            elif opcion == 2:
                id1 = int(input("Ingrese el ID del monopatin que desea modificar: "))
                cargar_datos(opcion)
                modificar_Monopatin(precio1, id1)

            elif opcion == 3 :
               id1 = int(input("Ingrese el ID del monopatin que desea eliminar: "))
               borrar_monopatin(id1)

            elif opcion == 4:
                cargar_datos(opcion)
                actualizacion_cantidad = Monopatin(marca1, cant_disponibles = cant_ingresada)
                actualizacion_cantidad.cargarDisponibilidad()

            elif opcion == 5:
                mostrarTabla()

            elif opcion ==0:
                print("Gracias por usar nuestro programa")
                break

            else:
                print("Ingrese un numero dentro de las opciones")
        except ValueError:
            separador()
            print("Valor invalido, ingrese un numero")
            separador()

def cargar_datos(opcion):
    global marca1
    global precio1
    global cant_ingresada
    if opcion == 1 or opcion == 4:
        Valido = True
        while Valido == True:
            try:
                marca1 = input("Ingrese la marca: ").upper()
                Valido = False
            except ValueError:
                separador()
                print("Valor inavlido, introduzca un numero")
                separador()
    if opcion == 1 or opcion == 2:
        Valido = True
        while Valido == True:
            try:
                precio1 = float(input("Ingrese el precio: "))
                Valido = False
            except ValueError:
                separador()
                print("Valor inavlido, introduzca un numero")
                separador()
    if opcion == 1 or opcion == 4 :
        Valido = True
        while Valido == True:
            try:
                cant_ingresada = int(input("Ingrese la cantidad disponible de monopatines "))
                Valido = False
            except ValueError:
                separador()
                print("Valor invalido,introduzca un numero")
                separador()


crearTabla()
menuPrincipal()




    
