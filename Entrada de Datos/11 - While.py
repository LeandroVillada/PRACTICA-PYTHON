pregunta = "Agrega un numero y te dire su es par o impar \r\n"
pregunta += ' (Escribe "cerrar" para salir de la aplicacion )\r\n'

preguntar = True
while preguntar:

    numero = input(pregunta)
    if numero == "cerrar":
        preguntar = False
    else:
        # Mezclarlo con operadores
        numero = int(numero)
        if numero % 2 == 0:
            print("El numero ingresado es par")
        else:
            print("El numero ingresado es impar")
