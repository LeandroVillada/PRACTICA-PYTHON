from msilib.schema import Extension
import os

CARPETA = "INTRODUCCION/Proyecto/contactos/"  # Carpeta de contactos
EXTENCION = ".txt"  # Extension de archivos

# Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


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
            preguntar = False
            print("Hasta luego...")
        elif opcion == 1:
            # preguntar = False
            agregar_contacto()
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


def agregar_contacto():
    print("Escribe los datos para agregar el nuevo Contacto.")
    nombre_contacto = input("Nombre del Contacto: ")

    with open(CARPETA + nombre_contacto + EXTENCION, "w") as archivo:
        # Resto de los campos
        telefono_contacto = input("Agrega el Telefono: ")
        categoria_contacto = input("Categoria Contacto: ")

        # Instanciar la clase
        contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

        archivo.write("Nombre: " + contacto.nombre + "\r\n")
        archivo.write("Telefono: " + contacto.telefono + "\r\n")
        archivo.write("Categoria: " + contacto.categoria + "\r\n")

        print('\r\n CONTACTO AGREGADO. \r\n')


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
