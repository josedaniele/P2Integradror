from ast import Num
import database

def menuPrincipal():
    print("Bienvenido al sistema de cargas de Monopatines")
    opcion:int = 5
    while opcion > 4 or opcion <1:
        print(
            "1.Cargar monopatin\n"
            "2.Mostrar monopatines\n"
            "3.Eliminar monopatin\n"
            "4.Modificar precios\n"
        )
        try :
            opcion =int(input("Ingrese un numero en base a la opcion: "))
            if opcion == 1:
                print("cargarMonopatin()")
            elif opcion == 2:
                print("mostrarMonopatines()")
            elif opcion == 3 :
                print("eliminarMonopatin()")
            elif opcion == 4:
                print("modificarPrecio()")
            else:
                print("Ingrese un numero dentro de las opciones")
        except ValueError:
            print("Valor invalido, ingrese un numero")
menuPrincipal()