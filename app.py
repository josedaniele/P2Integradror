from tkinter import E
from database import crearTabla, crearTabla2
from funciones import Monopatin, Monopatin2, modificar_Monopatin, borrar_monopatin, mostrarTabla, separador

def menuPrincipal():
    print("\nBienvenido al sistema de cargas de Monopatines")
    while True:
        print(
            "1.Cargar Monopatin\n"
            "2.Modificar precio de un monopatin\n"
            "3.Borrar Monopatin\n"
            "4.Cargar Disponibilidad\n"
            "5.Mostrar Tabla\n"
            "6.Cargar Monopatin avanzado\n"
            "0.Salir del Menu\n"
        )
        try :
            opcion =int(input("Ingrese un numero en base a las opciones: "))
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
            
            elif opcion == 6 :
                cargar_datos(opcion)
                monopatin2 = Monopatin2(modelo1,marca1,potencia1,color1,precio1,fecha1)
                monopatin2.cargar_monopatin2()


            elif opcion ==0:
                print("Gracias por usar nuestro programa")
                break

            else:
                print("Ingrese un numero dentro de las opciones: ")
        except ValueError:
            separador()
            print("Valor invalido, ingrese un numero")
            separador()

def cargar_datos(opcion):
    global marca1
    global modelo1
    global potencia1
    global precio1
    global cant_ingresada
    global color1
    global fecha1
    #modelo
    if opcion == 6 :
        Valido = True
        while Valido == True:
            try:
                modelo1 = input("Ingrese el modelo: ").upper()
                caracteres = len(modelo1)
                if caracteres < 30:
                      Valido = False
                else:
                      print("Ingresó una longitud mayor a 30 caracteres.")
                      Valido = True
            except ValueError:
                separador()
                print("Valor invalido, introduzca bien el modelo")
                separador()
    #marca
    if opcion == 1 or opcion == 4 or opcion == 6:
        Valido = True
        while Valido == True:
            try:
                marca1 = input("Ingrese la marca: ").upper()
                caracteres = len(marca1)
                if caracteres < 30:
                      Valido = False
                else:
                     print("Ingresó una longitud mayor a 30 caracteres.")
                     Valido = True
            except ValueError:
                separador()
                print("Valor invalido, introduzca bien la marca")
                separador()
    #potencia
    if opcion == 6:
        Valido = True
        while Valido == True:
            try:
                potencia1 = input("Ingrese la potencia del monopatin: ")
                if int(potencia1) > 0:
                     Valido= False
                else:
                    Valido = True
            except ValueError:
                separador()
                print("Valor invalido")
                separador()
    #color
    if opcion == 6:
        Valido= True
        while Valido == True:
            try:
                color1 = input("Ingrese el color del monopatin: ")
                caracteres = len(color1)
                if caracteres < 30:
                      Valido = False
                else:
                     print("Ingresó una longitud mayor a 30 caracteres.")
                     Valido = True
            except ValueError:
                separador()
                print("Valor invalido")
                separador()
    #precio
    if opcion == 1 or opcion == 2 or opcion == 6:
        Valido = True
        while Valido == True:
            try:
                precio1 = float(input("Ingrese el precio: "))
                if float(precio1) > 0:
                     Valido= False
                else:
                    Valido = True
            except ValueError:
                separador()
                print("Valor invalido, introduzca un numero")
                separador()
    #cantidad de monopatines
    if opcion == 1 or opcion == 4 :
        Valido = True
        while Valido == True:
            try:
                cant_ingresada = int(input("Ingrese la cantidad disponible de monopatines: "))
                if int(cant_ingresada) > 0:
                     Valido= False
                else:
                    Valido = True
                Valido = False
            except ValueError:
                separador()
                print("Valor invalido, introduzca un numero")
                separador()

    #fecha
    if opcion == 6:
        fecha1= input("Ingrese la fecha: ")


crearTabla()
crearTabla2()
menuPrincipal()




    
