lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

print(lenguajes)
# Los arrays (list) comienzan en la posición 0
print(lenguajes[0])
print(lenguajes[1])
print(lenguajes[2])
print(lenguajes[3])
# Ordenar los elementos
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo {lenguajes[0]}"
print(aprendiendo)

#Modificando valores de un arreglo
lenguajes[2] = "PHP"
print(lenguajes)

# Agregar elementos a un arreglo (list)
lenguajes.append("Ruby")
print(lenguajes)

# Eliminar elementos a un arreglo (list)
del lenguajes[1]
print(lenguajes)

# Eliminar el ultimo elemento del arreglo (list)
lenguajes.pop()
print(lenguajes)

# Eliminar por nombre
lenguajes.remove("PHP")
print(lenguajes)
