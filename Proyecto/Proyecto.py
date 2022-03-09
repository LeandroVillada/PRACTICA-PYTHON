import os

CARPETA = "INTRODUCCION/Proyecto/contactos/"  # Carpeta de contactos


def app():
    crear_directorio()


def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)


app()
