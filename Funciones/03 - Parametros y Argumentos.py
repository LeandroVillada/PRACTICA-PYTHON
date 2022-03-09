def informacion(nombre, puesto = "Desconocido"):
    print(f"Soy {nombre} y tengo el puesto de {puesto}")

informacion('Leandro', "Programador")
informacion('Nahuel', "Diseñador")
informacion("pepito")

def miNombre():         #FUNCION QUE RETORNA ALGO
    nombre = "Leandro"
    return nombre

nombre = miNombre()
print(f"Mi nombre es {nombre}")