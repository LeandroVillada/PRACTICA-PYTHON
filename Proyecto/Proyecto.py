from __future__ import print_function
from ast import Expression, Try
from msilib.schema import Extension
import os
from turtle import up, update
from xml.dom.minidom import Identified

CARPETA = "INTRODUCCION/Proyecto/contactos/"  # Carpeta de contactos
EXTENSION = ".txt"  # Extension de archivos

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
            editar_contacto()
        elif opcion == 3:
            # preguntar = False
            ver_contactos()
        elif opcion == 4:
            # preguntar = False
            buscar_contacto()
        elif opcion == 5:
            # preguntar = False
            eliminar_contacto()
        else:
            print("Opcion ingresada incorrecta.")


def eliminar_contacto():
    nombre = input(" Seleccione el contacto que desea eliminar: \r\n")
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print("\r\n Contacto Eliminado\r\n")
    except IOError:
        print("Contacto no encontrado.")
        print(IOError)


def buscar_contacto():
    nombre = input(" Seleccione el contacto que desea buscar: \r\n")

    # La funcion try intentara abrir el archivo
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print("\r\n Informacion del Contacto:\r\n")
            for linea in contacto:
                print(linea.strip())
            print("\r\n")
    except IOError:
        print("Contacto no encontrado.")
        print(IOError)


def ver_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            # Imprime el contenido
            for linea in contacto:
                print(linea.rstrip())
            # Imprime un separador entre contactos
            print("\r\n")


def editar_contacto():
    print("Escribe el nombre del contacto a Editar")
    nombre_anterior = input("Nombre del Contacto Anterior: ")

    if existe_contacto(nombre_anterior):
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:
            nombre_contacto = input("Nombre del Contacto: ")
            telefono_contacto = input("Agrega el Telefono: ")
            categoria_contacto = input("Categoria Contacto: ")

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Telefono: " + contacto.telefono + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")

        # Renombrar el archivo
        os.rename(
            CARPETA + nombre_anterior + EXTENSION,
            CARPETA + nombre_contacto + EXTENSION,
        )

        print("\r\n CONTACTO EDITADO. \r\n")
    else:
        print("Ese contacto ya existe.")


def agregar_contacto():
    print("Escribe los datos para agregar el nuevo Contacto.")
    nombre_contacto = input("Nombre del Contacto: ")

    if not existe_contacto(nombre_contacto):
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
            # Resto de los campos
            telefono_contacto = input("Agrega el Telefono: ")
            categoria_contacto = input("Categoria Contacto: ")

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Telefono: " + contacto.telefono + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")

            print("\r\n CONTACTO AGREGADO. \r\n")
    else:
        print("Ese contacto ya existe.")


def mostrar_menu():
    print("Seleccione del Menu lo que desea hacer:")
    print("1)   Agregar Nuevo Contacto")
    print("2)   Editar Contacto")
    print("3)   Ver Contactos")
    print("4)   Buscar Contacto")
    print("5)   Eliminar Contacto")
    print("0)   Salir del Programa\r\n")


def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)


def existe_contacto(nombre_contacto):
    # Revisar si el archivo ya existe antes de crearlo
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)
    if existe:
        return True
    else:
        return False


app()
