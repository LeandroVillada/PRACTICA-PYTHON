def app():
    with open("archivo.txt") as archivo:
        for contenido in archivo:
            print(contenido.rstrip())  # .rstrip() remueve saltos de lineas


app()
