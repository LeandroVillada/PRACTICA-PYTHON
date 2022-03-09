"""
    Un objeto es en cierta medida similar a un array, te permite agrupar contenido de diferentes tipos de datos.
    Usualmente se accede a un elemento de un array por medio de su indice, en un objeto se accede por medio de un a llave(key).
    Algunos lenguajes no soportan Objetos, en Python se usiliza algo llamado Dictionary.
"""
# Creando un diccionario Simple
cancion = {
    "Artista" : "Metallica",    # llave y valor
    "Cancion" : "Enter Sadman",
    "Lanzamiento" : 1992,
    "Likes" : 3000
}
# Acceder a los elementos del diccionario
print(cancion["Artista"])
print(cancion["Lanzamiento"])

#mezclar con un string
artista = cancion["Artista"]
print(f"Estoy escuchando {artista}")
print(cancion)

# Agregar nuevos valores
cancion["Playlist"] = "Heavy Metal"
print(cancion)

# Reemplazar valor existente
cancion["Cancion"] = "Seek & Destroy"
print(cancion)

# Eliminar un valor
del cancion["Lanzamiento"]
print(cancion)

