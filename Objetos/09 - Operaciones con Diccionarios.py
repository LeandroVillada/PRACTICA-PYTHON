# Diccionario Vacio
jugador = {}
print(jugador)

# Se une un Jugador
jugador["Nombre"] = "Leandro"
jugador["Puntaje"] = 0
print(jugador)

# Modificar el Puntaje
jugador["Puntaje"] += 100
print(jugador)
jugador["Puntaje"] += 100
print(jugador)
jugador["Puntaje"] += 100

#Acceder a un valor
print(jugador.get("Puntaje", "No existe ese valor"))

# Iterar en el diccionario
for llave, valor in jugador.items():
    print(valor)

# Eliminar Jugador y Puntaje
del jugador["Nombre"]
del jugador["Puntaje"]
print(jugador)