from database import crearTabla
from funciones import Monopatin, modificar_Monopatin, borrar_monopatin, mostrarTabla

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
        opcion =int(input("Ingrese un numero en base a las opciones: \n"))
        try :
            
            if opcion == 1:
                marca= input("Ingrese la marca del monopatin: ")
                precio = float(input("Ingrese el precio del monopatin: "))
                cant_disponibles = int(input("Ingrese la cantidad de unidades disponibles: "))
                monopatin1 = Monopatin(marca, precio, cant_disponibles)
                monopatin1.cargar_monopatin()

            elif opcion == 2:
                id1 = int(input("Ingrese el ID del monopatin que desea modificar: "))
                precio = float(input("Ingrese el nuevo precio para el monopatin: "))
                modificar_Monopatin(precio, id1)

            elif opcion == 3 :
               id1 = int(input("Ingrese el ID del monopatin que desea eliminar: "))
               borrar_monopatin(id1)

            elif opcion == 4:
                marca = input("Ingrese la marca del monopatin: ")
                cant_disponibles = int(input("Ingrese la nueva cantidad de monoppatines disponibles: "))#se puede automatizar
                actualizacion_cantidad = Monopatin(marca, cant_disponibles)
                actualizacion_cantidad.cargarDisponibilidad()

            elif opcion == 5:
                mostrarTabla()

            elif opcion ==0:
                print("Gracias por usar nuestro programa")
                break

            else:
                print("Ingrese un numero dentro de las opciones")
        except ValueError:
            print("Valor invalido, ingrese un numero")


crearTabla()
menuPrincipal()




    
