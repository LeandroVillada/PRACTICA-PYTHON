# # Leer datos de tipo String
nombre = input("Cual es tu nombre: ")
print(f"Hola {nombre}")

# # Leer datos que séran números
edad = input("Cual es tu edad: ")
edad = int(edad)
if edad >= 18:
    print("Ya puedes votar")
else:
    print("Aun no puedes votar")

# Mezclar con Operadores
numero = input("Agrega un numero y te dire si es par o no\r\n")
numero = int(numero)
if numero % 2 == 0:
    print(f"El {numero} es par")
else:
    print(f"El {numero} es impar")