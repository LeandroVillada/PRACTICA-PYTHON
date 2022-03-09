import os

CARPETA = "INTRODUCCION/Proyecto/contactos/"  # Carpeta de contactos


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menu de opciones
    mostrar_menu()

    # Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opcion: ")
        opcion = int(opcion)
        # Ejecutar las opciones
        if opcion == 0:
            # preguntar = False
            print("Hasta luego...")
        elif opcion == 1:
            # preguntar = False
            print("Agregar contacto")
        elif opcion == 2:
            # preguntar = False
            print("Editar contacto")
        elif opcion == 3:
            # preguntar = False
            print("Ver contactos")
        elif opcion == 4:
            # preguntar = False
            print("Buscar contacto")
        elif opcion == 5:
            # preguntar = False
            print("Eliminar contacto")
        else:
            print("Opcion ingresada incorrecta.")


def mostrar_menu():
    print("Seleccione del Menu lo que desea hacer:")
    print("1)   Agregar Nuevo Contacto")
    print("2)   Editar Contacto")
    print("3)   Ver Contactos")
    print("4)   Buscar Contacto")
    print("5)   Eliminar Contacto")


def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)


app()
