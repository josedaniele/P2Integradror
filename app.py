from clases import Monopatin, Monopatin2
from database import crearTabla, crearTabla2, crearTablaHistorico
from funciones import actualizar_precios, modificar_Monopatin, borrar_monopatin, mostrar_tabla_segunFecha, mostrarTabla, separador, mensajeError
import datetime


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
            "7.Aumentar precio respecto al dolar\n"
            "8.Mostrar registros desde la fecha ingresada\n"
            "0.Salir del Menu\n"
        )
        try:
            opcion = int(input("Ingrese un numero en base a las opciones: "))
            if opcion == 1:
                cargar_datos(opcion)
                monopatin1 = Monopatin(marca1, precio1, cant_ingresada)
                monopatin1.cargar_monopatin()

            elif opcion == 2:
                cargar_datos(opcion)
                modificar_Monopatin(precio1, id1)

            elif opcion == 3:
                cargar_datos(opcion)
                borrar_monopatin(id1)

            elif opcion == 4:
                cargar_datos(opcion)
                actualizacion_cantidad = Monopatin(marca1, cant_disponibles=cant_ingresada)
                actualizacion_cantidad.cargarDisponibilidad()

            elif opcion == 5:
                mostrarTabla()

            elif opcion == 6:
                cargar_datos(opcion)
                monopatin2 = Monopatin2(modelo1, marca1, potencia1, color1, precio1, fecha1)
                monopatin2.cargar_monopatin2()

            elif opcion == 7:
                cargar_datos(opcion)
                actualizar_precios(porcentajeDolar)

            elif opcion == 8:
                cargar_datos(opcion)
                mostrar_tabla_segunFecha(fecha1)
                
            
            elif opcion == 0:
                print("Gracias por usar nuestro programa.")
                break

            else:
                print("Ingrese un numero dentro de las opciones: ")
        except ValueError:
            mensajeError(1)

#Carga de datos para luego pasarlo a la DB

def cargar_datos(opcion):

    global marca1
    global modelo1
    global potencia1
    global precio1
    global cant_ingresada
    global color1
    global fecha1
    global id1
    global porcentajeDolar
    

    # modelo
    if opcion == 6:
        Valido = True
        while Valido == True:
            modelo1 = input("Ingrese el modelo: ").upper()
            caracteres = len(modelo1)
            if caracteres < 30:
                Valido = False
            else:
                separador()
                print("Ingresó una longitud mayor a 30 caracteres.")
                separador()
    # marca
    if opcion == 1 or opcion == 4 or opcion == 6:
        Valido = True
        while Valido == True:
            marca1 = input("Ingrese la marca: ").upper()
            caracteres = len(marca1)
            tipo = marca1.isalpha()
            if tipo == True:
                if caracteres < 30:
                    Valido = False
                else:
                    separador()
                    print("Ingresó una longitud mayor a 30 caracteres.")
                    separador()
            else:
                mensajeError(2)

    # potencia
    if opcion == 6:
        Valido = True
        while Valido == True:
            try:
                potencia1 = input("Ingrese la potencia del monopatin: ")
                if int(potencia1) > 0:
                    Valido = False
                else:
                    separador()
                    print("La potencia no puede ser menor o igual a 0.")
                    separador()
            except ValueError:
                mensajeError(1)
    # color
    if opcion == 6:
        Valido = True
        while Valido == True:
            color1 = input("Ingrese el color del monopatin: ")
            caracteres = len(color1)
            tipo = color1.isalpha()
            if tipo == True:
                if caracteres < 30:
                    Valido = False
                else:
                    print("Ingresó una longitud mayor a 30 caracteres.")
            else:
                mensajeError(2)

    # precio
    if opcion == 1 or opcion == 2 or opcion == 6:
        Valido = True
        while Valido == True:
            try:
                precio1 = float(input("Ingrese el precio: "))
                if float(precio1) > 0:
                    Valido = False
                else:
                    separador()
                    print("El precio no puede ser menor o igual a 0.")
                    separador()
            except ValueError:
                mensajeError(1)
    # cantidad de monopatines
    if opcion == 1 or opcion == 4:
        Valido = True
        while Valido == True:
            try:
                cant_ingresada = int(input("Ingrese la cantidad disponible de monopatines: "))
                if int(cant_ingresada) >= 0:
                    Valido = False
                else:
                    separador()
                    print("La cantidad de monopatines debe ser debe ser mayor o igual a 0.")
                    separador()
            except ValueError:
                mensajeError(1)

    # fecha
    if opcion == 6 or opcion == 8:
        Valido = True
        while Valido == True:
            try:
                fecha1 = input("Ingrese la fecha: ")
                fecha1 = datetime.datetime.strptime(fecha1, '%d/%m/%Y')
                Valido = False
            except ValueError:
                mensajeError(3)
    # ID
    if opcion == 2 or opcion == 3:
        Valido = True
        while Valido == True:
            try:
                if opcion == 2:
                    id1 = int(input("Ingrese el ID del monopatin que desea modificar: "))
                else:
                    id1 = int(input("Ingrese el ID del monopatin que desea eliminar: "))

                if id1 > 0:
                    Valido = False
                else:
                    separador()
                    print("ID invalido, el id no puede ser menor o igual a 0.")
                    separador()

            except ValueError:
                mensajeError(1)

    if opcion == 7:
            Valido = True
            while Valido == True:
                try:
                    porcentajeDolar = int(input("Ingrese en que porcentaje desea aumentar el precio respecto al dolar: "))
                    Valido = False
                    if porcentajeDolar > 0:
                        Valido = False
                    else:
                        separador()
                        print("El porcentaje no puede tomar valores negativos.")
                        separador()
                except ValueError:
                    mensajeError(1)
#Llamadas a las funciones

crearTabla()
crearTabla2()
crearTablaHistorico()
menuPrincipal()